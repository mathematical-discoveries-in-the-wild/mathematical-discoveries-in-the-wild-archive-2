# Spectral-Synthesis-Free Katznelson--Tzafriri Theorem for Measures

Status: **candidate full result, likely valid; human review requested**

Source paper: David Seifert, *A Katznelson--Tzafriri theorem for measures*,
arXiv:1410.1301; *Integral Equations and Operator Theory* 81 (2015),
255--270.

Source question: Remark 1.3, p. 2 asks whether spectral synthesis can be
dropped from the Hilbert-space measure theorem (Theorem 1.2).

## Result

The answer is affirmative. Let \(T\) be a bounded \(C_0\)-semigroup on a
complex Hilbert space with generator \(A\). Assume that, for some \(R>0\),

\[
 \{is:|s|\ge R\}\subset\rho(A),\qquad
 \sup_{|s|\ge R}\|R(is,A)\|<\infty.
\]

If μ is any finite complex Borel measure on \(\mathbb R_+\) whose Fourier
transform vanishes on \(i\sigma(A)\cap\mathbb R\), then

\[
 \|T(t)\widehat\mu(T)\|\longrightarrow0.
\]

No spectral-synthesis hypothesis is needed.

## Proof Map

1. The high-frequency resolvent condition gives negative critical growth
   bound on Hilbert space. This makes \(T\) uniformly norm-continuous at
   infinity.
2. If operator-norm decay failed, take almost-norming vectors at times
   \(t_n\to\infty\), smooth the vectors by one fixed \(L^1\) bump, and pass
   them to the continuous part of a Hilbert ultrapower.
3. Tail norm-continuity ensures that the resulting measure-calculus vector
   has an orbit bounded away from zero.
4. The standard unitary asymptote has spectrum inside the original boundary
   spectrum. The spectral theorem annihilates the same vector because
   \(\widehat\mu\) vanishes there, forcing its orbit to decay: a contradiction.

The \(L^1\) smoothing is placed on the **vectors**, not on μ. This is the
point that avoids the false variation-norm approximation of a singular
measure.

## Packet Contents

- solution_packet.pdf: typeset full proof and review packet.
- main.tex: self-contained LaTeX source.
- source_paper.pdf: the original arXiv paper.
- supporting_paper_1410.1294.pdf: Seifert's companion Hilbert-space
  \(L^1\) theorem and unitary-asymptote construction.
- figures/open_problem_crop.png: full-width crop of Theorem 1.2 and
  Remark 1.3 from source p. 2.
- VERIFICATION.md: adversarial proof verification.
- tmp/: build and rendering intermediates.

No computation is used in the proof.

## Novelty Check

On 9 August 2026, bounded web/arXiv searches used the exact sentence from
Remark 1.3, the title, author, arXiv id, and combinations of “bounded Borel
measure,” “Hilbert,” “spectral synthesis,” and “Katznelson--Tzafriri.” They
found the source paper, the companion arXiv:1410.1294, the Batty--Chill--Tomilov
paper, and the 2022 Batty--Seifert survey, but no later work claiming to remove
spectral synthesis from this measure theorem. This is not a comprehensive
priority search.

## Human Review Recommendation

Review especially:

1. the critical-growth-to-tail-uniform-continuity lemma;
2. the definition of the continuous ultrapower subspace and its spectrum
   inclusion;
3. why the measure integral passes through the ultrapower on the smoothed
   vector;
4. the Fourier-sign identification between the unitary spectrum and
   \(i\sigma(A)\cap\mathbb R\).

