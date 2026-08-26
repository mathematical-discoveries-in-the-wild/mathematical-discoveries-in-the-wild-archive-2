# Verification record

Verified at: `2026-08-13T14:54:41Z`

## Claim audited

There is a nonempty weakly compact convex `K subset c0` and a Borel
fixed-point-free map `T:K -> K` satisfying condition `(L)` and property
`(*)`.  The ambient space is NUNC and has `M(c0)=MW(c0)=2`.  This is a full
negative answer to the source's extension question under those three
hypotheses, with no claim about uniformly nonsquare spaces.

## Source provenance

- Official source: `https://arxiv.org/pdf/1209.5368`
- Local source: `source_paper.pdf`
- Source PDF: 15 pages, letter size, unencrypted.
- Exact question: page 14, Remark 4.8.
- Evidence image: `source_question_crop.png`, deterministically produced by
  `code/crop_source.py` from the 180-DPI RGB render
  `tmp/source_audit/page-14.png`.
- The evidence image was visually inspected at original resolution and
  retains the preceding geometric statement, Corollary 4.7, and the full
  text of Remark 4.8.

## Mathematical audit

Seven focused passes were recorded in
`runs/fa_banach_001/attempts/1209.5368_c0_condition_l_counterexample.md`.
The decisive checks were:

1. `u_n` is weakly null because its finite support escapes every coordinate,
   and consecutive tent distances are positive and tend to zero.
2. The closed convex hull is weakly compact by the closed-convex-hull theorem.
3. For every `z in K`, `||u_n-z|| -> 1`; positivity also makes all these
   distances at most one.  Therefore the nearest-orbit index is attained,
   including when its infimum equals one.
4. Every approximate fixed-point sequence is asymptotic to orbit points with
   indices tending to infinity and has distance tending to one from every
   point of `K`.
5. Every nonempty invariant subset contains an orbit tail, so condition-(L)(i)
   holds; the distance-one classification makes condition-(L)(ii) an equality.
6. The same classification makes every relative asymptotic center in `(*)`
   equal to the whole invariant relative set.
7. Finite/tail estimates prove `R(a,c0)=RW(a,c0)=max(1,a)` and `b(t,x)=0`
   for `0<t<=1`, yielding `M(c0)=MW(c0)=2` and NUNC.

The final adversarial audit specifically rechecked weak compactness, nearest
index attainment, strict positivity of every finite tent step, orbit-tail
invariance, the asymptotic-diameter restriction in `R`, and the source's
quantifiers in the NUNC definition.

## Computational check

Command:

```sh
/Users/pacuaviva/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 code/verify_tents.py
```

Output:

```text
moving-tent checks: PASS
sampled d_2=1.000000000, d_22=0.925302944
late sampled steps: d_100=0.426369391, d_1000=0.129730721, d_10000=0.040341923
analytic bound at n=10000: 0.040341923
```

The checker compares dense sampling with the piecewise-linear knot
calculation, tests large-index decay, and checks nearest-point/AFPS
inequalities on orbit points and seeded random finite convex combinations.

## PDF build and visual QA

Build command:

```sh
/Library/TeX/texbin/latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp/latex main.tex
```

- Build completed without overfull boxes, underfull boxes, unresolved
  references, or LaTeX/package warnings.
- `solution_packet.pdf` has 4 pages, letter size, no encryption, and no
  JavaScript.
- Every final page was rendered at 160 DPI to
  `tmp/final_render/sealed-1.png` through `sealed-4.png`.
- All four final renders are RGB, `1360 x 1760` pixels.
- Every sealed page was visually inspected at original resolution.  Text,
  formulas, the result box, page numbers, and the genuine source crop are
  legible; no clipping, overlap, missing glyphs, or layout defects were seen.
- `pdftotext -layout` extraction was inspected for the result, theorem,
  coefficient formulas, scope caveat, checker command, and source citation.

## SHA-256 hashes

```text
0ea3c9479e99664c3aefa4702a55b0dc28468c154808ab740349f868c4eefa3a  solution_packet.pdf
4c2f52249c96a4d1b1b00cfca809a1b9a728fd25864c01a7e97d006fa0c27749  source_paper.pdf
471aa6e58ca11751123b11219c3c3dd8f36f71fb95a4ee3926a43e5f6e181309  source_question_crop.png
d0aad9339cfe70755db7bb21b8de76d99b338fc796e2d93bf791d5c8040e30e2  main.tex
334e9a5df82be7ace26a494e97708e8564b883003586172e7bb73f0c4f95003d  code/verify_tents.py
7fa3e932d23de1e9e3684fc7f276cc592f3c61d54d2ca24469005e2a7b2d2f86  code/crop_source.py
b86b0053cbe29526f3bb9f9981241c54fff73a950167c8feefad8f0b055cb333  attempt log
```

## Novelty scope

Exact-ID and core-keyword searches of the four cheap run indexes found no
duplicate.  A bounded public literature search through 2026-08-13 located
general fixed-point-free condition-(L) examples but no answer combining
condition `(L)` with a weakly compact convex domain in the specific
`c0`/NUNC/`M` geometry proved here.  Human review should focus on the
least-nearest-index selection, the AFPS classification, and whether any
later non-keyworded literature contains this exact construction.
