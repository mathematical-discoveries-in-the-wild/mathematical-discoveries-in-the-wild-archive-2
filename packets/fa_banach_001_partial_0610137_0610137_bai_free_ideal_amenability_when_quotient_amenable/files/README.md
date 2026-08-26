# BAI-free ideal amenability when the quotient is amenable

Status: `candidate_partial_likely_valid`.

Source: M. Eshaghi Gordji, B. Hayati, and S. A. R. Hosseiniun,
“Derivations into duals of closed ideals of Banach algebras,”
arXiv:math/0610137v2 (2006).

## Result

Let `I` be a closed ideal of a Banach algebra `A`.  If `I` is ideally
amenable and `A/I` is amenable in Johnson's sense, then `A` is ideally
amenable.  No approximate identity is assumed on `I`.

The packet also proves an exact structural variant.  It is enough that `I`
and `A/I` be ideally amenable and that every closed ideal `J` of `A` satisfy

```text
I+J is closed,      I intersect J = closure(IJ+JI).
```

These two relations are precisely what a bounded approximate identity in
`I` supplies in the original theorem.

The proof reduces an arbitrary derivation `D:A -> J*`, modulo an inner
derivation, to a derivation on `A/I` with coefficients in

```text
(J / closure(IJ+JI))*.
```

Ordinary amenability of the quotient handles this arbitrary dual module.
Under the structural hypotheses it is instead the dual of the closed ideal
`(I+J)/I`, so quotient ideal amenability suffices.

This is a substantial partial answer, not a solution of the unrestricted
question.  It leaves open whether endpoint ideal amenability alone controls
the residual module.

## Concrete non-BAI instance

For an infinite-dimensional Hilbert space `H`, the trace-class algebra
`S_1(H)` is topologically simple and weakly amenable, hence ideally
amenable, but it has no bounded approximate identity in trace norm.  Its
unitization has quotient `C`, so the first theorem proves the unitization is
ideally amenable without using a BAI in the ideal.  The packet gives short
self-contained proofs of these assertions.

## Later claim and proof-gap status

Theorem 4.1 of A. Ranjbari and A. Rejali, “Ideal Amenability of Fréchet
Algebras,” U.P.B. Sci. Bull. A 79(4) (2017), 51--60, states a stronger
theorem which would settle the Banach case.  The proof has a coefficient-
module gap; this investigation therefore does not treat the source question
as answered literature.  See
`runs/fa_banach_001/proof_gaps/2017_frechet_ideal_amenability_three_space_gap`.

## Files

- `solution_packet.pdf`: complete proof and review notes.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: the question on source PDF page 13.
- `novelty.md`: bounded literature and duplicate audit.
- `verification.md`: mathematical, build, and rendering checks.

Human review should focus on the passage from restricted vanishing on
`I intersect J` to vanishing on `I`, and on the identification of the
residual annihilator with a quotient-ideal dual in the structural theorem.
