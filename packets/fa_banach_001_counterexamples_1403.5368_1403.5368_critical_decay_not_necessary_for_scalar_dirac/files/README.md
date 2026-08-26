# Critical decay is not necessary for the scalar Dirac operator

Result type: `counterexample` / endpoint theorem

Status: candidate full negative answer to the necessity question in Remark 3.8,
pending expert review.

Source paper:

- Sebastian Stahlhut, “L^p-L^q theory for holomorphic functions of perturbed
  first order Dirac operators,” arXiv:1403.5368.
- Open-question location: Remark 3.8, source PDF page 12.
- `source_paper.pdf` is a local reconstruction compiled twice from the cached
  arXiv TeX source because network download was unavailable.
- `figures/open_problem_crop.png` is the exact source crop.

## Claimed contribution

The strict condition `tau > n/p-n/q` in Proposition 3.3 is not necessary in
general. For `D=-i d/dx` on the line and `B=I`, write
`delta=1/p-1/q`. At the critical exponent `tau=delta`, the full family

`{g(D) psi(tD): t>0}`

satisfies `L^p-L^q` off-diagonal estimates for every order
`0 <= K <= sigma+delta`, uniformly for every
`psi in Psi_sigma^delta` and every bounded holomorphic `g`.

The proof obtains a uniform normalized kernel bound

`|k_t(x)| <= C min(|x|^(delta-1), |x|^(-1-sigma))`.

Hardy--Littlewood--Sobolev gives the global critical mapping, while Young's
inequality on the truncated far tail gives the off-diagonal order.

The explicit symbol

`psi_0(z)=w(z)^sigma/(1+w(z))^(sigma+delta)`,
`w(z)=sgn(Re z)z`,

has exact decay `|z|^-delta`, so the endpoint is not inherited from a
faster-decaying symbol class.

## Files

- `main.tex`: self-contained theorem and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source reconstruction from cached arXiv TeX.
- `figures/open_problem_crop.png`: full-width crop of Remark 3.8.
- `verification.md`: proof audit, novelty scope, and review focus.
- `tmp/`: LaTeX intermediates and rendered visual-QA pages.

## Scope and novelty

This is a full negative answer to necessity in general and is stronger than a
single-symbol counterexample: it proves the endpoint uniformly over all
admissible `psi` and `g` in the unperturbed scalar model. It does not establish
a universal endpoint theorem for all rough perturbations `DB` or `BD`.

The run registry and bounded primary-source searches through August 11, 2026
found no later claimed solution. Novelty confidence is moderate pending
specialist citation review; priority is not asserted.
