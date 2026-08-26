# Projection-free Clark-operator formula from Liaw--Treil

Status: `literature_implied_answer (full for the selected open problem)`

In arXiv:1205.4376, Theorem 6.1 gives a formula for the adjoint Clark
operator in the non-inner scalar case that still contains the orthogonal
projection `P_theta`.  Remark 6.2(b), PDF page 10, asks for a reasonable
formula for `Phi_1^* f` without that projection.

Liaw and Treil, arXiv:1308.3298, Theorem 3.1 (PDF pages 11--12), give a
universal singular-integral representation for the adjoint Clark operator in
an arbitrary transcription of the functional model.  It contains no model
projection.  Under the parameter correspondence between the papers, the
source's `Phi_1^*` is the later paper's `Phi_0^*`; specializing equations
(3.1)--(3.3) at `gamma=0` gives

```text
Phi_1^* f(z)
  = (f(z),0)^T
    + (1-theta(z),-Delta(z))^T
      integral_T (f(xi)-f(z))/(1-conjugate(xi)z) dmu(xi).
```

This fully answers the selected projection-removal problem.  The supporting
paper cites the survey, but the precise `gamma=1`/`gamma=0` parameter
translation is an identification made in this packet, so the provenance
bucket is `literature_implied_answers` rather than
`literature_already_answered`.

Files:

- `source_paper.pdf`: arXiv:1205.4376.
- `supporting_paper_1308.3298.pdf`: the Liaw--Treil answer.
- `figures/source_question_page10.png`: Theorem 6.1 and Remark 6.2(b).
- `figures/supporting_theorem3_1_page12.png`: the universal formula and its
  explicit Sz.-Nagy--Foias coefficients.
- `main.tex` and `solution_packet.pdf`: compact identification note.
- Ledger:
  `runs/fa_banach_001/ledger/results/1205.4376_clark_projection_removed_by_1308.3298.json`.

Scope: the packet answers this one concrete formula question, not the survey's
independent questions on singular continuous spectra, Anderson localization,
or higher-rank Aronszajn--Donoghue theory.

Human-review recommendation: check the normalization correspondence
`mu=mu_1`, `U_0=M_xi-(.,conjugate(xi))1`, `theta=theta_0`, and hence
`Phi_1^*(source)=Phi_0^*(supporting)`.  Then set `gamma=0` in supporting
equations (3.1)--(3.3).

