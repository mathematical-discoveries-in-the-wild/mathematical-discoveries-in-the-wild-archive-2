# Verification report

Status: candidate counterexample; likely valid; human review required.

## Exact target and scope

On source PDF page 4 the authors say that Theorem 6 is a partial result
related to whether the Kruglov property of an r.i. space `E` is necessary for
an isomorphic embedding `T:U_E -> E`. The source defines `Y subsetsim X` to
mean the existence of an arbitrary isomorphic Banach-space embedding. The
quoted statement does not require `E` to be separable/order continuous and
does not require `T` to preserve the canonical basis, disjointness, or
independence.

The packet addresses exactly this literal unrestricted formulation. It does
not claim to settle any strengthened formulation with one of those extra
hypotheses.

## Separability of `U_E`

The source defines `U_E` as the closed linear span in `Z_E` of the sequence
`(chi_{A_n})_{n>=1}`. Finite rational linear combinations of a countable
dense scalar set and finitely many basis vectors form a countable dense
subset. Thus `U_E` is separable for every `E`, including
`E=L^infinity[0,1]`.

No separability of the ambient r.i. space is needed.

## Every separable Banach space embeds in `ell_infinity`

For a separable Banach space `X`, choose a dense sequence `(x_n)` in the unit
sphere and norm-one functionals `(x_n^*)` with `x_n^*(x_n)=1`. The map

    Jx=(x_n^*(x))_n

is linear and contractive. If `||x||=1` and `x_n` approximates `x`, then

    |x_n^*(x)| >= 1-||x-x_n||.

Taking arbitrarily good approximants gives `||Jx||_infinity=1`. Homogeneity
proves that `J` is a linear isometry. The complex case is identical after
choosing the Hahn--Banach functionals with the indicated phase.

## `ell_infinity` embeds in `L^infinity[0,1]`

Let `(B_n)` be a measurable partition of `[0,1]` with every `m(B_n)>0`, and
define

    S(a)=sum_n a_n chi_{B_n}.

This is a well-defined essentially bounded function and

    ||S(a)||_infinity = sup_n |a_n|,

because every coordinate value occurs on a positive-measure set. Thus `S` is
a linear isometry. Applying `S J` with `X=U_{L^infinity}` establishes the
required embedding into the same r.i. space `E=L^infinity[0,1]`.

## Failure of the Kruglov property

The source defines `pi(f)=sum_{i=1}^N f_i`, where the `f_i` are independent
copies of `f` and `N` is an independent Poisson random variable with
parameter one. For `f=1`, every copy equals one, so `pi(f)=N`.

For every integer `m>=0`,

    P(N=m)=exp(-1)/m! > 0.

Hence `N` is not essentially bounded. Therefore `1 in L^infinity` but
`pi(1) notin L^infinity`, so `L^infinity` lacks the Kruglov property. It does
have the Fatou property, so adding that common regularity assumption does not
remove the counterexample.

## Compatibility with the source's partial theorem

The universal embedding constructed above need not send canonical block
vectors to independent symmetrically distributed random variables and need
not satisfy the lower-tail condition in Theorem 6. Hence the counterexample
does not contradict the source theorem; it shows why structural restrictions
on `T` matter.

## Novelty bounds

On 11 August 2026, the run indexes and local arXiv corpus were searched by
arXiv id and the terms `Kruglov property`, `U_E`, `isomorphic embedding`, and
`necessary`. External exact and close searches used the same phrases, the
paper title and authors, and the journal DOI. They surfaced the source and
earlier sufficient-condition literature but no explicit answer or this
`L^infinity` observation. OpenAlex listed no citing works for the DOI at the
time of the check; MaRDI listed five thematically related citing titles, none
of which surfaced an answer in the bounded search. Novelty confidence is
moderate and concerns the explicit identification of this counterexample,
not the standard universality facts used in its proof.

No computation is part of the mathematical argument.
