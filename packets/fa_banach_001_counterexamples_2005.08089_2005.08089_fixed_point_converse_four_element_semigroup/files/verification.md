# Verification Report

Status: `candidate_counterexample_likely_valid`

## Claim checked

Remark 5.3 of arXiv:2005.08089 asks whether the common-fixed-point property of
`P(phi)` in Corollary 5.2(ii) implies that `S` is `phi`-amenable.  The packet
claims a negative answer for the finite discrete semigroup
`S=C_2 x R_2`, with `R_2` right-zero and the nontrivial sign character on
`C_2`.

## Adversarial checks

1. **Semigroup and topology.** The multiplication is a direct-product
   multiplication, hence associative.  The finite discrete topology makes
   multiplication and the character continuous.

2. **Character and kernel.** `phi(eps,i)=(-1)^eps` is multiplicative, and
   `P(phi)={(0,0),(0,1)}`.  Its multiplication is `p_i p_j=p_j`, exactly the
   two-element right-zero semigroup.

3. **Fixed-point orientation.** For a representation with
   `T_(pq)=T_p T_q`, Schauder-Tychonoff supplies a fixed point `y` of one map
   `T_(p_0)`.  Then `T_p y=T_p T_(p_0)y=T_(p p_0)y=T_(p_0)y=y` for every `p`.
   This proves the precise affine fixed-point property in Corollary 5.2(ii).

4. **Mean consequence is not assumed.** The packet derives the needed
   functional from right `phi`-amenability using
   `X=C(S)/C phi` and the canonical derivation
   `D(s)=s.F_0-F_0.s`.  All boundedness and continuity requirements are
   automatic for finite discrete `S`.  Identifying `X*` with the annihilator
   of `phi` is valid because `C phi` is an `S`-submodule.

5. **Module orientation.** On `C(S)`, the proof uses
   `(s.f)(t)=f(ts)` and `(f.s)(t)=phi(s)f(t)`.  Thus the quotient has the
   scalar *right* action required in the source definition of right
   `phi`-amenability.  Dualizing gives the right-translation equation
   `m(R_s f)=phi(s)m(f)`, the orientation used in the contradiction.

6. **Contradiction.** For `p_i=(0,i)`, right multiplication sends every
   `(eps,j)` to `(eps,i)`.  Hence
   `R_(p_i)(phi u_(1-i))=0`.  Since `phi(p_i)=1`, invariance forces both
   `m(phi u_0)` and `m(phi u_1)` to vanish.  Their sum is `m(phi)`, which must
   equal one.  No positivity assumption is used.

7. **Exact computational check.** `code/verify_finite_semigroup.py` checks 64
   associativity triples, 16 character pairs, the right-zero kernel, and the
   entire invariant-functional linear system over `Fraction`.  The coefficient
   matrix has rank 4 and the augmented matrix rank 5, so the system is
   inconsistent.

8. **Semantic scope.** The counterexample refutes the source's literal
   two-sided term `phi`-amenable.  It does not refute the possible repaired
   statement with `left phi-amenable` as conclusion.  This distinction is
   explicit throughout the packet.

## Novelty bounds

Local run indexes and the full-source scan were searched.  Bounded web/arXiv
searches on 2026-08-09 covered the exact remark wording, paper title/DOI and
authors, plus fixed-point, `P(phi)`, right-zero, and character-amenability
variants.  No later answer or matching construction was located.  The search
is bounded, not exhaustive.

## Verdict

`likely valid`.  The mathematical argument is elementary and self-contained.
The principal review risk is interpretive rather than algebraic: a reviewer
should confirm that Remark 5.3 is read literally with the paper's defined
two-sided notion.
