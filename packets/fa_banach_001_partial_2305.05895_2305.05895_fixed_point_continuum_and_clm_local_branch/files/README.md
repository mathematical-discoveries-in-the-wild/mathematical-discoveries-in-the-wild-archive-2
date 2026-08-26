# Fixed-point continuum and local CLM profile branch

This packet gives two rigorous partial advances on Conjecture 3.12 of
arXiv:2305.05895.

1. On every compact parameter interval, the fixed-point graph contains a
   compact connected component projecting onto the whole interval.  On
   `[0,1]` it joins the unique profiles at `a=0` and `a=1`.  Every possible
   fixed-point selection is continuous at those two unique anchors.
2. The exact `a=0` spectrum from arXiv:2607.19762, after fixing spatial
   scale, gives a locally unique real-analytic branch of strongly regular
   normalized self-similar profiles by the implicit-function theorem.

The result is partial: a connected continuum need not have a continuous
section, and strong local uniqueness does not exclude other fixed points
that are close only in the source paper's weak weighted topology.  The
pointwise parameter-monotonicity conjecture remains open.

Build with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -jobname=solution_packet main.tex
```
