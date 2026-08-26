# Verification

## Mathematical audit

- **Parameter conversion:** With `beta=gamma-p` and
  `a=(beta+1)/p`, the assumptions give `-1<beta<p-1`, `0<a<1`, and
  the source upper threshold becomes `(2+a)/3`.
- **Lower endpoint:** Multiplication `M f=x_1 f` is an exact isometry from
  `L^p(w_gamma)` to `L^p(w_beta)`.
- **Trace identities:** On smooth functions,
  `Tr_0(Mf)=0`, `Tr_1(Mf)=Tr_0 f`, and
  `Tr_2(Mf)=2 Tr_1 f`; continuity of the relevant traces extends these
  identities to the endpoint Sobolev spaces.
- **Full-zero endpoint:** Lemma 3.6(ii) of arXiv:2406.03297 gives
  `M:W_0^{3,p}(w_gamma) -> W_0^{3,p}(w_beta)` as an isomorphism. At the
  lower weight, the latter is exactly the kernel of normal traces 0, 1, and 2.
- **Dirichlet endpoint, forward map:** Lemma 3.6(i) makes `M` bounded on the
  full Sobolev space. A zero zeroth trace at the original weight produces zero
  normal traces 0 and 1 after multiplication.
- **Dirichlet endpoint, inverse map:** If `g` has lower-weight traces 0 and 1
  zero, put `q=Tr_2 g`. The trace theorem gives
  `q in B_{p,p}^{1-a}=B_{p,p}^{2-(gamma+1)/p}`. The universal right inverse
  `ext_1` at the original weight maps `q/2` boundedly into `W^{3,p}(w_gamma)`,
  has trace 0 zero and trace 1 equal to `q/2`. Thus
  `h=g-M ext_1(q/2)` has all lower-weight traces 0, 1, and 2 zero. Divide `h`
  by `M` using the full-zero isomorphism. This proves surjectivity and the
  inverse norm bound.
- **Interpolation:** Theorem 6.4 of arXiv:2503.14636 applies because the shifted
  weight is Muckenhoupt, `X` is UMD, `s_0=0>-1+a`, and the top smoothness is 3.
  For `3 theta<2+a`, the boundary systems `(Tr_0,Tr_1)` and
  `(Tr_0,Tr_1,Tr_2)` define the same intermediate Bessel-potential space.
- **Critical parameters:** The theorem excludes only
  `3 theta=a` and `3 theta=1+a` inside the desired interval. For either value,
  choose noncritical parameters on both sides, use the already proved endpoint
  equalities there, and apply exact complex reiteration. The endpoint couples
  are regular since their smooth interior test functions are dense in `L^p`.

## Literature boundary

The local registry and solution indexes were searched by arXiv id, title, and
core interpolation terms. External searches covered the exact title, exact
question language, “Remark 4.9”, equation (4.3), the four authors, and citation
pages for arXiv:2507.13478, 2503.14636, and 2406.03297 through 2026-08-12. The
current arXiv versions and author/publication pages were also checked. No later
paper explicitly resolving this interpolation identity was found. Novelty is
therefore plausible but remains subject to specialist citation-database review.

## Artifact checks

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully after the final edit.
- The final log was checked for undefined references, overfull boxes, and
  LaTeX warnings.
- `pdftotext` extraction was checked for the theorem, all proof steps, scope,
  and references.
- Every rendered page was visually inspected for clipping, collisions,
  illegible formulas, and malformed figures.
- The final packet has four pages and SHA-256
  `294ad25554808f7f523c6e0e657b8da1bfbc0d124b6310a9b29a3c76a18df9dd`.

## Human-review recommendation

Prioritize the surjectivity part of the endpoint weight-shift lemma and the
critical-index reiteration. Once those two steps pass, the application of
Roodenburg's Theorem 6.4 and the trace-threshold comparison are direct.
