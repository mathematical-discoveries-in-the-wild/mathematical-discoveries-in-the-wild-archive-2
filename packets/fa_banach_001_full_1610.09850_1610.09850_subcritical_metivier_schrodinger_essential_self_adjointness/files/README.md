# Essential self-adjointness in the full subcritical Métivier range

Status: candidate full affirmative answer, likely valid, awaiting specialist
review.

Bruno and Calzi ask in Remark 4.8 of arXiv:1610.09850 whether
`(L+V_alpha,C_c^infinity)` is essentially self-adjoint when
`0 < alpha < 2`.  This packet proves that it is.

The source lower bound implies that the negative part of `V_alpha` is
compactly supported and bounded by `C N^(alpha-2)`.  Since the homogeneous
dimension is `Q >= 4`, one can choose

`Q/2 < p < Q/(2-alpha)`.

Thus `(V_alpha)_-` lies in `L^p`.  Heat-kernel scaling gives the strict
resolvent contraction

`||(V_alpha)_- (L+lambda)^(-1)||_(2->2)
 = O(lambda^(-1+Q/(2p))) = o(1)`.

Kato's inequality then forces every large negative-energy deficiency vector
to vanish.  The proof also verifies the nonsmooth unitary conjugation at the
identity, so the source weighted form operator is unitarily equivalent to the
closure of the Schrödinger operator throughout the open range.

Contents:

- `main.tex` and `solution_packet.pdf`: theorem, full proof, and source
  application.
- `source_paper.pdf`: arXiv:1610.09850.
- `figures/open_problem_crop.png`: Corollary 4.7 and the complete Remark 4.8
  from source PDF page 12.
- `code/verify_exponent_window.py`: independent arithmetic checks of the
  exponent window and decay powers.
- `code/crop_source_statement.py`: reproducible source crop.
- `VERIFICATION.md`: mathematical, novelty, source, and PDF QA record.

The main abstract lemma applies more generally to real
`V in L^2_loc` on a stratified group whenever `V_- in L^p` for some
`p>Q/2`.
