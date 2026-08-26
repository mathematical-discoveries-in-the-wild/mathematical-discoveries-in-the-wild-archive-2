# Contractively split compact projectives are free

Status: **candidate partial result; likely valid; human review requested**

Source: D. Clausen and P. Scholze, *Condensed Mathematics and Complex
Geometry*, arXiv:2605.11731, Question 3.6, page 26.

## Result

Let `S` be an extremally disconnected profinite set and let

```text
e : Z[S] -> Z[S],             e^2 = e,
```

be an idempotent.  Under the free/forgetful adjunction, `e` is determined by
a generator map `g:S -> Z[S]`.  If `g` lands in the integral `l1`-ball of
radius one in the standard filtration of `Z[S]`, then

```text
image(e) is isomorphic to Z[T]
```

for an extremally disconnected profinite retract `T` of `S`.

More precisely, `S` has a clopen partition `S_0 sqcup S_+ sqcup S_-`, and
there is a continuous map `r:S_+ sqcup S_- -> T` with `r|_T=id`, such that

```text
g(s) = 0          on S_0,
g(s) =  [r(s)]    on S_+,
g(s) = -[r(s)]    on S_-.
```

Conversely, every such signed partial retraction defines a radius-one
idempotent.  Thus Question 3.6 has an affirmative answer for every compact
projective admitting a contractive splitting in the canonical integral
`l1` gauge.

## Proof mechanism

For `S=lim S_i`, the radius-one part of the source's explicit model is

```text
lim_i Z[S_i]_(l1<=1) = {*} sqcup S sqcup S,
```

the three components being zero, a positive basis vector, and a negative
basis vector.  Idempotence forces the target of every nonzero signed basis
vector to be a positively fixed point.  The fixed-point set `T` is therefore
the image of a continuous retraction.  The signed partial retraction then
induces maps `Z[S] -> Z[T] -> Z[S]` whose composite is `e` and whose reverse
composite is the identity.

## Boundary and novelty status

This does not answer Question 3.6 for idempotents of generator bound at least
two.  At radius two, an image generator can already be a sum or difference of
two basis vectors, so idempotence no longer selects a continuous basis-point
retract.  The general problem is explicitly linked by the source to the old
classification problem for injective Banach spaces.

A bounded search on 9 August 2026 covered the exact wording of Question 3.6,
`compact projective condensed abelian group` with `idempotent`, `l1`,
`contractive`, and `retract`, the source lecture notes, recent condensed-
mathematics notes, and the cited injective-Banach context.  No statement of
this radius-one classification was located.  Originality is provisional.

## Verification report

Verdict: **likely valid**.  The proof is formal once the radius-one piece is
identified with `* sqcup S sqcup S`.  The included finite-model script
exhausted all generator maps on sets of sizes one through five and checked
every idempotent (2, 8, 44, 288, and 2192 cases respectively) against the
signed-partial-retraction normal form.  This corroborates only the algebraic
step; the packet contains the profinite continuity argument.

Human review should focus on the identification of the radius-one inverse
limit, the claim that `T` is a retract of `S`, and the two adjunction-induced
maps realizing `image(e)` as `Z[T]`.

## Files

- `solution_packet.pdf`: complete review packet
- `main.tex`: proof source
- `source_paper.pdf`: original source paper
- `figures/open_problem_crop.png`: Question 3.6 on source page 26
- `code/check_finite_contractive_idempotents.py`: finite corroboration

