# The `p>2` Hilbert-core obstruction for weakly hypercyclic Toeplitz operators

Status: `candidate_substantial_partial_likely_valid_pending_human_review`

Source: Stanislav Shkarin, *Orbits of coanalytic Toeplitz operators and weak
hypercyclicity*, arXiv:1210.3191, Question 5.4 on PDF page 17.

## Result

Question 5.4 asks whether, for some `p>2`, an analytic symbol `g` whose image
misses the open unit disc can induce a weakly hypercyclic coanalytic Toeplitz
operator on `H^p`.

The question is not settled here. The packet proves a sharp obstruction to the
positive method used in the source paper. Let `q=p/(p-1)<2`, identify the
coanalytic Toeplitz operator on `H^p` with the Banach adjoint of multiplication
by `g` on `H^q`, and let `U` be any Hilbert-space isometry with no nonzero
finite-dimensional invariant subspace. If a bounded map `J` satisfies

```text
T_g^* J = J U,
```

then `J=0`. Consequently, no invariant dense Hilbert core can satisfy
conditions (B1)--(B2) of Shkarin's weak-hypercyclicity criterion on `H^p` when
`p>2`. This rules out every isometric-Hilbert-core implementation, not only the
paper's canonical `L^2` contact-set construction.

The proof has three ingredients:

1. Every vector with a bounded forward orbit factors uniquely through
   `L^p(A)`, where `A={|1/g|=1}` is the boundary contact set.
2. The unilateral-shift part of an isometric core would give an impossible
   embedding `H^2 -> L^p(nu)`; analytic peak functions force
   `nu(I) <= C |I|^(p/2)`, hence `nu=0`.
3. The unitary part would give an impossible non-atomic embedding
   `L^2(mu) -> L^p(nu)`; equal-mass partitions again force `nu=0`.

The exponent changes direction exactly at `p=2`, explaining why the source's
Hilbert proof works at and below the Hilbert endpoint and cannot be repaired
above it by changing weights, contact measures, smoothness, or the isometric
Hilbert model.

## Scope boundary

This is a partial result, not a negative answer to Question 5.4. A weakly dense
orbit need not contain a bounded weakly-null sequence, so the theorem does not
exclude a genuinely non-Hilbertian, nonsequential weak-closure construction.
Eight focused upgrade attempts are documented in the attempt log; the direct
series, finite `n`-weak, smooth-contact, interpolation, and global-negative
routes all meet this same obstruction or a clearly identified nonsequential
closure gap.

## Files

- `main.tex`, `solution_packet.pdf`: exact theorem, proof, novelty check, and
  limitations.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_question_crop.png`: source Question 5.4 and its `p>2` context.
- `verification_report.md`: proof and artifact audit.

Attempt record:
`runs/fa_banach_001/attempts/1210.3191_hp_gt2_weak_hypercyclicity_upgrade_log.md`.

Ledger:
`runs/fa_banach_001/ledger/results/1210.3191_hp_gt2_no_isometric_hilbert_core.json`.

