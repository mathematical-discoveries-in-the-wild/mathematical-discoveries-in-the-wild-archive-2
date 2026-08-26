# Verification record

Status: `candidate_full_solution_likely_valid`

## Source verification

- Official arXiv PDF for 2510.12424 downloaded and stored as
  `source_paper.pdf` (92 pages).
- Remark 5.13 was located on PDF page 59 and compared with source TeX label
  `rmk:m_inf_B_q_diff`.
- The screenshot in `figures/open_problem_crop.png` is a direct 200-dpi render
  and crop of that official PDF.  It was inspected at original resolution.
- Official arXiv PDF for 2503.18157 was stored as
  `supporting_paper_2503.18157.pdf` (27 pages).
- The decisive supporting statements were checked in its source and PDF:
  Theorem 1.4 (exact local-current mass superposition, injective curves and
  exact boundary variation in the acyclic case) and Remark 4.19 (finite
  endpoints plus transport to/from infinity).

## Mathematical audit

Eight focused upgrade attempts are recorded in
`attempts/2510.12424_local_plan_duality/upgrade_attempts.md`.

The final proof was audited in the following order:

1. The compact-plan `B_q^*` route was confirmed to prove only `D_q <= B_q^*`.
2. Direct cutoff plans were rejected because of the shell divergence term
   `b(chi_R)m` and loss of boundary at infinity.
3. The local derivation-to-current map was checked against the source's sign
   convention: `partial t_loc(b)=-div(b)`.
4. Exact local mass was reduced by bounded cutoffs to Theorem 4.21 of the
   source; local surjectivity was checked by the same cutoff/gluing argument.
5. The pointwise mass identities were checked to identify subderivations with
   subcurrents and hence preserve acyclicity.
6. Theorem 5.9 of the source was checked to give an acyclic minimizer for every
   finite `D_q(mu)`, including `q=infinity`.
7. The local superposition theorem was checked to give exact mass and boundary
   variation for that acyclic current; injectivity converts curve-current mass
   to arclength occupation.
8. The converse local-plan-to-current construction was checked using local
   arclength and endpoint-boundary integrability, yielding `|b_eta|<=Bar(eta)`.
9. Endpoint signs were checked: finite starts give `mu^+`, finite ends give
   `mu^-`, and a ray starting at zero has boundary `-delta_0`.
10. The finite-reference-measure compatibility statement was restricted to
    finite `mu`, exactly the scope of Proposition 5.12.

No unproved lemma or computational dependency remains in the packet.  The main
expert-review focus is the localized isometric correspondence (Lemma 2), in
particular the inverse cutoff/gluing construction.

## Computational sanity checks

`code/verify_examples.py` ran successfully under the `sandbox` environment and
checked, with exact rational arithmetic:

- for the disjoint-interval example through `n=1000`, the squared `L^2`
  barycenter norm is `sum 1/n^2 < 2`, while the partial `L^1` norm is `1000`;
- an oriented ray from zero to infinity has current boundary `-delta_0`, hence
  derivation divergence `+delta_0`.

Both Python files compile with `python -m py_compile`.  These checks are
sanity tests only and are not used as proof.

## Build and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully.
- Final packet: six pages, 262706 bytes.
- The final log has no warnings, undefined references, overfull boxes, or
  underfull boxes.
- Ghostscript text extraction contains the theorem, both cost equalities,
  review caveat, and references.
- All six pages were rendered to PNG and visually inspected.  The final first
  page was rerendered after the crop refinement and inspected separately.

## Bounded novelty check

Searches on 13 August 2026 used:

- arXiv ids `2510.12424` and `2503.18157`;
- both exact titles and all author names;
- the exact phrase about plans on locally rectifiable curves;
- `local dynamic cost`, `local plan`, `divergence measure`, `barycenter Lq`,
  and close combinations;
- arXiv, CVGMT, author publication pages, the published Nonlinear Analysis
  page, and fresh general web indexes.

No separate completion of Remark 5.13 was found.  The journal page for the
local-superposition paper reported zero citing papers.  Novelty confidence is
moderate rather than high because Remark 5.13 itself explicitly identifies the
decisive supporting theorem and describes the missing work as details.

## SHA-256

- `solution_packet.pdf`:
  `fb06b172df094a83af503e88b0f60640fe6d360466da647b74a07643fbbbbb3a`
- `source_paper.pdf`:
  `5a299108be7d6f2f0c4849cd3db063b3670b4cf0086c5acfb40f10041ac18c6d`
- `supporting_paper_2503.18157.pdf`:
  `49ff8e94323792e2379950b39c6a0008572c4bbf9f206fc230ef9e7ef340e264`
- `figures/open_problem_crop.png`:
  `8eeecde314a715dcfbeef1ccd002f678b21005561ce6ffef1f13951fb7271020`
- `code/verify_examples.py`:
  `fe47c35c02bbaf59ca4a9d38aa48eff28be8b42da3a09a54932328e6e1e2c010`
- `code/make_open_problem_crop.py`:
  `2d829c715e1fbf9616907716f9c02f3e5d305834cfef73ff1523ee75034b72ff`
- `main.tex`:
  `fd7c7d7f73159c553b896d2baab84b7da23e2a1eb0146c3f5786f4442b7ff794`
