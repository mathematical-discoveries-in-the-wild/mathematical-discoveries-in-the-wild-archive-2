# No Stepanov almost periodicity in variation

This packet gives a candidate full negative answer to the question in
Example 3.3 of arXiv:2205.09031 for every `1 <= p < infinity`.

The key general lemma says that if the `L^p([0,1])` Bochner transform of a
`C^1` scalar function is almost periodic in variation, then its derivative
is Stepanov-1 almost periodic and hence Stepanov-1 bounded.  For the source's
function

`f(t) = sin(1 / (2 + cos(t) + cos(sqrt(2)t)))`,

irrational recurrence produces increasingly deep strictly convex wells of
the denominator.  A monotone change of variables on one side of each well
shows that the local `L^1` norm of `f'` is unbounded.  This contradicts the
general lemma.

Files:

- `solution_packet.pdf` — self-contained proof packet.
- `main.tex` — LaTeX source.
- `source_paper.pdf` — arXiv:2205.09031v1.
- `figures/open_question_crop.png` — exact source question.
- `VERIFIER_REPORT.md` — mathematical, source, novelty, and render checks.
