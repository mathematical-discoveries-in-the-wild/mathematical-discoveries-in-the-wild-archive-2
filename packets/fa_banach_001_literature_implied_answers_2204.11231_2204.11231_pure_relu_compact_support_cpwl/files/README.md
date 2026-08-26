# Literature-Implied Full Answer: Pure ReLU Networks Suffice

Run: `fa_banach_001`

Status: `literature_implied_answer` (full answer to the qualitative open question)

## Source question

- A. Kratsios and B. Zamanlooy, *Do ReLU Networks Have An Edge When Approximating Compactly-Supported Functions?*, arXiv:2204.11231.
- Source location: PDF page 16, final discussion on the significance of bilinear pooling.

The source asks whether a pure deep ReLU network, without a bilinear pooling layer, can approximate a compactly supported Lipschitz function while retaining compact support strongly enough to satisfy Lemma 2 of the paper.

## Answer

Yes. Bilinear pooling is unnecessary for the paper's qualitative universality theorem.

Triangulate one fixed cube strictly containing the target support and take the nodal continuous piecewise-affine interpolant. Because the target vanishes on the boundary of the larger cube, the interpolant extends by zero to a globally continuous, compactly supported, finite CPWL map. Its uniform error is at most the Lipschitz constant times the mesh diameter. Theorem 5.2 of He--Li--Xu--Zheng, arXiv:1807.03973, states that every finite scalar CPWL function on Euclidean space is represented exactly by a finite ReLU DNN; parallelizing the coordinate networks handles vector outputs.

Thus every compactly supported Lipschitz target admits pure-ReLU approximants converging uniformly (hence in `L1`) with all supports in one fixed enlarged cube. This is precisely the sufficient hypothesis of the source's Lemma 2, and its density lemma then makes pure ReLU networks dense in the source's cs`L1` topology.

## Provenance and scope

This is a full resolution of the source's qualitative existence question, but it is classified as literature-implied rather than new: the decisive exact CPWL-to-ReLU theorem predates the source paper. The packet does not claim the particular pooling-based width/depth estimates in the source's quantitative Theorem 3.

## Files

- `main.tex`: complete reduction and proof.
- `solution_packet.pdf`: rendered answer.
- `source_paper.pdf`: arXiv:2204.11231.
- `supporting_paper_1807.03973.pdf`: exact CPWL-to-ReLU representation theorem.

