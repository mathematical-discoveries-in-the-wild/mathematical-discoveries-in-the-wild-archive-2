# Verification record

## Mathematical checks

- Re-read the source's Open Problem 1, Theorems 1.2 and 5.4, canonical-radius lemma, Remark 6, and the complete Xia-symbol proof.
- Verified that comparability of positive weights preserves `A_p` membership.
- Proved the planar regularized-power criterion `(1+|z|)^gamma in A_p` iff `-2<gamma<2(p-1)` by centered-disk necessity and a near/far disk sufficiency split.
- Solved the inequalities separately for `m<=2` and `m>2`.
- Checked that `p_-=2m/(m+2)` and `p_+=2m/(m-2)` are conjugate and that the two `A_p` equalities occur at those endpoints.
- Recomputed the Xia tail directly: `rho^{-2} MO(f)^p dA ~ rho^(p-2) |z|^(-2p) dA`. Its polar exponent equals `-1` at `p=p_-`, so the endpoint divergence is logarithmic.
- Used Theorem 1.2 only for the one-sided membership of `H_f`, and Theorem 5.4 contrapositively only after showing the IMO integral diverges.
- Kept the range `p>=p_+` for `m>2` explicitly unresolved.

## Reproducible algebra

Run:

```sh
conda run --no-capture-output -n sandbox python code/verify_thresholds.py
```

The script uses exact rational arithmetic, checks four representative values `m>2`, checks both endpoint identities and the Xia exponent, and samples the all-`p` range for `m<=2`.

## Literature check

Bounded arXiv/web searches through 2026-08-12 covered the exact title, doubling Fock Schatten Berger–Coburn terms, Muckenhoupt/Beurling terms, and later citing material. Located items were the published source, a thesis reproducing the result, adjacent generalized/standard Fock results, and unrelated later work. No later paper answering the `1<p<infinity` doubling-Fock question was found. This is a bounded novelty check, not a claim of exhaustive bibliographic coverage.

## Artifact checks

- Official source PDF retained as `source_paper.pdf`.
- LaTeX compiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
- PDF metadata and text extraction checked.
- Every rendered page inspected for clipping, overlap, missing glyphs, and formula overflow.
