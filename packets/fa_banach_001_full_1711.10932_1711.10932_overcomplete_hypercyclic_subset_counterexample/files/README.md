# 1711.10932 — an overcomplete sequence which is not a hypercyclic subset

Status: `candidate_full_solution_human_review_needed`.

Model: `GPT5.6`.

Source: Sophie Charpentier and Romuald Ernst, *Hypercyclic subsets*, arXiv:1711.10932, Question 6 on source PDF page 33.

## Result

Question 6 asks whether almost overcomplete sequences are hypercyclic subsets. This packet gives a full negative answer in a stronger form: there is an **overcomplete** sequence `C` in a separable complex Hilbert space and a bounded non-hypercyclic operator `T` such that `Orb(C,T)` is dense.

## Construction

Let `B` be the unilateral backward shift on `ell^2`, choose a hypercyclic vector `x` for `S=2B` with nonzero zeroth coordinate, and define

`T = 4 I_C direct-sum 2B` on `H = C direct-sum ell^2`.

The scalar summand makes `T` non-hypercyclic. On the other hand, sample the analytic curve

`f(t) = (t, x + t h(t))`, where `h(t)=sum 2^{-k} t^k e_k`,

at pairwise distinct parameters `t_n=alpha_n 4^{-m_n}`. The times `m_n` are selected so that `(2B)^{m_n}x` shadows a tail-dense list of vector targets and the perturbation has norm `O(2^{-m_n})`. Then `T^{m_n}f(t_n)` shadows a tail-dense list in the whole direct sum.

Every infinite subsequence of `(f(t_n))` has dense span: a functional annihilating it gives a scalar analytic function with zeros accumulating at zero, hence vanishes identically; the Taylor coefficients of `f` span `H`.

## Verification and novelty

The verification report checks the shift dynamics, inductive choice of times, density argument, analytic identity-theorem argument, linear independence, and the scalar obstruction to hypercyclicity. No computation is used as proof evidence.

On 2026-08-11, bounded local-index and web/arXiv searches using the exact question and close variants found the source paper but no later claimed answer. Novelty remains subject to specialist review.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: compiled human-review packet.
- `verification_report.md`: adversarial proof audit.
- `source_paper.pdf`: official 35-page arXiv PDF.
- `figures/open_problem_crop.png`: source PDF page 33 crop containing Question 6 and the authors' comment.

## Human review recommendation

Review as a likely valid full solution. The highest-value checks are the all-subsequences quantifier in overcompleteness and the simultaneous inductive selection of the hitting times `m_n`; both are written explicitly in the packet.
