# Verification

Date: 2026-08-09

## Finite-dimensional support-formula checks

Command:

    conda run --no-capture-output -n sandbox python code/verify_finite_model.py

Output:

    finite l1 models checked: 360
    worst primal-dual gap:   5.329e-15
    support formula: OK

The test compares the primal support maximization under
`||f_i +/- g||_infinity <= 1` with the decomposition formula of Lemma 3,
using independent random nonnegative coefficients in finite-dimensional
`ell_1` models. This is a stress test of the adjoint equations and factor
`2`; it is not part of the proof.

## Proof audit

- The constraint norm `N` is a genuine norm, and its defining map into the
  finite maximum sum of copies of `X*` is an isometry with closed range.
- The support functional is the dual norm because the constraint ball is
  symmetric. Hahn--Banach gives an extension with the same norm; the dual
  of the finite maximum sum is the finite `ell_1` sum of copies of `X**`.
- Expanding the adjoint conditions gives
  `p_i+q_i=(a_i+b_i)Jx_i` and
  `sum(p_i-q_i)=sum(a_i-b_i)Jx_i+cJy`. Setting
  `r_i=p_i-a_iJx_i` gives exactly `2 sum r_i=cJy`.
- For `c=0`, the required lower bound is termwise triangle inequality. For
  `c>0`, local reflexivity is applied only to the finite span of the
  `r_i`, `Jx_i`, and `Jy`; it fixes every canonical vector exactly and
  preserves the prescribed sum. Letting its distortion tend to one
  transfers the DOH inequality without loss.
- If the coordinate image misses the closed upper orthant, compact-versus-
  closed strong separation applies in finite dimensions. The separating
  coefficients are nonnegative because the separating functional must be
  bounded below on the upper orthant.
- Choosing `rho` strictly below every slice width and the requested
  tolerance turns the non-strict coordinate bounds into the strict slice
  and norm inequalities required by weak-star SSD2P.

## Source and novelty audit

- The official arXiv PDF is stored as `source_paper.pdf`; SHA-256:
  `c9d91aaeeb1fa70661479241f388d3f43fa6df9189baa3f2d530d11b76dff3df`.
- ArXiv:2404.11430 is stored as `supporting_paper_2404.11430.pdf`; SHA-256:
  `57c424aa8d9479522574878113c8b066dea4507176cf6bdb6a7162f5d2e9913e`.
  Its Section 4 explicitly says the general converse remains open.
- Exact-title, arXiv-id, exact-phrase, and core-term searches on August 9,
  2026 found no later proof or counterexample. Later dissertation material
  returned by the search also retained the question as open.

## Packet build and visual QA

- `latexmk` completed with no remaining warnings, undefined references,
  overfull boxes, or underfull boxes.
- The final PDF has 5 letter-sized pages.
- All 5 pages were rendered at 150 dpi and visually inspected. A first pass
  caught and corrected two malformed spacing commands; the final render has
  no clipping, overlap, missing glyphs, broken equations, or unreadable text.
- `solution_packet.pdf` SHA-256:
  `0dbc3886a9db4cc578f4e482a56fd8f43d77510851152b510edba2551699112c`.

## Human review focus

- Confirm the Hahn--Banach support formula and its use of the full bidual.
- Confirm that the stated form of local reflexivity fixes the whole
  intersection of the finite-dimensional domain with `JX`.
- Check the orientation of the upper-orthant separation.
- Check that the source's definition is the real-scalar definition used in
  the packet; no complex-scalar extension is claimed.

