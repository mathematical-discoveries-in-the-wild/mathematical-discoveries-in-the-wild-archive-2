# A norm-increasing 4-isometry without Wold-type decomposition

Source target: Chavan--Trivedi, *Wold-type decomposition for
left-invertible weighted shifts on a rootless directed tree*,
arXiv:2501.01296.

## Result

Shimorin's question has a negative answer.  On the source's rootless
quasi-Brownian tree, take

```text
p_m(j) = 1 + a_m j + j^2,
a_2 = 1,
a_m = 2 for m != 2,
```

and use the weights of source Proposition 5.1.  The resulting bounded shift is
analytic and norm-increasing, but has no Wold-type decomposition.  Its third
defect is diagonal, vanishes off the spine, and has spine entries `-2` for
`m<=1` and `-2/m` for `m>=2`.  Those entries are transported exactly by the
spine weights, so `Delta_4=0`.  Hence the operator is a 4-isometry and an
`r`-isometry for every `r>=4`.

This fully refutes the universal `m>=3` question.  It does not settle the
separate sharper question restricted to `m=3`.

## Reproduction

From the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2501.01296_norm_increasing_four_isometry_no_wold/code/verify_four_isometry.py
```

The checker uses exact rational arithmetic, propagates all depth-four tree
paths on a large finite window, checks norm increase, verifies the closed
third-defect formula, and checks `Delta_4=0`.

Compile the packet with:

```bash
cd runs/fa_banach_001/solutions/counterexamples/2501.01296_norm_increasing_four_isometry_no_wold
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`source_paper.pdf` was compiled locally from the cached arXiv source.  The
figures are real crops of pages 2 and 16 of that PDF.

## Literature status

arXiv:2212.04446 has the exact claimed order-3 answer in its abstract, but its
current v3 metadata explicitly says it was withdrawn because the proof of the
main result has a gap.  The 2025 source says the question remains unresolved
and replaces the claimed construction by a 3-expansion of the wrong sign.
Cheap run-index, exact-phrase, and bounded arXiv searches found no prior
order-4 construction.  Novelty remains provisional pending expert review.
