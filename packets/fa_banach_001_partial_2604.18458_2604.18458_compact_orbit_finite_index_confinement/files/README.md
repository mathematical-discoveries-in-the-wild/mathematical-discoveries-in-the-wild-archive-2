# Compact orbit closures force finite-index descent of confinement

Status: `candidate_partial_likely_valid`

Source problem: Question 3.9 of Tattwamasi Amrutam and Yongle Jiang,
*$C^*$-simplicity, confined subalgebras, and operator algebraic uniform
recurrence*, arXiv:2604.18458.

## Result

Let \(\Gamma\) be i.c.c. and
\(\mathcal N\subseteq\mathcal M\subseteq L(\Gamma)\) have finite
Pimsner--Popa index. If the Effros--Maréchal orbit closure of \(\mathcal M\)
is compact, then confinement of \(\mathcal M\) implies confinement of
\(\mathcal N\).

More precisely, if \(\mathcal N^{g_i}\to\mathbb C\) and
\(\mathcal M^{g_i}\) has an EM cluster point \(\mathcal P\), then
\(\mathcal P\) is finite-dimensional and every nonzero projection in
\(\mathcal P\) has trace at least
\([\mathcal M:\mathcal N]^{-1}\). This forces \(\mathcal M\) itself to be
non-confined. Hence any counterexample to the source question must exhibit
genuinely noncompact escape along every sequence witnessing non-confinement of
\(\mathcal N\).

## Files

- `main.tex` / `solution_packet.pdf`: self-contained proof and scope audit.
- `source_paper.pdf`: the source arXiv PDF.
- `figures/source_question_page.png`: source page showing Question 3.9.
- `verification.md`: proof-obligation audit.
- `code/check_matrix_obstruction.py`: exact finite-matrix sanity check showing
  why bare Pimsner--Popa domination cannot prove the unrestricted problem.

## Reproduction

Run the sanity check:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2604.18458_compact_orbit_finite_index_confinement/code/check_matrix_obstruction.py
```

Compile from this directory with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

## Scope

This is not a full answer to Question 3.9. It settles compact conjugacy orbit
closures (in particular compact URAs) and identifies a necessary noncompact
escape mechanism for any counterexample. The unrestricted noncompact case
remains open.
