# A classical counterexample to the Lip_p state-span conjecture

Run: `fa_banach_001`

Agent: `agent_lane_14`

Status: `candidate_counterexample_likely_valid`

## Result

Conjecture 4.13 of Chirvasitu (arXiv:1407.0960, PDF page 23) predicts that the
states in the weak*-closed linear span of the `(Lip_p)`-isometric states
`S_p(A)` coincide with `S_p(A)`.  The packet disproves this for every
`p >= 1` using the regular action of the classical group `C3` on the
three-point path metric.

Haar measure has a whole relative neighborhood contained in `S_p(A)`, so
`S_p(A)` spans the entire finite-dimensional dual `A*`.  Yet the point mass at
the non-isometric three-cycle belongs to that span and is not in `S_p(A)`.
The proof also gives a family theorem for every faithful transitive
non-isometric finite classical action.

## Scope

This fully negates Conjecture 4.13.  It does not settle the paper's separate
earlier conjecture that the conjunction of all `(Lip_p)` conditions implies
`(D)`-isometry.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1407.0960_lipp_state_span_classical_counterexample/code/verify_c3_transport.py
```

The checker computes exact finite optimal-transport costs by min-cost flow for
the three spanning states at several exponents, verifies their nonzero
determinant, and checks the point-mass violation.

## Files

- `main.tex`: theorem, construction, and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv:1407.0960.
- `figures/open_problem_crop.png`: Definition 4.12 and Conjecture 4.13.
- `code/verify_c3_transport.py`: exact rational finite-transport checker.
- `code/crop_open_problem.py`: reproducible source-page crop.

## Review recommendation

Check the total-variation coupling estimate and the identification of states
of `C(C3)` with measures on `C3`.  The remaining steps are finite-dimensional
linear algebra and an explicit distance expansion.

