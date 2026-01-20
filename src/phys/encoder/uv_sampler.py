# Enumerates pixel centers and maps them to (u,v) coordinates for a given resolution and UV range. Optionally supports tiling/chunk iteration for caching and parallelization later, but contains zero physics.
# class UVSampler: iterate pixels -> (i,j,u,v), tiling/chunking
