# Index obstruction to renorming weighted bicyclic algebras

**Status:** full solution, likely valid; pending human review.

**Source:** Matthew Daws and Bence Horvath, *Ring-theoretic (in)finiteness in
reduced products of Banach algebras*, arXiv:1912.07108, question on PDF page
18 and the corresponding first open question in Section 7.

## Result

For the source's weighted bicyclic algebra `A_x=l^1(BC,omega_x)`, every norm
equivalent to the original norm that makes `A_x` a unital Banach algebra with
unit norm one satisfies

```text
C_DI(A_x, ||.||_0) >= exp(2x).
```

The original weighted norm has equality.  Therefore there is no absolute
constant `K` such that every Dedekind-infinite Banach algebra can be
equivalently renormed to have `C_DI<=K`.

The key is to treat every possible one-sided inverse pair at once.  Annular
characters give a holomorphic symbol on `exp(-x)<=|z|<=exp(x)`.  The faithful
unilateral-shift representation sends a proper one-sided inverse to a
surjective, noninjective Fredholm Toeplitz operator, so its symbol has nonzero
winding.  Circular means of `log|f|` then force annular condition number at
least `exp(2x)`, and spectral radius transfers this lower bound to every
equivalent norm.

## Files and verification

- `main.tex` and `solution_packet.pdf`: complete proof and novelty boundary.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_question_crop.png`: actual rendering of the source question
  on PDF page 18.
- `runs/fa_banach_001/attempts/1912.07108_bicyclic_renorming_attempt.md`:
  discovery route and obstruction audit.

The proof is exact and has no computational dependency.  Recommended human
review focus: faithfulness of the shift representation on the weighted
completion, the Toeplitz Fredholm-index step for arbitrary algebra elements,
and the annular circular-mean lemma.

## Novelty check

Bounded searches on 17 August 2026 covered the cheap run indexes, exact arXiv
id and title, and arXiv queries for the Dedekind-infinite Banach-algebra
renorming terminology.  No later answer or duplicate packet was found.
Novelty confidence is moderate because the Toeplitz and annulus ingredients
are classical, although their combination closes exactly the alternative-
witness gap identified by the source.
