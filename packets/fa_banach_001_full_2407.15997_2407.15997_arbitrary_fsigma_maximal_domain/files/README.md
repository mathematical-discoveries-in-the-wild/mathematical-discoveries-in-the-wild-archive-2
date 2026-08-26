# arXiv:2407.15997 — arbitrary F-sigma maximal domains

Status: `candidate_full_solution`, pending expert review.

Source: Mikhail Mironov and Jeet Sampat, *Jointly cyclic polynomials and
maximal domains*, arXiv:2407.15997v2, Problem 4.7 on printed page 13.

## Result

For every `F_sigma` subset `Gamma` of the unit circle there is a Banach space
`X` of holomorphic functions on the disk satisfying P1--P3 whose maximal
domain is exactly `D union Gamma`.  This affirmatively answers Problem 4.7 in
the Banach category, including the explicit dense countable example
`Gamma = Q/Z` mentioned by the authors.

## Main mechanism

For each boundary point `gamma`, the construction controls the pair

`(p(gamma), (p-p(gamma))/(z-gamma))`

in `C plus A_0`, where `A_0` is the space of analytic power series with a
`c_0` coefficient sequence.  The `c_0` condition excludes the boundary pole
and therefore prevents ghost vectors.  At the same time, Abel summation shows
that divided differences of standard boundary peak polynomials tend to zero
uniformly on every closed boundary set away from the peak.  An `l_1` sum over
closed layers of `Gamma` then realizes an arbitrary `F_sigma` set.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: self-contained packet source.
- `source_paper.pdf`: official arXiv v2 PDF.
- `figures/open_problem_crop.png`: source Problem 4.7 and surrounding remark.
- `verification.md`: mathematical and novelty audit.
- `code/check_peak_coefficients.py`: finite numerical sanity check of the
  peak divided-difference coefficients.
- `code/crop_source.py`: reproducible evidence crop.

Associated attempt:
`attempts/2407.15997_arbitrary_fsigma_maximal_domain_full.md`.

