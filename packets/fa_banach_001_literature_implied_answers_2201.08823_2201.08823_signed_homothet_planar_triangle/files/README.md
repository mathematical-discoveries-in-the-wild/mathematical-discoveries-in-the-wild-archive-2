# Signed homothetic coverings: two planar classes

Classification: **literature-implied answer (partial subcase)**.

Ambrus's Conjecture 4 asks whether a signed homothetic cover of a convex body \(K\subset\mathbb R^d\) by coefficients \(-1<\lambda_i<1\) must satisfy \(\sum_i|\lambda_i|\ge d\).

This packet identifies two complete planar subcases:

1. **Every nondegenerate planar triangle.** Dumitrescu--Jiang, Theorem 1 (EJC 15 (2008), R37), explicitly treats both positive and negative equilateral homothets and proves the sharp bound \(\sum_i|\lambda_i|\ge2\). Affine covariance transfers it to every triangle.
2. **Every centrally symmetric planar convex body.** A negative homothet is a translate of a positive homothet of the same magnitude; the positive planar Soltan--Vasarhelyi theorem cited in the source paper applies.

The packet does **not** claim a solution for arbitrary planar noncentrally symmetric bodies or in higher dimension.

Files:

- `solution_packet.pdf`: compact status packet with exact bridge proofs and source evidence.
- `source_paper.pdf`: official arXiv PDF for arXiv:2201.08823.
- `supporting_dumitrescu_jiang_2008.pdf`: official EJC PDF of the decisive theorem.
- `solution.tex`: LaTeX source.
- `code/`: reproducible numerical search/checkers used during the direct attack.

