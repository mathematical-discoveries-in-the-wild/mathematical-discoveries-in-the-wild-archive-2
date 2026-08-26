# Critical Vicsek endpoint: one-cut stability and finite-horizon loss

Status: `candidate_partial_likely_valid`.

Source: Joseph Feneuil, *Reverse inequalities for super-Riesz transforms on
graphs with a slow diffusion*, arXiv:2606.05475v2 (2026).

## Result

For every tree satisfying the source paper's Ahlfors-regularity, laziness, and
sub-Gaussian upper-bound hypotheses, the indicator of either component cut off
by one edge satisfies

```text
|Delta^gamma 1_A(x)| <= C (1 + distance(x,e))^(-beta gamma).
```

Consequently `Delta^gamma 1_A` belongs to `L^p` whenever
`p beta gamma>D`.  At the missing Vicsek exponent

```text
beta gamma*(p) = 1 + (D-1)/p,
```

this condition reduces to `p>1`.  Thus no single bottleneck cut can disprove
the critical reverse inequality; any counterexample must accumulate across
scales.

The packet also proves, for `p>=2`, a finite-horizon endpoint estimate for the
source's Lusin area functional:

```text
||L_{gamma*(p),K} f||_p
    <= C sqrt(1 + log K) ||grad f||_p.
```

Since the full area functional is equivalent to `||Delta^gamma f||_p`, this
isolates the unresolved issue to whether the harmonic loss across diffusion
scales can be removed by cancellation.

## Full-result upgrade attempt

Exact dense computations through self-similar level four and sparse
Balakrishnan computations through level six strongly favor failure away from
`p=2`.  For `p=4`, the critical reverse norms at levels 4, 5, 6 are
approximately `1.41905, 1.49025, 1.54647`; after division by
`(level+1)^(1/4)` they are `0.949, 0.952, 0.950`.  This is the predicted
multiscale law.  A fixed local witness stabilizes when embedded into larger
graphs, while re-optimization grows, confirming that the effect is genuinely
multiscale.

These computations are evidence, not proof.  The missing step for a full
counterexample is a uniform cell-block lemma converting the numerical
hierarchy into lower bounds on the infinite graph.  The source defines
"Vicsek graph" more broadly than the canonical self-similar model, so a
compact-fractal scaling argument alone would not settle the stated problem.

## Reproduction

Run the dense probe with:

```bash
conda run --no-capture-output -n sandbox python code/finite_vicsek_probe.py \
  --levels 0,1,2,3 --ps 1.5,3,4 --offset 0.06
```

Run the sparse critical optimizer with:

```bash
conda run --no-capture-output -n sandbox python code/sparse_optimizer.py \
  --level 5 --p 4 --starts 6 --iters 180 --step 0.8 --margin 10
```

The PDF packet contains the complete proofs, scope limits, and verifier notes.

