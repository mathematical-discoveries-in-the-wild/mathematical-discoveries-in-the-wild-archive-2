# Verification

Status: `candidate_full_solution_lorentz_endpoint_likely_valid; general_question_open`

## Mathematical checks

- `L^{1,q} -> L^1` for `0<q<1` follows from the dyadic rearrangement discretization and `ell^q -> ell^1`.
- The Köthe associate of `L^{1,q}` is `L^infinity`; separability and the standard bidual-closure description therefore give `(L^{1,q})^ = L^1`.
- The outer cutoff has modulus `min(1,N/|f|)`, tends to `1` in measure because its logarithm tends to zero in `L^1` and conjugation is weak `(1,1)`, and is contractive on the boundary. Order-continuous dominated convergence therefore proves bounded analytic functions are dense in every `H[Z]` covered by the lemma.
- Radial approximation of a bounded analytic function is dominated and each fixed radial dilation has uniformly convergent Taylor polynomials, completing the polynomial-density argument without assuming boundedness of the Riesz projection.
- For a real `(1,2)` atom, the local rearrangement estimate uses only the `L^2` norm of `P_+`; the far estimate uses mean-zero cancellation and the derivative bound for the conjugate kernel. Both integrals in the `L^{1,q}` quasi-norm are finite uniformly in the supporting arc.
- The finite `(1,2)` atomic characterization is applied only to the smooth real part of an analytic polynomial. Applying `P_+` yields an exact finite decomposition, avoiding convergence or completion ambiguities.
- The two inequalities are proved on analytic polynomials, which are dense on both sides; completing them gives the claimed isomorphism.
- No claim is made for an arbitrary rearrangement-invariant `Z`.

## Source and novelty checks

- The source's Question 5.8 asks exactly whether `H[Z]^ = H[Z^]` without the nontrivial-Boyd-index hypothesis.
- The source proof requires boundedness of `P` on `Z`; this fails for `L^{1,q}`, whose upper Boyd index is `1`.
- Exact-phrase, title, arXiv-id, endpoint Lorentz, and analytic-polynomial-density searches found no later resolution of Question 5.8 or statement of this endpoint theorem.
- Eight materially distinct upgrade routes are recorded in `attempts/1708.00910_lorentz_endpoint_envelope_upgrade.md`.

## Reproducibility and presentation

- The official source PDF is included.
- `main.tex` was compiled twice with `pdflatex` without errors or layout diagnostics.
- The final PDF was text-extracted, rasterized, and visually inspected page by page.
