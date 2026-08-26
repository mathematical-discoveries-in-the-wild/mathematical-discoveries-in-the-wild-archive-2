# Counterexample to extrapolation without operator-norm BMO

Status: `counterexample_likely_valid`

Source: Tao Mei, *An Extrapolation of Operator Valued Dyadic
Paraproducts*, arXiv:0709.4229, Open Question on PDF page 9.  The question
asks whether the hypothesis
`phi in BMO_M(T,M)` can be removed from Theorem 1.2, i.e. whether boundedness
of the left operator-valued dyadic paraproduct on one noncommutative `L^p`
forces boundedness on every `L^p`.

## Claimed contribution

The answer is no.  In `M=B(H)` for

```text
H = direct_sum_{n>=1} C^n,
```

put an `n x n` row-Rademacher symbol on the dyadic atom

```text
I_n = [2^(-n), 3*2^(-(n+1))).
```

With local Rademachers `r_(n,k)` and matrix units `e_(1,k)^(n)`, set

```text
phi = sum_n sum_(k=1)^n r_(n,k) e_(1,k)^(n).
```

The intervals are disjoint and exponentially short, so `phi` is Bochner
integrable in operator norm (indeed in every finite `L^q(T;M)`).  Martingale
orthogonality and

```text
||e_(1,k) x||_2 = ||e_(k,k) x||_2
```

give the exact global bound `||pi_phi||_(2->2) <= 1`.

For the test `f_n=1_(I_n) P_n`, where `P_n` is the identity of the nth
matrix corner,

```text
||pi_phi f_n||_p / ||f_n||_p = n^(1/2-1/p).
```

This diverges for every fixed `p>2`, so the same paraproduct is bounded on
`L^2` and unbounded on every `L^p`, `p>2`.  Moreover
`||phi||_(BMO_M)=infinity`, as the oscillation on `I_n` is exactly `sqrt(n)`.

The packet also records a finite tracial variant using the product algebra
`prod_n M_n` with a weighted normalized trace.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/0709.4229_no_bmo_extrapolation_counterexample/code/verify_counterexample.py
```

The checker validates the dyadic interval geometry, local conditional-mean
identities, random finite-block `L^2` contractions through `n=8`, singular
values, and exact witness ratios.  The analytic proof is self-contained and
does not rely on numerical evidence.

## Novelty and review

The bounded search on 2026-08-11 covered all cheap run indexes, exact arXiv-id
and title matches, the source question, the phrases “operator-valued
paraproduct bounded L2 unbounded Lp” and “extrapolation without BMO,” and later
citing work.  Wei--Zhang, arXiv:2401.08729, still describe the general `L^2`
boundedness characterization as open and retain the strong BMO hypothesis in
their extrapolation theorem.  No matching counterexample was found.  This is
negative search evidence, not a priority claim.

Human review should focus on the global martingale-difference bookkeeping and
the `L^2` orthogonality argument.  The construction otherwise reduces to
one-line Schatten norm computations.

Files:

- `source_paper.pdf`: official arXiv PDF.
- `source_material/source_paper.tex`: ingested source TeX.
- `figures/open_problem_crop.png`: real full-width crop from source PDF page 9.
- `main.tex`, `solution_packet.pdf`: proof packet.
- `code/make_source_crop.py`: reproducible source crop.
- `code/verify_counterexample.py`: finite-block checks.
- `verification.md`: build and review record.
