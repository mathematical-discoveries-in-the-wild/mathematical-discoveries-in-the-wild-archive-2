# Verification report

Status: `candidate_counterexample_likely_valid`

## Claim checked

Conjecture 2.1 of arXiv:2008.03253v2 is false as printed.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Ambient space | valid | The construction acts on a two-dimensional subspace of a complex separable infinite-dimensional Hilbert space and is zero on its orthogonal complement. |
| Source quantifiers | valid | `T=N` is fixed. For every proposed `a,b,t>0`, the source normalization is `T_tilde=aN`, and `F=bN` has exactly the required norm `b`. |
| Perturbation class | valid | `F` has rank one and `F^2=0`, hence is quasinilpotent. |
| Adjoint-side hypothesis | valid | On `span{e1,e2}`, `(aN^*+alpha bN)^2=alpha*a*b I`; for every `alpha != 0` it has two nonzero eigenvalues. |
| Non-adjoint conclusion side | valid | `(aN+alpha bN)^2=0`, so its spectrum is `{0}` for every `alpha`. |
| Disconnectedness failure | valid | `{0}+B(0,r)=B(0,r)` is connected for every admissible ball radius. At radius zero, either the singleton convention is connected or the empty-ball convention cannot contain the nonempty pseudospectrum. |
| Quantifier conclusion | valid | The hypothesis holds for all nonzero `alpha`, but condition (ii) fails for each one; consequently no set `S` with at least two elements can work. |

## Computational sanity check

`code/check_matrices.py` checks the two matrix identities for 36 choices of
positive `a,b` and nonzero complex `alpha`. Run with:

```bash
python code/check_matrices.py
```

The result is `36 matrix instances passed`. This finite test is not used in
the proof; the displayed symbolic identities establish the result for all
parameters.

## Novelty check

The local lightweight indexes and bounded web queries described in the README
found no prior counterexample or later resolution. The official arXiv record
shows v2 as the current version, revised 2021-08-25, with a comment that an
error in the previous version had been fixed. Novelty is therefore plausible
but not certified.

## Reviewer focus

Confirm from page 5 that the hypothesis uses `T_tilde^*+alpha F` while the
pseudospectral/disconnectedness conclusion uses `T_tilde+alpha F`. The
counterexample exploits exactly this asymmetry and makes no claim about a
version in which both sides use the same orientation.
