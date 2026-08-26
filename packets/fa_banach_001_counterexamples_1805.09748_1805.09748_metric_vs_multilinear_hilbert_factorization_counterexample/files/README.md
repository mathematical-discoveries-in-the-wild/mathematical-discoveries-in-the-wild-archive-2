# Counterexample packet: metric versus multilinear Hilbert factorization

Status: `candidate_counterexample_likely_valid`

Source: Maite Fernández-Unzueta and Samuel García-Hernández, *Multilinear
Operators Factoring through Hilbert Spaces*, arXiv:1805.09748, Questions 1--2
in Section 2.2 (printed pages 7--8).

## Result

Both questions receive negative answers over the real scalars.

- For the canonical bilinear tensor map
  `J_m: ell_1^m x ell_1^m -> ell_1^{m x m}`, the packet proves
  `Gamma(J_m)=m` but
  `gamma_2^Lip(f_{J_m}) <= 120 sqrt(2m)`.  At `m=2^15`, the latter bound is
  `30720 < 32768`, so the comparison map is not an isometry.  The norm gap is
  unbounded with dimension.
- A weighted diagonal sum of these maps gives one bounded bilinear operator
  `T` such that `gamma_2^Lip(f_T) <= 1` while `T` does not belong to the
  multilinear Hilbert-factorization ideal `Gamma`.  Thus metric Hilbert
  factorization of the associated Segre operator does not imply multilinear
  Hilbert factorization.

The main new device is an explicit quadratic Hilbert embedding of the real
rank-one cone.  It identifies the simultaneous sign ambiguity in normalized
rank-one factors and has distortion `O(sqrt(m))`.  A Rademacher average gives
the exact multilinear lower bound `m`.

## Files

- `main.tex`: self-contained proof and bounded novelty audit.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop_page7.png` and
  `figures/open_problem_crop_page8.png`: source evidence for both questions.
- `code/check_rank_one_factorization.py`: random numerical sanity checks for
  the proved inequalities; the code is not part of the proof.
- `verification.md`: algebraic, computational, and final render audit.
- `tmp/`: LaTeX intermediates and rendered source pages.

## Verification

The proof was audited algebraically in four stages:

1. normalized rank-one factors are stable modulo simultaneous sign, with
   `rho <= delta <= 8 rho`;
2. the quadratic feature turns that quotient metric into a Hilbert metric with
   the displayed dimension loss;
3. adjoining the radial coordinate gives the explicit constants
   `Lip(F_m) <= 24 sqrt(2)` and `Lip(F_m^{-1}) <= 5 sqrt(m)`;
4. the diagonal sum is well-defined because each block feature is injective,
   and the diagonal projection of the projective tensor product is
   contractive.

Run the independent sanity check with:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1805.09748_metric_vs_multilinear_hilbert_factorization_counterexample/code/check_rank_one_factorization.py
```

Human review should focus on Lemmas 1--2 and on the global definition of the
inverse map in Theorem 6. The result is explicitly real-scalar; a complex phase
analogue is not claimed.

## Novelty status

The run indexes, exact question phrases, arXiv/web search, and the four works in
the source paper's OpenAlex citation record were checked on 2026-08-09. No
later answer to either question was found within those bounds. Novelty is
plausible, not certified.

Ledger:
`runs/fa_banach_001/ledger/results/1805.09748_metric_vs_multilinear_hilbert_factorization_counterexample.json`
