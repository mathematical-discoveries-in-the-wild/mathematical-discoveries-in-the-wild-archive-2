# Verification report

verdict: candidate_counterexample_likely_valid

review_date: 2026-08-09

## Claim checked

Removing `dom(A) subset E_u` from Theorem 5.2 of arXiv:2204.00146 destroys its four-way equivalence. For `E=L^2(0,1)`, `u=1`, `P f=(integral f)1`, and `A=P-I`, source conditions (i), (ii), and (iii) hold, while (iv) fails.

## Algebra audit

1. `P^2=P` because `integral_0^1 1 = 1`.
2. `A=0*P-1*(I-P)`, so `sigma(A)={0,-1}`, `s(A)=0`, and the spectral projection at zero is `P`.
3. `exp(tA)=P+exp(-t)(I-P)=exp(-t)I+(1-exp(-t))P`.
4. `C(r)=a_r I+(1-a_r)P`, where `a_r=(1-exp(-r))/r` and `0<a_r<1` for every `r>0`.
5. `R(lambda,A)=lambda^{-1}P+(lambda+1)^{-1}(I-P)=(lambda+1)^{-1}I+[lambda(lambda+1)]^{-1}P`.
6. At `mu=-1/2`, `R(mu,A)=2I-4P`.

All identities were rederived using the complementary invariant subspaces `ran(P)` and `ker(P)`; no symbolic or numerical oracle is needed.

## Order and quantifier audit

- For each `0<f in L^2`, `integral f>0`; hence `Pf=(integral f)1` is strongly positive relative to `1`.
- For every `r>0`, `C(r)f >= (1-a_r)(integral f)1`. The coefficient is positive; for all `r>=r0>0` it has a positive uniform lower bound.
- For every `lambda>0`, `R(lambda,A)f >= (integral f)/[lambda(lambda+1)] * 1`. On any interval `(0,epsilon)` this also supplies the standard scaled maximum inequality with one positive constant.
- The fixed witness `f(x)=x^{-1/4}` is positive and lies in `L^2(0,1)` because `f^2=x^{-1/2}` is integrable. Its integral is `4/3`.
- For every `mu in (-1,0)`, `R(mu,A)f=(1+mu)^{-1}(x^{-1/4}-4/(3|mu|))`, which is positive near zero. Thus this one witness defeats ordinary and strong anti-maximum negativity for every point in every possible left neighbourhood of zero.
- `dom(A)=L^2(0,1)` because `A` is bounded, while `E_1=L^infinity(0,1)`, and the witness itself lies outside `L^infinity`.

## Literature-audit check

The PDF and TeX of arXiv:2203.05680v2 were inspected. Page 3 uses the same operator, prints the same resolvent formula, and then asserts `R(mu,A) preceq -1 tensor 1` for all `mu in (-1,0)`. At `mu=-1/2`, the exact identity `R=2I-4P` and the witness above show that the asserted inequality fails. This observation concerns the auxiliary example after Theorem 1.2; it does not by itself refute Theorem 1.2, whose weak domination hypothesis fails for this bounded operator.

## Novelty bounds

Searched on 2026-08-09:

- `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and `proof_gaps/index.tsv` for arXiv:2204.00146 and core terms;
- local source trees for arXiv:2204.00146 and arXiv:2203.05680;
- arXiv/web exact and close searches for the source titles, `A=P-I`, rank-one projection, Cesaro means, anti-maximum principle, `dom(A)`, `E_u`, erratum, and correction.

No prior run result, later erratum, or exact later correction was found. The construction is prior literature; the corrected conclusion appears unrecorded in the searched sources. Mathematical-confidence assessment: high. Novelty-confidence assessment: medium.

## Source and rendering audit

- Source paper: arXiv:2204.00146v3, PDF page 18 for the future-work paragraph; page 17 begins Theorem 5.2.
- Supporting paper: arXiv:2203.05680v2, PDF page 3 for the audited example.
- `figures/open_problem_crop.png` was rendered from the original source PDF at 150 dpi and visually inspected for full-width legibility and unclipped text.
- `figures/literature_audit_crop.png` was rendered from the supporting PDF at 150 dpi and visually inspected for full-width legibility and unclipped displayed formulas.
- Final packet compiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp/pdfs main.tex`.
- The final log contains no warnings, overfull/underfull boxes, undefined references, multiply-defined labels, or errors.
- All five final pages were rendered at 180 dpi and inspected individually. Headings, equations, page numbers, source crops, citations, and section transitions are legible and unclipped; no overlaps, missing glyphs, black boxes, or misplaced floats were found.

## Final checksums

- `solution_packet.pdf`: `af3ac95a75ce57bebf47649e48b2ff00958823ca3f40cc1ee31e5225728f7f3a`
- `source_paper.pdf`: `f3209234f9920ed93a0510afb20937b06b0e1bfcfb134547cad1426ab7a59668`
- `supporting_paper_2203.05680.pdf`: `f2385f4c4439c993b5aacf374cbd2c9fd79b947d8df06cf61fe38e8e9197ac52`
- `figures/open_problem_crop.png`: `4909c3434260d6a2dfcb3bab648322d4d4f6e2837e13fdf3553c9f3364346e50`
- `figures/literature_audit_crop.png`: `4e56c522f8d5e685a2a7201a80086dd0d1064c2e2281ca339278e50b5f449dd7`
