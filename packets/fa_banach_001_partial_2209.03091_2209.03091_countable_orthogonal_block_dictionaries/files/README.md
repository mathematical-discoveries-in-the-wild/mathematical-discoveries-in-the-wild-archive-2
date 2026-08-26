# Countable orthogonal-block greedy convergence

## Classification

- Status: `substantial_partial_result_likely_valid`.
- Source: Oliaro--Tomatis--Valiullin--Valiullin, *Greedy expansions with
  prescribed coefficients in Hilbert spaces for special classes of
  dictionaries*, arXiv:2209.03091, Section 5.
- Model: GPT5.6.

## Result

Let `H` be a countable orthogonal sum of Hilbert spaces `H_j`. If each block
has a symmetric dictionary `D_j` whose maxima are attained and whose local
support function satisfies

```text
rho_j(x) >= alpha ||x||
```

with one `alpha>0` independent of `j`, then the union dictionary has exact
greedy convergence for every positive sequence `c_n -> 0` with divergent
sum.

Consequently, an orthonormal basis can be augmented by arbitrary closed sets
of atoms in infinitely many disjoint finite coordinate blocks, provided the
block sizes are uniformly bounded. This strictly extends the source result,
which confines all added atoms to one fixed finite coordinate set.

## Main mechanism

At the first time the global dictionary support drops below the `N`th initial
block support, the tail blocks are untouched and the head is uniformly small.
The resulting bound tends to zero because decreasing `ell_2` sequences obey
`N*s_N^2 -> 0`. A new exact-greedy lemma then upgrades liminf decay to full
convergence using monotonicity of `||r_n||^2-rho_D(r_n)^2`.

## Files

- `main.tex`, `solution_packet.pdf`: theorem and self-contained proof.
- `source_paper.pdf`: arXiv source.
- `figures/open_question_crop.png`: exact conclusion question.
- `novelty.md`, `verification_report.md`: bounded search and proof audit.

## Remaining scope

The full characterization remains open, including general Riesz-basis
dictionaries, atoms coupling different blocks, and nonuniform local widths.
