# Infinite-Dimensional Affine-Flat Minsum Counterexample

Status: `candidate_counterexample_likely_valid`

Source: Thomas Jahn, Yaakov S. Kupitz, Horst Martini, and Christian Richter, *Minsum Location Extended to Gauges and to Convex Sets*, arXiv:1410.3690, Section 6 (PDF p. 34).

## Claimed contribution

The finite-dimensional theorem that every finite family of affine flats has a nonempty Fermat--Torricelli locus does not survive in infinite dimension, even for two closed affine flats in a real Hilbert space with the ordinary Hilbert norm. The packet gives an explicit example at strictly positive distance whose sum-of-distances objective has infimum one but no minimizer.

It also proves the exact two-flat criterion. For `A=a+U` and `B=b+V`, with `U,V` closed linear subspaces and `P` the orthogonal projection onto `closure(U+V)`, the minsum locus is nonempty exactly when `P(b-a)` belongs to the algebraic sum `U+V`. When it exists, the locus is the union of the segments joining nearest pairs.

## Packet contents

- `solution_packet.pdf`: four-part proof/review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: the exact Section 6 question.
- `figures/finite_affine_flat_statement_crop.png`: Proposition 4.1 and the finite-dimensional affine-flat conclusion.
- `code/verify_affine_flat_counterexample.py`: numerical check of the truncation formula and escaping preimages.
- `code/verification_output.txt`: saved PASS output.
- `VERIFIER_REPORT.md`: adversarial verification report.
- `main.tex`: packet source; build intermediates and rendered pages are under `tmp/`.

## Reproduce the computational check

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1410.3690_infinite_hilbert_affine_flat_empty_minsum/code/verify_affine_flat_counterexample.py
```

The script is only a sanity check. The proof is analytic and self-contained.

## Human-review focus

Check the equivalence between minsum attainment and attainment of the distance between the two flats, and the projection criterion `P(b-a) in U+V`. In the explicit example, verify that `y=(1/n)` lies in `ell^2` but not in the range of `D(x)_n=x_n/n`, and that the extra real coordinate makes the unattained distance exactly one.

Novelty is plausible rather than certified: bounded searches through 2026-08-13 found the standard literature on nonclosed sums of subspaces and later Hilbert-space Fermat--Torricelli algorithms, but no paper presenting this exact result as an answer to the source's Section 6 question.
