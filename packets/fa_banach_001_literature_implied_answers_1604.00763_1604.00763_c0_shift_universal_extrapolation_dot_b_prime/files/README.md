# The universal extrapolation space of the shift on C0(R)

Status: `literature_implied_answer` (full resolution of the stated
conjecture; the identification with the later theorem is supplied here).

## Source question

Christian Bargetz and Sven-Ake Wegner, *Pivot duality of universal
interpolation and extrapolation spaces*, arXiv:1604.00763, Section 4,
PDF page 8, conjecture that the universal extrapolation space of the shift
semigroup on `C_0(R)` is the space `dot B'(R)` of distributions vanishing at
infinity.

## Supporting result

Christian Bargetz, Eduard A. Nigsch, and Norbert Ortner, *A simpler
description of the kappa-topologies on the spaces D_{L^p}, L^p, M^1*,
arXiv:1711.06577, PDF page 6, prove the topological identity

`dot B'(R) = ind_m (1-d^2/dx^2)^m C_0(R)`.

For the standard invertible shift of the generator, `A=1-d/dx`, the
extrapolation steps are `A^n C_0(R)`.  The two Banach-step systems are
cofinal: `A^n C_0` embeds continuously into
`(1-d^2/dx^2)^n C_0`, and the latter's `m`-th step embeds continuously into
`A^{2m}C_0`.  Hence their locally convex inductive limits coincide.  The
supporting paper's limit is `dot B'` and is complete, so the completion in the
definition of the universal extrapolation space adds nothing.

The supporting authors cite the source paper, but do not state that this
topological representation resolves its final conjecture.  The implication
is therefore classified as literature-implied rather than an explicitly
announced literature answer.

See `solution_packet.pdf` for the complete cofinality argument and bounded
literature check.

Ledger: `ledger/results/1604.00763_c0_shift_universal_extrapolation_dot_b_prime.json`.
