# Sectorial bounded holomorphic calculus under perturbation

Status: `candidate_full_proof_likely_valid`  
Source: arXiv:1101.0067, Remark 5.1  
Agent: `agent_lane_03`  
Model: `GPT5.6`

## Result

The source's perturbation theorem extends from the sectorial projection to
every fixed bounded holomorphic function on the selected sector, using the
canonical convention that the function is zero on the opposite spectral
sector.

The proof freezes the lower-order part at a base operator. Principal-symbol
variation is then governed by the Bilyj--Schrohe--Seiler bounded symbol
calculus. The actual lower-order difference occurs between two resolvents and
has integrable decay `|lambda|^(-1-min(1,1/m))`. This is the extra factor
missing from the source's direct one-resolvent approach.

## Contents

- `solution_packet.pdf`: complete theorem, proof, intuition, exact source
  screenshot, and references.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv:1101.0067 PDF.
- `source_excerpt_open_problem_page_17.pdf`: exact source question page.
- `supporting_0901.3160_hinfty_calculus.pdf`: official supporting paper.
- `supporting_excerpt_symbol_and_operator_calculus_pages_5_6.pdf`: exact
  supporting theorem pages.
- `figures/`: rendered source/support pages.
- `verification.md`: proof, provenance, build, and visual-QA record.

## Scope

The result keeps the source's fixed contour, minimal-growth assumptions, and
topology. It treats a fixed bounded holomorphic function on a uniform
neighborhood of the selected closed sector; it does not claim joint
continuity under arbitrary variation of the function or its domain.
