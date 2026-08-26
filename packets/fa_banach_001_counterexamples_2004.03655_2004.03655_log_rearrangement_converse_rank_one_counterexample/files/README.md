# Counterexample Packet: The Logarithmic Rearrangement Converse Fails

Run: `fa_banach_001`

Status: `candidate_counterexample_likely_valid`

## Source Problem

- Sergey Astashkin and Mario Milman, *Extrapolation: Stories and Problems*,
  arXiv:2004.03655, Problem 28 on page 42.
- Problem 28 asks for a direct proof that the two rearrangement inequalities
  displayed as (10.8) are equivalent.
- `source_paper.pdf` is a local copy of the arXiv PDF.
- `figures/rearrangement_inequalities_10_8_crop.png` shows (10.8) on page 41.
- `figures/open_problem_crop.png` shows Problem 28 on page 42.

## Claimed Contribution

The equivalence is false in its literal standalone form. One direction is
always true: if

`int_0^t (Tf)^* <= C int_0^t f^* log(t/s)`,

then Tonelli's theorem gives

`int_0^t (Tf)^* log(t/s) <= (C/2) int_0^t f^* log^2(t/s)`.

The converse fails for the rank-one linear operator

`Tf = (int_0^1 f(s) log^2(1/s) ds) 1`.

This operator is bounded on every `L^p(0,1)`, `1<p<infinity`. The second
inequality holds with constant one for every bounded input, by the elementary
rearrangement inequality and the monotonicity of `f^*`. However, for
`f_epsilon = 1_(0,epsilon)` and `t=1`, the ratio required in the first
inequality equals

`L + 1 + 1/(L+1)`, where `L=log(1/epsilon)`,

and hence tends to infinity.

## Scope Warning

This is a counterexample to the literal claim that the two explicit
inequalities (10.8) are equivalent as operator properties. It does not
contradict a version that retains an additional `O(p/(p-1))` norm-growth
hypothesis from the preceding extrapolation-scale discussion. Indeed, the
constructed operator has

`||T||_(L^p -> L^p) = Gamma(2p'+1)^(1/p')`,

which grows on the order of `(p')^2`, not `p'`, as `p` decreases to one.
Human review should therefore check the intended scope of the word
"equivalence" in Problem 28 as well as the mathematical construction.

## Verification Status

The proof is self-contained and noncomputational. The verifier report checks:

- boundedness on every stated `L^p` space;
- the second inequality for all bounded inputs and all `0<t<=1`;
- the exact indicator-function ratio that destroys the first inequality;
- the one-way Tonelli implication and its factor `1/2`;
- the semantic distinction between the literal problem and a version with a
  retained `O(p')` hypothesis.

Verdict: `likely valid`, with the scope warning above.

## Novelty Check

The run indexes were searched for arXiv:2004.03655, the title, the exact
Problem 28 phrase, `equivalence of rearrangement inequalities`, logarithmic
kernels, and rank-one counterexamples. No duplicate solution, attempt, or
proof-gap packet was found.

Bounded web/arXiv searches on 2026-08-09 used the exact problem phrase,
variants involving Astashkin--Milman and logarithmic rearrangement
inequalities, and later Astashkin--Lykov--Milman extrapolation papers. The
search found the source paper and related extrapolation work, but no later
paper resolving or correcting Problem 28 and no matching rank-one
counterexample. This is not an exhaustive novelty claim.

## Files

- `main.tex`: complete counterexample proof and scope analysis.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original source paper.
- `figures/`: source evidence crops from pages 41--42.
- `verification.md`: adversarial proof check and human-review focus.
- `code/README.md`: records that no computation is part of the proof.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Human Review Recommendation

Send to a functional analyst familiar with extrapolation scales. The
mathematical counterexample is elementary; the main review question is whether
Problem 28 intended the explicit inequalities as standalone properties or
silently retained the preceding `O(p')` operator-norm hypothesis.
