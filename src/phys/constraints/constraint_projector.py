# Uses ResidualModel + NewtonSolver to project an initial guess onto the manifold required by the view (always COM/P; optionally E/L/scale). Decides which degrees of freedom are adjustable and returns the projected state plus solver diagnostics.
# class ConstraintProjector: project guess -> satisfy constraints
