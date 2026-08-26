# Candidate full counterexample: negative-p normalized moments

**Status:** candidate full counterexample, likely valid; human review requested.

Jie Xiao's Remark 2.2 in arXiv:0708.2644 conjectures that the normalized
moment monotonicity of Theorem 2.1(i) extends to a lower exponent in
`(-1,0)`.  This packet disproves that extension at `c=1` with an explicit
positive `C^1` function `X` satisfying both differential hypotheses.

The proof is analytic.  The included Python script only checks illustrative
values.  Build with

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

and run the QA check with

```sh
conda run --no-capture-output -n sandbox python code/check_counterexample.py
```

The main review focus is the Stieltjes integration identity and the endpoint
limit as `p` tends to `-1` from above.
