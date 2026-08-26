# No invariant algebraic complement of the constants in the Bloch space

This packet gives a candidate full negative answer to the question in
footnote 1 on page 3 of arXiv:2211.06055.

## Result

The constant functions have no algebraic complement in the classical Bloch
space on the unit disk that is invariant under the Möbius composition action.
In fact, invariance under one explicit hyperbolic automorphism already makes a
complement impossible.

## Proof idea

Conjugate the disk automorphism

```text
phi(z)=(3z+1)/(z+3)
```

by the Cayley map `C(z)=(1+z)/(1-z)` to multiplication by 2 on the right
half-plane.  The Bloch function

```text
h(z)=Log(C(z))/log 2
```

satisfies the Abel equation `h o phi-h=1`.  An invariant projection onto the
constants would send the left side to zero and the right side to one.

## Files

- `main.tex`: statement, source excerpt, and proof.
- `solution_packet.pdf`: compiled packet.
- `verification.md`: independent proof and render checks.
- `source_paper.pdf`: arXiv source PDF.
- `figures/`: source-question crops from page 3.

Status: candidate full proof, likely valid.  Independent human verification is
still requested.

