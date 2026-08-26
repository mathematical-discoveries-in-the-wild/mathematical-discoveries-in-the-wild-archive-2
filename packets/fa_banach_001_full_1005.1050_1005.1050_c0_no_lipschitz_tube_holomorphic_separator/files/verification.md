# Verification notes

## Claim checked

Let `X` be a real Banach space containing an isomorphic copy of `c0`, and let
`X_C` be a complexification.  There are no constants `delta,L,m,M>0` and a
holomorphic function

    F:{x+iy in X_C : ||y||<delta}->C

such that:

1. `F` is globally `L`-Lipschitz on the tube;
2. `Q=F|_X` is real-valued, `Q(0)=0`, and `Q>=0`;
3. `Q(x)>=m||x||` whenever `||x||>=M`.

This gives a negative answer for `X=c0` to the explicit property used in
Theorem 2 of arXiv:1005.1050v5.

## Proof audit

1. A copy of `c0` supplies a basic sequence `(u_n)` and constants `a,b>0`
   with `||u_n||>=a` and the complex upper estimate
   `||sum z_n u_n||<=b max|z_n|` for finite scalar families.
2. For every continuous complex `k`-homogeneous polynomial `P`, the sequence
   `(P(u_n))` is in `ell_1`.  For `k>=2`, independent `k`th roots of unity
   kill every monomial except those with all `k` indices equal; preliminary
   phases turn the surviving coefficients into their absolute values.  For
   `k=1`, the statement follows directly from the same `c0` upper estimate.
3. Holomorphy and continuity of `F` at zero give a norm ball on which its
   Taylor series converges uniformly on a smaller ball.  The diagonal lemma
   plus a uniform Taylor-tail bound yields `F(tu_n)->0` for every `t` in a
   nonempty real interval about zero.
4. The functions `f_n(z)=F(zu_n)` are all holomorphic on the common strip
   `|Im z|<delta/b`.  Since `F` is globally Lipschitz and `F(0)=0`,
   `|f_n(z)|<=Lb|z|`; hence they form a normal family.
5. Every locally uniform subsequential limit vanishes on the real interval
   from step 3, and so vanishes identically by the scalar identity theorem.
   A subsequence contradiction then gives `f_n(z)->0` at every fixed point of
   the strip.
6. Choose real `T>=M/a`.  Separation gives
   `F(Tu_n)=Q(Tu_n)>=m||Tu_n||>=maT`, contradicting step 5.

All estimates are uniform in `n`.  No computation or unproved external lemma
is used beyond standard scalar Montel compactness and the identity theorem.

## Definition and scope audit

The source defines a separating function by `Q(0)=0` and a linear lower bound
`Q(x)>=m||x||` outside a ball.  Theorem 2 explicitly assumes “a Lipschitz
holomorphic extension” on `{x+iy: ||y||<delta}`.  The proof uses both the
fixed tube width and Lipschitz control of the extension.

The sentence after Theorem 2 asks whether `c0` has “such a Lipschitz separating
function.”  The packet treats “such” as referring to Theorem 2's explicit
hypothesis.  It does not settle the potentially weaker reading in which only
the real restriction is Lipschitz while the tube extension has no uniform
growth or Lipschitz control.

## Bounded novelty and literature audit (2026-08-11)

The run's registry, solution, attempt, and proof-gap indexes contained no
duplicate for arXiv:1005.1050 or the `c0` tube-separator question.

OpenAlex record `W2963896228` listed 13 citing works for the published paper.
All 13 titles were inspected.  The mathematically relevant ones were checked
in available abstracts or full text:

- M. Johanis, *A simple proof of the approximation by real analytic Lipschitz
  functions* (JMAA 388, 2012), still assumes a separating polynomial.
- M. Mytrofanov, *Separating polynomials, uniform analytical and separating
  functions* (Carpathian Math. Publ. 7, 2015), surveys the weaker uniformly
  analytic separator on `c0` and cites the source, but does not assert a
  globally Lipschitz tube extension.
- *Approximations of Symmetric Functions on Banach Spaces with Symmetric
  Bases* (2021) repeats the classical separator
  `d(x)=sum_n x_n^(2n)` on `c0`; this function is not globally Lipschitz.
- The other citing works concern derivative approximation, polynomial
  algebras, boundary values, Hölder approximation, o-minimal maps, or
  applications outside this question.

Exact-phrase searches for the source question and close searches combining
`c0`, Lipschitz, separating function, fixed-width tube, and holomorphic
extension found no direct answer.  The novelty assessment is moderate-to-high
under these bounded searches, not an exhaustive priority claim.

## Artifact verification

- The source PDF is arXiv:1005.1050v5, 43 pages.
- The question crop was rendered from PDF page 4 and visually inspected.
- The packet was built with `latexmk`; its log was checked for undefined
  references, warnings, and overfull boxes.
- Every rendered packet page was visually inspected.

## Human-review recommendation

Prioritize review.  The theorem is stronger than the `c0` instance and its
proof is short.  The main review points are the phase/root-of-unity extraction
of polynomial diagonals and whether the source intended the explicit
Lipschitz-extension hypothesis or the weaker ambiguous reading noted above.
