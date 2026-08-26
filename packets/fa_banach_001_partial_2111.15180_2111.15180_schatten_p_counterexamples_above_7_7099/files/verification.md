# Verification record

The proof is exact.  Run:

```bash
conda run --no-capture-output -n sandbox python verify_counterexample.py
```

The script checks symbolically that:

- the off-diagonal matrix `N` is unitary;
- `B=N^* C N` has the stated diagonal form;
- `H` has eigenvalues `7, 5, 29/10, 29/10, 0, 0`;
- `A+B` has eigenvalues `32/5, 32/5, 5`;
- the nontrivial root lies between `7.70998` and `7.71000`.

It also evaluates the exact normalized difference on either side of the
bracket.  The analytic proof that this is the unique root above one is in
`main.tex` and uses strict convexity.

