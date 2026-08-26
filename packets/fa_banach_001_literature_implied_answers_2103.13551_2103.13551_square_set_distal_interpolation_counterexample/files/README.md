# 2103.13551 — A sublacunary distal interpolation set

Status: `literature_implied_answer` (full negative answer to Question 6.4).

Anh N. Le asks whether no sublacunary set can be an interpolation set for
distal sequences.  The answer is no.  Pavlov's 2008 Corollary 5.1, as
formulated explicitly in the 2024 follow-up by Koutsogiannis, Le, Moreira,
Pavlov, and Richter, says that an increasing set `S={s_n}` is a distal
interpolation set whenever

    limsup log(s_{n+1}) / log(s_{n+1}-s_n) < infinity.

Taking `s_n=n^2` gives a counterexample: the displayed ratio tends to `2`,
whereas

    log(s_n)/n = 2 log(n)/n -> 0,

so the square set is sublacunary.

The 2024 follow-up also confirms that the target's other two genuine
questions survive: finite-union stability for distal interpolation sets is
still open, and the strict hierarchy between `k`- and `(k+1)`-step
interpolation remains open for `k>=2`.

## Files

- `main.tex`, `solution_packet.pdf` — identification, proof, and status note.
- `source_paper.pdf` — arXiv:2103.13551.
- `supporting_paper_pavlov_2008.pdf` — primary 2008 construction.
- `supporting_paper_2401.15339.pdf` — later paper explicitly stating the
  distal interpolation criterion and current open status.
- `figures/open_problem_crop.png` — exact source Questions 6.3 and 6.4.
- `tmp/` — build and render artifacts.

## Classification

This is literature-implied rather than a new counterexample.  Pavlov's result
predates the 2021 question, but is phrased as an arbitrary-value realization
theorem for skew products.  The later paper, coauthored by Le and Pavlov,
states the exact interpolation-set consequence; substituting `s_n=n^2`
makes the negative answer immediate.

