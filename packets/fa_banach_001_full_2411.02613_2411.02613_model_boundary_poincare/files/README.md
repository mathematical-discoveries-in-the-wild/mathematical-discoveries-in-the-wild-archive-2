# Poincare inequality on the finite-type model boundary

Source: Tuomas Hytönen, “Schatten properties of commutators on metric
spaces,” arXiv:2411.02613, Example 1.24, PDF page 8.

Status: candidate_full_likely_valid.

For every integer `k >= 2`, the model boundary `partial Omega_k`, equipped
with its Carnot--Caratheodory metric and Lebesgue measure, is a complete
doubling metric measure space supporting a global `(1,1)`-Poincare
inequality.  In particular it supports the requested `(1,4)` inequality.

The proof checks that its two horizontal fields are 1-homogeneous for the
dilations `(x,y,t) -> (sx,sy,s^(2k)t)` and satisfy Hormander's rank condition
at the origin.  The global Poincare theorem of
Biagi--Bonfiglioli--Bramanti then applies.  A flow-line argument bounds the
horizontal gradient of any control-metric Lipschitz function by the lower
pointwise slope used in the source, and Holder upgrades `(1,1)` to `(1,4)`.
Properness of the control metric supplies completeness.

The packet also disambiguates the notation in the cited geometry paper:
its quantity named `d` is comparable to the volume of a control ball, while
the length metric with lower dimension 4 and upper dimension `2k+2` is
`d_cc`.

Review files:

- `solution_packet.pdf`
- `main.tex`
- `verification.md`
- `figures/source_question_crop.png`
- `figures/global_poincare_theorem_crop.png`
- `source_paper.pdf`
- `cited_geometry_paper.pdf`
- `supporting_global_poincare_paper.pdf`
- `code/verify_geometry.py`
- `../../../../attempts/2411.02613_model_boundary_poincare.md`

