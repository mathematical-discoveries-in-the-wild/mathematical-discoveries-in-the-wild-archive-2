# Verification report

Status: `candidate_substantial_partial_likely_valid_pending_human_review`

## Mathematical audit

- Confirmed the exact source target as Question 5.4 on PDF page 17.
- Checked the Hardy duality orientation both bilinearly and sesquilinearly;
  only `g` versus `conjugate(g)` changes on the contact set, and both are
  unimodular.
- Checked the bounded-orbit identity
  `x(f)=(T^n x)(h^n f)` and the dominated-convergence limit onto
  `A={|h|=1}`.
- Checked injectivity and dense range of the restriction `H^q -> L^q(A)` by
  Hardy boundary uniqueness and the annihilator argument.
- Checked the normalized Poisson-kernel peak calculation giving
  `nu(I) <= C |I|^(s/r)`.
- Checked both Wold components separately. The shift part uses orthogonality;
  the unitary part uses atomlessness forced by the absence of eigenvectors.
- Checked that the `L^2(mu) -> L^p(nu)` inequality first implies
  `nu << mu`, then extends to indicators, before the equal-mass partition is
  used.
- No computational lemma or unproved numerical claim enters the result.

## Scope audit

- The packet explicitly states that Question 5.4 remains open.
- The promoted theorem rules out all isometric Hilbert cores satisfying the
  source criterion, including unitary and unilateral-shift Wold parts.
- It does not claim that every weakly hypercyclic construction must arise from
  such a core.
- Eight distinct upgrade attempts and the final obstruction are recorded in
  the attempt log.

## Artifact audit

- `source_paper.pdf` downloaded from the arXiv PDF endpoint.
- `figures/open_question_crop.png` rendered from source PDF page 17 at 180 dpi
  and visually checked.
- `main.tex` compiled with all intermediates confined to `tmp/`.
- Final packet: 5 pages, 404282 bytes.
- Final LaTeX log: no warnings, overfull/underfull boxes, undefined
  references, or multiply defined labels.
- All five final rendered pages were inspected at original image detail; no
  clipping, overlap, illegible formula, or stray build artifact was found.
- SHA-256:
  - `solution_packet.pdf`:
    `00f90601ed85df558edcec2f4e00edabbeeb6f8b886e89c0cee46ddf35548957`
  - `source_paper.pdf`:
    `e9f5b8b345cb11f024b59853e4dbe173a53854316d355cee52c500841ae1039a`
  - `figures/open_question_crop.png`:
    `a8b270e01c693a334ce953a3abbe5254d559436c8cc1d1e49884da6b7c09e3c0`
  - `main.tex`:
    `1220ad7baa272cc5528370f9327b2f4dea56a16cff6d6f744ddb439cbd76dfcb`

