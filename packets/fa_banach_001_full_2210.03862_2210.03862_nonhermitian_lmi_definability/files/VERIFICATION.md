# Verification record

## Automated check

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2210.03862_nonhermitian_lmi_definability/code/verifier.py
```

Transcript:

```text
trials=200
worst_decomposition_error=8.772e-17
worst_skew_after_projection=3.130e-15
worst_final_feasibility_violation=6.261e-15
status=PASS
```

## What the check covers

- `p=q+i r` for arbitrary non-Hermitian homogeneous matrix pencils;
- real-linear projection of a finite matrix tuple onto `ker r`;
- exact vanishing of the skew-Hermitian part after projection, to numerical
  tolerance;
- positive scalar rescaling makes `1-p(Z)` positive semidefinite.

## What still needs human review

- the canonical real coefficient-space identification used in Lemma 1;
- the uniform bound for amplifications of a fixed finite scalar-coordinate
  map over arbitrary operator systems;
- use of the source's uniform zero-set criterion for a definable predicate;
- the interpretation of `1 >= p(X)` as membership of `1-p(X)` in the
  positive cone when `p` is not formally Hermitian.
