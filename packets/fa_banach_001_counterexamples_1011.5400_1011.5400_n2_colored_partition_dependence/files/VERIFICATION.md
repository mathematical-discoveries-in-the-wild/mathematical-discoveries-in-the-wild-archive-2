# Verification

## Mathematical audit

- Theorem 3.5 and its `n>=2` quantifier were checked on source PDF page 10.
- Definition 3.1, the tensor-map formula, the blockwise color-swap
  identification, and the `2n` index convention were checked in the source.
- Every block in the eleven diagrams has equal numbers of black and white
  legs, so every diagram belongs to `D_s(0,6)` for all `s`.
- Noncrossing, diagram distinctness, adjacent-pair support, orientation sums,
  and the two-value pigeonhole identity were audited separately.
- Exact-title, theorem-phrase, determinant, colored-partition, and citation
  searches found no published correction or the displayed dependence through
  11 August 2026.

## Independent exact checks

- `code/check_relation.py` directly evaluates the eleven diagram tensors on
  all `4^6=4096` coordinates. Every coordinate of the relation is zero and
  every diagram occurs nontrivially.
- `code/gram_small.py` independently enumerates the 33 diagrams in
  `D_5(0,6)` and uses signed union-find constraints to build the exact
  polynomial Gram matrix. SymPy factors its determinant as
  `N^33 (N-2)^26 (N-4)^2` and computes exact rank 31 at `N=4`.
- The hand proof does not depend on either computation.

## Artifact checks

- [x] Both exact checkers pass.
- [x] Source crop and supporting source pages are RGB and visually inspected.
- [x] `main.tex` compiles without errors, undefined references, or box warnings.
- [x] Final PDF metadata and text extraction are healthy (2 letter-size pages,
  5,414 extracted text characters).
- [x] Every final page is rendered RGB and inspected for layout defects.
- [x] SHA-256 hashes are recorded below.

## SHA-256

```text
46246c10ca81aaf159236cff76cd76c17eb7f4bbf3c1f6188fc970e659c41c5e  main.tex
89a531c73ace197d458256aa9adc3bd97a3d08c26b8a18b91e07c8a242cf196e  README.md
e59b3964afa7d99f6da55560333e1ad9bffb2c4b6c26ec3362b762d4dc75a0f1  solution_packet.pdf
f1ff56d284148433b24d3ac3418f5fd7b32eea29ab81ba9a700e1426cca6bf01  source_paper.pdf
5275dc7c4855f15682c82020d5b5d887b781b6d29072007d53778049d5747008  source_theorem_crop.png
45431f4bdaefa66183e333d2519db06ce0a8ad385880d631135f5c1a79d21fa4  code/crop_source.py
df85b86cece71b8ab130affd00b667c9fc0ead142865c8abddf278e4233697b2  code/check_relation.py
99c51463e57da932db57b08e6fcf96d324f644d2eaada8bc4d464f00d3ad1878  code/gram_small.py
```

Verification completed at 2026-08-11T21:47:51Z.
