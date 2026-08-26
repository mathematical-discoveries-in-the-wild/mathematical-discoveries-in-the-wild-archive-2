# Verification Report

Status: `candidate_full_counterexample_likely_valid`.

## Source and question

- `source_paper.pdf` is arXiv:1901.10697, 15 pages.
- Question 4.1 appears on PDF page 12.
- `figures/open_problem_crop.png` is a readable crop of the actual source
  page, including the section heading and exact question.

## Mathematical checks

1. For each embedded graph6 string, the verifier checks all 26 degrees and
   all 325 common-neighbor counts, establishing
   `SRG(26,10,3,4)` exactly.
2. It checks `S^2=25I` and `tr(S)=0` exactly. Therefore `S` has eigenvalues
   `+5,-5` with multiplicity 13 each, and `X=I+S/5=2P_+` is a real
   `(26,13)` ETF Gram matrix.
3. The sign-line enumeration uses an exact rational nullspace basis and an
   invertible 13-coordinate restriction. Exhausting `2^13` assignments is
   therefore complete; no floating eigenvector threshold is used.
4. Cut case: exactly 130 sign lines are found and the integer identity
   `5 sum(zz^T)=130(5I+S)` is checked entrywise.
5. Noncut case: exactly 14 sign lines are found. Their affine feature matrix
   has exact rank 14. The unique rational weights are one `-3/10` and thirteen
   `1/10`, and all 326 affine equations are checked.
6. Any cut decomposition of `X` is supported in `ran(X)`: for every
   `u in ker(X)`, positivity of `sum lambda_z (u^T z)^2=0` forces every
   positive-weight sign vector to be orthogonal to `ker(X)`.
7. Since `N=26` is even, the terminal generalized elliptope is
   `E_26^26=C^26`. The cut example has depth 26; the noncut example has depth
   at most 24. This is enough to refute dependence only on `(N,r)`.

## Code checks

Exact command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1901.10697_same_parameters_different_sos_depth/code/verify_counterexample.py \
  --write-certificate \
  runs/fa_banach_001/solutions/counterexamples/1901.10697_same_parameters_different_sos_depth/code/exact_certificate.json
```

Observed deterministic summary:

- cut sign lines: 130;
- noncut sign lines: 14;
- noncut feature rank: 14;
- unique weights: `-3/10` once, `1/10` thirteen times;
- both frame parameters: `(N,r)=(26,13)`.

The script completed successfully on 2026-08-13.

## Novelty check

The cheap run indexes contain no target or core-question duplicate. Bounded
web/arXiv searches through 2026-08-13 covered the exact question wording,
ETF generalized-elliptope membership, regular two-graphs, the
`SRG(26,10,3,4)` catalogue, `(26,13)` ETF constructions, and cut-polytope
membership. No prior same-parameter counterexample or matching exact affine
certificate was found. Novelty confidence is moderate pending specialist
search in the two-graph and cut-polytope literature.

## Rendering checks

- `main.tex` compiled twice with `latexmk` to a three-page PDF; the final log
  contains no LaTeX warnings, overfull/underfull boxes, or undefined references.
- `pdfinfo` reports an unencrypted three-page letter-size PDF with no suspect
  objects, forms, JavaScript, or rotation.
- PyMuPDF extracted 1,125 words from all three pages and recovered both the
  title and theorem statement, providing an independent text-layer check.
- All three pages were rasterized at 160 dpi and inspected at original detail
  on 2026-08-13. The source-question crop is readable and complete; equations,
  graph6 strings, references, and page boundaries have no clipping or overlap.
- Final SHA-256 hashes: `solution_packet.pdf`
  `694dfac9e12dab412782475996a972dd959ef1909f4f7b85ae567741ada68a5d`;
  `source_paper.pdf`
  `4b37ff47dd94da9116c9241340cde856a55b1ba7b9e379514f6fc721ec59feec`;
  verifier
  `750775d790d3cd898760af1e23b47dfdd9456bcc07802ca8cb007b69e3470413`;
  certificate
  `b0af408408bb9a6b1919b8c6e67fce98bd97cf9e492dcf7d102e8735bb8fb889`.
