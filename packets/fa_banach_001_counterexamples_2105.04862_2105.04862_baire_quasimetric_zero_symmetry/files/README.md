# Counterexample packet: a Baire quasi-metric space with zero symmetry index

status: counterexample_likely_valid

source_arxiv: 2105.04862

source_problem: Open Questions 1 and 2 of Mohammed Bachir, *Asymmetric Normed Baire Space* (Results in Mathematics 76 (2021), article 176; arXiv:2105.04862v2).

counterexample: On \(X=\mathbb R\), set
\[
 d(x,y)=(y-x)_+ + (e^{-y}-e^{-x})_+.
\]

## Summary

This packet gives negative answers to both open questions. The displayed \(d\) is a quasi-metric because it is the sum of the two directed potential quasi-metrics associated with the functions \(t\mapsto t\) and \(t\mapsto e^{-t}\). Its forward topology is exactly the usual Euclidean topology on \(\mathbb R\), so \((\mathbb R,d)\) is Baire. In fact,
\[
 d_s(x,y)=\max\{|x-y|,|e^{-x}-e^{-y}|\}
\]
is complete, so the example is bicomplete.

Nevertheless, for \(x_n=n+1\) and \(y_n=n\),
\[
 \frac{d(x_n,y_n)}{d(y_n,x_n)}
 =(1-e^{-1})e^{-n}\longrightarrow 0,
\]
and hence \(c(X)=0\). This directly disproves the implication proposed in Open Question 1. Theorem 3 of the source paper then gives that the semi-Lipschitz free space \(\mathcal F_a(X)\) is not Baire, although \(X\) is Baire, which also answers Open Question 2 negatively.

The example is not induced by an asymmetric norm: its directional distortion varies with position, and \(d\) is not translation invariant. Thus it does not conflict with the source theorem for asymmetric normed spaces.

## Evidence

- `source_paper.pdf`: the original paper, arXiv:2105.04862v2.
- `figures/open_question_1_crop.png`: Open Question 1 and its bicomplete context on PDF page 6.
- `figures/open_question_2_crop.png`: source Theorem 3, Proposition 3, and Open Question 2 on PDF page 8.
- `main.tex`: complete proof and review notes.
- `solution_packet.pdf`: rendered proof packet.
- `code/check_counterexample.py`: finite numerical sanity checks for the formulas used in the proof.

## Novelty Check

A bounded check on 2026-08-09 found no hit for arXiv:2105.04862 or the core terms in the run's registry, solution, attempt, and proof-gap indexes. Web searches for the exact title and DOI, `"Open question 1"`, `"c(X)=0" Baire quasi-metric`, `"index of symmetry" quasi-metric Baire`, and `"semi-Lipschitz free space" Baire found the source paper, bibliographic mirrors, and later papers citing it for background, but no later paper claiming to answer either question. This supports only bounded novelty confidence; it is not an exhaustive citation review.

## Human Review Recommendation

Likely valid and suitable for promotion as a counterexample. Verify especially (i) the orientation in the definition \(c(X)=\inf d(x,y)/d(y,x)\), (ii) the two inclusions between the forward \(d\)-topology and the Euclidean topology, and (iii) the application of source Theorem 3 to Open Question 2. The proof is elementary and has no unproved dependency.
