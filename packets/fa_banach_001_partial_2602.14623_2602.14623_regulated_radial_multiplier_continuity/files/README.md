# Candidate Partial Result: Regulated Radial Multiplier Profiles Are Continuous

Status: `partial_result_likely_valid`

Model: GPT5.6

Source: Mikael de la Salle, *Kakeya conjecture and High-Rank Lattice von
Neumann algebras*, arXiv:2602.14623v1 (2026), Question 1.6 on page 4,
Theorem 1.7 on page 5, and Proposition 2.4.

## Claimed contribution

Let `d >= 2`, `1 < p < infinity`, and `p != 2`. Suppose the radial symbol
`xi -> m(|xi|)` is an `L_p(R^d)` Fourier multiplier. If the equivalence class
of `m` contains a locally regulated representative on `(0,infinity)`, then it
contains a continuous representative. Consequently, Question 1.6 has a
negative answer for all locally bounded-variation profiles, all locally finite
`q`-variation profiles (`1 <= q < infinity`), and all cadlag profiles.

This is a partial result only. It does not settle Question 1.6 for general
bounded measurable symbols and does not decide the highly oscillatory
`sin(log log)` candidate in Question 1.8.

## Proof mechanism

Write `f(t)=m(exp(t))`. The source theorem and Proposition 2.4 imply that
every weak-* limit of zooms `f(s_n + x/r_n)`, with `r_n -> infinity`, is
constant. At a regulated discontinuity, the centered zooms converge by
dominated convergence to the step function formed from the left and right
limits. Hence those limits must agree at every point. Replacing removable
point values by this common limit gives a continuous representative equal to
the original profile almost everywhere.

## Verification

- The only external mathematical dependency is Theorem 1.7 together with
  Proposition 2.4 of the source paper.
- The weak-* convergence is tested against arbitrary `L_1(R)` functions and
  follows from pointwise convergence off the origin plus the uniform bound.
- Equality almost everywhere is justified because, on each compact interval,
  the points where a regulated function differs by at least `1/n` from its
  common two-sided limit form a finite set.
- No computational evidence is used.

Verifier verdict: likely valid. The main review point is the passage from
matching one-sided limits to an almost-everywhere equal continuous
representative; a complete compactness argument is included in `main.tex`.

## Novelty and search bounds

On 2026-08-11, the run's four lightweight indexes were searched for
`2602.14623`, radial multiplier continuity, and core variants. The locally
parsed arXiv corpus was searched for later citations. Bounded arXiv/web
searches used the exact arXiv id, the exact `sin(log log)` phrase, and
`regulated`, `one-sided limits`, `bounded variation`, and `radial Fourier
multiplier`. No explicit prior statement of this regulated-profile corollary
was found. Novelty confidence is nevertheless modest because the result is an
elementary consequence of Proposition 2.4 in the source itself.

## Files

- `main.tex`: full candidate partial-result packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: real crop of Question 1.6 from source page 4.
- `../../../attempts/2602.14623_sinloglog_radial_multiplier_attack.md`:
  failed routes against the full question and Question 1.8.

Human review recommendation: check the elementary regulated-function lemma;
if accepted, retain as a narrow partial result and do not describe it as an
answer to the full radial multiplier continuity question.
