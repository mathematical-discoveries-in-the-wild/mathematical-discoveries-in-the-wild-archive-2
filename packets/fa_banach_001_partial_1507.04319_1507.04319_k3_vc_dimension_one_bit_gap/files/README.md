# A one-bit determination of the three-sparse VC dimension

This packet gives a new partial answer to Problem 8 of arXiv:1507.04319.

For the class `C_{n,k}` of signs of real Walsh polynomials with at most `k`
terms, it proves

- `VCdim(C_{n,1}) = VCdim(C_{n,2}) = n+1`;
- `VCdim(C_{1,3})=2`, `VCdim(C_{2,3})=4`, and `VCdim(C_{3,3})=7`;
- for every `n>=4`,
  `3n-3 <= VCdim(C_{n,3}) <= 3n-2`.

The proof classifies `C_{n,3}` as the Boolean quadratic phases
`ell + L_1 L_2`, counts them exactly, and shatters an explicit set whose
pair-sum points are indexed by the edges of `K_{2,n-2}`. This improves the
source bounds for `k=3` from a linear interval with constants `1` and at most
`6` to a single-bit ambiguity.

Files:

- `solution_packet.pdf`: self-contained statement and proof.
- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_crop.png`: real source-page crop containing Problem 8.
- `code/verify_low_sparsity.py`: independent finite checks.
- `VERIFICATION.md`: proof and artifact audit.

The final one-bit gap for `n>=4` and the source problem for arbitrary `k`
remain open.

