# Basis-mixture extremals for the sine transform

Status: `partial_result_likely_valid`

Source: Gabriel Maresch and Franz E. Schuster, “The Sine Transform of
Isotropic Measures,” arXiv:1207.7266, IMRN 2012, pp. 717–739.

The source conjectures that, among even isotropic measures on the sphere,
cross measures precisely maximize the polar sine-transform volume and
minimize the primal sine-transform volume.

This packet proves both inequalities, including rigidity, for the closed
convex hull of cross measures: every measure that is a probability mixture
of rotated cross measures.  Equivalently, the theorem applies whenever one
can couple the measure's directions into random orthonormal bases.  For a
discrete measure this has an exact fractional-perfect-matching criterion on
the hypergraph of orthonormal bases in its support.

The proof is short but genuinely two-sided.  Linearity of the sine transform
turns the body into a Minkowski integral of rotated copies of the cross body.
Minkowski's first inequality gives the primal-volume minimum, while strict
convexity of `t -> t^{-n}` in the polar-coordinate volume formula gives the
polar-volume maximum.  Equality in either argument, together with injectivity
of the sine transform on even measures, forces a single cross measure.

The full conjecture remains open: not every isotropic measure is a mixture of
cross measures (a regular-simplex frame is a basic obstruction).  The 2017
Grassmannian formulation identifies the sine case as the non-divisible-rank
case for which sharp reverse inequalities remain open.

Files:

- `solution_packet.pdf`: review document.
- `source_paper.pdf`: official arXiv source paper.
- `figures/open_problem_crop.png`: source page 14.
- `code/verify_basis_mixtures.py`: deterministic dimension-three numerical
  sanity checks (not used as proof).
- `verification_report.md`: proof and artifact audit.

Human-review recommendation: verify the equality passage for the Minkowski
integral and the use of sine-transform injectivity.  These are the only
non-algebraic rigidity inputs.
