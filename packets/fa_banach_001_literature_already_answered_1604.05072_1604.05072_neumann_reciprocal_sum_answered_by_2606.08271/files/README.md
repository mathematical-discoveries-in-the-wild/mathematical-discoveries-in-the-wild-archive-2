# Reciprocal-sum Neumann inequality: exact literature answer

Status: `literature_already_answered`.

The source survey arXiv:1604.05072 asks whether the normalized sum of the
reciprocals of the first `N` nonzero Neumann eigenvalues is minimized by a
ball in every dimension. He, Li, and Tang prove exactly this
Ashbaugh--Benguria conjecture in arXiv:2606.08271, with equality only for
balls. Li and Wang, arXiv:2607.19008, state the same theorem for bounded
Lipschitz domains and prove quantitative stability.

The source numbers the zero eigenvalue as `mu_1`, whereas both later papers
number it as `mu_0`; the packet writes out the one-step index shift and the
scale normalization explicitly.

Files:

- `solution_packet.pdf`: final status packet.
- `main.tex`: packet source.
- `source_1604.05072.pdf` and `.tex`: source survey.
- `supporting_2606.08271.pdf` and `.tex`: exact proof by He--Li--Tang.
- `supporting_2607.19008.pdf` and `.tex`: Lipschitz-domain formulation and
  stability refinement by Li--Wang.
- `VERIFICATION.md`: claim-to-source audit and build checks.

Scope: this packet does not resolve the survey's separate Steklov question
about the sharp topology-free bound for `P(Omega) sigma_2(Omega)`.
