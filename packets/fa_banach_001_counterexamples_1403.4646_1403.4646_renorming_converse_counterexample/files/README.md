# Counterexample packet: renorming does not recover the tail pseudometric

Status: candidate full counterexample, likely valid, needs human review.

Source: C. Angosto, M. C. Listán-García, and F. Rambla-Barreno,
*Continuity properties of sequentially asymptotically center-complete spaces*,
arXiv:1403.4646; RACSAM 110 (2016), 809–822.

Question: Conjecture 3.3 asks whether two bounded sequences that have the same
asymptotic center and radius under every equivalent renorming must have tail
pseudodistance zero.

Result: no, in every nonzero Banach space. Fix `u != 0`; alternate `-u,u` in
one sequence and cycle through `-u,0,u` in the other. Their complete
asymptotic-radius functions agree pointwise under every norm, because the
distance from a point to the midpoint is bounded by the maximum distance to
the endpoints. Yet their tail pseudodistance is exactly `||u||`.

Stronger obstruction: periodic sequences supported on finite sets with the
same convex hull have identical farthest-distance functions under every norm,
while the tail pseudometric can distinguish the sets.

Novelty check: exact-title, conjecture, and renorming-phrase searches were run
on 2026-08-12. They found the source and later center-continuity literature but
no resolution or correction of Conjecture 3.3. The run indexes had no prior
result for this arXiv id.

Files:

- `main.tex`: full counterexample and convex-hull obstruction.
- `solution_packet.pdf`: compiled and visually checked packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_conjecture_crop.png`: source page crop.
- `VERIFICATION.md`: analytic and visual QA report.

Review recommendation: verify the pointwise midpoint inequality and compute
the tail Hausdorff distance between `{-u,u}` and `{-u,0,u}`. No numerical or
conditional dependency is used.

