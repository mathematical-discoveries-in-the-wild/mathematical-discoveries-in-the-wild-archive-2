# Counterexample Packet: Target Translations Defeat Gradient-Only Control

Run: `fa_banach_001`

Source: Giacomo Canevari and Giandomenico Orlandi, *Topological singular
set of vector-valued maps, I: Applications to manifold-constrained Sobolev
and BV spaces*, arXiv:1712.10203v2.

Status: `candidate_full_counterexample_likely_valid`.

## Result

In the sphere case, take `d=m=k>=2`, `Omega=B_1(0)`, and

```text
u_0(x)=x,        u_1(x)=x+3e_1.
```

Then `grad u_1-grad u_0=0`, but the two singular-chain families are the
signed preimage chains over the disjoint ranges `B_1(0)` and
`3e_1+B_1(0)`.  In fact,

```text
||S(u_1)-S(u_0)||_Y >= |B_{1/2}^k|/4 > 0.
```

Consequently no continuity estimate controlled only by Sobolev norms of
the gradient difference, with right-hand side vanishing at zero, can hold
in general.  A repaired statement must break target-translation freedom,
for example by including a norm of `u_1-u_0` or imposing a common
normalization.

## Files

- `main.tex`, `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_question_crop.png`: the question on source page 21.
- `code/crop_source_question.py`: reproducible crop script.
- `code/verify_translation_obstruction.py`: numerical geometry sanity check.
- `VERIFICATION.md`: proof audit and verification commands.
- `tmp/`: build and render intermediates.

## Human review recommendation

Accept as a complete negative answer to the literal gradient-difference
question, with the scope stated above.  The only convention-sensitive
quantity is the sign of the generator in the signed preimage chain; the
argument uses only its nonzero unit multiplicity, so the sign is irrelevant.
