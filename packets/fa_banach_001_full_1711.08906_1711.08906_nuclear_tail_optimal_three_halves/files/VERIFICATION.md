# Verification report

Verdict: `candidate full solution — likely valid`.

Checks completed:

1. The identity
   `T-PTQ = (3T-UT-TV-UTV)/4`, with `U=2P-I` and `V=2Q-I`, was expanded directly. Each of the four sign-change compositions preserves the nuclear norm, so the `3/2` upper bound is immediate.
2. The source paper's finite-coordinate approximation step was checked to combine with the improved complement norm without an extra factor.
3. The trace-dual orientation was checked: on `N(ell^q,ell^p)^*=L(ell^p,ell^q)`, the adjoint of `T -> PTQ` is `S -> QSP`.
4. At the endpoint `(p,q)=(infinity,1)`, the matrix `[[1,-1],[-1,-1]]` has induced norm `2`, while deleting its `(1,1)` entry gives induced norm `3`. Finite-dimensional norm continuity therefore yields dual projection norms tending to `3/2` for admissible `p -> infinity`, `q -> 1`.
5. The general projection/quotient identity
   `||I-Phi|| = sup_{b in ker Phi} ||b||/dist(b,ran Phi)`
   was proved in both directions.
6. For the replicated set, both equalities were checked: its Hausdorff measure of norm noncompactness is the finite-dimensional quotient distance, and its corner-tail functional is the norm of the kernel vector. The large `(1,1)` anchor handles finite corners omitting the common coordinate.
7. `code/check_corner_constant.py` ran successfully and reported:

   - sign-flip identity maximum error: `2.220e-16` over 100 random matrices;
   - endpoint original norm: `2.0`;
   - endpoint deleted-corner norm: `3.0`;
   - endpoint ratio: `1.500000`.
8. `solution_packet.pdf` was compiled twice from `main.tex`.  The final log has
   no warnings, underfull boxes, or overfull boxes.  All five pages were
   rendered at 150 dpi and inspected visually; the theorem, equations, source
   crop, and references are legible and unclipped.  Text extraction found all
   expected packet headings and statements.

The computation is a sanity check only; the packet's proof is exact and does not depend on numerical approximation.

Bounded novelty searches found no later explicit answer. Human review is recommended before treating novelty as certified.
