# Endpoint a.e.-limit stability fails for weak chain upper gradients

Status: `candidate_counterexample_likely_valid_needs_human_review`

Source: Caputo--Cavallucci, arXiv:2408.15071, the remark after Proposition
5.9 (continued on source PDF page 22).

## Result

The source asks whether Proposition 5.9 remains true for the asymmetric
endpoint chain integrals `lambda=1` and `lambda=0`. The answer is no for every
`p>=1` and every `epsilon>0`, already on the real line with Lebesgue measure.

For `lambda=1`, take

```text
u_j = 0,  g_j = 0,  u = 1_{0},  g = 0.
```

Then `u_j -> u` pointwise almost everywhere and `g_j -> g` in `L^p`. Each
`g_j` is a weak endpoint upper gradient of the constant function `u_j`.
But along every one-edge chain `(x,0)`, the limit inequality fails:
`u(0)-u(x)=1` while the `lambda=1` integral of `g` is zero.

This failure family cannot be discarded. Any modulus-admissible `rho` must
satisfy `rho(x)|x|>=1`, so

```text
integral rho(x)^p dx >= 2 integral_0^r x^{-p} dx = infinity.
```

Thus the family has infinite `(epsilon,1,p)`-modulus. For `lambda=0`, take
`u=-1_{0}` and use the reversed chains `(0,x)`; the identical modulus
calculation applies.

## Mechanism

At `lambda=1`, the directed integral ignores each edge's terminal vertex, so
changing the a.e. limit representative at a null terminal point can still be
seen by a large-modulus family. At `lambda=0`, the ignored endpoint is the
initial one. Ordinary a.e. convergence is therefore too weak at both
asymmetric endpoints.

## Duplicate and novelty checks

The four cheap run indexes have no exact hit for arXiv:2408.15071 or this
endpoint question. Bounded arXiv-facing searches for the paper title,
Proposition label, and endpoint weak chain upper gradients found only the
source paper and no matching resolution. Human review should still search for
the same representative-instability observation under different terminology.

## Files

- `main.tex`: full proof.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_question_crop.png`: actual crop of the endpoint remark.
- `code/crop_open_question.py`: crop script.
- `verification_report.md`: definition, modulus, build, and visual checks.
