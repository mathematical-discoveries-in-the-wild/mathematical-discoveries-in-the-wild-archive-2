# Exact nullity thresholds for fat Cantor sets

This packet gives a full candidate answer to two open questions in Hewett and
Moiola, arXiv:1507.02698:

- positive-measure empty-interior sets with nullity threshold strictly between
  `0` and `n/p` do exist; and
- the generalized Smith--Volterra--Cantor sets from their Example 4.7 have an
  exact threshold.

For every `n>=1`, `1<p<infinity`, `0<alpha<1/2`, and
`0<beta<1-2 alpha`, the packet proves

```text
s_{G_{alpha,beta}^{(n)}}(p)
    = (1/p) (1 + log(2)/log(alpha)),
```

and proves nullity at the threshold itself.

The proof has three ingredients:

1. a level gap in every comparable ball gives the missing capacity-density
   upper bound;
2. localizing the source Swiss-cheese criterion to a deep basic interval
   removes the source's small-`beta` restriction below the threshold; and
3. a directional Bessel-potential slicing lemma transfers the exact
   one-dimensional result to every Cartesian power.

Files:

- `main.tex` — self-contained proof manuscript;
- `solution_packet.pdf` — compiled proof packet;
- `verification.md` — dependency, endpoint, and novelty audit;
- `code/check_threshold.py` — exact and high-precision arithmetic checks;
- `source_paper.pdf` — official arXiv PDF;
- `figures/open_questions_page.png` — source page containing the two questions;
- `figures/fat_cantor_question_page.png` — source page with the conjectured
  threshold and preceding partial result.

Status: `full_solution_likely_valid`; specialist review is recommended for the
directional multiplier lemma and the use of the source capacity-density
criterion at the critical exponent.
