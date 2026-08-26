# Canonical almost-periodic extensions of C-distribution cosine orbits are even

**Status:** candidate full proof, likely valid; pending expert review.

**Source question:** Marko Kostić, Stevan Pilipović, and Daniel Velinov,
*Subspace Almost Periodic C-Distribution Semigroups and C-Distribution
Cosine Functions*, arXiv:1808.01197, item 3 on PDF page 10.

## Result

No additional condition is needed in the source question. If
`Gbold` is a `C`-distribution cosine function, `Etilde` is a subspace of
`Z_2(A)`, and every positive orbit

```text
  f_x(t) = G(delta_t)x,  t >= 0,
```

is almost periodic for `x in Etilde`, then its unique canonical extension
`Cbold_x=F(f_x)` to the real line is automatically even:

```text
  Cbold_x(-t) = Cbold_x(t) = G(delta_t)x
```

for every real `t>=0` and every `x in Etilde`.

## Proof idea

Fix `t` and choose increasingly accurate positive almost periods `tau_n>t`
of the orbit. The isometric extension theorem makes them equally accurate
periods on the whole real line. With `y_n=G(delta_tau_n)x`, the positive-time
cosine identity gives, uniformly for `0<=s<=t`,

```text
  G(delta_s)y_n
    = (G(delta_(tau_n+s))x + G(delta_(tau_n-s))x)/2
    -> (Cbold_x(s)+Cbold_x(-s))/2.
```

The possibly unbounded component operator `G(delta_t)` need not be assumed
closed. Lift instead to the paper's associated first-order
`Ccal`-distribution semigroup on `E x E`. Its operator at time `t` is closed,
and its orbit from `(0,y)` is

```text
  ( integral_0^t G(delta_s)y ds, G(delta_t)y ).
```

Both coordinates converge for `y=y_n`, while `y_n->x`. Closedness therefore
forces the second limiting coordinate to equal `G(delta_t)x`. This says

```text
  (Cbold_x(t)+Cbold_x(-t))/2 = Cbold_x(t),
```

which is the desired evenness.

## Files

- `main.tex` / `solution_packet.pdf`: self-contained statement and proof.
- `source_paper.pdf`: arXiv:1808.01197.
- `figures/source_question.png`: exact source question.
- `verification.md`: source, domain, literature, and artifact audit.
- `../../../attempts/1808.01197_even_extension_closed_graph.md`: the
  multi-stage derivation and upgrade record.

## Review focus

The only specialized input worth checking against the source conventions is
the standard orbit formula for the associated `2 x 2` first-order reduction.
The packet derives it directly from the mild-solution identities. Everything
else is the source cosine identity, its isometric half-line extension theorem,
and closedness of the associated distribution-semigroup operator.

Bounded exact-title, exact-formula, phrase, author/title, and citation searches
through 2026-08-11 did not locate a later answer. Novelty confidence is
moderate; mathematical confidence is high.
