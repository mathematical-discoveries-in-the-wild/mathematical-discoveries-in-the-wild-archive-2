# Verification record

Verified at: `2026-08-13T15:05:44Z`

## Claim audited

The uniform greedy estimate (B.4) from arXiv:1506.03549 fails for a fixed
five-dimensional sparse approximation triple, even under unique greedy
choices and even though every signal is compressible.  For
`x_epsilon=(2,3/2,2,1,epsilon)`, `0<epsilon<1`, the two-step ratio is
`(1+epsilon)/epsilon`, and the three-step greedy residual is nonzero although
the best three-term error is zero.

## Source provenance

- Official source: `https://arxiv.org/pdf/1506.03549`
- Local source: `source_paper.pdf`
- Source PDF: 29 pages, letter size, unencrypted.
- Exact open question: printed page 27, equations (B.2)--(B.4).
- Evidence image: `source_question_crop.png`, deterministically produced by
  `code/crop_source.py` from the 180-DPI RGB render
  `tmp/source_audit/page-27.png`.
- Both the complete source page and the final crop were visually inspected at
  original resolution.  The crop retains the compressibility definition,
  best-error definition, lower bound, exact question, and positive-constant
  inequality.

## Mathematical audit

Seven focused attempts are recorded in
`runs/fa_banach_001/attempts/1506.03549_overlapping_coordinate_groups_greedy_counterexample.md`.
The final audit checked:

1. The four coordinate subspaces form a finite closed union `A`.
2. The inclusions `A subset ell_1^5 subset ell_2^5` are bounded with the
   source's normalization `||i_M||=1`.
3. Finite dimensionality makes every nonempty closed subset proximinal.
4. Every coordinate projection is the unique simultaneous best approximator
   in `ell_1` and `ell_2`, and both source norm-splitting identities hold.
5. `E_{S1}+E_{S2}+E_{S4}=R^5`, hence `3A=R^5` and sparse density holds.
6. Captured masses make all three greedy choices strict for `0<epsilon<1`.
7. Exhaustion of two-support unions gives `sigma_2=epsilon`; the displayed
   three-support decomposition gives `sigma_3=0`; and `3A=M` makes every
   vector compressible under the exact source definition.

The coordinate-projection identity also proves the structural reduction to
weighted greedy maximum coverage, so the construction is not dependent on
floating-point optimization.

## Exact-rational verifier

Command:

```sh
conda run --no-capture-output -n sandbox python code/verify_counterexample.py
```

Output:

```text
epsilon=1/2: choices=[3, 1, 2], g2=3/2, sigma2=1/2, ratio=3, g3=1/2, sigma3=0
epsilon=1/10: choices=[3, 1, 2], g2=11/10, sigma2=1/10, ratio=11, g3=1/10, sigma3=0
epsilon=1/1000: choices=[3, 1, 2], g2=1001/1000, sigma2=1/1000, ratio=1001, g3=1/1000, sigma3=0
coordinate-group greedy counterexample: PASS
```

The script uses `fractions.Fraction`, enumerates all support multisets, and
asserts uniqueness of every greedy minimizer.

## PDF build and visual QA

Build command:

```sh
/Library/TeX/texbin/latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp/latex main.tex
```

- Build completed without overfull boxes, underfull boxes, unresolved
  references, or LaTeX/package warnings.
- `solution_packet.pdf` has 3 pages, letter size, no encryption, and no
  JavaScript.
- All three final pages were rendered at 160 DPI to
  `tmp/final_render/sealed-1.png` through `sealed-3.png`.
- Each sealed render is RGB, `1360 x 1760` pixels.
- Every final page was visually inspected at original resolution.  The source
  crop, support table, formulas, result box, proof, scope statement, and
  references are legible with no clipping, overlap, missing glyphs, or layout
  defects.
- `pdftotext -layout` extraction was checked for the result, definitions,
  triple lemma, uniqueness table, theorem, compressibility conclusion, and
  verifier output marker.

## SHA-256 hashes

```text
c01118e6107cda2d95a13c5dbb7cdd25ac0f4fdf504d7add3905c374cd27970c  solution_packet.pdf
f102b9cf2d45ac7a07aecf51706b6406aa3cc5c134e1cd143bc4782e71808cf4  source_paper.pdf
7722c6c23021c6800025fae10a98d68b545f18360d1a6b3b6a1dfc32a2a74101  source_question_crop.png
2e82fcacdc8e03cd17b209e2134c7964d32c50ef3c3908d0820baa47560b5a4c  main.tex
0a377313a2aa1ff51249be0201121c35f95f5de3bcec28b505f80aab3c3df7fa  code/verify_counterexample.py
c010a57d9b4e500b30948082727a98f0bf815179208388dc03c1e6fceec5cc96  code/crop_source.py
b9fa44f5f88dd84fa705a8972938b511181c62f0549c121cac857ab8e9e3cf07  attempt log
```

## Novelty scope

Exact-id and core-phrase searches of the four cheap run indexes found no
duplicate.  Bounded exact-phrase and concept searches through 2026-08-13
found the arXiv and 2017 published source but no later resolution of the
specific sparse-approximation-triple greedy question.  Human review should
prioritize the interpretation of the source's global constant and a broader
citation search for an equivalent coordinate-support counterexample.  The
zero-best-error failure is decisive even if the constant were allowed to
depend on the individual signal.
