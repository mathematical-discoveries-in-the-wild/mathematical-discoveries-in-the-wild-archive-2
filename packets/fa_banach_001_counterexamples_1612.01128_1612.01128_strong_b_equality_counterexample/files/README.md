# A determinant-one counterexample to the proposed strong-(B) equality case

Status: `counterexample_likely_valid`

Source target: Shiri Artstein-Avidan and David Katzin, *Isotropic Measures
and Maximizing Ellipsoids: Between John and Loewner*, arXiv:1612.01128,
Conjecture 4.1, PDF pages 8--9.

Conjecture 4.1 proposes log-concavity of

`phi(t) = vol_n(e^{t Lambda} K intersect B_2^n)`

and states that midpoint equality occurs only when `K subset B`, `B subset
K`, or `Lambda` is scalar.  The equality classification is false, even for
an unconditional centrally symmetric box and a nonzero trace-zero diagonal
matrix.

Take

`K=[-1/2,1/2] x [-2,2] x [-3,3]` and
`Lambda=diag(0,1,-1)`.

For every `s in [0,1]`, the last two half-widths of `e^{s Lambda}K` are at
least one.  Inside the unit ball those constraints are redundant, hence

`e^{s Lambda}K intersect B = {x in B: |x_1| <= 1/2}`.

Thus `phi(s)=11 pi/12` throughout `[0,1]`, so equality holds at `t=1`.
Yet neither containment holds and `Lambda` is nonscalar.  Its trace is zero,
so the counterexample directly survives the determinant-one restriction
used in the paper's uniqueness argument.

The packet proves a general constant-intersection family and records a deep
upgrade check.  Equal overlap along this path does not settle uniqueness of
the maximum intersection ellipsoid: for the displayed box, the unit ball is
not a local maximizer, as an explicit positive first variation shows.  The
log-concavity inequality itself is also not refuted; the example satisfies
it with equality on an interval.

Files:

- `solution_packet.pdf`: exact source statement, proof, general family, and
  scope analysis.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: complete Conjecture 4.1 and its use in
  Proposition 4.2.
- `code/verify_counterexample.py`: deterministic transcription checks.
- `code/crop_open_problem.py`: reproducible source crop.
