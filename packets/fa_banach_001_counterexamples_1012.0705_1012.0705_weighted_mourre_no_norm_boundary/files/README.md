# Weighted Mourre LAP without norm boundary values

Source: S. Golénia and T. Jecko, *Weighted Mourre's commutator theory,
application to Schrödinger operators with oscillating potential*,
arXiv:1012.0705v3.

Status: candidate full negative answer, likely valid, at the level of the
paper's general weighted Mourre/localised Putnam theorem.

## Result

There are self-adjoint `H`, bounded self-adjoint `B`, and bounded positive
injective `C` satisfying the strict weighted Mourre estimate

```text
[H,iB] = C^2
```

and all conjugation/localization hypotheses of the source's abstract
Theorem 3.4, while

```text
C(H-i eta)^(-1)C
```

has no operator-norm limit as `eta` decreases to zero.  Thus the weighted
Mourre estimate and the localised Putnam energy argument do not, by
themselves, imply norm boundary values or their continuity.

The example is a direct sum of rescaled copies of the exact model

```text
Q = multiplication by x,
D = (1+P^2)^(-1),
[Q,iB_0] = D^2.
```

Each fixed block has a norm boundary value, but the boundary modulus is not
uniform under the rescaling.  This destroys the boundary limit of the
direct sum while preserving the uniform LAP.

The packet explicitly does not claim to settle the narrower possibility
that the additional simultaneous structure `C=<A>^(-s)`, `B=phi(A)` across
the full family of estimates in Theorem 1.1 forces continuity.

## Files

- `main.tex`: exact counterexample and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_question_crop.png` and
  `figures/open_question_continuation.png`: exact source question.
- `code/verify_scaled_blocks.py`: symbolic and scale checks.
- `verification.md`: proof, build, checksum, and visual-QA record.

