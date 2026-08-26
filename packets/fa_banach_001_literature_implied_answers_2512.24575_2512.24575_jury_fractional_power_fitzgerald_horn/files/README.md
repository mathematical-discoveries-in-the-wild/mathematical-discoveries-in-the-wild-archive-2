# Jury fractional powers from FitzGerald--Horn

Status: `literature_implied_answer (full resolution)`

Source: Javad Mashreghi, Mostafa Nasri, and Prateek Kumar Vishwakarma,
*Functional Calculi, Positivity, and Convolution of Matrices*,
arXiv:2512.24575, Question 8.2 on page 36.

Supporting theorem: Dominique Guillot, Apoorva Khare, and Bala Rajaratnam,
*Complete characterization of Hadamard powers preserving Loewner positivity,
monotonicity, and convexity*, arXiv:1311.1581, Theorem 2.1 on page 5,
restating the FitzGerald--Horn theorem.

## Result

Question 8.2 has an affirmative answer. If $N\ge3$, $A=(a_{mn})$ is
positive semidefinite with entries in $I=(0,\rho)$, and
$\alpha>N-2$, then

\[
 \mathcal B(\alpha,A)_{ij}
 =\left.\partial_x^i\partial_y^j
 \left(\sum_{m,n=0}^{N-1}a_{mn}x^my^n\right)^\alpha
 \right|_{x=y=0}
\]

defines a positive semidefinite (N\times N) matrix. Together with the
necessity already proved in the source paper, this gives the exact
classification

\[
 x^\alpha\text{ preserves Jury positivity on }\mathbb P_N(I)
 \quad\Longleftrightarrow\quad
 \alpha\in\mathbb Z_{\ge0}\cup[N-2,\infty).
\]

No part of the fractional-power classification remains open.

## Identification

Let

\[
 F_A(x,y)=\sum_{m,n=0}^{N-1}a_{mn}x^my^n
          =v(x)^TAv(y),
 \qquad v(x)=(1,x,\ldots,x^{N-1})^T.
\]

For $h>0$, sample at $0,h,\ldots,(N-1)h$. The matrix

\[
 C_h=(F_A(ph,qh))_{p,q}=V_hAV_h^T
\]

is positive semidefinite and has positive entries. FitzGerald--Horn therefore
implies $C_h^{\circ\alpha}\succeq0$ for $\alpha\ge N-2$. Congruence by
the lower-triangular forward-difference matrix preserves positivity, and as
$h\downarrow0$ the resulting matrix converges entrywise to
$\mathcal B(\alpha,A)$. The positive cone is closed, so
$\mathcal B(\alpha,A)\succeq0$.

The supporting authors could not have known they were answering the 2025
question. The relation is an agent-identified implication of their statement
of the 1977 FitzGerald--Horn theorem, hence the conservative
`literature_implied_answers` provenance rather than `full/`.

## Verification and search bounds

- `main.tex` gives the general finite-difference transfer lemma and complete
  proof.
- `solution_packet.pdf` is the rendered review note.
- `source_paper.pdf` contains Question 8.2.
- `supporting_paper_1311.1581.pdf` contains the decisive Theorem 2.1.
- `figures/` contains readable crops of both statements.
- `code/verify_numeric.py` computes the derivative matrices by truncated
  bivariate series. The exploratory run tested 390,000 random positive-entry
  Gram matrices for $N=3,4$ and eight exponents above the threshold; no
  violation beyond floating-point roundoff was found. This is not the proof.

The bounded literature check covered the run indexes, the current arXiv and
journal versions of arXiv:2512.24575, arXiv:1311.1581, the 1977 theorem
metadata, later Jury-product papers arXiv:2602.21056 and 2607.13251, and exact
or close searches for the Question 8.2 formula and Jury fractional powers. No
paper recording this precise transfer was located. That absence is not a
novelty guarantee.

Human review recommendation: **accept as a likely-valid full-scope
literature-implied answer**. Check the orientation of the finite-difference
congruence and the application of the dimension-$N$ FitzGerald--Horn
threshold.
