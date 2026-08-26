# Polynomial CLTs for the canonical Gaussian weighted-shift measure

Result type: substantial partial result.

Status: candidate theorem, likely valid pending expert review.

Source paper:

- Frédéric Bayart, “Central limit theorems in linear dynamics,”
  arXiv:1304.2621; *Annales de l'Institut Henri Poincaré, Probabilités et
  Statistiques* 51 (2015), 1131--1158, DOI 10.1214/13-AIHP585.
- Open problem: Question 4.6 on source PDF page 30.

## Claimed contribution

Let `B_w` be a bounded backward weighted shift on `ell^p(N_0)`, let
`W_n=w_1...w_n`, and assume

    sum_n W_n^{-p} < infinity.

Over either the real or complex scalar field, the packet constructs the canonical Gaussian measure given by the law of

    X=(W_n^{-1} gamma_n)_{n>=0},

where the `gamma_n` are independent standard real Gaussians in the real case
and standard circular complex Gaussians in the complex case.  This measure is
`B_w`-invariant, strongly mixing, and has full support.  The packet proves
that every continuous real polynomial on the underlying real space of `ell^p`
belongs to every finite
`L^q` of this measure and satisfies the centered square-root central limit
theorem, possibly with zero limiting variance.

This completely answers the weighted-shift half of Question 4.6.  It also
weakens the hypothesis in Corollary 4.4: the source assumes
`W_n >= C n^alpha` for some `alpha>1/p`, which implies the summability above,
whereas the new proof only needs the summability condition itself.

## Proof mechanism

The orbit process is a nonlinear Bernoulli shift.  Replacing one Gaussian
innovation changes exactly one coordinate of the Banach-space input.  A
coordinatewise Taylor expansion reduces the physical-dependence coefficient
to diagonal coefficients of the derivatives of the polynomial.  For a
continuous `r`-linear form on `ell^p`, those diagonal coefficients lie in
`ell^{p/(p-r)}` when `r<p`, and are bounded when `r>=p`.  Hölder's inequality
then pairs them with `(W_n^{-r})`, while fixed-degree Gaussian polynomial norm
equivalence handles the random derivative coefficients.  The physical
dependence coefficients are summable, so the theorem of El Machkouri--Volný--Wu
applies.

## Why the packet is partial

Question 4.6 also asks for the analogous assertion for parabolic composition
operators on `H^2(D)`.  The source's parabolic construction has only
individual translation decay of order `n^{-beta}` for `beta<1`; its linear
CLT uses a cancellation estimate that does not survive a polynomial Taylor
expansion.  Neither the Gaussian eigenvector-field route nor the source's
Bernoulli coding supplied summable physical dependence for nonlinear
polynomials.  That half remains open here.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `supporting_clt_1109.0838.pdf`: the physical-dependence CLT reference.
- `figures/open_problem_crop.png`: Corollaries 4.4--4.5 and Question 4.6.
- `verification.md`: proof audit and eight focused attempts.
- `tmp/`: LaTeX build and visual-QA artifacts.

## Novelty check

On August 11, 2026, the run indexes and bounded exact-question, exact-title,
author, weighted-shift, Gaussian-measure, polynomial-CLT, and parabolic-
composition searches found the source paper and general physical-dependence
or linear-dynamics references, but no later paper resolving Question 4.6 or
stating this weighted-shift theorem.  Novelty confidence is moderate pending
a specialist citation search.

## Human review focus

Review the uniform Gaussian coefficient-deletion estimate, the diagonal
multilinear lemma for real `ell^p` via complexification, and the passage from
summable physical dependence to the zero-variance case.  The parabolic half
is explicitly not claimed.
