# Left-ideal cores for asymptotically nonexpansive actions

Status: `candidate_substantial_partial_likely_valid`.

Source: Bui Ngoc Muoi and Ngai-Ching Wong, *Fixed point theorems of
various nonexpansive actions of semitopological semigroups on weakly/weak*
compact convex sets*, arXiv:2006.15393v4 (2022), Question 5.5.

## Result

The packet proves two sufficient structural conditions under which the seven
fixed-point results named in Question 5.5 extend from super asymptotically
nonexpansive or pointwise eventually nonexpansive actions to asymptotically
nonexpansive actions.

1. If `S` has a least left ideal `L`, every asymptotically nonexpansive action
   is automatically super asymptotically nonexpansive: `L` lies in every
   pair-witness ideal and in every principal left ideal `S t`.
2. More generally, if `K` has density at most `kappa`, principal left ideals
   are closed, and every family of at most `kappa` closed left ideals
   intersects, the same upgrade follows from separate weak continuity and
   weak lower semicontinuity.

The first condition includes noncompact amenable examples.  For instance,
`S = Z x {0,1}` with `(g,i)(h,j)=(g+h,min(i,j))` is an infinite discrete
commutative semigroup whose least left ideal is `Z x {0}`.

The packet also proves an unrestricted compactification lemma: under right
reversibility, the pointwise-weak closure of every principal tail of the
action contains a globally nonexpansive map.  This does not finish the source
question because such a limit map need not be weakly continuous or
surjective.

## Reproduction

Run the exhaustive finite-semigroup check with:

```bash
conda run --no-capture-output -n sandbox python code/verify_left_ideal_core.py
```

The PDF contains the exact source screenshot, definitions, complete proofs,
verification discussion, novelty scope, and the obstruction to a full
result.
