# Two smooth counterexamples for semicocycles in Banach spaces

**Status:** candidate full counterexamples, likely valid; human review needed.

**Source:** Mark Elin, Fiana Jacobzon, and Guy Katriel, *Continuous and
holomorphic semicocycles in Banach spaces*, arXiv:1807.09965; Journal of
Evolution Equations 19 (2019), 1199--1221, DOI
`10.1007/s00028-019-00509-5`.

## Result

The packet gives negative answers to both unresolved general questions isolated
in the source:

1. A real-analytic continuous semigroup on the open unit ball of the real
   Hilbert space `ell_2 direct-sum_2 R` need not act strictly inside the ball.
2. A scalar, globally bounded, smooth semicocycle can be T-continuous at time
   zero but fail T-continuity at time one.

The common mechanism is a real-analytic nonnegative function

`g(u)=sum_{k>=1} k(2u_k)^(2k)`

with `g((1/2)e_n)=n`. It drives translation in a scalar `artanh` coordinate
inside the Hilbert ball. A smooth moving-threshold coboundary then converts the
same nonuniform speed into the T-continuity counterexample.

## Packet contents

- `solution_packet.pdf`: self-contained theorem and proof.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original source paper.
- `figures/strict_inside_open_question.png`: Definition 2.4 and first open
  question, source PDF page 5.
- `figures/t_continuity_open_question.png`: second open question and context,
  source PDF page 10.
- `verification.md`: hypothesis-by-hypothesis verifier notes.

## Scope and novelty

The construction answers the general continuous/smooth questions. It does not
address the narrower holomorphic-semigroup setting on hyperbolic complex
domains, for which the source records a positive strict-inside result.

A bounded search on 2026-08-11 used the exact title and arXiv id, both quoted
open-question sentences, and the key phrases “acts strictly inside” and
“T-continuity at time zero.” No later paper explicitly answering either
question and no matching counterexample was located. This supports review as a
potentially new result, but is not a comprehensive priority search.

## Human-review recommendation

High priority. Check the local uniform convergence/analyticity of `g`, the
Hilbert-ball coordinate change, and the two-case uniform estimate proving
T-continuity at zero. The discontinuity at time one is then immediate.
