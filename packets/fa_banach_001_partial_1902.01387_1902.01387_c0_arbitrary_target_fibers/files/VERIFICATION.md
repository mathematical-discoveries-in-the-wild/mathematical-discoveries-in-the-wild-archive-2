# Verification report

Status: `candidate_partial_result_likely_valid`

## Mathematical checks

- Checked the source question against arXiv:1902.01387, PDF page 15.
- Checked the decisive later theorem against arXiv:1909.05105, Theorem 2.4,
  PDF pages 9--10.
- Checked the new dichotomy directly from Schwarz--Pick:
  `rho(u_n(y),u_n(0)) <= ||y||`. If the center subsequence stays in
  `q D`, then `|u_n(y)| <= (q+||y||)/(1+q||y||) < 1`; if its center values
  converge to the circle, all point values converge to the same circle point.
- Audited the proof of Theorem 2.4 after its Lemma 2.2. The scalar maps depend
  only on the `c0` source coordinates and the point values `g(y),h(y)`.
  Hartogs' theorem works on `B_Y x B_Y`; weak-star compactness of the general
  vector spectrum is established in arXiv:1902.01387; and its Lemma 2.3 gives
  the target-domain-free point-evaluation criterion for holomorphy.
- Checked the complemented-transfer fiber identity on every `x* in X*`.
- Checked exact Gleason preservation: restriction `R(f)=f o J` maps the unit
  ball onto the unit ball because `E(u)=u o P` is an isometric right inverse.

No computational experiment is needed; the result is qualitative.

## Upgrade attempts

After obtaining the `X=c0` partial result, two further upgrades were tested.
The arbitrary-`Y` upgrade succeeded through the center-value Schwarz--Pick
dichotomy, and the 1-complemented-`c0` transfer succeeded. Removing the
`c0` source structure was not credible: known largeness of each scalar fiber
does not supply a coherent analytic family as the base point varies, while
the source paper's perturbation radius collapses at norm one.

## Literature check

The run indexes and bounded arXiv searches used arXiv ids 1902.01387,
1909.05105, and 2102.06771 together with `vector-valued spectrum`, `c0`,
`arbitrary Banach Y`, `separable Banach Y`, and `fiber`. The exact known result
located is only `X=Y=c0` in arXiv:1909.05105. No arbitrary-target or
complemented-`c0` version was found. Novelty confidence is bounded.

## Rendering check

Compiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`.

The final eight-page packet was rendered at 150 DPI. Every page was visually
inspected for clipping, overflow, broken formulas, crop readability, and page
transitions. The final LaTeX log contains no warnings, overfull boxes, or
underfull boxes.

## Human-review recommendation

Review as a likely valid partial result. The highest-value check is the
domain-independence audit of the proof of arXiv:1909.05105, Theorem 2.4.
