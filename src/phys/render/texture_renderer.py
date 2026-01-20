# Orchestrates the full UV→x10→decode→simulate loop and writes results into texture arrays with masks and diagnostics channels. This is the “main driver” for producing textures, and it should call into decoder/sim rather than re-implementing any physics.
# class TextureRenderer: orchestrate full render loop -> textures + masks
