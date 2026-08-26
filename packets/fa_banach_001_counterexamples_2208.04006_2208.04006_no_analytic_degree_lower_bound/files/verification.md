# Verification record

Status: `candidate_counterexample_likely_valid`

## Source and target

- Source: arXiv:2208.04006v2 and Nonlinear Analysis 237 (2023), 113372.
- Exact target: the last paragraph of Section 6.2, printed page 25.
- Cheap registry/solution/attempt/proof-gap indexes: no exact hit.
- Bounded primary-source searches through 2026-08-11 found the source and
  published open-access version, but no later answer. The published version
  retains the same unnormalized lower-bound statement.

## Six-pass proof and upgrade audit

1. **Literal constant obstruction.** The function `f=1` has analytic degree
   zero, while the prescribed Cauchy weight has positive finite degree.
2. **Nonconstant upgrade.** Replaced constants by `f_delta(z)=1+delta*z` to
   prevent the result from depending on a degenerate allowed case.
3. **Uniform Remez estimate.** On `D_1`, the ratio of every relevant sup norm
   is at most `(1+delta)/(1-delta)`, so the analytic degree is at most its
   logarithm divided by `log(4)` and tends to zero.
4. **Weight invariance audit.** Varying `delta` changes `M_0` but not
   `mu_j=C*j/epsilon`; the source's degree depends on the latter and on
   `epsilon`, hence is fixed throughout the near-constant limit.
5. **Unbounded-degree upgrade.** For `epsilon_n=exp(-n)`, the starting index
   in the degree definition is `n`, so the degree is at least `n` and tends
   to infinity.
6. **Normalization and literature audit.** The source imposes no lower
   oscillation or minimal-weight condition. Exact-phrase searches located no
   later repair or answer.

## Computational check

Run:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2208.04006_no_analytic_degree_lower_bound/code/check_near_constant.py
```

The script verifies the explicit analytic-degree upper bounds and the exact
starting-index lower bound for the source degree. The proof is analytic and
does not depend on finite sampling.

Observed output on 2026-08-11:

```text
checked n=1,...,12
last epsilon: 6.14421235333e-06
last degree lower bound: 12
last analytic-degree upper bound: 5.44636963879e-11
all near-constant checks passed
```

`latexmk` compiled the four-page packet without undefined references,
overfull boxes, or final-pass LaTeX warnings. All four final pages were
rendered at 150 dpi and inspected; no clipping, overlap, broken glyphs, or
illegible evidence was found.

## Human-review focus

- Confirm that the source's phrase “in terms of” asks for a uniform positive
  lower bound depending only on `dfrak_{2mu}(epsilon)`.
- Confirm that the Cauchy conversion constant `C` is fixed independently of
  `f`, `delta`, and `epsilon`.
- Confirm that complex-valued functions are the intended objects in Section
  6.2; this is explicit in the holomorphic setup and Remark 6.1.

Under the literal printed formulation, the counterexample is decisive.
