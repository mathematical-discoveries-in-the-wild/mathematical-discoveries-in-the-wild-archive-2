# Verification record

Status: `candidate_counterexample_likely_valid`.

## Mathematical audit

- The exact source definition and question were checked on source PDF page 6.
- The source's Lemma 6 supplies a class of infinite degree on the c0 sum of
  odd spheres; Theorem 7 supplies odd degree zero for every Cuntz--Krieger
  algebra used here.
- The matrix `Q` was checked to be irreducible and non-permutation.  The
  Smith invariants of `I-Q^T` are `(1,1,0)`, giving
  `K_0(O_Q)=K_1(O_Q)=Z`.
- Since the K-groups on both sides are free, the UCT identifies the chosen
  graded K-theory isomorphism with an invertible KK-class.  Dadarlat's
  Theorem 2.3(i) was checked in the primary PDF and has exactly the required
  hypotheses and direction.
- KK sigma-additivity was checked in the contravariant variable: K-homology
  of a c0 direct sum is the product of the coordinate K-homology groups.
- The direct-sum Fredholm module was audited: normalized phase cycles have
  zero defect; commutator blocks are compact with norms bounded by
  `2||b_j|| -> 0`; finite-support smooth elements form a dense *-subalgebra;
  a finite direct sum of Schatten-p operators remains Schatten-p, including
  `0<p<1`.
- For a surjection `q:C -> B`, density of `q^{-1}(B_p)` follows from the open
  mapping theorem and small-norm lifting.  This proves rather than assumes
  preservation of p-summability under the evaluation map.
- The mapping-cylinder contraction `h(r) -> h(tr)` was checked to be a
  point-norm-continuous homotopy of *-homomorphisms.  The identities in the
  K-homology pullback diagram were checked with the contravariant direction.

## Focused upgrade audit

Eight proof-development and adversarial checks are recorded in
`runs/fa_banach_001/attempts/1401.2123_mapping_cylinder_summability_upgrade_attempts.md`.
They cover the failed arbitrary-pullback route, the successful surjective
pullback mechanism, matrix selection, KK realization, countable direct sums,
the mapping-cylinder comparison, and bounded novelty search.

## Computational audit

Run:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1401.2123_summability_degree_not_homotopy_invariant/code/verify_ck_matrix.py
```

The script checks strong connectivity, non-permutation, determinant zero,
rank two, gcd of entries and 2-by-2 minors, the kernel generator, and the
resulting Smith invariants.  These finite checks support the exact hand proof
in the packet and do not replace any analytic argument.

## Build and rendering audit

`main.tex` was compiled with `latexmk` into `tmp/`.  The final five-page PDF
was rendered page by page with Poppler and all pages were visually inspected.
The final log has no undefined references, missing files, overfull boxes, or
other substantive warnings.
