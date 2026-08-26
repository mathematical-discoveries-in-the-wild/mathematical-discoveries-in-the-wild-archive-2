# Verification report

Verdict: `likely valid`.

## Exact algebraic audit

Let `R=-I` and choose `u != 0`. At `x=u`, `y=-u`:

```text
||Rx-Ry|| = 2||u||
||x-y||   = 2||u||
||x-Rx||  = 2||u||
||y-Ry||  = 2||u||
||x-Ry||  = 0
||y-Rx||  = 0
```

Therefore the quasi-contraction inequality would read
`2||u|| <= 2h||u||`, contradicting `h<1`.

The half-average is exactly
`R_(1/2)=(1/2)I+(1/2)(-I)=0`. For the zero map the left side of the defining
inequality is always zero, so any `h in (0,1)` works. This proves strict
containment in the enriched class.

For the Ciric-Reich-Rus condition, the same pair gives right side
`2(a+2b)||u||`, strictly below the left side because `a+2b<1`.

## Edge and semantic checks

- `lambda=1/2` lies in the source interval `(0,1]`.
- `-I` is a self-map on every real or complex normed space.
- A nonzero `u` exists exactly when `X != {0}`.
- On `X={0}`, there is one self-map, it belongs to the class, and averaging
  does not create another map; the class is saturated.
- Completeness is unused, so the proof is stronger than requested.

## Novelty/scope audit

Exact-phrase web searches through 2026-08-11 found a 2022 explicit answer to
Open Problem 1 (Ciric-Reich-Rus) but no explicit answer to Open Problem 2
(Ciric quasi-contractions). The packet therefore claims candidate novelty only
for Open Problem 2.

