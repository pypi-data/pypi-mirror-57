import sys
import os
import inspect
import subprocess

from .passes import DefinitionPass, InstanceGraphPass
from .backend import verilog, blif, firrtl, dot
from .backend.coreir_ import InsertWrapCasts
from .config import get_compile_dir
from .logging import warning
from .uniquification import uniquification_pass, UniquificationMode
import magma as m


__all__ = ['compile']


def write_file(file_name, extension, code):
    with open("{}.{}".format(file_name, extension), 'w') as file:
        file.write(code)


def __compile_to_coreir(main, file_name, opts):
    # Underscore so our coreir module doesn't conflict with coreir bindings
    # package.
    from .frontend import coreir_
    backend = coreir_.GetCoreIRBackend()
    InsertWrapCasts(main).run()
    backend.compile(main)
    passes = opts.get("passes", [])
    if "markdirty" not in passes:
        passes.append("markdirty")
    namespaces = opts.get("namespaces", ["global"])
    backend.context.run_passes(passes, namespaces)

    backend.modules[main.coreir_name].save_to_file(file_name + ".json")
    if opts.get("output_verilog", False):
        deps = opts.get("coreir_libs", set())
        pass_ = InstanceGraphPass(main)
        pass_.run()
        for key, _ in pass_.tsortedgraph:
            if key.coreir_lib:
                deps.add(key.coreir_lib)
            elif hasattr(key, 'wrappedModule'):
                deps |= key.coreir_wrapped_modules_libs_used
        for namespace in namespaces:
            deps.add(namespace)
        # TODO(rsetaluri): Expose compilation to verilog in pycoreir rather than
        # calling the binary from the command line.
        lib_arg = ""
        if deps:
            lib_arg = f"-l {','.join(deps)}"
        cmd = f"coreir {lib_arg} -i {file_name}.json"
        if opts.get("split", ""):
            split = opts["split"]
            cmd += f" -o \"{split}/*.v\" -s"
        else:
            cmd += f" -o {file_name}.v"
        if opts.get("inline", False):
            cmd += " --inline"
        if opts.get("verilator_debug", False):
            cmd += " --verilator_debug"
        assert not subprocess.run(cmd, shell=True).returncode, \
            "Running coreir failed"


def compile(basename, main, output='coreir-verilog', **kwargs):
    opts = kwargs.copy()

    # Rather than having separate logic for 'coreir-verilog' mode, we defer to
    # 'coreir' mode with the 'output_verilog' option set to True.
    if output == 'coreir-verilog':
        opts["output_verilog"] = True
        output = "coreir"

    # Allow the user to pass in a mode for uniquification. The input is expected
    # as a string and maps to the UniquificationMode enum.
    uniquification_mode_str = opts.get("uniquify", "UNIQUIFY")
    uniquification_mode = getattr(UniquificationMode, uniquification_mode_str,
                                  None)
    if uniquification_mode is None:
        raise ValueError(f"Invalid uniquification mode "
                         f"{uniquification_mode_str}")
    uniquification_pass(main, uniquification_mode)

    if get_compile_dir() == 'callee_file_dir':
        (_, filename, _, _, _, _) = inspect.getouterframes(inspect.currentframe())[1]
        file_path = os.path.dirname(filename)
        file_name = os.path.join(file_path, basename)
    else:
        file_name = basename

    if output == 'verilog':
        suffix = "v"
        # Handle the case when DefineFromVerilogFile is used with a system
        # verilog file
        if hasattr(main, "verilog_file_name") and \
                os.path.splitext(main.verilog_file_name)[-1] == ".sv":
            suffix = "sv"
        write_file(file_name, suffix, verilog.compile(main))
    elif output == 'blif':
        write_file(file_name, 'blif', blif.compile(main))
    elif output == 'firrtl':
        write_file(file_name, 'fir', firrtl.compile(main))
    elif output == 'coreir':
        __compile_to_coreir(main, file_name, opts)
    elif output == 'dot':
        write_file(file_name, 'dot', dot.compile(main))
    else:
        raise NotImplementedError(f"Backend '{output}' not supported")

    if hasattr(main, 'fpga'):
        main.fpga.constraints(file_name);
