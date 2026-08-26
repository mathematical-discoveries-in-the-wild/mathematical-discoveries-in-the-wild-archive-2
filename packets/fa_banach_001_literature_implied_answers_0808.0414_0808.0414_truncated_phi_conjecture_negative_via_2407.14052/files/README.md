# Maz'ya's critical uniform-truncation conjecture: full negative answer

Status: `literature_implied_answer (full negative)`

Source: Vladimir Maz'ya, *Estimates for differential operators of vector
analysis involving L1-norm*, arXiv:0808.0414 (2008), conjecture after
Theorem 1 on PDF page 2.

Supporting papers:

- Dmitriy Stolyarov, *Fractional integration of summable functions: Maz'ya's
  Phi-inequalities*, arXiv:2109.08014 (whole-space answer).
- Dmitriy Stolyarov, *Maz'ya's Phi-inequalities on domains*,
  arXiv:2407.14052, Theorems 1.2–1.3 and Section 2 (hemisphere necessity).

## Result

The conjecture as originally written is false for every `n >= 2`. At the
critical exponent `p=n/(n-1)`, take

```text
Phi(v) = |v|^(p-1) v_1.
```

This function is positively `p`-homogeneous, Lipschitz on the sphere, and
has zero full-sphere mean. Nevertheless, a unit-mass mollifier concentrating
near the boundary of `B(0,1)` produces a nonzero hemisphere term of size
`c log m`. Subtracting a fixed unit-mass smooth bump makes the data mean zero;
the subtraction changes the nonlinear integral by only `O(1)`. Thus there
are smooth compactly supported `f_m` with mean zero and `||f_m||_1 <= 2` for
which

```text
| integral_{B(0,1)} Phi(grad Gamma*f_m) | -> infinity.
```

Since the source supremum includes `R=1`, this is a full counterexample.

## Literature distinction

arXiv:2109.08014 proves the later whole-space version. The source conjecture
is stronger because it asks for a uniform supremum over ball truncations.
arXiv:2407.14052 identifies hemisphere cancellation as the correct boundary
condition but does not explicitly connect that theorem back to the exact
2008 supremum formulation. The packet makes that implication and verifies
the required zero-mean correction.

## Files

- `main.tex`, `solution_packet.pdf`: statement, construction, and proof.
- `source_paper.pdf`: arXiv:0808.0414.
- `supporting_paper_2109.08014.pdf`: whole-space theorem.
- `supporting_paper_2407.14052.pdf`: domain theorem and necessity proof.
- `verification_report.md`: mathematical and artifact audit.

Ledger:
`runs/fa_banach_001/ledger/results/0808.0414_truncated_phi_conjecture_negative_via_2407.14052.json`.
