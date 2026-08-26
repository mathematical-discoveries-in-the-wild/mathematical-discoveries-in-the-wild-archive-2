# Finite-index obstruction and finite-block erasure

Result type: `partial`

Status: candidate substantial reduction, likely valid pending expert review.
The general problem remains open.

Source paper:

- E. V. Tokarev, “On Banach spaces with the Tsirelson property,”
  arXiv:math/0206181.
- Open-question location: Problem 1, source PDF page 8.
- `source_paper.pdf` is reconstructed from the cached arXiv TeX source.
- `figures/open_problem_crop.png` is the exact source crop.

## Claimed contribution

Two obstructions materially narrow the search for a finite-equivalence class
whose common classical-subspace spectrum is infinite.

1. No finite exponent can lie in the divisibility index of a positive
   example. If finite `p in Index(X^f)`, the source's saturation theorem produces a
   `p`-saturated representative. Such a representative cannot contain
   `ell_q` for `q!=p`, so the common intersection has size at most one.
2. The obvious repeated countable sum fails. For distinct `q_n!=2`,

   `X=(sum_(n,k) ell_(q_n))_2`

   is finitely equivalent to the finite-block space

   `Z=(sum_(n,k,m) ell_(q_n)^m)_2`.

   The first contains every advertised `ell_(q_n)`, while the second contains
   none. A gliding-hump argument forces every weakly null sequence in `Z` to
   have an `ell_2` subsequence.

## Files

- `main.tex`: self-contained statements and proofs.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source reconstruction from cached arXiv TeX.
- `figures/open_problem_crop.png`: crop of Problem 1 and its context.
- `verification.md`: proof audit and limitations.
- `tmp/`: build and visual-QA files.

## Scope

This does not decide whether a class with no finite divisibility exponent can force infinitely many
distinct `ell_p` subspaces in every representative. It shows why both
divisible/self-similar classes and the standard repeated direct-sum idea
cannot solve the problem.

Bounded searches through August 11, 2026 found no later answer. Priority is
not asserted; specialist citation review is recommended.
