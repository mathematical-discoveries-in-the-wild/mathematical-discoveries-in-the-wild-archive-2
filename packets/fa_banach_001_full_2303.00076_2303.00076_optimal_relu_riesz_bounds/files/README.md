# Full solution: exact Riesz bounds for the ReLU tent-function basis

Source: Cornelia Schneider and Jan Vybíral, *A multivariate Riesz basis of
ReLU neural networks*, arXiv:2303.00076, ACHA 68 (2024), article 101605.

Status: claimed full solution; likely valid, pending human review.

## Result

The exact optimal uniform spectral interval for the Gram matrices of

```text
{1} union {sqrt(3) C_k, sqrt(3) S_k : 1 <= k <= N}
```

is `[2/3, 3/2]`. Thus the source's lower bound `1/2` improves to the sharp
value `2/3`, while its upper bound `3/2` is already sharp. The same exact
Riesz bounds hold for the source's normalized multivariate system in every
dimension.

The unnormalized cosine and sine Gram blocks plotted in the source have exact
optimal uniform interval `[2/9, 1/2]`.

## Proof mechanism

After splitting indices by their 2-adic valuation, the normalized cosine Gram
kernel on odd indices is

```text
gcd(m,n)^4/(m^2 n^2)
  = product over odd primes p of p^(-2 |v_p(m)-v_p(n)|).
```

Each one-prime factor is the Toeplitz kernel `r^|a-b|`, whose exact form bounds
are `(1-r)/(1+r)` and `(1+r)/(1-r)`. Tensoring and evaluating the odd-prime
Euler products gives `2/3` and `3/2`. Finite rectangular prime-exponent grids,
with constant or alternating signs, approach both endpoints and prove
sharpness. The sine block is a diagonal sign conjugate of the cosine block.
The multivariate Gram operator splits into identical univariate blocks along
primitive lattice rays.

## Files

- `main.tex`: self-contained proof packet source.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv source PDF.
- `figures/open_problem_crop.png`: full-width crop of Theorem 2.2 and Remark
  2.3 on source PDF page 5, including the complete open question and Figure 3.
- `code/verify_bounds.py`: finite spectral, sign-similarity, and sharpness
  witness audit.
- `verification.md`: commands, output, scope, and review checklist.
- `tmp/`: LaTeX intermediates and rendered inspection pages.

## Novelty status

A bounded search through 2026-08-17 found no exact answer. The strongest
relevant follow-up, Kulbatov–Lang–Schneider–Vybíral, arXiv:2511.23179, proves
cosine/sine isospectrality and improves the lower estimate only to
`0.5787...`; it does not obtain `2/3` or prove optimality. This is a bounded
negative search, not an exhaustive novelty claim.

## Human review focus

Check the finite-support-to-finite-prime tensor identification, the explicit
two-stage sharpness limit, and the primitive-ray multivariate direct sum. The
computations are consistency checks only; the proof is analytic.
