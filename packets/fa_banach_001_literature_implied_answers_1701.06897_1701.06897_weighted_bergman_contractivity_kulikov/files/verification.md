# Verification

Verified on 2026-08-12.

## Mathematical checks

- The source question was checked in the primary arXiv:1701.06897 PDF,
  pp. 9--10.
- Kulikov's critical-line inequality and Hardy endpoint were checked in the
  primary arXiv:2203.12349 PDF, Corollary 1.3 on p. 3.
- The source condition `q/beta <= p/alpha` was independently rearranged as
  `beta >= alpha*q/p`.
- The radial normalization was checked after the substitution `x=r^2`:
  `(gamma-1)(1-x)^(gamma-2) dx` has total mass one.
- Its tail is `(1-t)^(gamma-1)`, so increasing `gamma` makes the radial
  variable stochastically smaller.
- The circular means of `|f|^s` are nondecreasing because `|f|^s` is
  subharmonic for every `s>0`.
- The cases `p<q`, `p=q`, `alpha=1`, and the forced endpoint
  `alpha=beta=1` were checked separately.
- The packet explicitly limits its scope to the one-variable weighted
  Bergman embedding question.

## Packet checks

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully.
- The final log contains no warnings, undefined references, overfull boxes,
  fatal errors, or compilation errors.
- `solution_packet.pdf` has 4 pages.
- All four pages were rendered to PNG at 150 dpi and visually inspected.
- No clipping, overlap, unreadable text, missing glyphs, or broken figures
  were found.

## SHA-256

- `solution_packet.pdf`:
  `47d07884dff257cb0052f61fb8e94b1a91c002aaa0ae392cdcbc16fbc3d9baf2`
- `source_paper.pdf`:
  `964eeb90d00ea5026fc6a71911d94466f486534d635ac2023c499ab1912291b5`
- `supporting_paper_kulikov_2203.12349.pdf`:
  `703b69593ff0ecea69a9db18dadabc360238bbe6768e663c3f04905cea2e1d3b`
- `figures/open_question_crop.png`:
  `9f40fae0132513bb1523e3604d0acdf438709110f332bd5754f792f28376b580`
- `figures/open_question_continuation_crop.png`:
  `328f65ae4225780d7722324c59ca19f93e716ff2e3522c5e6440ed388488cfa6`
- `figures/supporting_corollary_crop.png`:
  `da2d51ae7762a24767543d79e2968263f6ae99b7ffb5cc499446eaf60e75750d`

