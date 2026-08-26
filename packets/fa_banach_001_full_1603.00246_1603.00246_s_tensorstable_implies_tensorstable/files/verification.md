# Verification report

Status: candidate full proof; likely valid; human review required.

## Exact target

The final open question on source PDF page 27 (printed page 26) asks whether
every s-tensorstable operator ideal is tensorstable. Definitions 7.7 and 7.11
make clear that the ambient object is a p-normed operator ideal, `0<p<=1`.
The theorem in the packet proves exactly this implication, over the real or
complex scalars, and gives explicit tensorstability constants.

## Block-diagonal ideal operator

For nonzero `u in I(E;F)` and `v in I(G;H)`, let `a=||u||_I` and
`b=||v||_I`. On finite `ell_1` sums define

    W = i_F (u/a) p_E + i_H (v/b) p_G.

All coordinate maps have norm one. The ideal property puts each summand in
`I` with ideal norm at most one. Hence the p-triangle inequality gives

    ||W||_I^p <= 2,  so  ||W||_I^2 <= 2^(2/p).

No direct-sum stability hypothesis on the ideal is being assumed; this is
only linearity, the ideal property, and the p-triangle inequality.

## Mixed-block embedding

Write `z vee z'` for the averaged symmetric product

    (z tensor z' + z' tensor z)/2.

The map

    J(x tensor g) = i_E(x) vee i_G(g)

is the restriction of the linearization of the standard symmetrization map
used in Proposition 7.12 of the source. Its norm is at most the second
polarization constant, hence at most `2`. Equivalently, the elementary
identity

    z vee z' = ((z+z')^2-(z-z')^2)/4

followed by scalar balancing proves
`pi_s(z vee z') <= 2||z||||z'||`. The universal property of the ordinary
projective tensor product then gives a bounded map on the completion.

This check avoids the incorrect shortcut of assuming that the symmetric
projective norm is simply the restriction of the full projective norm.

## Mixed-block extraction

The source uses the canonical norm-one inclusion

    iota_Y^2 : tensorhat_{pi_s}^{2,s} Y -> Y tensorhat_pi Y.

With `q_F,q_H` the coordinate projections from `Y=F directsum_1 H`, set

    Q = 2(q_F tensor q_H)iota_Y^2.

Then `||Q||<=2`. Under the averaged convention,

    iota_Y^2(i_F f vee i_H h)
      = (i_F f tensor i_H h + i_H h tensor i_F f)/2.

The first coordinate tensor projection kills the second summand and returns
half of `f tensor h`; the prefactor `2` therefore gives exactly
`Q(i_F f vee i_H h)=f tensor h`.

## Intertwining identity

The defining identity for the symmetric square is initially given on pure
squares. Polarizing it yields

    (tensor^{2,s} W)(z vee z') = Wz vee Wz'.

On `x tensor g`, the two diagonal blocks of `W` therefore give

    Q (tensor^{2,s} W) J(x tensor g)
      = (u(x)/a) tensor (v(g)/b).

Elementary tensors are dense, so the identity holds on the completed
projective tensor product.

## Ideal estimate and iteration

Symmetric-square stability and the ideal property give

    ||(u/a) tensor (v/b)||_I
      <= ||Q|| C_2 ||W||_I^2 ||J||
      <= 4 C_2 2^(2/p).

Thus

    ||u tensor v||_I <= 2^(2+2/p) C_2 ||u||_I ||v||_I.

Zero factors are trivial. Applying the same two-operator estimate repeatedly
and using the canonical isometric associativity of projective tensor products
gives the n-fold constant `K^(n-1)`. This is precisely tensorstability as in
Definition 7.11.

## Scalar field and completions

The algebraic symmetrization formula and all coordinate maps work over both
the real and complex fields. Scalar balancing uses positive real scalars,
which are available in either field. Every algebraic identity is extended to
the indicated completed tensor products by boundedness and density.

## Novelty bounds

On 11 August 2026, the four lightweight run indexes and the local downloaded
arXiv source corpus were searched by arXiv id and by the exact terms
`s-tensorstable`, `symmetrically tensorstable`, and the verbatim open
question. The exact terminology occurred only in arXiv:1603.00246 in the
local corpus.

External searches used the same exact phrases, the source title and authors,
and the DOI. OpenAlex metadata listed nine works citing the journal article;
their titles and available abstracts/records did not identify an answer. The
most directly relevant open citing document, a 2020 dissertation on
associativity of projective and injective tensor products, was downloaded and
text-searched and contained none of the exact terminology. No explicit later
answer or mixed-block proof was found. This is a bounded search, not an
exhaustive novelty guarantee.

No computation is part of the mathematical proof.
