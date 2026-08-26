# Verification report

## Mathematical checks

- Verified the extrema signs directly from
  `-epsilon Delta u + epsilon^{-1} W'(u)=lambda`:
  at a maximum, `W'(max u) <= epsilon lambda`; at a minimum,
  `epsilon lambda <= W'(min u)`.
- Verified that the mean constraint implies
  `min u <= V/vol_g(M) <= max u`.
- Verified finiteness of
  `A=sup_{s<=a}W'(s)` and `B=inf_{s>=a}W'(s)` from
  `W''>=c_0>0` near both infinities.
- Checked both contradiction cases separately, including extrema lying in the
  extended rather than the unchanged part of the potential.
- Checked that the fixed truncation can be chosen nonnegative, with no new
  wells, `C^2`, subcritical, and convex on both tails by matching endpoint
  two-jets and interpolating to a power `q in (2,2*)` (arbitrary finite
  `q>2` in dimensions one and two).
- Checked that every truncated critical point is an original critical point,
  not only those below an energy cutoff.
- Checked the nondegenerate case: the potentials and their second derivatives
  coincide on the entire range of every transferred solution, so the
  constrained Hessians agree.
- No numerical experiment is needed; the proof is qualitative and exact.

## Source and novelty checks

- Exact question located on original PDF page 28; Theorem 5.9 continues on
  page 29.
- The 2024 corrigendum was included and its corrected photography theorem is
  the subcritical input used by the proof.
- Searched `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`,
  and `proof_gaps/index.tsv`: no duplicate for arXiv:2007.07024.
- Bounded exact-phrase/title/core-keyword searches through 2026-08-11 found no
  later solution.
- Inspected arXiv:2604.23920 (2026 survey, with a source coauthor): it still
  states the scalar closed-manifold result for a subcritical potential and
  does not report this tail-growth extension.

## Packet checks

- `source_paper.pdf` was compiled from the cached arXiv source bundle because
  the current arXiv PDF is the corrigendum rather than the original article.
- The two open-problem crops were rendered opaquely at 180 dpi and visually
  inspected for completeness and readability.
- LaTeX compiled cleanly to a five-page packet (no undefined references; one
  harmless 0.65-point overfull line).
- All five pages were rendered opaquely at 144 dpi and visually inspected;
  equations, screenshots, theorem text, proof, and references are complete and
  unclipped.

## Recommendation

Expert review is recommended. The result appears to be a full proof; the main
review focus is whether the source's admissible-potential class permits the
standard convex `C^2` subcritical tail interpolation exactly as stated.
