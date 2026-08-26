# Orbit-barycenter fixed points for affine rotative maps

Status: `candidate_substantial_partial_likely_valid`

Source: Tammatada Pongsriiam and Imchit Termwuttipong, *Fixed points of continuous rotative mappings on the real line*, arXiv:1405.7872 (2014), Questions 3--6 on PDF page 4.

This packet gives a complete answer for the affine subclass in every Banach space: every affine Lipschitz `(n,a)`-rotative self-map of a nonempty closed convex set has a fixed point whenever `a<n`. Equivalently, the affine-restricted threshold is infinite for all spaces and parameters. Thus every finite counterexample relevant to the source questions must be genuinely nonlinear.

The proof iterates the barycenter of the first `n` orbit points. Affineness makes the new displacement exactly `(T^n x-x)/n`, so it contracts by `a/n<1`, while the barycenter steps are summable. A robust extension proves the same conclusion for nonlinear maps whose orbit-barycentric defect is at most `eta||Tx-x||`, provided `eta+a/n<1`.

The unrestricted values of `gamma(X,n,a)`, including Question 4 for `C[0,1]` and `a<=1`, remain open.

## Files

- `main.tex` and `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_questions_crop.png`: full-width source crop of Questions 3--6.
- `code/crop_source.py`: reproducible crop script.
- `tmp/`: LaTeX and rendering intermediates.

## Verification and review recommendation

The proof is symbolic. Human review should check the affine telescoping identity, the summable-step estimate, and the precise normalization of the nonlinear orbit-barycentric defect. A bounded index and literature search through 2026-08-17 found no exact match; novelty confidence is provisional.

