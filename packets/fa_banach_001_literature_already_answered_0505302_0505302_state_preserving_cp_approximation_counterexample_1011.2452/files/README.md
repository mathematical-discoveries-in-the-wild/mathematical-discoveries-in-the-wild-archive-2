# State-preserving approximation question in arXiv:0505302 answered negatively

Status: `literature_already_answered`

This is a literature-status record, not a new counterexample proved by this
run.

## Source question

Eric Ricard and Quanhua Xu, *Khintchine type inequalities for reduced free
products and applications*, arXiv:math/0505302; *Journal fur die reine und
angewandte Mathematik* 599 (2006), 27--59.

In the CCAP application section the authors say that they do not know whether
every nuclear unital C*-algebra with a given state admits a net of finite-rank,
unital completely positive maps which preserve that state and converge
pointwise to the identity.

## Explicit later counterexample

Caleb Eckhardt, *Free products and the lack of state-preserving approximations
of nuclear C*-algebras*, arXiv:1011.2452; *Proceedings of the American
Mathematical Society* 141 (2013), 2719--2727,
doi:10.1090/S0002-9939-2013-11702-8.

The abstract explicitly says that the paper answers a question of Ricard and
Xu.  It constructs a faithful state on the nuclear unital algebra
`M_2 tensor C[0,1]` which is not CP-approximable.  More precisely, choose a
measurable set `X` such that both `X` and its complement have positive measure
in every nonempty open interval and put

`phi((f_ij)) = integral_X f_11 dm + integral_(X^c) f_22 dm`.

Proposition 2.3 proves that every finite-rank, phi-preserving UCP map in the
corner-preserving form forced by the preceding reduction has zero
off-diagonal component.  Such maps cannot converge pointwise to the identity
on the off-diagonal matrix corner.  Hence `phi` is not CP-approximable.

## Scope

This completely answers the source's auxiliary state-preserving approximation
question in the negative.  It does not decide whether CCAP itself is preserved
by arbitrary reduced free products; Eckhardt explicitly records that broader
problem as still open and asks specifically about the reduced free square of
this counterexample pair.

## Files

- `source_paper.pdf`: arXiv:math/0505302.
- `supporting_paper_1011.2452.pdf`: the answering paper.
- `main.tex`, `solution_packet.pdf`: compact literature-status note.

Ledger:
`runs/fa_banach_001/ledger/results/0505302_state_preserving_cp_approximation_counterexample_1011.2452.json`.
