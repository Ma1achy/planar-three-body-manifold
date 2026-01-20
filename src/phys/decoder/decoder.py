# Main entry decode(x10, view_spec) -> SliceResult: uses a chart to create an initial-guess State, then runs constraint projection, then canonicalizes the result. Should return rich diagnostics on failure (residual norms, which constraint failed, etc.).
# class Decoder: x10 -> state (chart -> projector -> canonicalize)
