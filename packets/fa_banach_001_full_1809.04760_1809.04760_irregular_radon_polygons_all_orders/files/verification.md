# Verification report

## Mathematical checks

- For `m=4n+2`, the regular polygon `P_m` is centrally symmetric and contains
  the origin in its interior, so its gauge is a norm.
- The source paper's Theorem 2.7 states that this regular `m`-gonal normed
  plane is Radon.
- The gauge of `T(P_m)` is exactly `z -> ||T^{-1}z||_{P_m}`; therefore `T` is
  a surjective linear isometry, not merely an affine equivalence.
- The identity
  `||Tx+tTy||_T=||x+ty||` proves preservation of Birkhoff--James
  orthogonality directly for every real `t`, so symmetry is preserved.
- Invertibility of `T` preserves the face lattice and in particular all
  `m=4n+2` vertices.
- The trigonometric edge-vector identity and the displayed length formula were
  recomputed from the subtraction formulas for sine and cosine.
- The special index `k=n` satisfies `(2n+1)pi/m=pi/2` exactly.
- Equality of the `k=0` and `k=n` side lengths reduces to
  `(1-lambda^2)cos^2(pi/m)=0`; neither factor vanishes for `m>=6` and
  `lambda>0`, `lambda!=1`.
- Unequal Euclidean side lengths suffice to violate the source's definition
  of a regular polygon. No classification of all polygonal Radon planes is
  needed.

No conditional lemma remains.

## Numerical regression check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1809.04760_irregular_radon_polygons_all_orders/code/check_edge_lengths.py
```

Output:

```text
verified n=1,...,100 at stretch=2
```

The script compares directly computed image edge lengths with the proof's
closed formula and checks the two distinguished lengths are unequal. This
finite test is only a sanity check; the symbolic argument is the proof.

## Novelty check

- Searched `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`,
  and `proof_gaps/index.tsv` for arXiv:1809.04760 and the central terminology;
  no duplicate was found.
- Bounded web/arXiv searches through 2026-08-11 used the exact source question,
  exact title and arXiv id, and combinations of `irregular polygon`, `4n+2`,
  `Radon plane`, `affine image`, and `affinely regular`.
- The search found literature recognizing affine-regular hexagonal Radon unit
  spheres but no explicit later answer to the source's exact all-orders question.

Novelty confidence is moderate-to-low because affine invariance is elementary
and the search was bounded rather than exhaustive.

## Source evidence

- Source: arXiv:1809.04760v2, 11 pages.
- Exact location: page 11, conclusion, final open question.
- `figures/open_problem_crop.png` was rendered from `source_paper.pdf` at
  200 dpi, retains the full page width, and shows the complete question.

## PDF QA

- Final packet: 4 US-Letter pages, 339,638 bytes, PDF 1.7.
- Final SHA-256:
  `87ada538c09568767b6bbe3ada2f21bf0b3261c7169755d8b548b8e3bb107a48`.
- `tmp/main.pdf` and `solution_packet.pdf` are byte-identical.
- The final LaTeX log has no warnings, overfull/underfull boxes, undefined
  references, or errors.
- Ghostscript text extraction contains the construction algorithm, bounded
  novelty check, and references.
- All four pages were individually inspected at 150 dpi after the final edit;
  no clipping, overlap, broken glyph, unreadable formula, or page-flow defect
  was found.
- The source crop was separately inspected and is fully readable.

## Human-review recommendation

Check the source's Euclidean meaning of `irregular` and the bounded literature
search. If those agree with the source formulation, the packet is ready for
promotion as a complete affirmative answer with a uniform algorithm.

