# Absolutely continuous trace formula for strongly commuting normal pairs

Status: candidate_partial_likely_valid.

Source: A. B. Aleksandrov, V. V. Peller, and D. S. Potapov, *On a
trace formula for functions of noncommuting operators*, arXiv:1901.09495,
Open Problem 2 on page 6.

## Result

Let N1,N2 be bounded normal operators which commute with one another, and
assume K=N2-N1 is trace class.  The packet proves that there are real
L1(R^2) functions v1,v2 such that, for every C^1 function f,

    Tr(f(N2)-f(N1)) = int_R2 (f_x v1 + f_y v2) dxdy.

Thus the measures nu_j=v_j dxdy are absolutely continuous, answering both
parts of the source question under the additional cross-commutation
assumption N1N2=N2N1.  Quantitatively,

    int sqrt(v1^2+v2^2) <= 3 ||N2-N1||_1

and hence ||v1||_1+||v2||_1 <= 3 sqrt(2)||N2-N1||_1.

The proof uses Fuglede's theorem to decompose the compact normal difference
into finite-dimensional reducing eigenspaces.  Each block becomes a summable
family of scalar spectral moves a -> b.  An explicit planar L1 vector field
represents each endpoint difference, with norm at most 3|b-a|; summing these
fields proves absolute continuity.

## Scope and novelty

This is a substantial solved subcase, not a solution for arbitrary normal
N1,N2.  Without cross-commutation, the missing step is equivalent in finite
dimensions to controlling the planar W1 matching distance between the two
eigenvalue multisets by ||N2-N1||_1 with a dimension-free constant.  Neither
that estimate nor an unbounded-ratio counterexample was found.

The bounded search covered the exact question, normal-operator trace formulas,
commuting self-adjoint tuples, and spectral matching in Schatten norms.  The
closest papers found were arXiv:1402.0792 (a second-order Hilbert--Schmidt
Stokes formula) and arXiv:1008.1638 (Besov/Schatten perturbation estimates).
Neither contains this first-order absolutely continuous formula.  Novelty
confidence is moderate because the strong-commutation reduction is elementary
once identified.

## Files and review focus

- main.tex: full theorem, explicit divergence construction, and proof.
- solution_packet.pdf: rendered proof packet.
- source_paper.pdf: original arXiv paper.
- figures/open_problem_crop.png: page-6 source question.
- tmp/: rendering and QA intermediates.

Human review should focus on the distributional divergence identity in Lemma
1 and the reducing-eigenspace decomposition in the theorem.  The result should
remain classified as partial unless the cross-commutation hypothesis can be
removed.

Ledger:
runs/fa_banach_001/ledger/results/1901.09495_commuting_normal_absolute_continuous_trace_formula.json.
