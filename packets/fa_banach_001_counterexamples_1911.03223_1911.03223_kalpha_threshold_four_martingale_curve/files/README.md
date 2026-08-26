# Counterexample packet: the `K_alpha` threshold `4` is sharp

Status: `candidate_full_counterexample_likely_valid`.

## Result

For every `0 < alpha < 4`, there is a compact regular curve `Gamma_alpha`
in the first Heisenberg group such that the nonnegative singular integral
with

```text
K_alpha(x,y,t) = |t|^(alpha/2) / ||(x,y,t)||^(alpha+1)
```

is not uniformly bounded on `L^2(H^1|Gamma_alpha)`.

In particular, this gives a negative answer to the question following
Theorem 1.7 of Fässler--Orponen, arXiv:1911.03223, asking whether their
positive theorem for `alpha >= 4` persists for `alpha >= 2`.  Together with
their theorem, it makes `alpha = 4` the exact threshold.

The 2026 paper of Chousionis--Li--Zhang, arXiv:2605.17680, independently
constructs counterexamples for `0 < alpha < 2` and explicitly leaves
`[2,4)` as a possible extension.  The packet's stopped-martingale graph is a
different construction and covers the missing interval.

## Mechanism

A bounded stopped dyadic martingale has increments `epsilon_j` with
`sum epsilon_j^2 < infinity` but
`sum epsilon_j^(alpha/2) = infinity`.  Integrating its terminal function
twice produces a horizontal intrinsic Lipschitz graph.  Across opposite
halves of each active dyadic interval, the graph's normalized vertical
coordinate is bounded below by `epsilon_j`.  The relevant pair rectangles
are disjoint, and positivity of `K_alpha` converts their contributions into
the divergent series above.

## Contents

- `main.tex` and `solution_packet.pdf`: complete statement and proof.
- `source_paper.pdf`: Fässler--Orponen, arXiv:1911.03223.
- `supporting_paper_2605.17680.pdf`: the May 2026 status paper.
- `figures/open_problem_crop.png`: the source theorem and question, PDF page 4.
- `code/verify_martingale_curve.py`: finite-grid and exponent checks.
- `verification_report.md`: adversarial proof, novelty, and artifact audit.

## Scope limitation

The kernels `K_alpha` are not smooth across the horizontal plane for the
critical values in this counterexample.  Thus the construction settles the
separate `K_alpha` threshold question but does not by itself settle the
smooth-kernel Question 1 printed immediately afterward.

Human review should focus on the uniform tail estimate in the martingale
lemma, the pair-rectangle disjointness, and the conversion from parametric
energy divergence to failure of uniform `L^2` truncation bounds.
