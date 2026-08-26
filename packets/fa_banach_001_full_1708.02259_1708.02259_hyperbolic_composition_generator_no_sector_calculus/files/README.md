# Hyperbolic Composition Generator: No Proper-Sector Calculus

Status: `candidate_full_solution_likely_valid`

Source: Eva A. Gallardo-Gutiérrez and Dmitry V. Yakubovich, *On
generators of C0-semigroups of composition operators*, arXiv:1708.02259,
Section 3, displayed Question (source PDF p. 7).

## Claimed contribution

For every positive weight sequence `beta` for which the source's weighted
Hardy-space hypotheses hold and

`T(t) = C_{alpha_{tanh t}}`

is a C0-semigroup, its generator `A=(1-z^2)d/dz` is unbounded and admits no
bounded H-infinity calculus on any shifted sector of angle `< pi/2`.

This resolves both readings of the source's grammatically ambiguous question:

- literally, no weights can make the generator bounded;
- if “bounded” was intended to describe the composition semigroup, then
  every admissible weight sequence has the requested proper-sector failure
  (and `beta_n=1` is already an example).

The result concerns the fixed hyperbolic automorphism flow. It does not
classify arbitrary noninvertible composition semiflows.

## Proof mechanism

On normalized monomials `e_n=z^n/beta_n`, the forward coefficient of `Ae_n`
and the backward coefficient of `Ae_(n+1)` multiply to `n(n+1)`. One of the
two generator norms is therefore at least `sqrt(n(n+1))`, independently of
the weights.

Reflection `z -> -z` conjugates positive-time hyperbolic composition
operators to the negative-time operators, so the semigroup extends to a C0
group. A proper-sector H-infinity calculus would make it analytic. An
analytic C0 group has bounded generator, contradicting the monomial bound.

## Packet contents

- `solution_packet.pdf`: complete proof and review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/source_question_crop.png`: rendered source question.
- `code/verify_hyperbolic_generator.py`: algebraic/numerical sanity checks.
- `code/verification_output.txt`: saved PASS output.
- `VERIFIER_REPORT.md`: adversarial step-by-step review.
- `main.tex`: packet source; build intermediates and rendered pages are under
  `tmp/`.

## Reproduce the verification

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1708.02259_hyperbolic_composition_generator_no_sector_calculus/code/verify_hyperbolic_generator.py \
  --suite
```

## Human-review focus

Check the interpretation of “bounded” in the displayed source wording and
the standard implication from a bounded H-infinity calculus on a sector of
angle below `pi/2` to analyticity of the generated semigroup. The bounded
novelty search found no later explicit answer; novelty remains plausible
rather than certified.
