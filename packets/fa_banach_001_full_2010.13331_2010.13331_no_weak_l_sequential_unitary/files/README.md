# No weakly l-sequentially supercyclic unitary

Status: candidate full result, likely valid, subject to expert review.

This packet proves that no unitary on a Hilbert space of dimension greater
than one is weakly l-sequentially supercyclic.  Consequently, every weakly
l-sequentially supercyclic contraction on an infinite-dimensional Hilbert
space is weakly stable.  This answers the strengthened Hilbert-space question
in Section 4 of arXiv:2010.13331.

The proof uses the cyclic spectral model.  Any weakly convergent sequence from
one projective unitary orbit is uniformly bounded in its scalar multipliers,
so its spectral-model limit is essentially bounded.  Infinite-dimensional
L2 contains unbounded functions, preventing direct weak sequential density.

The result conflicts with repeated later descriptions of the 2006
Bayart--Matheron Kronecker-set example as weakly l-sequentially supercyclic.
That construction establishes weak density, but its weak neighbourhood
approximants need not be norm bounded.  Independent review of this distinction
is the main recommendation.

Build from this directory with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```
