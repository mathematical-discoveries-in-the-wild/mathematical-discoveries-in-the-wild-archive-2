# Verification record

Date: 2026-08-12 UTC

Status: candidate major partial result; likely valid; pending human review.

## Source and scope audit

- Source PDF: official arXiv PDF for arXiv:2006.04901, 24 pages.
- Exact target: Question 1.1 on physical/source page 4.
- The crop includes the definition of `eta`, the surrounding compressed-shift
  setup, and the complete question.
- The packet claims an exact diagonal-SDP characterization for arbitrary
  distinct zeros, a full degree-two formula, a sharp pairwise lower bound, and
  a full regular-pseudohyperbolic-polygon formula.
- It explicitly does not claim an elementary closed formula for arbitrary
  nonsymmetric zero configurations.

## Proof audit

1. Each zero `z_j` supplies the normalized Szego kernel eigenvector of
   `S_Theta^*`; distinct eigenvalues make these vectors a basis.
2. `eta(A)=eta(A^*)` follows by replacing an eigenvector matrix `X` with
   `X^{-*}`, whose spectral condition number is the same.
3. Every remaining eigenvector choice is positive diagonal column scaling,
   up to phases and permutation. Squaring the matrix condition number produces
   the condition number of the scaled kernel Gramian.
4. The equivalence `kappa(DGD)<=t` iff there is positive diagonal `P` with
   `P<=G<=tP` is checked in both directions by congruence. Compactness of the
   normalized feasible `P`-set proves attainment.
5. The disk-automorphism transformation of `G` was expanded algebraically and
   gives a diagonal-unitary congruence. This commutes with positive diagonal
   scaling.
6. In degree two, fixing the product of scales fixes the determinant; AM-GM
   minimizes the trace at equal scaling, and the positive 2-by-2 eigenvalue
   ratio is increasing in trace at fixed determinant.
7. The general pairwise lower bound follows from principal-submatrix
   interlacing and the exact two-point optimum.
8. For regular zeros, the geometric-series/root-of-unity computation gives
   the complete Fourier spectrum of the circulant Gram matrix.
9. Pulling the extreme flat Fourier vectors back through `D^{-1}` gives two
   Rayleigh quotients with the same denominator. Their quotient proves the
   lower bound for every diagonal scaling; scalar scaling attains it.
10. The packet explicitly handles the harmless inner-product convention under
    which the matrix Gramian is `G` or `conj(G)`: complex conjugation preserves
    eigenvalues and the relevant Loewner comparisons with real diagonal
    matrices.

No unproved lemma or numerical dependency remains in the stated results.

## Computational checks

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2006.04901_eigenvector_condition_number_sdp_regular_polygon/code/verify_condition_numbers.py
```

Output: `all condition-number checks passed`

The script checks:

- regular polygons for `2<=n<=8` and radii `0.2, 0.5, 0.8`;
- the exact formula on 100 random two-point configurations;
- invariance under random disk automorphisms;
- a generic five-point configuration in which unequal scaling strictly
  improves the raw normalized Gram condition number.

These are sanity checks only; the proof is exact.

## Literature and duplicate audit

- Cheap indexes searched: `registry_index.tsv`, `solutions/index.tsv`,
  `attempts/index.tsv`, and `proof_gaps/index.tsv`.
- Exact web/arXiv phrases searched included combinations of `minimal condition
  number`, `finite Blaschke product`, `compressed shift`, `eigenvector matrix`,
  and `M_Theta`.
- OpenAlex returned 14 indexed works citing the source paper; titles were
  screened for overlap.
- The closest later primary sources inspected at title/abstract/full-text-search
  level were arXiv:2306.12183, arXiv:2312.04537, and arXiv:2506.15444.
- No exact diagonal-SDP reduction, degree-two formula in this formulation, or
  regular-polygon formula was found.

Novelty confidence is medium because this was a bounded search, not an
exhaustive proof of absence from the literature.

## Build and visual audit

- Built with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
- Final LaTeX log: no warnings, undefined references, overfull boxes, or
  underfull boxes.
- Final PDF: 6 pages; PyMuPDF opens it and extracts 10,666 text characters.
- Every final page was rendered to `tmp/final_page-1.png` through
  `tmp/final_page-6.png` and visually inspected at high/original detail.
- Page 1: title/status/source question and crop are legible; no clipping.
- Page 2: theorem statements and displayed formulas fit cleanly.
- Page 3: intuition and SDP reduction are legible; convention note is clear.
- Page 4: automorphism and degree-two proofs fit cleanly.
- Page 5: Fourier/Rayleigh proof and scope notes are legible.
- Page 6: novelty audit and references are complete and unclipped.

Hashes:

- `solution_packet.pdf`:
  `99b4b975b13f09e5f95734945bb6c3a154e3907106c008effe19dba99785dadf`
- `source_paper.pdf`:
  `cb73f8f5ad00efc425d92c7456695aac985a65bad18b59bc9923582ada63210d`

## Human-review recommendation

Prioritize review of the passage from `M_Theta` to adjoint kernel eigenvectors,
the SDP congruence, the disk-automorphism phase factors, and the shared
Rayleigh-quotient denominator for the extreme Fourier vectors. If those four
points pass, the rest is routine algebra and eigenvalue interlacing.
