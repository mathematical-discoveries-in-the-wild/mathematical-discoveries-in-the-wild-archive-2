# A noncommutative 2-adic Fourier system, and a strict-model obstruction

Status: `candidate_full_dichotomy_likely_valid`

This packet gives a candidate full answer to Question 5.17 on page 31 of
Jiao--Luo--Zhao--Zhou, arXiv:2506.14431.

## Result

Let `A=Z[1/2]/Z`, the character group of the 2-adic integers.  In the
odometer crossed product

```text
R = L-infinity(Z_2) crossed-product_(x -> x+1) Z,
```

the unitaries

```text
X_(r,n)=chi_r u^n,             (r,n) in A x Z,
```

form a complete orthonormal basis of the hyperfinite II_1 factor, contain the
classical 2-adic character system as the subfamily `n=0`, and satisfy

```text
X_(r,n) X_(s,m)=exp(-2 pi i n s) X_(r+s,n+m).
```

This is an explicit genuinely noncommutative 2-adic Fourier system.

There is also a sharp obstruction to the most literal analogue of the paper's
noncommutative Vilenkin construction: every projective unitary family indexed
by two copies of `A` is commuting.  Therefore no such doubled-character family
can generate a noncommutative factor, and compatible finite cyclic Weyl bases
cannot be nested along the classical 2-adic character inclusions.

## Proof idea

The positive construction pairs a 2-adic frequency `r` with an integer
translation `n`.  Translation by 1 multiplies `chi_r` by its scalar value at
1, producing exactly the displayed twisted multiplication law.  Dyadic
residue projections and integer translations yield nested matrix algebras;
their union approximates the implementing odometer unitary in `L_2`, proving
hyperfiniteness directly.

For the obstruction, the commutators of any projective family indexed by
`A x A` define a homomorphism from the divisible group `A x A` into its dual
`Z_2 x Z_2`.  That dual has no nonzero divisible subgroup, so every commutator
is trivial.

## Scope

The source does not formally define “noncommutative 2-adic integer system.”
The affirmative construction satisfies the core properties visible in the
paper's noncommutative Vilenkin systems: a unitary orthonormal basis of the
hyperfinite factor, projective closure under multiplication, and recovery of
the classical characters.  It does not claim that a particular one-parameter
enumeration has the Cesaro/maximal inequalities proved in the source paper.
The strict doubled-dual finite-stage interpretation is impossible by the
second theorem.

## Files

- `main.tex`: exact source question, definitions, theorem, and proofs.
- `solution_packet.pdf`: compiled review packet.
- `VERIFICATION.md`: proof, source, novelty, and rendering audit.
- `source_paper.pdf`: local copy of arXiv:2506.14431.
- `figures/open_problem_crop.png`: full-width crop of Question 5.17.
- `../attempts/2506.14431_noncommutative_2_adic_system_attempt.md`: eight-route
  upgrade history (relative to the run root).

Human review should focus on whether the four stated Fourier-system axioms
match the authors' intended undefined term, and on the commutator-bicharacter
no-go argument.
