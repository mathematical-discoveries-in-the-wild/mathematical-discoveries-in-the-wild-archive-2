# Exact fixed-chaos slice of the L2 Haar-multishift commutant

Status: candidate partial result, likely valid. The unrestricted commutant
problem remains open.

## Source question

ArXiv:2005.04648 states that a comprehensive description of the commutant
of the Haar multishift is open even in `L2`. It proves an exact scalar
`H-infinity` criterion when the generator is a first-order Haar chaos.

## Result

For every fixed chaos order `d >= 1`, this packet gives an exact criterion
and exact operator norm. If

`hat f(z1,...,zd) = sum xi_(k1,...,kd) z1^k1 ... zd^kd`

is the source's multivariable symbol and `R=2^(-1/2)`, then

`||T_f|| = 2^(-(d-1)/2) sup_(|z1|<R)
            ||hat f(z1,.)||_(H2(D_R^(d-1))).`

Consequently `T_f` is bounded on mean-zero `L2` exactly when the mixed
`H-infinity_(z1)(H2_(z2,...,zd))` norm is finite. For `d=1` this is precisely
the scalar theorem in the source.

The proof identifies the normalized Haar multishift with the two-letter
Fock left shift. Words in one fixed chaos split into an initial zero run and
a suffix from a suffix-free code. Their right-creation ranges are
orthogonal, reducing the operator to a vector-valued Hardy multiplier.

## Limitation

Suffix families from different chaos orders are nested, so their ranges
are no longer orthogonal. The formula therefore does not describe the full
unrestricted commutant. A pure chaos of order `d > 1` also cannot generate
an equivalent Haar basis because its multiplier is not onto.

## Files

- `solution_packet.pdf`: self-contained theorem, proof, scope, and review notes.
- `main.tex`: editable source.
- `verification.md`: proof and computation audit.
- `code/fixed_chaos_probe.py`: finite-word numerical check.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: source open-problem excerpt.

Human review should focus on word orientation in the right-multiplier
identity, the suffix-free argument, and the factor `2^(-(d-1)/2)`.
