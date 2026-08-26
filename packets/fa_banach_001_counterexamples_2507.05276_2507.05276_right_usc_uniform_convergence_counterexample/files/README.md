# Counterexample packet: right-USC does not give bounded-set uniform convergence

Status: `candidate_counterexample_likely_valid`

Source: Hassan Khandani, *A Study of Kirk's Asymptotic Contractions via
Leader Contractions*, arXiv:2507.05276v1 (2025).

## Result

This packet gives a complete bounded ultrametric space, a continuous countdown
map `T`, and a control function `phi` that is positive, strictly below the
identity, and upper semicontinuous from the right.  Taking `phi_n = phi` for
every positive integer `n`, all three hypotheses of source Theorem 3.11 hold.
The map has the unique fixed point `x_0`, every orbit reaches it in finitely
many steps, and `T` has a complete graph.  Nevertheless, the iterates do not
converge uniformly on the bounded set `X`.

Thus the example directly disproves the uniform-convergence conclusion of
Corollary 3.9 and the uniform clause of Theorem 3.11.  It does not contradict
their pointwise-convergence or fixed-point clauses.

## Mechanism

The source's key Lemma 3.8 is false: a positive function that is only lower
semicontinuous from the right need not have positive infimum on a compact
interval.  In the counterexample, the gaps `t - phi(t)` tend to zero along
realized distances approaching `1` from the left.  Right semicontinuity at
`1` cannot see that approach.  Each individual orbit has a finite countdown,
but the countdown lengths are unbounded over the bounded space.

## Verification

The proof in `main.tex` is exact.  The auxiliary exact-arithmetic checker

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2507.05276_right_usc_uniform_convergence_counterexample/code/verify_counterexample.py
```

checks all ultrametric triples through index 80, the contraction inequalities
for iterates 1 through 40, and explicit non-uniformity witnesses for iterates
0 through 40.  These finite checks guard against transcription mistakes and
are not a substitute for the proof.

## Novelty check

On 2026-08-09, bounded searches covered the exact source title together with
`counterexample` and `uniform convergence`, and close phrases combining
`right upper semicontinuity`, `Kirk asymptotic contractions`, `Leader
contraction`, and `uniformly on bounded`.  The searches found the source,
earlier positive fixed-point literature, and later adjacent asymptotic-
contraction papers, but no prior counterexample to Corollary 3.9 or Theorem
3.11.  Novelty confidence is therefore moderate, not definitive.

## Files

- `main.tex`: full counterexample and verification discussion.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: local copy of arXiv:2507.05276v1.
- `figures/open_problem_crop.png`: source page 9, containing Lemma 3.8 and
  Corollary 3.9.
- `figures/source_theorem_crop.png`: source page 10, containing Theorem 3.11.
- `code/verify_counterexample.py`: finite exact-arithmetic sanity checks.

## Human review recommendation

Check first that the convention in Theorem 3.11 is `n >= 1`, as required by
its strict contraction inequality.  Then verify the step-function control at
the breakpoints `r_k` and at `1`, and the formula
`T^n x_k = x_max(k-n,0)`.  These checks establish every hypothesis and the
failure of uniform convergence.
