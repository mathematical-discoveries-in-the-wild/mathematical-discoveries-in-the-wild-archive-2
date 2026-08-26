# Uniform transport Følner sets for virtually abelian groups

Status: candidate substantial partial theorem, likely valid, human review
required.

Source: Christian Rosendal, “Amenability, Optimal Transport and Abstract
Ergodic Theorems,” arXiv:2509.10686.

Problem 10.8 asks whether, for every finitely generated amenable group with no
nonzero homomorphism to `R`, the Wasserstein-almost-invariant probability from
Theorem 10.4 can be chosen as the uniform probability on a genuine finite
subset.

This packet proves an affirmative answer for every finitely generated
virtually abelian group satisfying the source's character hypothesis.  If
`A isomorphic to Z^d` is normal and finite index and `T` is a transversal, the
sets are explicit lattice boxes

`F_N = {a t : a in {0,...,N-1}^d, t in T}`.

For each fixed `g`, their transport defect is `O_g(1/N)`.  The key is that the
sum of the coset displacements is a homomorphism `Gamma -> A`, hence vanishes.
After collapsing the finitely many coset layers, the defect kernel has zero
mass and zero first moment, so it belongs to the square of the augmentation
ideal of `R[Z^d]`.  Convolution with a box turns every resulting second
difference into an `O(1/N)` Arens--Eells molecule.

Files:

- `solution_packet.pdf` — review-ready theorem and proof
- `main.tex` — packet source
- `source_paper.pdf` — source paper reconstructed from the run's ingested
  official arXiv TeX
- `figures/open_problem_crop.png` — source Problem 10.8 and its motivation
- `code/crop_open_problem.py` — reproducible crop script
- `verification_report.md` — proof and artifact checks

Human review should focus on the transfer identity, the signed layer-collapse
estimate, and the augmentation-ideal-square step.  The packet does not settle
the problem for arbitrary amenable groups.

