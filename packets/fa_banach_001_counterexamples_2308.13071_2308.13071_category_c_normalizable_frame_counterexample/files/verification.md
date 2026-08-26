# Verification report

Verdict: `candidate_counterexample_likely_valid`.

## Formal proof audit

The proof reduces to the following exact checks.

1. For fixed `k` and `p`, adding the two rank-one operators associated to
   `u_{k,p}^{+}` and `u_{k,p}^{-}` cancels the cross terms and leaves diagonal
   weights `2-a_k` at `p` and `a_k` at `sigma_k(p)`.
2. Because `sigma_k:E_k -> E_k^c` is bijective, the complete block operator is
   `S_k=a_k I+(2-2a_k)P_{E_k}`.  Its optimal bounds are `a_k` and `2-a_k`.
3. On a coordinate in `E_m`, the normalized union has eigenvalue
   `2-a_m + sum_{k != m} a_k = 3-2a_m`.  These values have infimum `2` and
   supremum `3`.
4. On the same coordinate, the unnormalized union has eigenvalue
   `C+r_m^2(2-2a_m)`, where `C=sum r_k^2 a_k=1/7`.  The added term has maximum
   `1/4` at `m=1` and tends to zero.  Hence the optimal bounds are `1/7` and
   `11/28`.
5. With `delta_k=(3/2)r_k`, one has
   `delta_{k+1}<r_k<delta_k`; the neighboring norms are already outside this
   interval.  Thus the band is exactly `r_k U_k`, with optimal bounds
   `2^{-3k}` and `4^{-k}(2-2^{-k})`.

All series involved are positive diagonal operator series, so their quadratic
forms may be summed coordinatewise without a rearrangement issue.  The
displayed uniform upper bounds show bounded strong limits.

No numerical computation or external theorem is used in the proof.

## Source-figure generation

From the packet directory:

```bash
conda run --no-capture-output -n sandbox python code/crop_source_pages.py
```

This renders pages 8 and 9 of `source_paper.pdf` at 180 dpi into `tmp/` and
writes the two final crops to `figures/`.

## PDF build and audit

The final packet was built with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

Audit result on 2026-08-09:

- `solution_packet.pdf` has 4 letter-sized pages.
- The final LaTeX log contains no overfull or underfull boxes, undefined
  references, or LaTeX/package warnings.
- `pypdf` extracted 6,684 characters.  Required markers for Conjecture 3.14,
  the counterexample theorem, the optimal bounds, scope, novelty, and the
  human-review recommendation were all present.
- All four final pages were rendered at 150 dpi and visually inspected.  No
  clipping, overlap, missing glyphs, illegible figures, or stray build
  artifacts were found.
- Both source crops were inspected at original resolution.  They legibly show
  Theorem 3.13(c) and Conjecture 3.14 on source pages 8 and 9.

Final SHA-256 checksums:

```text
02a65b92ca69a7f712c1c24ef88dd42102a9909bd66923aa389ea055ff884a46  solution_packet.pdf
a5ffcb310625ef676720778ab2a125298dca9a2faacc041182a7b7d0fd60ff63  source_paper.pdf
8b5c245c6547ac22c846c0c8abb3444ab229adf3ef1d54e89484ee61a1bc3017  figures/category_c_theorem_crop.png
a2ad4604f59ce685abce5da536c8a937a716f886e3f8ca38b13313cbed31e3e3  figures/open_problem_crop.png
```

## Suggested reviewer focus

- Verify the rank-one cancellation identity.
- Verify the coordinatewise eigenvalues of the normalized and scaled unions.
- Verify that the half-open bands isolate exactly the scale `r_k`.
- Check whether an answer to Conjecture 3.14 appeared after the bounded search.
