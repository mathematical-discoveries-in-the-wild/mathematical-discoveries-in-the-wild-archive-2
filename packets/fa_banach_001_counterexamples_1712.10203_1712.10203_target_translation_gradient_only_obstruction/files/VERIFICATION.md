# Verification audit

## Mathematical audit

1. **Admissible setting.**  For any `k>=2`, the choice
   `N=S^{k-1} subset R^k`, `d=m=k`, and `Omega=B_1` satisfies the source
   hypotheses.  Both affine maps are smooth, bounded, and belong to the
   domain of the operator.
2. **Zero gradient difference.**  Both derivatives equal the identity
   matrix pointwise.  Every homogeneous or inhomogeneous Sobolev norm of
   their gradient difference is therefore zero.
3. **Singular chains.**  In the source's sphere specialization the
   exceptional complex is `{0}` and the smooth construction is the signed
   zero-dimensional preimage chain.  Hence `S_y(u_0)` has its unique unit
   point at `y` for `y in B_1`, while `S_y(u_1)` has its unique unit point
   at `y-c` for `y in c+B_1`, up to one common orientation sign.
4. **Disjointness.**  `|c|=3>2`, so the two range balls are disjoint.  For
   every `y in B_{1/2}`, the chain difference is a single unit point at
   `y` up to sign.
5. **Positive relative flat norm.**  Test the relative-flat decomposition
   against the compactly supported 1-Lipschitz cutoff
   `phi(x)=min(1/4,(3/4-|x|)_+)`.  It equals `1/4` on `B_{1/2}`, while
   both its sup norm and Lipschitz constant are at most one.  Smooth
   approximation gives `F_Omega([y])>=1/4` for `y in B_{1/2}`.
   Integration gives the asserted positive lower bound.
6. **Logical scope.**  The pair refutes every estimate depending only on
   Sobolev norms of the gradient difference whose right-hand side vanishes
   when those norms vanish.  It does not refute estimates containing
   `||u_1-u_0||`, nor estimates under a fixed target-translation
   normalization.

No gap was found in a second pass through the source definitions of the
smooth chain, the sphere specialization, and the relative quotient norm.

## Reproduction commands

From the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1712.10203_target_translation_gradient_only_obstruction/code/verify_translation_obstruction.py

cd runs/fa_banach_001/solutions/counterexamples/1712.10203_target_translation_gradient_only_obstruction
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp main.tex
```

The checker is only a sanity check; the packet contains the proof for all
dimensions `k>=2`.

## Final artifact audit

- Sanity cases passed for `k=2,3,5,8`.
- LaTeX compiled twice with no warnings, undefined references, overfull
  boxes, or underfull boxes.
- All three rendered letter-size pages and the source crop were visually
  inspected.
- `solution_packet.pdf` SHA-256:
  `4df8065a9b9916489999e727cbc01123662686acfc36bf17ba94b8b99ff33927`.
