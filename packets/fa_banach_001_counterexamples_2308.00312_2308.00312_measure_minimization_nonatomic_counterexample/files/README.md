# Nonatomic counterexample to the Measure Minimization Conjecture

Status: `counterexample_likely_valid`

Source: K. Mahesh Krishna, *Functional Continuous Uncertainty Principle*,
arXiv:2308.00312. The target is Conjecture 3.2 on source PDF page 6.

## Result

Conjecture 3.2 is false even for a one-dimensional real Hilbert space and a
normalized continuous Parseval frame.

Take `Omega=[0,1]` with Lebesgue measure, `H=R`, and `tau_alpha=1`. For any
`0<a<1`, define

```text
f_a = a^(-1) 1_(0,a).
```

The frame coherence is 1, so the conjectured support threshold is 1. We have

```text
mu(supp f_a)=a<1,
theta_tau^* f_a = integral_0^1 f_a = 1.
```

Yet, for every `0<b<a`, the function `f_b` synthesizes the same `h=1` and has
strictly smaller support. Hence `f_a` is not a minimizer of `(P_M)`, much less
its unique minimizer. Indeed, the infimum support measure in this synthesis
fiber is zero and is not attained.

## Scope

This is a full disproof of the Measure Minimization Conjecture exactly as
stated. It does not address the paper's separate three-part question about
equality, endpoint versions, or Tao/Meshulam analogues, nor Problem 3.3 on
NP-hardness. A repaired sparsity theory would need atomicity, an amplitude
constraint, or a different objective such as total variation.

## Files

- `solution_packet.pdf`: expert-facing counterexample and proof.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: Conjecture 3.2 from source PDF page 6.
- `code/verify_counterexample.py`: exact rational checks.
- `verification.md`: build and verification record.

## Novelty check

A bounded search on 2026-08-11 covered the run indexes; the exact conjecture
name and formula; arXiv id and author queries; continuous-frame support-measure
minimization; and later related papers by the same author. No existing
counterexample or retraction was found. Novelty confidence is moderate because
the example is elementary and the source is a short preprint.

## Human review recommendation

Review as a likely valid full counterexample to Conjecture 3.2. Check only the
standard continuous-frame normalization and the synthesis calculation; both
are immediate in dimension one.
