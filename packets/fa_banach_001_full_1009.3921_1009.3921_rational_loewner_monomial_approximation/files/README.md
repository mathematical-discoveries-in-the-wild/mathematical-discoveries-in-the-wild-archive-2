# Rational Löwner Approximation of Positive Monomials

Result type: full

Status: candidate full solution, likely valid pending expert review.

Source paper:

- Jim Agler, John E. McCarthy, and N. J. Young, “Operator Monotone
  Functions and Löwner Functions of Several Variables,” arXiv:1009.3921v3
  (2013; published in *Annals of Mathematics* 176 (2012), 1783–1826).
- Question location: source pages 48--49 (PDF pages 48--49), final section,
  immediately after Example 9.8 asserting that (z1 z2)^s is operator
  monotone for 0 <= s <= 1/2; source file glob.tex, lines 247--290.
- Local source: source_paper.pdf.
- Evidence crops: figures/open_problem_context_crop.png (the exponent range)
  and figures/open_problem_crop.png (the question).

## Claimed contribution

The packet answers the source question affirmatively, in a stronger
multivariable form. If a_1,...,a_d >= 0 and their sum is at most one, then
the monomial

    x_1^(a_1) ... x_d^(a_d)

is a compact-open limit on the positive orthant of rational functions that
are globally operator monotone there. By the source paper’s local Löwner
theorem, every approximant belongs to the Löwner class.

For the original problem take d=2 and a_1=a_2=s.

The approximants are constructive. Weighted geometric means are written as
positive integrals of weighted harmonic means and the outer power is written
as a positive Stieltjes integral. Replacing both integrals by finite positive
quadrature sums gives rational operator-monotone building blocks; nested
composition preserves global operator monotonicity.

## Files

- main.tex: proof packet source.
- solution_packet.pdf: rendered proof packet.
- source_paper.pdf: original arXiv paper.
- figures/open_problem_context_crop.png: preceding source context fixing the
  range 0 <= s <= 1/2.
- figures/open_problem_crop.png: source-question crop.
- verification.md: proof audit, numerical status, and review focus.
- tmp/: LaTeX intermediates and rendered PDF QA pages.

## Novelty check

Bounded web searches on August 9, 2026 used the exact displayed monomial,
the phrases “rational functions in the Löwner class,” “operator monotone
monomial rational approximation,” and variants involving weighted geometric
and harmonic means. They found the source paper, standard operator-mean
literature, and later work on one-variable rational approximation of operator
monotone functions, but no paper explicitly answering this multivariable
question or stating the stronger monomial theorem. The run’s cheap indexes
also contained no match for arXiv:1009.3921. Because the ingredients are
classical and the argument is short, novelty confidence is moderate-to-low
pending a specialist citation search; correctness does not depend on novelty.

## Human review focus

Please check:

- that the source intended compact-open approximation on the positive quadrant;
- the implication “globally operator monotone implies Löwner class” via the
  source paper’s Theorem 8.1;
- the order reversal argument for the harmonic resolvent block;
- the recursive weighted-geometric composition and the uniform-on-compacts
  diagonalization.
