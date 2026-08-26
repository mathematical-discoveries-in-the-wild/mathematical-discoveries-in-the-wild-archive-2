# Alternating coordinate-block counterexample

Status: `full_counterexample_pending_human_review`

Conjecture 2.5 of arXiv:2301.03365 is false under the precise
strict-diagonal-dominance condition in Definition 2.4.

On `ell_2`, partition the indices into blocks
`I_k={k^2,...,(k+1)^2-1}` and, for `n in I_k`, define

- `tau_n=e_k`;
- `f_n=(-1)^(n-k^2)e_k^*`.

The alternating rank-one terms in each odd block sum to the `k`th coordinate
projection, so the ordered frame operator is the identity. Also
`inf_n |f_n(tau_n)|=1`. But every finite partition puts two indices from some
growing block in the same class. Their interaction has modulus one, already
equal to the diagonal coefficient, so strict diagonal dominance fails.

The paper prints “ARBs” in the conjecture although it defines “ARS” and uses
ARS terminology elsewhere. The counterexample is robust to this typo: two
indices in the same block have identical vectors, so no class containing both
can be a Riesz sequence under the usual interpretation either.

The example is not intrinsically localized and does not contradict Theorem
2.7.

## Files

- `main.tex`, `solution_packet.pdf`: complete proof, terminology audit,
  limitations, and novelty scope.
- `source_paper.pdf`: arXiv:2301.03365.
- `figures/open_problem_crop.png`: source Definition 2.4 and Conjecture 2.5.
- `verify_finite_blocks.py`: exact finite sanity checks; not needed by the
  proof.
- `references.md`, `verification_report.md`: search and QA records.

## Human review

- [ ] A human expert has independently checked the proof, interpretation, and
  novelty status.
