# Verification report

Verdict: likely valid candidate full solution, pending expert review.

## Scope match

The source paper proves nonemptiness for triples of `2 x 2` Hermitian
matrices and describes the arbitrary-size version for three matrices as a
conjectural extension. The packet keeps the number of matrices fixed at three,
allows every finite matrix size `n`, and uses the same Pauli matrices as the
source's localizer.

## Proof audit

The argument was checked at the following points.

1. **Boundary gap.** With `K = sum A_j tensor sigma_j`,
   `F_t(omega)=tK-R I tensor (omega dot sigma)` satisfies
   `||F_t(omega)v|| >= (R-t||K||)||v||`. Thus the entire boundary homotopy is
   invertible whenever `R>||K||`.
2. **Bundle rank.** If the localizer is invertible on the closed ball, its
   negative spectral projection is continuous. The boundary homotopy ends at
   a matrix having exactly `n` negative eigenvalues, hence the bundle rank is
   `n` everywhere on the connected ball.
3. **Boundary class.** The negative eigenspace of
   `-R I tensor (omega dot sigma)` is `C^n tensor H_+(omega)`. The packet gives
   explicit north and south frames for `H_+`; their equatorial transition is
   `exp(-i phi)`. The determinant transition for `n` copies is therefore
   `exp(-in phi)`, of nonzero winding.
4. **Contradiction.** A complex vector bundle on the contractible ball is
   trivial, so its determinant restricts to a trivial line bundle on the
   sphere. This contradicts item 3.
5. **Closed bound.** The contradiction gives a zero in every ball of radius
   `R>||K||`. Zeros chosen for radii decreasing to `||K||` have a convergent
   subsequence, and singularity is closed under matrix limits.

No external classification theorem beyond the elementary triviality of
bundles over a contractible base is needed; the nonzero boundary class is
computed directly from transition functions.

## Computational sanity check

The included script samples random Hermitian triples for sizes `1` through
`5`, checks the explicit boundary lower bound and constant negative rank on a
grid of homotopy parameters and sphere points, and independently unwraps the
determinant transition phase for `n` copies of the Hopf line.

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2602.15302_three_matrix_clifford_spectrum_nonempty/code/verify_boundary_obstruction.py
```

These finite tests are not used as proof.

Output on 2026-08-09:

```text
gap_checks=3600
rank_checks=3600
hopf_windings=-1,-2,-3,-4,-5
status=PASS
```

## Principal review risk

The main issue for expert review is not an algebraic estimate but the scope
and convention: confirm that the arbitrary-size conjecture intended in
arXiv:2602.15302 fixes the standard irreducible Pauli Clifford representation.
For any other irreducible complex three-generator representation the same
argument has the opposite or transformed Hopf class, still nonzero; direct
sums are singular whenever one summand is singular.
