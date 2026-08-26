# Even-exponent matrix-level lower bounds

- **Run:** `fa_banach_001`
- **Agent:** `agent_lane_08`
- **Model:** `GPT5.6`
- **Source:** Mikael de la Salle, *Complete isometries between subspaces of
  noncommutative Lp-spaces*, arXiv:0707.0427.
- **Status:** substantial partial result, likely valid.

For `p=2m`, this packet proves

`floor(m/2)+1 <= n_{2m,1} <= m`

and

`max(2,ceil(m/2)) <= n_{2m} <= m`.

The upper bounds are from the source. The new lower bounds come from exact
finite-dimensional counterexamples: Amitsur--Levitzki supplies a cyclic
trace-polynomial direction invisible at matrix level `r` but visible at level
`r+1`, and finite-dimensional convex separation realizes that direction as
the difference of two positive tracial matrix-tuple distributions. A common
tagging summand makes the tuples linearly independent and therefore defines
an honest linear map between finite-dimensional noncommutative Lp subspaces.

The packet also proves that the source's cyclic-word isolators have optimal
matrix size `ceil(N/2)`. The non-even finiteness questions remain open: their
norm expansions involve infinitely many moment degrees, beyond the finite
tracial-separation argument used here.

## Files

- `solution_packet.pdf`: expert-facing proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:0707.0427.
- `figures/open_problem_crop.png`: source Section 3.3, printed page 24.
- `code/verify_trace_identity.py`: exact small-rank audit of the standard
  polynomial, chain witness, marker trace, and boundary coefficient.
- `verification.md`: build, algebraic, and review notes.

## Review focus

Review the finite tracial separation lemma and the two coefficient-extraction
identities that convert norm polynomials into the marked standard polynomial.
The explicit Amitsur--Levitzki witness and scalar coefficient are independently
checked by the verifier; computation is not used as proof.

