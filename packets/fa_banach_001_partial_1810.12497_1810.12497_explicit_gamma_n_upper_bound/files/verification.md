# Verification

Status: passed as a candidate partial result.

## Mathematical checks

- For the multiplicity-one coordinate tuple on `L^2([0,1]^n)`, the universal
  formula gives `gamma_n = (k_n^-(tau))^n` because the multiplicity integral
  is exactly one.
- The dyadic conditional-expectation projections are finite rank, nested, and
  converge strongly to the identity.
- On each cell and for each coordinate, the commutator is exactly one
  skew-symmetric rank-two block with both singular values `1/(sqrt(12) N)`;
  it vanishes on the orthogonal complement of that block.
- Orthogonality of the cell decomposition therefore gives exactly `2 N^n`
  equal nonzero singular values, with no omitted cross-cell terms.
- Substitution into the paper's Lorentz `(n,1)` norm and
  `sum_{r<=M} r^(-1+1/n) ~ n M^(1/n)` gives the limiting modulus bound
  `n 2^(1/n)/sqrt(12)`.  Raising to the `n`th power gives
  `gamma_n <= 2 n^n / 12^(n/2)`.
- The rectangular calculation has the volume scaling forced by the universal
  formula.
- The shifted-Legendre recurrence coefficient was checked against the
  rank-two `r=0` calculation.  The displayed algebra proves that every
  integer `r>=1` gives a strictly larger constant when `n>=2`.
- The packet distinguishes the previously known positivity from the new
  explicit upper estimate.  It explicitly does not claim sharpness, a new
  numerical lower bound, or a full hybrid result.

## Computational checks

- `1810.12497_gamma_n_dyadic_check.py` reran successfully.
- It directly verified the local rank-two singular values.
- Direct Lorentz sums for `N=128` approach the exact limits for `n=1,2,3`;
  the resulting upper values are `1/sqrt(3)`, `2/3`, and `3 sqrt(3)/4`.
- Tensor-polynomial constants were checked for `n=2,...,6` and
  `r=0,...,10`; `r=0` matches the dyadic constant and every tested `r>=1`
  is strictly worse.  The packet contains the general symbolic proof.

## Source verification

- The locally compiled source paper has 25 A4 pages.
- Rendered source page 21 was visually inspected.  It contains Sample Open
  Problem 1 and explicitly asks for upper and lower bounds for `gamma_n`,
  `n>=2`, and for the analogous hybrid constants.

## Build and visual QA

- The final packet LaTeX log contains no warnings, overfull boxes, underfull
  boxes, undefined references, or errors.
- Final packet: 3 US-letter pages, 209595 bytes.
- All three packet pages were rendered at 130 dpi and visually inspected.
  The theorem, proof blocks, equations, scope statement, reference, and
  margins are clean; nothing is clipped or overlapped.
- Ghostscript text extraction finds the main theorem, higher-degree check,
  remaining-obstruction paragraph, and references.

## Artifact hashes

```text
source_paper.pdf                           a6b94d0d6022659185eb3fb554e4a48feea6563bf50f5d79d3bd2ad7f824d99d
source_question_page.png                   ee1bafef546e165b2bfc2b2582c2a6b83c998afc27a47f06ee24c3d6b098a92b
solution_packet.pdf                        65dcc42ab7d44ee1f1f191009caccd322b69f69be65ad0688e664ba68915b5d9
1810.12497_gamma_n_dyadic_check.py         27d4e03460405896c1da324804dbbc5710527154c9e552dc2b2379f788a3a995
1810.12497_gamma_n_dyadic_upper_bound_attempts.md
                                           63d484ca61671c8acc868e6cf14170d0014481121bdc0252f87afef90592fb2d
```
