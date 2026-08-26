# Candidate counterexample and exact characterization

**Status:** candidate counterexample / full norm-level characterization, likely valid, pending human review.

**Source:** T. A. Abrahamsen, R. Haller, V. Lima, and K. Pirk, *Delta- and Daugavet-points in Banach spaces*, arXiv:1812.02450, Problem 1 on printed page 21.

## Result

Let
\[
D=C([0,1];\mathbb R),\qquad E=\mathbb R\oplus_1D,
\qquad Z=E\oplus_\infty D.
\]
Then (E) fails the convex-DLD2P, while (Z) has the convex-DLD2P. Thus the convex-DLD2P of an ℓ∞-sum need not pass to a factor.

Combined with Proposition 2 of Guerrero-Viu--Markowicz, arXiv:2607.01875, this gives the exact characterization: an absolute normalized norm (N) has convex-DLD2P inheritance from (X\oplus_NY) to both factors for all real Banach spaces (X,Y) if and only if (N\ne\ell_\infty).

## Proof mechanism

The only genuine Δ-points of (E) lie on its (D)-axis, so they do not convexly generate (B_E). However, Example 4.3 of Haller--Pirk--Veeorg, arXiv:2001.06197, provides Δ_k-points
\[
((1-1/k)\sigma,d/k),\qquad \sigma\in\{-1,1\},\ d\in S_D,
\]
which converge to the missing scalar endpoints as (k\to\infty). These points, together with the (D)-axis, convexly generate (B_E). Pairing each one with a unit vector of a second copy of (D), using conjugate Δ-exponents and Proposition 4.4 of the same paper, produces genuine Δ-points in (E\oplus_\infty D). The product convex-hull identity then fills the whole ball.

## Packet contents

- `solution_packet.pdf` / `main.tex`: full statement, proof, verification notes, and novelty bounds.
- `source_paper.pdf`: arXiv:1812.02450.
- `supporting_paper_2001.06197.pdf`: the Δ_k construction and conjugate-exponent proposition.
- `supporting_paper_2607.01875.pdf`: the positive (N\ne\ell_\infty) complement.
- `figures/open_problem_crop.png`: full-width source screenshot of Problem 1.

## Verification and review focus

The argument is non-computational. It was checked point-by-point for the zero-coordinate cases, the (k\)-dependent conjugate exponent, the density of the auxiliary Δ_k set in the missing scalar axis, and the product convex-hull identity. Human review should focus on the three cited results from arXiv:2001.06197 and the promotion from the auxiliary product set to all of (B_Z).

## Novelty status

A bounded index/arXiv/web search on 2026-08-09 found no prior version. The July 2026 paper arXiv:2607.01875 explicitly proves only the non-ℓ∞ case and identifies ℓ∞ as exceptional. Priority remains subject to expert literature review.

Ledger: `runs/fa_banach_001/ledger/results/1812.02450_linf_convex_dld2p_counterexample_and_characterization.json`.
