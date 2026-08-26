# Verification report

Status: `candidate_counterexample_likely_valid`

## Exact proof checks

- `A=diag(200^n)` is self-adjoint and bounded below by one.
- `X=.03I+.01(S+S*)` is positive, self-adjoint, and has norm at most `.05`.
- On `Dom(A)` with norm `||Au||`, conjugation gives
  `Z=AXA^(-1)=.03I+2S+.00005S*`.
- The series for `W` is bounded termwise by a geometric series with exact
  ratio `40601/400000`.
- Rouché's inequality on the unit circle puts both roots of
  `2z^2+(.03+i)z+.00005` inside the disk.  The resulting nonzero `l2`
  recurrence vector lies in `ker(Z*+i)`, so `i` is in `spec(Z)`.
- Polynomial spectral mapping then prevents `I+Z^2` from being invertible.
  The closed graph theorem transfers this to failure of domain preservation
  by `(I+X^2)^(-1)`.
- Skew symmetry of every `X^n(AX-XA)X^n` gives `W*=-W` on `Dom(A)`.
  The telescoping identity is `W+XWX=AX-XA`.
- Substitution in both block Riccati equations has been checked sign by sign.
- The inverse of `T=[[I,-X],[X,I]]` has diagonal block
  `(I+X^2)^(-1)`, so the graph-domain splitting fails.

## Deterministic script

Run from the repository root:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1307.6439_strong_riccati_not_reducing_graph/code/check_parameters.py
```

The script checks the exact rational norm bounds and series ratio, the strict
Rouché inequality, and both characteristic roots.  These numerical checks are
not a substitute for the infinite-dimensional proof.

## Reviewer focus

The highest-value independent check is the implication

```text
(I+X^2)^(-1) Dom(A) subset Dom(A)
  => I+(AXA^(-1))^2 is boundedly invertible on l2,
```

followed by the recurrence proof that `i` belongs to `spec(AXA^(-1))`.
