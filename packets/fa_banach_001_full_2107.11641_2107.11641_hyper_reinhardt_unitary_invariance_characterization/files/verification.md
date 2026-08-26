# Verification report

Verdict: **likely valid candidate full solution**

## Source and statement audit

The official arXiv:2107.11641v4 PDF has 33 pages.  Remark 4.4 is on PDF
page 17 and asks whether invariance under

```text
X_j -> W_(j-1)^* X_j W_j
```

characterizes hyper-Reinhardt free spectrahedra.  The final `P_A` in its
display is a local typo for `P_B`: `B` names the arbitrary domain in the
sentence, while `A` names only the already-constructed forward example.
The packet proves the well-typed intended equivalence.

The source normalizes every connector to norm one after noting that connector
scaling is coordinate scaling.  The theorem first gives the invariant
structural path form with arbitrary nonzero connector norms, then proves that
unit-radius coordinate slices force norm one.  Thus no hidden normalization
gap remains.

## Matrix-unit expansion audit

For an auxiliary tuple `Y_(j,ab)` of `m x m` matrices,

```text
X_j(Y) = sum E_ab tensor Y_(j,ab)
```

has size `nm`.  After a tensor permutation, the original coefficient is
`B_j tensor E_ab`.  Applying the quiver unitary `W_r tensor I_m` gives
`B_j tensor W_(j-1)^* E_ab W_j`.  Since the hypothesis holds at every size
`nm`, the two expanded pencils agree as *free* spectrahedra at all auxiliary
levels.  This is exactly the hypothesis needed for the Linear
Gleichstellensatz, not merely equality of one scalar LMI set.

## Inflation-minimality audit

Decompose a minimal tuple `B` into active irreducible reducing summands.  For
an irreducible summand, the positive-length star-words in its coefficients
span a nonzero two-sided ideal in the full coefficient matrix algebra, hence
span that algebra.  Compatible products of inflated matrix-unit coefficients
realize every such word tensored with every matrix unit.  The inflated
coefficient algebra is therefore the full tensor matrix algebra, so the
inflated summand is irreducible.

No inflated summand becomes redundant: restricting to
`Y_(j,aa)=Z_j`, with all off-diagonal variables zero, gives `I_n tensor Z_j`
and therefore `n` copies of each original summand.  Redundancy after inflation
would imply redundancy before inflation.  The expanded tuple is minimal.

This validates the packet's only nontrivial prerequisite for applying the
standard Linear Gleichstellensatz (minimal monic pencils defining the same
free spectrahedron are unitarily equivalent).

## Zero-product audit

At size two, let `F` be the flip matrix.  Exact arithmetic gives

```text
E_11 E_21 = 0,
E_11 F E_21 = E_11 != 0.
```

For the no-adjoint product, the transformed middle quotient is
`W_j W_(k-1)^*`, whose factors are independently selectable exactly when
`k!=j+1`.  The zero product therefore forces `B_j B_k=0` in those cases.

For `B_j B_k^*`, the middle quotient is `W_j W_k^*`, independently
selectable exactly when `j!=k`.  For `B_j^* B_k`, it is
`W_(j-1) W_(k-1)^*`, again independently selectable exactly when `j!=k`.
Outer unitary factors cannot turn the nonzero matrix-unit witness into zero.
The three claimed operator zero-product families follow with no omitted
index case.

## Reconstruction audit

With `R_j=ran(B_j)` and `S_j=ran(B_j^*)`:

- `B_j^*B_k=0` makes the `R_j` pairwise orthogonal;
- `B_jB_k^*=0` makes the `S_j` pairwise orthogonal;
- `B_jB_k=0` unless `k=j+1` makes `R_k` orthogonal to `S_j` unless
  `k=j+1`.

Hence `H_0=R_1`, `H_r=S_r+R_(r+1)`, and `H_g=S_g` are pairwise
orthogonal.  Their complement is annihilated by every `B_j` and `B_j^*`, so
it is a removable identity summand; minimality makes it zero.  Finally
`B_j` vanishes on `S_j^perp` and has range `R_j`, proving that only its
`(j-1,j)` block is nonzero.  Block-diagonal conjugation proves the converse.

## Computational check

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2107.11641_hyper_reinhardt_unitary_invariance_characterization/code/verify_matrix_unit_relations.py
```

Result:

```text
matrix-unit zero/nonzero witness passed
all path-block zero-product relations passed
exact block-conjugation identity passed
```

This is an index/adjoint and algebra check, not a substitute for the
Gleichstellensatz proof.

## Novelty audit

Eight focused attempts are recorded in
`runs/fa_banach_001/attempts/2107.11641_hyper_reinhardt_characterization/upgrade_attempts.md`.
The local registry, solution, attempt, and proof-gap indexes had no matching
paper or result.  Exact-title, exact-Remark-phrase, author, arXiv-id, and
hyper-Reinhardt/unitary-invariance/quiver-characterization searches on
2026-08-13 found no claimed answer.

The closest sources were:

- arXiv:2012.02289 / LAA 640 (2022), the graph characterization of weaker
  scalar-torus Reinhardt symmetry;
- arXiv:2301.02746 (2023), which uses the quiver-unitary condition only in
  the already-known necessary direction to exclude a particular example;
- the 2023 published chapter corresponding to the source, which retains
  Remark 4.4.

Novelty confidence is moderate because the search was bounded and the proof
depends on a standard structural theorem.

## Final PDF and visual QA

The final packet was built twice with `pdflatex`, text-extracted with
Ghostscript, rendered at 150 dpi, and all six pages were inspected.  An
initial transparent crop rendered with a black background; the cropper was
corrected to composite onto white, the PDF rebuilt, and the final page 2
reinspected.  The final PDF has no warnings, clipping, overlap, missing
glyphs, or malformed formulas.

## Human-review focus

High-priority review should check the matrix-unit inflation minimality lemma
and the exact scope of the Linear Gleichstellensatz for complex monic
pencils.  The matrix-unit witness, range-space reconstruction, normalization,
and source typo are direct.  No conditional dependency is currently known.

SHA-256 hashes of the final artifacts:

```text
436ebe0a37561a98ec614211a80b004d9364396514101d99175bc90856db882e  source_paper.pdf
6e7086de14507e94ea1166c91d2df5706f3ff2afed255a1319739fda367cfe49  supporting_paper_2012.02289.pdf
c7eb34a63cf86d0d997b451183b7e18fd11d10f4b0efd0ddd36b1e127c60a90d  supporting_paper_1604.05756.pdf
ccc201ad06881cb54d82057204615e0f3f0484ba5e77ae27992888d19757ed10  figures/open_problem_crop.png
1a0d3d27462a83190da8404e8e54f154fd6d08997e3b7664543c3549f306f70f  main.tex
cdbc5dfd3a5c9029275b6c904243375a5367e3c102d253baf8386960450d48bf  solution_packet.pdf
13e7e79d92e7244d2343ea85e8dabe776f34fdf0940e87574bf7eb8ffb7f0d62  code/verify_matrix_unit_relations.py
4c719b9d309badec0c48a42a8617c52e85765fa582cb9bb191701ec6f4c67022  code/make_open_problem_crop.py
```
