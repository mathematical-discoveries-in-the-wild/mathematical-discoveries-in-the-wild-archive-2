# Verification

## Proof audit

- For `lambda in rho(T)`, bounded-below control of the restriction follows directly from the norm of `(T-lambda)^{-1}`.
- Surjectivity of the quotient pencil is checked by lifting with `(T-lambda)^{-1}`.
- Both directions of the canonical quotient/cokernel isomorphism are written explicitly and checked for well-definedness.
- Componentwise defect constancy uses the standard local constancy of the extended index on the upper semi-Fredholm set; every pencil in the relevant resolvent component lies in that set.
- The realization uses standard spectra of the bilateral and unilateral shifts. Pairwise disjoint closed disks ensure blocks belonging to other holes are invertible at `lambda in D_j`.
- The restriction of the Jordan extension to `N_d direct-sum {0}` is exactly the shift model, while its ambient spectrum equals the diagonal spectrum.
- Nonnormality follows because the top-left blocks of `J*J` and `JJ*` differ by the identity.

## Scope audit

- The packet claims an exact invariant for a fixed pair `(T,M)` and universal realization for a specially constructed fixed nonnormal `T`.
- It does not claim to classify invariant subspaces or realizable hole profiles for every prescribed operator.

## Artifact checks

- `source_paper.pdf` SHA-256: `4feced1f756a3f06eb9b97e4a1a14737a1e636006f222f1e8cf36801965b831b`.
- `supporting_barnes_2007.pdf` SHA-256: `e3bfe92a94bb2d87f686c081ceba12f55e6a534528a96904fb81ceb0566ac42b`.
- `solution_packet.pdf` SHA-256: `8ed144b6d74e32ef20bdf55fb6e4fbcc9964d124d07f83e6eb58555cf975a134`.
- `latexmk` completed with no unresolved-reference, overfull-box, or underfull-box warnings.
- All four pages were rendered and visually inspected; theorem blocks, equations, proof endings, references, margins, and page breaks are clean.
