# Verification report

Verdict: `candidate_counterexample_likely_valid` for Problem 2 of
arXiv:0801.1749.

## Proof audit

- For the probability measure
  `mu=(99/200)(delta_-1+delta_1)+(1/100)gamma`, translation averaging gives
  `Up(x)=int p(x+t) dmu(t)`.  Hence every polynomial strictly positive on
  the real line is sent to another strictly positive polynomial.
- The translation identity and Gaussian moment formula give the formal
  constant-coefficient symbol
  `M(z)=(99/100)cosh(z)+(1/100)exp(z^2/2)`, which has infinitely many
  nonzero coefficients.
- Every finite moment form is strictly positive definite: for a nonzero
  polynomial `q`, its value is `int q^2 dmu >= (1/100) int q^2 dgamma > 0`.
  Thus the example is not a finite-support boundary point of the moment
  cone.
- Since `M(0)=1`, its formal reciprocal `N` exists.  On every polynomial,
  both `M(D)` and `N(D)` truncate, so `N(D)` is the genuine two-sided inverse
  of `M(D)` on `R[x]`.
- Independent exact symbolic arithmetic verifies
  `N(D)x^6=x^6-15x^4+(747/10)x^2-3027/50`.  Under `y=x^2`, the integer-scaled
  cubic is `50y^3-750y^2+3735y-3027`, with discriminant
  `-668917845000`.  It therefore has a nonreal conjugate pair.  Since `x^6`
  is hyperbolic, the inverse is not a hyperbolicity-preserver.

## Upgrade attempts

1. The seed two-point measure gives `U_0=cosh(D)`.  Its inverse sends `x^6`
   to `x^6-15x^4+75x^2-61`; the associated cubic factors as
   `(y-1)(y^2-14y+61)`, immediately displaying nonreal roots.
2. The deep upgrade mixes one percent standard Gaussian measure into the
   seed.  This removes every finite-order Hankel degeneracy while preserving
   the inverse obstruction, producing a robust strict-interior example.

## Novelty check

A bounded primary-source search used the exact wording of Problem 2 and the
terms `positivity-preserver`, `hyperbolicity-preserver`, inverse, moment
measure, `cosh(D)`, and `sech(D)`.  It found the source and later
moment/generator work including arXiv:2308.10455, but no primary source
stating this counterexample.  Correctness confidence is high and novelty
confidence is moderate.

## Reproducibility and visual checks

- `code/verify_counterexample.py` reproduces the reciprocal symbol through
  degree six, the inverse image of `x^6`, and the exact cubic discriminant.
- `latexmk` completed with resolved references and no overfull boxes,
  underfull boxes, or final logged warnings.
- The final packet contains three A4 pages.  Every page was rendered at 150
  DPI and inspected at original resolution.  The embedded source question,
  theorem, formulas, proof ending, references, margins, and page numbers are
  readable and unclipped.
- PDF text extraction finds `Theorem 1`, `Problem 2`, `strictly positive
  definite`, and the discriminant `-668917845000`.

## SHA-256

```text
2ceb70bdb27e7e2bab4efa34b604a32e8a6ffd05e18287d3e0f06bc770d96605  solution_packet.pdf
cb06ba6130e58d19a6e8c478834080f731acb85f09a118728e0b311cf83a83fd  source_paper.pdf
fff293f6e5525a44b6ac529d5e93b0b297b1f8fd470b7280429cd9f265ba3fb0  figures/open_problem_crop.png
28f9b775798e5cc1ba64b0a0e02296529e0dbb98254dc98d9622caac67336c41  code/verify_counterexample.py
```

## Human-review recommendation

Check the formal-series inverse convention from the source, the three
degree-six reciprocal coefficients, and the interpretation of negative
cubic discriminant.  Also repeat the primary-source novelty search before
public dissemination.
