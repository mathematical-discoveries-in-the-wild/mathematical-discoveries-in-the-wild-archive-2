# Kronecker-set unitary counterexample

Status: literature-implied full negative answer.

Bayart--Matheron Example 3.6 constructs a unitary multiplication operator
`M_z` that is weakly supercyclic.  Their same construction gives positive
integers `p_k -> infinity` with `z^(p_k) -> 1` uniformly on the supporting
Kronecker set.  Hence `<M_z^(p_k) 1, 1> -> 1`, so the operator is not weakly
stable.  This directly answers the broad question in arXiv:2010.13331.

The relation is an agent-identified implication; the supporting paper predates
the source question and does not state that it is answering it.

Build from this directory with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```
