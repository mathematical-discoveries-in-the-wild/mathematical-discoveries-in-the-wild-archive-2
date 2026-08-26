# Operator-norm convergence of unscaled subdiagonal Padé approximants

Status: claimed full solution; likely valid; pending expert review.

Source: Moritz Egert and Jan Rozendaal, *Convergence of subdiagonal Padé approximations of C0-semigroups*, J. Evol. Equ. 13 (2013), 875–895, arXiv:1210.8408.

Question: Remark 4.7 (arXiv PDF p. 13) asks whether, for every bounded analytic semigroup, the subdiagonal Padé method without scaling and squaring converges strongly on the whole space and even in operator norm.

## Result

Let \(A\) be sectorial of angle \(\varphi<\pi/2\), with \(-A\) generating a bounded analytic semigroup. For each \(\nu\in(\varphi,\pi/2)\), set \(\delta_\nu=1-2\nu/\pi\). The packet proves

\[
\sup_{t\ge0}\|r_n(-tA)-e^{-tA}\|
\le C_\nu M_\nu (n+1)^{-\delta_\nu}(1+\log(n+1)).
\]

Thus the answer is affirmative in operator norm, uniformly in \(t\ge0\).

## Mechanism

1. Saff–Varga–Ni’s theorem gives the positive-ray estimate
   \(\sup_{x\ge0}|r_n(-x)-e^{-x}|\le1/(2(n+1))\).
2. The two-constants theorem transfers this to every strict sector with decay \((n+1)^{-\delta}\).
3. An exact Padé coefficient identity and Eneström–Kakeya give the tail bound \(|r_n(-z)|\le4(n+1)^2/|z|\).
4. A three-range split of the sectorial contour yields the logarithmically corrected rate.

## Files

- solution_packet.pdf: expert-facing proof packet.
- main.tex: LaTeX source.
- source_paper.pdf: original Egert–Rozendaal paper.
- supporting_paper_saff_varga_ni_1976.pdf: decisive positive-ray estimate.
- figures/open_problem_crop.png: real crop of Remark 4.7.
- code/verify_pade_endpoint.py: exact and numerical sanity checks.
- verification.md: verification record and reviewer priorities.

## Novelty check

Searches covered the exact source wording, arXiv:1210.8408 citations, the core Padé/operator-norm/analytic-semigroup phrases, Neubrander–Özer–Windsperger (2020), Gomilko–Tomilov (2024), and Batty–Gomilko–Tomilov (2025). No matching theorem for the unscaled variable sequence \([n/(n+1)]\) on arbitrary Banach-space bounded analytic semigroups was found. The broader nonanalytic bounded-semigroup endpoint is not claimed.

## Human review

Check first the Saff–Varga–Ni indexing and the polynomial-tail lemma. If those pass, the remaining two-constants and sectorial-calculus steps are standard.
