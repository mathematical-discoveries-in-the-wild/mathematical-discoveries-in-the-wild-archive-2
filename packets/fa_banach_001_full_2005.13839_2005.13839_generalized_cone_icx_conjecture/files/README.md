# Generalized-Cone Conjecture via Increasing Convex Order

Result type: full

Status: candidate full solution, likely valid pending expert review.

Source:

- Bernardo González Merino, “Estimating the average of functions with
  convexity properties by means of a new center,” arXiv:2005.13839v2;
  Annali di Matematica Pura ed Applicata 200 (2021), 2285–2304.
- DOI: 10.1007/s10231-021-01080-y.
- Conjecture: Conjecture 1.7, source PDF page 5.

## Claimed contribution

The packet proves Conjecture 1.7’s inequality in all dimensions. The paper’s
Theorem 1.1 reduces the problem to affine functions on truncated cones. If
the ratio of the two base radii is q, set a=q^n. The normalized axial
quantile is

    R_a(u) = ((1+(a-1)u)^(1/n)-1) / (((1+a)/2)^(1/n)-1).

The cone law R_0 and R_a cross exactly once at their common median 1.
The cone law also has the larger mean. These facts imply stop-loss, hence
increasing-convex-order, domination for every admissible convex function
simultaneously.

For n at least 2, the mean gap is strict unless a=0. Thus a strictly convex
integrand has the conjectured unique nontrivial equality case: a generalized
cone with an affine function vanishing at its nondegenerate base.

## Equality caveat

The source’s literal equality statement omits the normalization
f(x_C,f)>0. Without it, f=0 gives equality for every convex body, so the
stated “if and only if” is false. The paper introduces its extremal problem
with f(x_C,f)=k>0; the packet proves exactly that intended nontrivial
statement and records the zero-function degeneracy.

## Files

- main.tex: proof source.
- solution_packet.pdf: rendered proof packet.
- source_paper.pdf: official arXiv source paper.
- figures/open_problem_crop.png: Conjecture 1.7.
- code/verify_icx.py: symbolic identity check and numerical stress tests.
- verification.md: verification output and audit notes.
- tmp/: LaTeX and rendered-QA intermediates.

## Novelty check

On August 9, 2026, bounded searches used the exact title, arXiv id,
formula fragments, and the core terms “generalized truncated cone,”
“x_C,f,” and “convex order.” The arXiv and published journal versions
both retain Conjecture 1.7. No later proof or counterexample was found.
Crossref and OpenAlex both reported zero citing works for the published
DOI. Novelty confidence is moderate pending specialist review.

## Human review focus

- The passage from the source’s Theorem 1.1 to the dimensionless axial law.
- The elasticity monotonicity in Lemma 1.
- The positive-coefficient ratio argument in Lemma 2.
- The stop-loss conversion and strict-equality argument.
- The source’s separate arithmetic inconsistency in Theorem 1.6, discussed
  in the packet but not used in the proof.
