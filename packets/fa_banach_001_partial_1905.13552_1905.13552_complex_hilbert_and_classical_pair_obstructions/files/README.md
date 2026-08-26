# Complex Hilbert and classical-pair obstructions for `L_{o,p}`

Status: `partial_result_likely_valid`

Source: Sheldon Dantas, Sun Kwang Kim, Han Ju Lee, and Martin Mazzitelli,
“On some local Bishop–Phelps–Bollobás properties,” arXiv:1905.13552,
published in *The Mathematical Legacy of Victor Lomonosov* (2020),
pp. 109–122.

Question 3 asks whether there are Banach spaces `X,Y`, both of dimension at
least two, for which the local operatorwise property `L_{o,p}` holds.  A
pre-existing theorem cited by the source rules out every pair of **real**
spaces, but its proof is explicitly real two-dimensional.  The complex case
is therefore the substantive unresolved part.

This packet proves two new complex negative subcases:

1. `(H,Y)` fails `L_{o,p}` for every complex Hilbert space `H` with
   `dim(H)>=2` and every complex Banach space `Y` with `dim(Y)>=2`.
2. `(ell_p^2,ell_q^2)` fails `L_{o,p}` over the complex field for every
   `1<=p,q<=infinity`.

The Hilbert-domain proof inserts the John ellipsoid of a two-dimensional
subspace of `Y`.  Two independent contact directions exist by the John
contact theorem.  A diagonal contraction fixes one contact direction and
slightly shrinks its orthogonal complement; at the other contact direction
the resulting norm-one operators almost attain their norms, while every
exact norming point lies on the fixed, separated line.

For the classical pairs, a diagonal construction handles `p<=q`.  When
`p>q`, the identity embedding has a whole torus of maximizers.  The symmetric
perturbation

`A_t(z_1,z_2)=(z_1+t z_2,t z_1+z_2)`

selects the equal-phase orbit, while the fixed opposite-phase vector remains
an almost maximizer after normalization.  A compactness and first-variation
argument proves that all exact maximizers converge to the equal-phase orbit.

The full complex question remains open.  The strongest attempted universal
upgrade reduces to finding, for arbitrary complex two-dimensional `X,Y`, a
contractive isomorphism with two suitably separated contact directions.
John's theorem supplies this when the domain is Hilbert, but no valid
analogue was obtained for a general domain; a maximal-determinant map can
have nonsmooth contact faces, and the proposed perturbation could not be
shown contractive.

Files:

- `solution_packet.pdf`: review document.
- `source_paper.pdf`: source paper.
- `figures/open_question_crop.png`: readable source page containing Question 3.
- `verification_report.md`: proof, literature, and artifact audit.

Human-review recommendation: check the use of the real John contact theorem
to obtain two complex-independent contacts, and check the uniform
first-variation passage in the `p>q` proof, especially the endpoint cases
`p=infinity` and `q=1`.
