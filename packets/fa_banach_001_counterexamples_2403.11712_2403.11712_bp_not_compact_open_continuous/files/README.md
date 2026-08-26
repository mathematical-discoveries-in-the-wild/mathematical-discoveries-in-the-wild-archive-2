# A bp-continuous functional that is not compact-open continuous

Source: Bernhard H. Haak and Markus Haase, *Vector-Valued Holomorphic
Functions and Abstract Fubini-Type Theorems*, arXiv:2403.11712v2.

Status: candidate full counterexample, likely valid.

## Result

Let `X=C([0,omega_1])`, `O=B_X`, and identify
`X*=M([0,omega_1])`.  Define

```text
Phi(f) = Df(0)({omega_1}),   f in H^infinity(O).
```

Then `Phi` is bp-continuous: derivatives of a bounded pointwise convergent
sequence converge weak-star, and every sequence of measures has jointly
countable support, making endpoint mass sequentially weak-star continuous.

It is not `tau_c`-continuous even on the unit ball.  The evaluation
functions `g_beta(x)=x(beta)` converge compact-open to `g_omega_1` as the
countable ordinals increase to `omega_1`, but `Phi(g_beta)=0` and
`Phi(g_omega_1)=1`.

This supplies the example explicitly requested in Remark 3.2(2) of the
source.

## Files

- `main.tex` -- complete proof and scope discussion
- `solution_packet.pdf` -- rendered solution packet
- `source_paper.pdf` -- official arXiv PDF
- `VERIFICATION.md` -- source, mathematical, build, and visual checks

Related attempt:

- `runs/fa_banach_001/attempts/2403.11712_bp_vs_compact_open_counterexample.md`

Ledger:

- `runs/fa_banach_001/ledger/results/2403.11712_bp_not_compact_open_continuous.json`

## Human review recommendation

Accept as a candidate full counterexample.  Check the countable-support
lemma for measures on `[0,omega_1]` and the compact-uniform convergence of
the evaluation net.
