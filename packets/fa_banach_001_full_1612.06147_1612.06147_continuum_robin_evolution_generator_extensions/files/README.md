# Continuum many evolution-generator extensions

Status: `candidate_full_likely_valid`

Source: H. Neidhardt, A. Stephan, and V. A. Zagrebnov, *Convergence rate
estimates for Trotter product approximations of solution operators for
non-autonomous Cauchy problems*, arXiv:1612.06147, Remark 3.6(i), PDF page 14
(printed page 12).

## Result

The source asks whether a single evolution pre-generator can admit several
extensions which are evolution generators. The answer is yes, and one can get
continuum many.

Take the closed minimal Laplacian `S` on `L2(0,1)`, with domain `H^2_0(0,1)`,
and form the canonical evolution pre-generator `D0 + mathcal(S)` on
`Lp([0,T],L2(0,1))`. Every nonnegative Robin Laplacian `A_a`, `a >= 0`, extends
`S` and generates a contraction heat semigroup. Its associated evolution
generator therefore extends the same canonical pre-generator. Distinct Robin
parameters have distinct boundary-condition domains, so the corresponding
propagators and evolution generators are pairwise distinct.

This also gives continuum many solution operators for the constant equation
`u'(t)=-S u(t)` in the deliberately weak sense of Definition 3.5(ii) of the
source paper.

## Novelty boundary

The cheap run indexes had no relevant hit. Bounded exact-phrase, arXiv-id,
DOI, evolution-pre-generator, nonuniqueness, minimal-Laplacian, and Robin web
searches on 2026-08-09 returned the source question but no later resolution.
The result is mathematically elementary once the weak solution-operator
definition is read literally, so novelty confidence is conservative pending an
expert literature search.

## Files

- `solution_packet.pdf`: source question, proof intuition, theorem, proof,
  scope, novelty bounds, and references.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: real crop of source PDF page 14.
- `VERIFICATION.md`: proof audit and reviewer focus.
- `novelty_search.md`: bounded novelty-search record.
- `code/crop_source.py`: reproducible Poppler render and full-width crop.

Human review should focus on the inclusion of the full canonical domain
`dom(D0) intersection dom(mathcal(S))` in every Robin evolution generator and
on the intended weakness of Definition 3.5(ii).
