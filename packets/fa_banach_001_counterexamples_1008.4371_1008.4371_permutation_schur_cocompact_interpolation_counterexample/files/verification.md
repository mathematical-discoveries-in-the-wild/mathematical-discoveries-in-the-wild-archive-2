# Verification notes

## Claim checked

Let `D={P_pi: pi is a permutation of N}` be the full coordinate-permutation
group. Set

    (A0,A1) = (B0,B1) = (ell_infinity,ell_1).

Then `A1 -> B1` is `D`-cocompact, but for every `theta in (0,1)`, with
`p=1/theta`, neither the complex interpolated identity on `ell_p` nor the
real interpolated identity for parameter pair `(theta,p)` is `D`-cocompact.
This negatively answers the abstract question in Remark 1.7 of
arXiv:1008.4371v3.

## Baseline-hypothesis audit

1. `ell_1` embeds continuously into `ell_infinity`.
2. The endpoint inclusions `Aj -> Bj` are identities for `j=0,1`.
3. Each `P_pi` is a linear bijective isometry on both endpoint spaces; the
   permutations form a group containing the identity.
4. If `x_k` is `D`-weakly null in `ell_1`, then it is weakly null because one
   may choose the identity permutation for every `k`. The Schur property gives
   `||x_k||_1 -> 0`, proving endpoint `D`-cocompactness.
5. The source's baseline theorem and question permit equal source and target
   couples and impose no reflexivity assumption. The extra mollifier family is
   precisely among the conditions whose unconditional removal is at issue.

## Interpolation audit

For `0<theta<1`, the standard sequence-space formulas are

    [ell_infinity,ell_1]_theta = ell_p,       1/p=theta,
    (ell_infinity,ell_1)_(theta,q) = ell_(p,q).

At `q=p`, the Lorentz sequence space `ell_(p,p)` is `ell_p` with an
equivalent norm. Equivalence of norms does not affect weak convergence or
norm convergence to zero. Coordinate permutations remain isometries for the
standard `ell_p` norm (and bounded isomorphisms under any equivalent
interpolation norm), so the cocompactness failure is intrinsic.

## `D`-weak convergence audit

Fix `p in (1,infinity)` and let

    u_k = k^(-1/p) sum_(j=1)^k e_j.

Then `||u_k||_p=1`. For an arbitrary permutation sequence `(pi_k)`, the
vector `P_(pi_k)u_k` is `k^(-1/p)` on a `k`-element set `S_k` and zero
elsewhere. Given `f in ell_(p')` and a finite set `F`, Hölder's inequality
gives

    |<P_(pi_k)u_k,f>|
      <= k^(-1/p)||f 1_F||_1 + ||f 1_(F^c)||_(p').

The first term tends to zero for fixed `F`. The second is independent of the
sets `S_k` and can be made arbitrarily small by enlarging `F`. Thus
`P_(pi_k)u_k` converges weakly to zero for every permutation sequence. This
is exactly `D`-weak convergence, with the required universal quantifier.
Since the norms stay one, the identity `ell_p -> ell_p` is not
`D`-cocompact.

## Definition and scope audit

Source Definition 1.1 requires `g_k(u_k-u)` to converge weakly to zero for
every sequence `(g_k)` in `D`; the estimate above is uniform in that choice.
Source Definition 1.2 then declares an embedding `D`-cocompact when every
such sequence converges in target norm. The construction violates exactly
this conclusion.

The counterexample refutes:

- complex persistence for every `theta in (0,1)`; and
- real-method persistence for every `theta in (0,1)` at the allowed choice
  `q=1/theta`.

It does not claim failure for every real-method fine index `q`.

## Bounded novelty and literature audit (2026-08-11)

The run's registry, solution, attempt, and proof-gap indexes contained no
duplicate for arXiv:1008.4371 or the arbitrary-group interpolation question.

Exact-phrase and close searches combined the source title/question with
`counterexample`, `Schur property`, `permutation group`, `ell_1`, and
`cocompact interpolation`; no direct answer was found. OpenAlex record
`W1972026762` listed twelve citing works. Their titles and available abstracts
were inspected. They concern applications to Sobolev/Besov spaces, invariant
subspaces, affine compactness, profile decompositions, and nonlinear PDE; none
advertises an answer to the abstract question.

C. Tintarev's later survey *Concentration analysis and cocompactness*,
arXiv:1309.3431 (2013), still says one would expect a general interpolation
principle and refers only to the source theorem under additional conditions.
The survey uses the flat sequence
`k^(-1/p)1_{1,...,k}` to illustrate a nonvanishing remainder for the shift
group. It does not pass to the full permutation group, invoke the Schur
endpoint, or state the present counterexample. Novelty confidence is
moderate-to-high under this bounded audit, not an exhaustive priority claim.

## Artifact verification

- The source PDF is arXiv:1008.4371v3, 41 pages.
- The question crop was rendered from PDF page 3 and visually inspected.
- The packet was built with `latexmk`; its log was checked for undefined
  references, warnings, and overfull boxes.
- Every rendered packet page was visually inspected.

## Human-review recommendation

Prioritize review. The construction is elementary and answers both halves of
the source question. The main checks are the weak-convergence quantifiers, the
reversed-couple exponent `p=1/theta`, and a broader priority search.
