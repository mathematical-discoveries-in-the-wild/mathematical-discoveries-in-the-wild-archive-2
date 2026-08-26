# Verification report

## Mathematical checks

- Exact SymPy verification confirms, with `U=E_12`, `V=E_23`, and
  `W=E_13`, that
  `exp(-tV) exp(-tU) exp(tV) exp(tU) = I-t^2 W` and
  `exp(t^2 W)(I-t^2 W)=I`.
- The first five-term block has additive sum `t^2 W`; the four-term block
  has additive sum zero.
- Since `W^2=0`, the first `N` four-term block products equal
  `I-H_N W`, which diverges in norm.
- For the `2 x 2` refinement, exact algebra confirms the commutator matrix,
  determinant one, trace `2+t^4`, the quadratic identity needed for its
  principal logarithm, and the positive harmonic component of `-log C(t)`.
- The sequence-to-step embedding has interval lengths `2^{-j}` and step
  values `2^j x_j`, hence its additive and exponential increments are exactly
  `x_j` and `exp(x_j)`.
- Product integrability in the positive examples is not inferred from the
  questionable converse of source Theorem 4.2.  The continuous invertible
  fundamental matrix is written down directly, and source Theorem 4.1 then
  applies.

Run the verifier with:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1410.1845_bidirectional_step_product_integrability/code/verify_commutator_blocks.py
```

## Source caveat

In the proof of the converse direction of source Theorem 4.2, the inference
`exp(x_alpha) -> I`, hence `x_alpha=log(exp(x_alpha)) -> 0`, is invalid without
eventual membership in a fixed logarithm chart.  For example,
`x_alpha=2 pi J` with `J^2=-I` has every exponential equal to `I` but does not
tend to zero.  The source's sequence formulation of the open problem is thus
not equivalent in complete generality to its step-integrability formulation.
All increments in the present construction tend to zero, and the original
step-integrability question is proved directly.

## Novelty check

On 2026-08-17 the run registry, solution, attempt, and proof-gap indexes were
searched for arXiv:1410.1845 and the core product-integrability terms.  No
duplicate was found.  Bounded web searches used the exact open-question
sentence, the paper title with `correction`/`erratum`, and combinations of
`well-ordered step mapping`, `Kurzweil product integrable`, `multipliable`,
`convergent product of exponentials`, and `divergent sum`.  They found the
source paper, a 2016 survey chapter by the same authors, and general work on
infinite matrix products, but no later answer, correction, or matching
commutator-block construction.  Novelty is therefore plausible, not certified.

## Packet QA

- Source question: arXiv PDF page 44, Section 9, first bullet.
- Source PDF and question crop are included locally.
- The final packet PDF was compiled with LaTeX and every rendered page was
  visually inspected.
- Final PDF: 3 A4 pages; no LaTeX box, reference, or layout warnings.
- SHA-256 `solution_packet.pdf`:
  `74943538fd70e041d1a256871de7b2a6026760239a441f9176b2c227e385f494`.
- SHA-256 `source_paper.pdf`:
  `e79e8aeeca19a679740c05d8b8778d531dfd8d35bf9ea5eb228c8c8b69f05dcc`.
- SHA-256 `figures/open_problem_crop.png`:
  `ac4bdee7b341f71a9d066804981bbb25bc5ecd67878fe3a65c27af964015eaa1`.
- SHA-256 `code/verify_commutator_blocks.py`:
  `76693ed1dc2042a88bcd710307b29fe71a2918ca502c535700d9be47175e14b5`.
