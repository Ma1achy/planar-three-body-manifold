# Turns a ViewSpec into a fully wired ViewProgram by constructing the sampler, packer, decoder, simulator, and renderer dependencies. This is where you enforce consistent configuration and avoid ad-hoc object creation scattered across the codebase.
# class ViewCompiler: wires objects -> View_program
