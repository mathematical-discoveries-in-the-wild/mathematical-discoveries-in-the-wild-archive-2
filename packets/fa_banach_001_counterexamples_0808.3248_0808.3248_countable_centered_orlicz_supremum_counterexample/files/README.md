# A centered countable counterexample to the Orlicz-supremum question

- **Source:** E. Ostrovsky, *Support of Borelian Measures in Separable
  Banach Spaces*, arXiv:0808.3248, p. 6, question (14).
- **Model:** GPT5.6
- **Status:** `candidate_counterexample_likely_valid` — full negative answer,
  pending human review.

## Result

There are standard Orlicz functions

\[
\Phi(u)=e^{u^2}-1,\qquad \Psi(u)=e^{|u|}-1,
\]

with `Psi << Phi`, and a **centered** separable random field on a countable
index set such that

\[
\sup_t\|\theta(t)\|_{Or(\Phi)}\le 2,
\qquad
\sup_t|\theta(t)|<\infty\quad\text{a.s.},
\]

but

\[
\left\|\sup_t|\theta(t)|\right\|_{Or(\Psi)}=\infty.
\]

This disproves the source's proposed conclusion even with centering.

## Construction in one line

Give level `m` total probability `2^{-m}`, split it among
`N_m=ceil(exp(2m^4))` atoms, and attach to each atom its own centered
coordinate of amplitude `m^2`. Splitting hides every spike from any single
coordinate's `Phi` moment, while the supremum recombines all level
probabilities and has no exponential moment at any scale.

## Files

- `solution_packet.pdf` / `main.tex`: complete statement and proof.
- `source_paper.pdf`: locally compiled from the exact arXiv source download.
- `figures/open_problem_crop.png`: source p. 6 with the complete question.
- `verification_report.md`: hypothesis-by-hypothesis audit and proof checks.
- `source_0808.3248.tex.gz`, `source_metadata_0808.3248.json`: source
  provenance.

## Novelty check

Searches covered the exact title and arXiv id, verbatim fragments of the
question, and close phrases involving uniform Orlicz coordinate bounds and
random-field suprema. They found only the source and general sufficient-
condition literature, not an exact later answer. Novelty is therefore
plausible but not certified; the proof itself is elementary and independent
of the search.

## Human-review focus

Check the Luxemburg-moment estimate at scale 2 and the distinction between
coordinate probabilities `p_m` and total level probabilities `2^{-m}`. No
computational or external theorem dependency remains.
