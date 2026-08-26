# Brown--Halmos converse for every regular polydomain

Status: `candidate_full_solution_likely_valid`

Source: Gelu Popescu, *Multi-Toeplitz operators associated with regular
polydomains*, arXiv:2002.00462v1 (2020).  The paragraph after Theorem 4.3 on
PDF page 28 asks whether the Brown--Halmos condition characterizes weighted
multi-Toeplitz operators for every noncommutative regular polydomain
`D_f^m`; the source knew the converse only for poly-hyperballs.

## Result

The converse is true in the full stated generality.  For each tensor
coordinate `i`, multiplying the Brown--Halmos equation by its row operator
and adjoint gives

```text
(I-Phi_i)^(m_i)(T) = T-P_i T P_i,
```

where `P_i` is the projection onto tensors whose `i`th word is nonempty.
The right side is supported on the vacuum row or column.  The formal inverse

```text
sum_{p>=0} binom(p+m_i-1,m_i-1) Phi_i^p
```

is finite on each matrix coefficient.  A contributing path strips a common
right suffix.  It reaches the vacuum boundary exactly for right-comparable
word pairs, and the sum over all factorizations of the suffix is precisely
Popescu's coefficient `b_(i,delta)^(m_i)`.  This yields the exact `tau`-ratio
matrix recurrence.  Iterating over all coordinates is Proposition 1.3's
weighted multi-Toeplitz characterization.

## Verification and novelty

Eight focused audits cover the Cauchy-dual multiplication, binomial signs,
coefficientwise finiteness, reversed-word orientation, telescoping creation
weights, comparability, tensor/operator-valued scope, and exhaustive finite
word checks.  Run the checker with:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2002.00462_brown_halmos_converse_all_regular_polydomains/code/verify_finite_words.py
```

Bounded searches through 2026-08-13 covered the exact title and open-problem
wording, Brown--Halmos/converse/regular-polydomain variants, Popescu's later
work, the local corpus, arXiv, and OpenAlex citations.  OpenAlex listed only
arXiv:2002.07801 as a distinct citing work, and it does not supply this
converse.  No later solution or matching argument was found.  Novelty is
plausible, not certified, and priority is not claimed.

Human review should check first the boundary-defect Lemma 1 and then the
reversal/path-weight calculation in Lemma 3.  No conditional or computational
dependency remains.

## Files

- `main.tex`: full proof and audit record.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source PDF page-28 evidence.
- `code/verify_finite_words.py`: finite-word sanity checker.
- `VERIFIER_REPORT.md`: explicit verification record.
- `tmp/`: LaTeX and rendered-page intermediates.
