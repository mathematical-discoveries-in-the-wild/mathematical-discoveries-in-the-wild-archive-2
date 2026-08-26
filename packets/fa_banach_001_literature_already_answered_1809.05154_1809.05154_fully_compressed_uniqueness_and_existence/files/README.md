# Fully compressed tuples: uniqueness and existence — literature answer

This packet matches Questions 4.8 and 4.9 in the arXiv version of
Passer--Shalit, *Compressions of compact tuples* (arXiv:1809.05154), to the
explicit answers in Davidson--Passer, *Strongly peaking representations and
compressions of operator systems* (arXiv:2005.11582).

- Corollary 2.13 gives an affirmative answer to the uniqueness question.
- Corollary 3.6 gives the necessary-and-sufficient existence criterion through
  the abstract operator system associated to a matrix convex set.

The later paper explicitly identifies both source questions. Its citation of
the second as “Question 4.19” refers to the journal numbering (or is a minor
numbering discrepancy); the wording and subject match Question 4.9 on page 15
of the official arXiv PDF.

Build with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

