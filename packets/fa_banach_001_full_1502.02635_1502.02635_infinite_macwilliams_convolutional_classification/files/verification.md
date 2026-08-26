# Verification report

Verdict: likely valid candidate full solution, pending expert review.

The proof was checked at four levels:

1. The source's exact open sentence was verified on page 2 of
   arXiv:1502.02635v1, and arXiv:0902.2235 confirms that “general” means
   F-linear rather than necessarily F[z]-linear.
2. The convolutional weight definition was checked in arXiv:0902.2235: it is
   the sum of the Hamming weights of all coefficient vectors, exactly the
   finitary weight on time-coordinate pairs.
3. The projective incidence Gram formula in Lemma 1 was enumerated over prime
   fields q = 2, 3, 5 in dimensions 1 through 4.
4. The local-to-global proof was audited against the only plausible compactness
   failure: a functional class cannot “escape to infinity,” because choosing a
   vector where the target functional is nonzero leaves only finitely many
   family members to separate.

Verifier command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1502.02635_infinite_macwilliams_convolutional_classification/code/verify_incidence.py
```

Expected terminal lines:

```text
cases=12
largest_matrix=156x156
status=PASS
```

Observed on 11 August 2026: all 12 cases passed, with the largest incidence
matrix of size 156 by 156.

The computation is a sanity check only. The proof uses the closed formula

```text
A A^T = q^(d-2) I + q^(d-2)(q-1) J
```

for d at least 2, whose two eigenvalues are strictly positive.

Human review should focus on:

- the off-diagonal inclusion-exclusion count in the incidence matrix;
- the argument that only finitely many coordinate functionals survive on a
  finite-dimensional subspace;
- the separator construction that converts equality of every finite
  restriction into equality of global projective multiplicities;
- whether the same theorem is already known under “finitary code,” “infinite
  length code,” or a related term.

The final packet compiled without undefined references, warnings, or overfull
boxes. All four pages were rendered at 150 dpi and visually inspected; the
source evidence is readable, equations and theorem blocks are unclipped, and
the references fit on the final page. Final SHA-256 values:

```text
solution_packet.pdf  92eba331292f3f1ab459a4c1a760a32ccc7b08205e7fb5803028547269ebdb6c
main.tex             ef3b55e47a1e6fd8a8cc81f215503dc4a4627081d315a8bdab87d90595319614
source_paper.pdf     0d1ccf58ab8849855338f8fa3bc017df3e3756cfd22b1c162e6b9473a32c4bf5
```
