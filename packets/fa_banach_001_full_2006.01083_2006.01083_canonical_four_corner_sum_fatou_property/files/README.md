# Canonical four-corner sum: Fatou property

Status: `candidate full solution, likely valid pending expert review`

Source: Nicki Holighaus and Felix Voigtlaender, *Schur-type Banach modules of
integral kernels acting on mixed-norm Lebesgue spaces*, arXiv:2006.01083v2.
The open statement is the unnumbered remark following Proposition A.7 on page
30.

## Claimed result

For arbitrary sigma-finite measure spaces `X` and `Y`, the natural infimal-sum
norm on

```text
L1 + Linfinity + L1,infinity + Linfinity,1
```

has the Fatou property. The packet also proves that every element has an
optimal four-way decomposition, so the infimum defining this canonical norm is
always attained.

The proof converts almost-optimal decompositions to positive ones, normalizes
their four pieces into one vector-valued `L2` space using a strictly positive
common dual density, and takes simultaneous Cesaro limits. The four component
Fatou lemmas preserve the limiting norm budget exactly.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv:2006.01083v2.
- `figures/open_problem_crop.png`: page-30 source evidence.
- `verification.md`: independent proof audit and review focus.
- `tmp/`: LaTeX and rendering intermediates.

## Novelty check

Bounded searches on 9 August 2026 used the exact source sentence, title,
arXiv id, and close variants of the four-corner sum plus “Fatou property.” The
run indexes and later citing material found no answer. The cited 2014 paper of
Mastylo and Sanchez-Perez gives a general characterization, but the source
authors explicitly could not verify that criterion here. Novelty confidence is
moderate pending specialist review.

## Human review focus

Please check the positive-decomposition reduction, the strictly positive
common Köthe-dual tensor, and the Hilbert-space Cesaro extraction. The proof is
finite-component: it does not claim the analogous statement for arbitrary
infinite lattice sums.
