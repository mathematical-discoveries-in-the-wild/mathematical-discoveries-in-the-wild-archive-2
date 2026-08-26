# A Bhatia-Semrl operator with infinite-dimensional norming span

Status: candidate counterexample / full negative answer to the question in Remark 3.3 of arXiv:2512.15208.

## Result

On the real reflexive space

```text
X = R direct-sum-infinity ell_2,
```

the coordinate functional `f(a,h)=a` has the Bhatia-Semrl property, while

```text
span(M_f) = X.
```

Thus an operator with the Bhatia-Semrl property need not have a finite-dimensional norming span.

## Proof mechanism

The dual is `X* = R direct-sum-1 ell_2`. If `g=(alpha,k)` and `f` is Birkhoff-James orthogonal to `g`, then

```text
||f + lambda g|| = |1 + lambda alpha| + |lambda| ||k||_2 >= 1
```

forces `|alpha| <= ||k||_2`. Choosing `h=-alpha k/||k||_2^2` gives a point `x=(1,h)` in `M_f` with `g(x)=0`, which is the required pointwise witness. Meanwhile the flat norming face contains `(1,h)` for every `h` in the unit ball, and its span contains the entire `ell_2` direction.

## Files

- `main.tex`: complete proof and scope discussion.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_question_crop.png`: Proposition 3.2 and Remark 3.3 from page 8.

## Novelty and scope

The 2019 Kim-Lee theorem that every functional on a reflexive Banach space has the Bhatia-Semrl property independently confirms the example, but the packet provides a direct proof. Bounded searches through 2026-08-09 found no explicit answer to Remark 3.3. Novelty is medium-low because the construction is a short consequence of a theorem already cited by the source.

This does not answer the source's broader essential-norm question: `f` is compact and has essential norm zero.
