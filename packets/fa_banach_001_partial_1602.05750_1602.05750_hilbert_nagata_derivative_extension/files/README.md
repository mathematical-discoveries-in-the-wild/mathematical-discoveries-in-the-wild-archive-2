# Hilbert–Nagata derivative-preserving extensions

This packet gives a substantial positive subcase of Question 1.3 in Martin
Koc and Jan Kolář, *Extensions of vector-valued functions with preservation of
derivatives* (arXiv:1602.05750).

For a closed finite-Nagata subset `F` of a separable real Hilbert space `H`, an
arbitrary map `f : F -> Y`, and a Baire-one prescribed derivative
`L : F -> L(H,Y)`, the packet constructs an extension that:

- has all general Koc–Kolář extension properties and is `C^infinity` off `F`;
- preserves the full strict-derivative conclusion of Theorem 1.1(vii);
- is globally Lipschitz whenever `f` is globally Lipschitz and `L` globally
  bounded, proving the global half of (viii);
- satisfies a uniform scaled-local version: local data on `B(a,R) cap F` give
  a Lipschitz extension on `B(a,theta R)`, where `theta` depends only on the
  Nagata data.

The new geometric lemma combines Basso's bounded-multiplicity finite-Nagata
Whitney cover (arXiv:2310.13554, Proposition 3.1) with the quantitative smooth
Lipschitz approximation theorem of Azagra–Ferrera–López-Mesas–Rangel
(arXiv:math/0602051, Theorem 1). It produces a locally finite smooth partition
with

`sum_i ||D phi_i(x)|| <= C / dist(x,F)`.

The exact local source clause—Lipschitz on every `B(a,r)` for `r<R`—is not
claimed. The finite-dimensional proof closes that step by compactness; the
noncompact deep-interior region of an infinite-dimensional Hilbert ball is the
remaining obstruction.

## Files

- `main.tex` / `solution_packet.pdf`: theorem, proof, limitations, and
  references.
- `verification.md`: adversarial proof audit and visual-verification record.
- `source_paper.pdf`: arXiv:1602.05750.
- `supporting_paper_2310.13554.pdf`: finite-Nagata Whitney cover.
- `supporting_paper_math_0602051.pdf`: smooth Lipschitz approximation.
- `figures/open_problem_crop.png`: Theorem 1.1(vii),(viii) and Question 1.3
  from source PDF page 2.
- `../../../../attempts/1602.05750_hilbert_nagata_derivative_extension_attempts.md`:
  seven focused attempts, including the deep upgrade attempt on the full local
  clause.

## Status

`partial_result_likely_valid (separable Hilbert ambient: full strict and global
Lipschitz conclusions; scaled local conclusion)`.

Human functional-analysis review is recommended, especially for the smooth
partition's local-finiteness step and the non-tangential boundary estimate.

