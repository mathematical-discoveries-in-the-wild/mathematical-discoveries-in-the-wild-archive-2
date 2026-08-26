# Candidate partial result: complemented-ell1 spaces

Status: **candidate substantial partial result, likely valid; human review required**.

Source target: Problem 3.7 of Carlo Alberto De Bernardi, Alessandro Preti, and Jacopo Somaglia, *A note on smooth rotund norms which are not midpoint locally uniformly rotund*, arXiv:2402.13869. It asks whether every infinite-dimensional separable Banach space has an equivalent rotund (optionally Gâteaux-smooth) norm with no LUR point on its unit sphere.

## Result

Every separable **real** Banach space containing a complemented copy of `ell_1` has an equivalent norm that is simultaneously:

- rotund (strictly convex),
- Gâteaux smooth,
- octahedral,
- and therefore has no LUR point on its unit sphere.

This is a substantial partial answer, not a full solution. It extends the explicit `ell_1` direction to every separable complemented-`ell_1` extension. Spaces not containing `ell_1` cannot admit any octahedral renorming, so the all-separable problem needs another mechanism.

## Construction in one line

Cobollo–Hájek (arXiv:2408.03737) construct a Gâteaux-smooth octahedral norm `N` with canonical witnesses `e_n` and an exact asymptotic `ell_1` tail estimate. Build a continuous injective smooth strictly convex norm `h` with `h(e_n)=2^{-n}` and set `M=N+h`. Strict convexity and smoothness come from `h` and the sum, while the vanishing tail cost preserves octahedrality with explicit constants.

## Packet contents

- `main.tex` and `solution_packet.pdf`: complete theorem, proof intuition, proof, obstruction audit, novelty bounds, and references.
- `source_paper.pdf`: arXiv:2402.13869.
- `supporting_paper_2408.03737.pdf`: the decisive Cobollo–Hájek construction.
- `figures/open_problem_crop.png`: full-width source crop of Problem 3.7, PDF page 9.
- `figures/supporting_theorem_crop.png`: supporting Theorem 1.1, PDF page 2.
- `figures/supporting_tail_estimate_crop.png`: supporting Proposition 2.6, PDF page 8.
- `VERIFICATION.md`: independent proof-interface audit, upgrade attempts, and review checklist.

## Human-review recommendation

Check the auxiliary norm’s strict convexity/smoothness, the exact passage from Cobollo–Hájek Proposition 2.6 to the full-space tail estimate, and the finite-dimensional uniform tail bound. If these pass, retain as a new partial-result packet with moderate novelty confidence.

Ledger: `runs/fa_banach_001/ledger/results/2402.13869_complemented_ell1_rotund_smooth_nowhere_LUR.json`.
