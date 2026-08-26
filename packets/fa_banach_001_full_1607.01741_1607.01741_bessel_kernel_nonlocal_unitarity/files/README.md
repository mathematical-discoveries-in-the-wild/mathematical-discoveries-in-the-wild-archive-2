# arXiv:1607.01741 — Bessel-kernel proof of restriction nonunitarity

Status: `candidate_full_solution`, pending expert review.

Source: David P. Hewett and Andrea Moiola, *A note on properties of the
restriction operator on Sobolev spaces*, arXiv:1607.01741, Remark 2.13 on
printed page 6.

## Result

For every nonempty open `Omega⊂R^n` whose complement has nonempty interior,

`restriction: Htilde^s(Omega) -> H_0^s(Omega)`

is a unitary isomorphism if and only if `s` is a nonnegative integer. This
proves the conjecture in Remark 2.13, extending the source's bounded-domain
Proposition 2.12 to every domain in the conjectured class.

The key observation is that the off-diagonal kernel of `(1-Delta)^s` equals
a nonzero Gamma factor times a strictly positive heat-kernel integral for
every noninteger `s`. Nonnegative test functions supported in `Omega` and in
the interior of its complement therefore have nonzero `H^s` inner product,
so the orthogonality criterion for unitarity fails.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: self-contained packet source.
- `source_paper.pdf`: official arXiv source paper.
- `figures/open_problem_crop.png`: Proposition 2.12 and Remark 2.13.
- `verification.md`: mathematical and novelty audit.

Associated attempt:
`attempts/1607.01741_bessel_kernel_nonlocal_unitarity_full.md`.
