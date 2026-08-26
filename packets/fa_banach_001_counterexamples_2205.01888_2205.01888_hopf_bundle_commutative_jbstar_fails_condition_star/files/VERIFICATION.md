# Verification report

Status: `candidate_counterexample_likely_valid`

## Structural checks

- For `E=C^T(L)`, the map `t -> delta_t` is weak*-continuous and injective,
  and for compact `L` it is a homeomorphism onto the relevant extreme
  functional set `Q_E`.
- The maximal proper sphere faces are `F_{t,lambda}` and equivalence classes
  of representative functionals are exactly the circle orbits.  This is the
  identification established and used in arXiv:2201.06307, Section 3.
- If condition (*) holds for a transversal `P`, any limit `r=lambda p` of
  `P` with `lambda != 1` contradicts (*) by taking a relatively closed tail
  `F` near `r`: continuity forces `|r(a)|<=1/2`, while `p(a)=1` gives
  `|r(a)|=1`.
- Thus `P` is closed.  Since the total bundle is compact, `P` is compact and
  its continuous bijection onto the compact Hausdorff base is a homeomorphism.
- Conversely, a continuous section trivializes the principal circle bundle.
  A scalar Urysohn function on the base lifts to an equivariant element of
  `C^T(L)` that vanishes on any prescribed closed representative subset.
- The Hopf bundle has no section: a section would trivialize it and yield
  `S^3 homeomorphic to S^2 x S^1`, contradicting their fundamental groups.

## Computational status

No computation is used.  The proof is topological and functional-analytic.
The source-question crop is rendered from page 45 of the original PDF, and
the final packet is compiled with all temporary files confined to `tmp/`.

## Reviewer focus

The highest-value audit is the passage from condition (*) to closedness of an
arbitrary representative transversal.  The neighborhood closure must exclude
the chosen representative `p` while retaining the putative phase-shifted
limit `lambda p`; compact Hausdorff separation supplies exactly this.
