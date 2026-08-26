# Verification report

Verdict: `candidate_substantial_partial_likely_valid`

Checked on 2026-08-13 by `agent_lane_12` / GPT5.6.

## Mathematical audit

- Checked the Moore--Penrose formula `G^dagger=T S^(-2) T*` on `ran(T)` and
  `ker(T*)`, and hence the identity between dual analysis and
  `G^dagger` applied to primal analysis.
- Checked the weak-`ell^p` tail estimate for every `0<p<2` and the synthesis
  constant `sqrt(B)`.
- Checked positivity and exact frame bounds of the rank-two perturbation
  `G=I+epsilon K`.
- Checked that `u=G^(-1/2)e_1` has primal analysis exactly `e_1`.
- Checked the unique primal coefficient sequence
  `G^(-1)e_1=(e_1-epsilon w)/(1-epsilon^2)`.
- Checked by the integral test that the squared tail of
  `w_n=C/(sqrt(n) log(n+1))` is comparable to `1/log N`.
- Checked that the lower Riesz bound converts that coefficient tail into the
  claimed lower bound for best primal approximation.
- No claim is made that the specific hybrid Gramian satisfies the transfer
  criterion.

## Upgrade audit

The attempt file records eight distinct routes. The localized-matrix and
frame-operator routes both isolate the same missing mixed-index inverse
estimate; the later full-plane dualizable-shearlet construction does not
control the bounded-domain hybrid cross terms.

## Artifact audit

- LaTeX built successfully in two passes. The final log has no warning,
  overfull-box, underfull-box, undefined-reference, or fatal-error message.
- All three A4 packet pages were rendered at 150 dpi and visually inspected.
  No clipping, collision, malformed formula, or stranded heading was found.
- Source-paper PDF page 18 was rendered and inspected; it contains the exact
  Outlook bullet asking for primal-frame approximation rates.
- Ghostscript text extraction contains both theorem statements, the
  Moore--Penrose formula, the logarithmic lower bound, the conservative scope
  qualification, and the bibliography.

SHA256:

- `solution_packet.pdf`:
  `cac9c38590aefd99e794c1523654ddb52b4818fa2aa77447a4bd4f9df6a45701`
- `source_paper.pdf`:
  `ade3efa07ef1ba0a94873965d8052be3f173ecbef4ec4ff2c5d076d37a7c07ee`
- `main.tex`:
  `4c778c8912811d019298fcebdedc67363eaf06e223710f46d556309ee7cdc4b7`

## Recommended reviewer focus

Verify the Moore--Penrose identity and the exact distinction between primal
analysis sparsity (dual-atom reconstruction) and canonical-dual analysis
sparsity (primal-atom reconstruction). Also assess whether the abstract
near-Parseval counterexample has appeared in equivalent form in the nonlinear
frame-approximation literature.
