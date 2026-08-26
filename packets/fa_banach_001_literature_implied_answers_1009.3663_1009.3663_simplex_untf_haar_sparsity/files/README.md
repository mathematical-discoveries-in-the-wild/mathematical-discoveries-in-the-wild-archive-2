# Exact optimal sparsity for real simplex tight frames

Status: `literature_implied_answer (complete real simplex tight-frame
subfamily)`.

Source: Peter G. Casazza, Andreas Heinecke, Felix Krahmer, and Gitta Kutyniok,
*Optimally Sparse Frames*, arXiv:1009.3663. Section 5, printed pages 10--11
(PDF pages 10--11), asks for an appropriate optimally sparse extension of
Spectral Tetris when some eigenvalues are below 2.

## Exact identification

For `m=n+1`, every real unit-norm tight frame of `m` vectors in `R^n` becomes,
after scaling, an orthonormal basis of the zero-sum hyperplane in `R^m` (up to
column signs). Appending the constant vector produces an `m x m` orthogonal
matrix with a full row, and this operation adds exactly `m` nonzeros.

Cheon and Shader's 2000 extremal theorem for sparse orthogonal matrices with a
full row therefore gives the exact frame optimum

`sigma(m) = m(ceil(log2(m))+1) - 2^ceil(log2(m))`.

A balanced non-dyadic Haar basis attains it. This is a complete infinite-family
answer in the low-redundancy regime. In particular, five vectors in `R^4`
require exactly 12 nonzeros. The source paper's high-redundancy tight-frame
formula, if formally extrapolated, gives 11; hence it cannot extend verbatim.

## Literature status and scope

Casazza--Fickus--Heinecke--Wang--Zhou, arXiv:1108.4061, Theorem 3.12, later
gave a Spectral Tetris construction for every positive prescribed spectrum
satisfying the trace condition. Their Section 3.2 explicitly notes that the
general construction is not generally globally sparsest. The simplex formula
above closes that global optimization problem only for real `N=n+1` tight
frames.

The frame/orthogonal-matrix relation is agent-identified. Cheon--Shader
predates the source question and does not mention frames; the source paper does
not cite it. Because the exact extremal input is known literature, this packet
is not claimed as a new theorem. General low-redundancy spectra, complex
frames, equiangularity, and compressibility remain outside its scope.

## Files

- `main.tex`: detailed identification, proof of the reduction, exact formula,
  Haar construction, and scope audit.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv:1009.3663.
- `supporting_paper_1108.4061.pdf`: later arbitrary-spectrum construction.
- `supporting_cheon_shader_2000_metadata.md`: metadata and access note for the
  decisive orthogonal-matrix theorem.
- `figures/open_problem_page_10_crop.png` and
  `open_problem_page_11_crop.png`: readable source crops containing the full
  two-page open problem; the uncropped rendered pages are retained beside
  them for provenance.

Human review recommendation: verify the one-line orthogonal completion and the
Cheon--Shader formula, then retain as literature-implied duplicate/status
memory rather than count it as an original run proof.
