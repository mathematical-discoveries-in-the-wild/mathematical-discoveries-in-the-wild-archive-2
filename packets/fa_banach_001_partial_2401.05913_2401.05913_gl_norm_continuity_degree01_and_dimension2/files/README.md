# Norm continuity of the GL action in low degree and dimension two

Status: `substantial_partial`, likely valid, pending human review.

Remark 4.3 of arXiv:2401.05913 asks whether the natural `GL(n,R)` action on
tau-continuous, dually translation invariant valuations on
`Lip(S^{n-1})` is continuous for the Banach norm

`||mu|| = sup_{||f||_Lip<=1}|mu(f)|`.

This packet proves:

- an affirmative answer on the complete degree-zero and degree-one summands
  for every `n>=2`;
- an affirmative answer on the entire valuation space when `n=2`;
- norm continuity for every degree-two valuation having the source's integral
  formula with an `L^1` matrix density, and for the norm closure of this class.

The degree-one mechanism is rigid: restriction to support functions and
McMullen's degree-one theorem force every such valuation to be integration
against a finite measure with zero first moment.  Small linear changes act
uniformly on the Lipschitz unit ball in the sup norm.  In dimension two, the
only remaining degree-two component is the one-dimensional area extension,
which transforms by `|det g|^{-1}`.

For `n>=3`, the only unresolved part is the nonsmooth degree-two summand.  Six
focused attempts are recorded in
`runs/fa_banach_001/attempts/2401.05913_gl_norm_continuity_low_degree_upgrade.md`.
Compact-open density of smooth valuations does not imply density for the
norm in the question, while the obvious singular-coefficient counterexamples
fail tau continuity.

Contents:

- `main.tex` / `solution_packet.pdf`: theorem, proof, integral extension,
  limitations, and novelty audit.
- `source_paper.pdf`: Colesanti--Knoerr--Pagnini, arXiv:2401.05913.
- `figures/source_question.png`: exact Remark 4.3 question from PDF page 18.
- `verification_report.md`: mathematical and rendered-PDF checks.

Ledger:
`runs/fa_banach_001/ledger/results/2401.05913_gl_norm_continuity_degree01_and_dimension2.json`.

