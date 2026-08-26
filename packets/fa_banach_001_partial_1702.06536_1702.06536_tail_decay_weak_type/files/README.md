# Partial Result: quantitative tail decay gives the weak endpoint in the correct orientation

- **Source:** Léonard Cadilhac, *Weak boundedness of Calderón-Zygmund operators on noncommutative L1-spaces*, arXiv:1702.06536.
- **Target:** Remark 1.4, asking whether an `alpha^(-n)` integral tail can replace pointwise kernel estimates.
- **Status:** `candidate_partial_resolution_likely_valid; input_orientation_and_two_sided_version_solved; literal_one_sided_T_endpoint_open`.
- **Model:** `GPT5.6`.

## Result

Let `T f(x)=int k(x,y)f(y)dy` be in the source's setting, with
`k(x,y) in M' cap M_tilde`, the Calderón-Zygmund size estimate, and the
assumed `L2(N) -> L2(N_tilde)` bound.

If for some `beta>0`

```text
int_{|x-y|>alpha|y-z|} ||k(x,y)-k(x,z)|| dx <= A alpha^(-beta),
```

then `T` is weak type `(1,1)`.  Thus any positive power decay suffices; the
source's `alpha^(-n)` rate is stronger than necessary in this orientation.

More generally it is enough to have tail modulus `omega(alpha)` with
`sum_j sqrt(omega(c 2^j))<infinity`.

The formula literally printed in the source varies the first/output variable.
It is the input-tail condition for the adjoint, so it proves weak type `(1,1)`
for the Hilbert adjoint.  If the tail estimate is imposed in both variables,
then both the operator and its adjoint are weak type `(1,1)`.

## Proof idea

On a remote shell of radius `R about 2^j ell(Q)`, the tail estimate gives an
`L1` bound `O(2^(-j beta))` for the kernel difference, while size gives an
`L-infinity` bound `O(R^(-n))`.  Their product is an `L2` bound.  After
multiplication by shell volume and square root, the annular term is
`O(2^(-j beta/2))`, hence summable.

This is the `L2`-Hörmander hypothesis of the later endpoint method in
arXiv:2105.05036.  Its proof extends from scalar/central kernels to the
source's `M' cap M_tilde`-valued kernels: kernel differences commute with all
Cuculescu projections and input values, and

```text
trace_tilde(|K|^2 pi f pi) <= ||K||^2 trace(pi f pi).
```

Every remaining good-, bad-, and exceptional-part estimate is unchanged.

## Scope

This settles the input-oriented and natural two-sided versions.  It does not
show that the old pseudolocalization estimate itself follows, and it does not
claim that the one-sided output-variable condition printed in the source
implies weak type `(1,1)` for `T` rather than for `T*`.

## Files

- `main.tex` — theorem, proof, orientation corollary, and literature relation.
- `solution_packet.pdf` — compiled proof packet.
- `source_paper.pdf` — official arXiv source PDF.
- `supporting_2009.03827.pdf` — later annular-L2 endpoint paper.
- `supporting_2105.05036.pdf` — later decomposition and L2-Hörmander theorem.
- `VERIFICATION.md` — mathematical and rendering audit.
