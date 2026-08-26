# Large vector-valued fibers over arbitrary target balls

Status: `candidate_partial_result_likely_valid`

Source: Verónica Dimant and Joaquín Singer, *A fibered description of the
vector-valued spectrum*, arXiv:1902.01387, page 15.

## Result

The later theorem of Dimant--Singer (arXiv:1909.05105, Theorem 2.4) says that
every fiber of `M_infty(B_c0,B_c0)` contains `2^c` disjoint analytic
Gleason-isometric copies of the full parameter ball. This packet proves two
extensions:

1. The target domain can be **any Banach space `Y`**. For every
   `g` in the closed unit ball of `H-infinity(B_Y,ell-infinity)`, every fiber
   of `M_infinity(B_c0,B_Y)` has the same huge analytic structure.
2. If `X` contains a 1-complemented isometric copy `J(c0)`, the same conclusion
   transfers to fibers over maps of the form `J** o g`.

The new input is a target-domain-free coordinate dichotomy. Select a
subsequence for which the scalar values `g_n(0)` converge. Schwarz--Pick then
forces either pointwise convergence to one unimodular constant or a uniform
strict bound on the selected coordinates at every fixed point. This exactly
replaces the only `Y=c0` compactness step in the published proof.

Consequently, the norm-one pointwise-interior question in arXiv:1902.01387 has
a positive answer for `X=c0` and arbitrary `Y`, not just for `X=Y=c0`.

## Scope

The general infinite-dimensional source space `X` remains open. Existing
large scalar fibers do not provide the coherent analytic dependence on
`g(y)` needed for a vector-valued homomorphism. The strict-ball construction
in the source paper also loses its perturbation radius when `||g||=1`.

A bounded index/arXiv search found the exact `X=Y=c0` theorem in
arXiv:1909.05105 and no arbitrary-`Y` or complemented-`c0` statement. This is
not a definitive novelty certification.

## Packet contents

- `main.tex`, `solution_packet.pdf`: statement, proof, scope, and references.
- `source_paper.pdf`: arXiv:1902.01387.
- `supporting_paper_1909.05105.pdf`: the decisive published `c0` theorem.
- `figures/open_problem_crop.png`: source question on PDF page 15.
- `figures/supporting_theorem_page9.png` and
  `figures/supporting_theorem_page10.png`: Theorem 2.4 and proof evidence.
- `VERIFICATION.md`: mathematical and rendering audit.

Human review should focus on the claim that every step after the coordinate
dichotomy in the proof of arXiv:1909.05105, Theorem 2.4, is independent of the
target domain.
