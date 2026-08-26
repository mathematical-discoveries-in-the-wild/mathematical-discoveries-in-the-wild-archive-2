# Hermitian and Toeplitz Form-Matrix Coercivity

status: full_solution_likely_valid

source_arxiv: 0807.2362

source_paper: Stefano Cardanobile, *Diffusion systems and heat equations on
networks* (2008), Section 1.3 discussion, printed page 49 (PDF page 60)

## Original Question

The source asks whether arguments for scalar-valued structured matrices can be
translated to matrices of sesquilinear forms, explicitly naming symmetric and
Toeplitz matrices.

## Claimed Full Answer

Yes. The packet gives two exact translations.

1. For a bounded Hermitian two-by-two form matrix, coercivity is equivalent to
   coercivity of one diagonal block and of its Schur complement. Recursive
   elimination gives the finite Hermitian block analogue of Sylvester/Schur
   criteria.
2. Let `K` be any complex Hilbert space and let `(B_k)_{k in Z}` be bounded
   operators on `K` with `sum ||B_k|| < infinity`. For the bilateral or
   one-sided Toeplitz form with entries `B_{m-n}`, put
   `F(theta)=sum B_k exp(i k theta)` and
   `G(theta)=(F(theta)+F(theta)^*)/2`. Its optimal coercivity constant is

   ```text
   min_theta inf_{||x||=1} <G(theta)x,x>.
   ```

   Hence the form is coercive exactly when its Hermitian symbol is uniformly
   positive. This includes every finite-band operator-valued Toeplitz form and
   does not require finite-dimensional coefficient spaces.

The Schur proof is an exact bounded congruence factorization. The Toeplitz
proof uses Fourier multiplication for sufficiency and normalized Hardy
reproducing kernels (Poisson kernels) for necessity, including the one-sided
boundary case.

## Source Correction Found During The Solve

The source's Proposition 17 is false as written. On `V_1=V_2=C`, take both
diagonal forms to be the identity and both off-diagonal forms to be zero. The
full form is coercive with constant one, while condition (1.22) fails after
setting the second coordinate to zero. This is recorded separately under
`proof_gaps/0807.2362_false_two_by_two_coercivity_criterion/` and is not used
as evidence for the positive theorem.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered review packet.
- `verifier_report.md`: adversarial verification report.
- `code/check_coercivity.py`: finite-dimensional checks of the Schur identity,
  Toeplitz lower edge, and the Proposition 17 counterexample.
- `source_paper.pdf`: original source.
- `figures/open_problem_crop.png`: source-question crop.

## Novelty Check

Bounded searches on 2026-08-09 covered the exact source wording and the terms
`operator-valued Toeplitz coercivity symbol`, `Toeplitz sesquilinear forms
coercive`, and `block operator matrix Schur complement coercivity`, in the run
indexes and arXiv-focused web search. No later paper explicitly claiming to
answer Cardanobile's question was found. The proof uses classical Fourier,
Poisson-kernel, and Schur-complement mechanisms, so priority or broad novelty
is not claimed; the contribution is the explicit self-contained translation
and exact optimal constant answering the source question.

## Human Review Recommendation

Send to human review as a full positive answer to the question as worded.
Check the Hardy-kernel necessity argument, the indexing convention
`B_{m-n}`, and whether the intended historical scope demanded Toeplitz arrays
beyond the natural `ell_1` coefficient/Wiener class.
