# Counterexample packet: a zero numerator refutes the positive lower-ratio conjecture

Status: **candidate full counterexample to the lower-ratio part of Remark 2;
likely valid; human review required**

Source: Shih-Yu Chang, *Generalized Multivariate Hypercomplex Function
Inequalities and Their Applications*, arXiv:2407.05062v1, Section 7.1,
Eqs. (74), (75), (81), (82), and Remark 2 on PDF pages 23--25 and 29.

## Result

The conjecture allows arbitrary continuous `f` and the broad polynomial maps
of Eq. (10).  In the scalar setting take `f=1` and
`Phi(X)=X^2-X^3`.  Then `Phi(f(A))=0` for every scalar `A`.  Consequently,
regardless of the proposed polynomial arguments and regardless of the
invertible denominator `g`, the lower ratio is zero and cannot be at least a
prescribed positive `alpha_2`.  The same example covers the averaged formula
by taking one term with weight one.

The structural obstruction is strict positivity: a positive lower ratio with
positive invertible denominator forces the numerator itself to be strictly
positive, a hypothesis missing from the conjecture.

## Scope

This refutes the universal lower-ratio requirements (75) and (82), and hence
Remark 2 as stated for arbitrary positive `alpha_2`.  It does not refute the
upper-ratio problem considered alone.  The separate difference-type remark is
not claimed to be resolved.

## Files

- `main.tex`: self-contained counterexample and structural obstruction.
- `solution_packet.pdf`: rendered human-review packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/`: source crops for the requirements and Remark 2.
- `code/verify_counterexample.py`: exact scalar audit.
- `verification.md`: source, proof, novelty, and rendering audit.

Ledger: `runs/fa_banach_001/ledger/results/2407.05062_zero_numerator_refutes_positive_lower_ratio.json`.
