# Counterexample packet: positive powers already recover the constant in finite Lp

Status: `candidate_counterexample_likely_valid`.

## Source conjecture

Philippe Jaming and Ilona Simon, *Density of the span of powers of a function
à la Müntz-Szász*, arXiv:1606.09092, Conjecture 1 (Conjecture 4.6 in the
published numbering), asserts for every `p in [1,infinity]` that totality of two
irrationally shifted cosine-power systems forces both exponent sets to be
`[-1,1]`-Müntz-Szász sequences. Their definition requires `0` to belong to such
an exponent set.

## Counterexample

Fix any `1 <= p < infinity`, take irrational `theta_1-theta_2`, and set both
exponent sets equal to the positive integers `{1,2,...}`.

At each center,

`1-(1-cos^2(2*pi*(t-theta)))^N`

is a linear combination of positive even cosine powers and converges to `1` in
`L^p`. Consequently the positive powers have the same closed span as all
nonnegative powers: the full subspace of functions even under reflection about
that center. The sum of the even subspaces for two irrationally separated
centers is dense; a common annihilator would be odd about both centers, and its
Fourier coefficients vanish because the two reflection phases are distinct at
every nonzero frequency.

Thus the union is total although neither exponent set is a `[-1,1]`-Müntz-Szász
sequence under the paper's definition, since neither contains zero.

## Scope

This is a full negative answer to the conjecture exactly as quantified and
defined in the source. It identifies a finite-`p` normalization issue rather
than resolving the intended arithmetic core. The counterexample does not work
in `C([0,1])`, where uniform approximation preserves the values at the zeros of
the cosine. The corrected conjecture obtained by requiring `0` in both exponent
sets remains open here.

## Files

- `solution_packet.pdf`: self-contained counterexample and proof.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: target arXiv PDF.
- `tmp/`: compilation and visual-QA intermediates.

