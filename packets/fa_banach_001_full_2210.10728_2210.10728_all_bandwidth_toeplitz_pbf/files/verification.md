# Verification report

Verdict: `likely valid candidate full solution`, pending expert review.

## Mathematical audit

1. **Edrei parameters.** The source uses the Edrei–Schoenberg theorem in the
   tetradiagonal Toeplitz case.  The identical finite-polynomial statement in
   bandwidth `r+2` gives positive roots `beta_1,...,beta_{r+1}` because the
   furthest subdiagonal is positive.
2. **Initial order.** With `S` the unilateral lower shift and `S* S=I`, direct
   multiplication gives
   `T=(S*+beta_1 I) product_{m=2}^{r+1}(I+beta_m S)`; the coefficients are the
   elementary symmetric polynomials in the betas.
3. **Local exchange.** Entrywise multiplication reduces
   `U^(m-1)L(beta_m)=B_(m-1)U^m` to one subdiagonal equality (true by the
   definition of `B`) and one diagonal equality.  The latter is exactly
   `h_n^(m)-beta_m h_(n-1)^m=h_n^(m-1)` and
   `h_(n+1)^m=h_(n+1)^(m-1)+beta_m h_n^m` after division.
4. **Strict positivity.** Complete homogeneous polynomials at positive betas
   are positive, so all quotients and all subdiagonal entries of every lower
   factor are strictly positive.  The final upper diagonal is also positive.
5. **Scope.** Repeating the local identity gives exactly `r` unit lower
   bidiagonal factors followed by one upper bidiagonal factor—the PBF order
   used by the source.  Taking `r=3` is the pentadiagonal question.

## Exact verifier

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2210.10728_all_bandwidth_toeplitz_pbf/code/verify_pbf.py
```

The verifier uses `Fraction` arithmetic, constructs the proposed factors, and
compares their product entrywise with twelve-by-twelve Toeplitz leading
truncations.  It checks five bandwidth/root cases (including repeated roots)
from one through five subdiagonals and asserts strict positivity of every
factor parameter.  It is a normalization sanity check, not a substitute for
the symbolic proof.

## Novelty audit

Search date: 2026-08-12.  Sources: arXiv search/full text and the run's cheap
indexes.  Queries covered the exact source title and question, pentadiagonal
Toeplitz PBF, arbitrary banded Toeplitz bidiagonal factorization,
quotient–difference refactorization, complete homogeneous polynomials, and
branched continued fractions.  arXiv:2412.03694 and arXiv:2603.21345 are later
papers on branched/MOP bidiagonal factorizations, but neither search result nor
source inspection produced the exact Toeplitz theorem or formula here.

Novelty confidence: moderate.  Mathematical confidence: high.  Human-review
recommendation: **prioritize review**, especially the exact orientation of the
source's PBF convention and the invocation of the general finite-polynomial
Edrei–Schoenberg classification.
