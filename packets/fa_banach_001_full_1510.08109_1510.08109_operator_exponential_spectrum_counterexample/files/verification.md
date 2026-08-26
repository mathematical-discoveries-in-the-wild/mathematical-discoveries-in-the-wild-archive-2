# Verification report

Status: candidate full result, likely valid pending human review.

## Mathematical audit

- Exact scope: the proof answers Question 4.2, not the adjacent universal
  torsion Question 4.1.
- Motakis input: Proposition 4.1 gives bounded diagonal lifts for every
  Lipschitz scalar function; Section 4.2 states that the lift is a unital
  algebra homomorphism on `Lip(K)`; Proposition 4.3 and Corollary 5.3 identify
  its Calkin class with the corresponding function and make the quotient map
  an isomorphism.
- Matrix quotient: for the finite direct sum `E=X direct-sum X`, every
  bounded operator and every compact operator has a two-by-two block matrix,
  and a block operator is compact exactly when all four entries are compact.
  Therefore `Cal(E)=M_2(Cal(X))` canonically.
- Multiplicativity: on the dense basis span,
  `D_f D_g d_gamma=f(kappa(gamma))g(kappa(gamma))d_gamma`; boundedness extends
  this equality to all of `X`. Finite matrix multiplication therefore gives
  `J(FG)=J(F)J(G)` exactly.
- Regularity: the Klaja-Ransford entries are restrictions of smooth functions
  to the compact smooth sphere, with denominator `1+it` bounded away from
  zero. Thus `a,b,c`, and `c^{-1}` have Lipschitz entries. The last fact also
  independently verifies that `J(c)` is invertible.
- Hard product: a product of operator exponentials remains a product of
  exponentials under every unital homomorphism. Hence the nontrivial Calkin
  component of `J(c)` proves `J(c)` is not in `Exp(B(E))`.
- Easy product: for real `t`,
  `(1-it)/(1+it)=exp(-2i arctan(t))`, so
  `-((1-it)/(1+it))^2=exp(i(pi-4 arctan(t)))`. The displayed logarithm is
  Lipschitz, and exponentiating its diagonal lift gives the reversed product
  exactly on every basis vector.
- Spectral scaling: `(1/2)I` is a single exponential. Since `Exp(B(E))` is a
  subgroup, multiplication by this scalar preserves whether an invertible
  element belongs to `Exp(B(E))`.
- Separability: Motakis's space has a Schauder basis; hence `X` and
  `E=X direct-sum X` are separable.

No numerical computation is needed for the proof.

## Novelty audit

The bounded search on 2026-08-13 and 2026-08-17 covered:

- the run's registry, solution, attempt, and proof-gap indexes;
- the local arXiv corpus for `1510.08109`, the exact title, Question 4.2,
  operator exponential spectrum, Calkin realizations, and the
  Klaja-Ransford/Motakis author combination;
- exact web searches for the question text and combinations of
  `C(S^4,M_2)`, Calkin algebra, and exponential spectrum;
- a citation-list query for the Klaja-Ransford paper.

The only directly relevant later publication found was Daniel-Ghosh (2025),
which proves commutativity for `B(ell^p direct-sum ell^q)` and a one-way
Calkin-to-operator implication. Its abstract and reference list do not state
this existence result or cite Motakis. Motakis's source contains no occurrence
of Klaja, Ransford, or exponential spectrum. Novelty confidence is moderate.

## Artifact audit

- `solution_packet.pdf` was compiled from `main.tex` with `latexmk` in two
  passes.  The final log contains no warnings, overfull or underfull boxes,
  or undefined references.
- The PDF has four US-letter pages and is 378,053 bytes.  All four pages were
  rendered to PNG with Poppler and inspected at original detail; no clipping,
  overlap, illegible text, or defective page break was found.
- The crop on page 1 was checked against page 7 of the source paper.  The
  source theorem and formulas were checked against pages 2--4 of
  Klaja--Ransford, and the lift and quotient inputs were checked against pages
  20--25 of Motakis.
- SHA-256 `solution_packet.pdf`:
  `83b6db22ede836504a36d22a4175236eb2b0a172b6edf8e34bf2d77624621d2f`.
- SHA-256 `source_paper.pdf`:
  `00d81fac40c1ab0124c25c30db6581efb44a4830475a3490fa26a4178636505c`.
- SHA-256 `supporting_paper_2110.10868.pdf`:
  `8900f171070c7c849668fbd31f5842ab24ec78e150d1867ba74b426ba76e3923`.
- SHA-256 `figures/open_problem_crop.png`:
  `869bc3c30d9eec73a0f70136c6f1bae23b068ea40c81449bed7a09518b2ea653`.
- SHA-256 `main.tex`:
  `92142f99035094990a3b020944f14227c195282ff6efa7d1833206d0e002c5f1`.

## Human review recommendation

Check the canonical identification `Cal(X direct-sum X)=M_2(Cal(X))`, the
orientation of the products `ST` versus `TS`, and the explicit logarithm
`g(t)=i(pi-4 arctan(t))`. These are the only non-black-box transitions beyond
the two cited papers.
