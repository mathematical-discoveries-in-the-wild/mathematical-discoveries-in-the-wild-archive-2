# No finite homogeneous constant on the stated Neumann strip

Status: candidate counterexample and full negative answer to the optimal-
constant question in Chapter 4 of arXiv:2106.08625, pending expert review.

The source asks for the best constant in its estimate

    N_-(H_{A,V}) <= C ||V||_{L^1(R;L^infinity(0,d))}.

For the standard gauge-covariant magnetic Neumann realization on the stated
strip `S=R x (0,d)`, no finite such constant exists.  The Aharonov--Bohm pole
is `(0,0)`, which lies on the boundary rather than in the strip.  Hence
`theta=Arg(x+iy)` is single-valued on `S` and

    A_phi = phi grad(theta)

is globally gauge-removable.

For any `epsilon>0`, choose `L>2/epsilon`, place
`V=epsilon` on the unit longitudinal interval `[L+1,L+2]`, and use the
constant transverse mode multiplied by a tent function with ramps of length
`L`.  After the gauge transformation, its exact quadratic-form value is

    2/L - epsilon < 0.

Thus the operator has a negative eigenvalue for every `epsilon>0`, while
`||V||_X=epsilon`.  Choosing `epsilon<1/C` contradicts every proposed finite
constant `C`.

The counterexample uses the mathematically standard magnetic Neumann form.
If the source intended ordinary, non-gauge-covariant normal derivatives, it
does not specify a standard self-adjoint magnetic realization; that would be
a different and presently ill-posed boundary problem.  The packet does not
address an Aharonov--Bohm pole lying strictly inside the waveguide or mixed
boundary conditions.

See `solution_packet.pdf` for the exact theorem, proof, source screenshots,
novelty search, limitations, and reviewer checklist.

