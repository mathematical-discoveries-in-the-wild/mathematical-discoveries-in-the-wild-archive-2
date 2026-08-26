# Counterexample to the Four-Matricization Criterion in Symmetric Dimension Four

Status: `counterexample_likely_valid`

Source: Gabriel Champagne, Nathaniel Johnston, Mitchell MacDonald, and Logan
Pipes, *Spectral Properties of Symmetric Quantum States and Symmetric
Entanglement Witnesses*, arXiv:2108.10405, Conjecture 1 on PDF page 14. The
lane target arXiv:2408.11684 renewed the surrounding `m >= 4` problem as open.

## Claimed contribution

Conjecture 1 of arXiv:2108.10405 is false.  Consider the ordered spectrum

```text
(lambda_1,...,lambda_10)
  = (1000,1000,1000,1000,703,703,703,660,660,594) / 8023.
```

The four matrices in the conjecture collapse in pairs.  After multiplication
by 8023, their two distinct values have leading principal minors

```text
M6=M13:   1188, 1376000, 753535708, 293705189448
M11=M12:  1188, 1176119, 465623314, 137338080.
```

They are therefore positive definite by Sylvester's criterion.  However, the
symmetric matricization obtained by placing the eigenvalues in upper-triangle
order `(10,9,3,1,7,4,2,5,6,8)` has, after the same scaling, determinant
`-337300392`.  It is not positive semidefinite.  The source paper's Theorem 1
then says that a state with this spectrum is not absolutely symmetric PPT.
Thus positivity of the four distinguished matrices is not sufficient.

## Verification

Run the dependency-free exact-integer checker:

```bash
python3 runs/fa_banach_001/solutions/counterexamples/2108.10405_d4_four_matricization_conjecture_counterexample/code/check_counterexample.py
```

It checks ordering and normalization, constructs the four source matrices,
checks all eight Sylvester minors, constructs the obstructing matricization,
and checks its exact negative determinant.

## Novelty and scope

A bounded search on 11 August 2026 covered all four run indexes, the exact
arXiv id, the exact phrases `four matrices` and `absolutely symmetric PPT`,
`Conjecture 1`, `symmetric matricization`, and `counterexample`, the current
arXiv record, and the 2022 journal metadata. It found the source conjecture
and no later proof or counterexample. This is not a claim of priority.

This refutes the displayed four-matrix criterion only. It does not determine
a minimal replacement family, nor does it resolve equality of absolute
symmetric separability and absolute symmetric PPT in dimension four.

Human review recommendation: high priority. The certificate is short and
entirely exact. Check the transcription of the four matrices and the placement
order of the obstructing matricization; the remaining audit is elementary
integer linear algebra.

