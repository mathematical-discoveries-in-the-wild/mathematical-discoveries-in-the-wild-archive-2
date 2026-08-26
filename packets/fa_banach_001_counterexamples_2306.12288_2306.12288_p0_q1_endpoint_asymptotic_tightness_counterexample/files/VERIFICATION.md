# Verification report

Verdict: `likely valid candidate counterexample`.

## Claim checked

For the binary Bonami--Beckner product semigroup, the source theorem's
explicit endpoint `(p,q)=(0,1)` has

```text
Xi_{0,1}^{(n)}(alpha)=+infinity
```

for every `n>=1` and `0<alpha<ln 2`, while the source's proposed limiting
quantity `Xi_1(alpha)` is finite.

## Independent proof audit

1. Theorem 2 of arXiv:2306.12288v2 quantifies over `p>=0,q>=1`, so the
   endpoint is genuinely inside the printed claim.
2. The source definition gives
   `Ent_{0,1}(f)=-ln(pi^n(f>0))`.  A positive entropy constraint therefore
   forces the support of every feasible nonzero `f` to be proper.
3. Every nonempty proper subset of the connected cube has a boundary edge.
   On an edge with values `a>0` and `0`, epsilon regularization contributes a
   positive multiple of `(a-epsilon)(ln(a)-ln(epsilon))`, which diverges.
   Every other symmetrized edge summand is nonnegative.
4. If the endpoint domain is restricted to strictly positive functions, the
   feasible set is empty at positive `alpha`; its infimum is again
   `+infinity`.  Thus the conclusion does not depend on the endpoint-domain
   convention.
5. The displayed binary formula is finite for `0<alpha<ln 2`, because its
   inverse-entropy parameter lies strictly between `0` and `1/2`.
6. Fact 1 in the source proof is not continuous on the closed simplex at
   `q=1`; the packet's binary family exhibits the divergence directly.

No missing sign, normalization, or support case was found.  The result is a
counterexample only to asymptotic tightness at the printed endpoint; it does
not challenge the lower bound or the `q>1` regime.

## Computation rerun

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2306.12288_p0_q1_endpoint_asymptotic_tightness_counterexample/code/verify_endpoint.py
```

The rerun enumerated all nonempty proper supports through `Q_4` (65,534 at
`n=4`), confirmed finite values of `Xi_1` at three interior parameters, and
confirmed monotone regularized divergence at `q=1` and at three values below
one.  These checks support but do not replace the proof.

## Artifact QA

`main.tex` compiles without errors into a four-page PDF.  All four pages were
rendered to PNG and visually inspected on 2026-08-21.  The theorem, formulas,
source crops, proof-failure crop, references, and page transitions are
readable; no clipping, overlap, missing glyphs, or placeholder text was found.
