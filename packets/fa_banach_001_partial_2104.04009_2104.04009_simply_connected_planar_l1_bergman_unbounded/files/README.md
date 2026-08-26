# Complete simply connected planar theorem: endpoint Bergman unboundedness

## Source

- Paper: Gian Maria Dall'Ara, *Around L^1 (un)boundedness of Bergman and
  Szegő projections*
- arXiv: `2104.04009`
- Published version: *Journal of Functional Analysis* 283 (2022), Paper
  No. 109550
- Local source PDF: `source_paper.pdf`

## Classification

- Status: `candidate_partial_solution_likely_valid`
- Strength: complete solution for every simply connected planar domain of
  finite area, with no boundary assumptions.
- Relation to source: partial, because the source asks about every bounded
  domain in every complex dimension; multiply connected planar domains and
  dimensions at least two remain.
- This materially replaces the earlier rectifiable-boundary-arc result.

## Main theorem

Every simply connected planar domain of finite area has an `L^1`-unbounded
Bergman projection. In particular this holds for every bounded simply
connected planar domain, regardless of boundary regularity or accessibility.

## Stronger weighted obstruction

If `g` is zero-free and analytic on the disk and `|g|` is integrable, then
the ordinary disk Bergman projection is unbounded on
`L^1(D, |g| dA)`.

The proof assumes boundedness and obtains the necessary column estimate

```text
integral_D |K_D(z,a)| |g(z)| dA(z) <= C |g(a)|.
```

The global kernel lower bound first forces `inf_D |g| > 0`. Reusing that
lower bound and integrating the unweighted kernel exactly forces `|g|` to
grow uniformly like `-log(1-r^2)` on every circle. The analytic reciprocal
`1/g` then contradicts the maximum principle.

For a Riemann map `psi:D -> Omega`, take `g=psi'`. The derivative is
zero-free and belongs to `A^2(D)` because `Omega` has finite area.

## Files

- `main.tex`: complete proof and audit.
- `solution_packet.pdf`: compiled final packet.
- `verification.md`: independent step and scope verification.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: exact source theorem/question crop.
- `tmp/`: extraction, rendering, and LaTeX build artifacts.

## Reviewer focus

- Verify the single conformal weight `|psi'|`.
- Verify the normalized-indicator derivation of the column estimate.
- Verify the exact unweighted kernel-column integral.
- Verify the uniform reciprocal maximum-principle contradiction.
