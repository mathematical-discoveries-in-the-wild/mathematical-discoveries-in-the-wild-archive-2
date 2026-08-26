# Verification record

Status: `candidate_full_solution_likely_valid`

## Source verification

- Official PDF downloaded from `https://arxiv.org/pdf/1305.7269` on
  2026-08-13 and stored as `source_paper.pdf`.
- Physical PDF page 91, Section 10.1, contains published Question 10.1:
  “Is H^3_cts(T,T) non-zero?”
- The source and its cited Austin--Moore paper define `H_cts` as the cohomology
  of globally continuous inhomogeneous bar cochains.  The target is therefore
  not the measurable, locally continuous, or Segal--Mitchison theory.
- The queue's deterministic `we_do_not_know` hit was separately checked and
  found inside commented-out TeX; it is not used as the promoted target.

## Proof audit

1. **Coefficient action.**  `Aut(T^m)=GL(m,Z)` is discrete.  A continuous
   homomorphism from connected `T^d` to this group is trivial.
2. **Normalization.**  The ordinary normalized bar subcomplex computes group
   cohomology.  The usual projection and homotopy are finite combinations of
   identity insertions and face maps, hence preserve global continuity.
3. **Factorization.**  A normalized degree-`n` cochain is zero on the fat
   wedge and factors continuously through `(T^d)^{ smash n}`.
4. **Simple connectedness.**  With the standard based CW structure, every
   non-basepoint cell in `T^d` has dimension at least one.  Every cell of the
   `n`-fold smash has dimension at least `n`; for `n>=2` there are no one-cells,
   so the connected smash product is simply connected.
5. **Lift.**  The universal covering `R^m -> T^m` therefore gives a unique
   based continuous lift.  Its restriction to the connected fat wedge is the
   lattice value zero, so the lift is normalized.
6. **Cocycle obstruction.**  The differential of a lifted torus cocycle is a
   continuous map from connected `(T^d)^(n+1)` to discrete `Z^m`.  It is
   constant and evaluates to zero at the identity tuple.
7. **Averaging.**  For a real degree-`n` cocycle `C`,

   ```text
   B(g_1,...,g_(n-1)) = (-1)^n integral C(g_1,...,g_(n-1),t) dt
   ```

   satisfies `dB=C`; this follows by integrating the cocycle equation and
   using Haar invariance.  Compactness gives a finite continuous integral.
8. **Projection.**  Reducing `B` modulo `Z^m` produces the required continuous
   torus-valued primitive.
9. **Low degrees.**  Degree-zero invariants are `T^m`; degree-one cocycles are
   continuous homomorphisms, boundaries vanish, and torus homomorphisms are
   integer matrices.

No unproved mathematical dependency remains.

## Independent checks

`code/verify_degree_complex.py` constructs the winding-number matrices induced
by the inhomogeneous bar differential and checks exactly that

```text
D_2(b_1,b_2)=(-b_1,0,b_2),
D_3(a_1,a_2,a_3)=(0,a_2,a_2,0),
D_(n+1) D_n=0 for n=1,...,8.
```

It also checks rational exactness of this winding complex through degree 8.
For the target degree, the displayed integral matrices directly give
`ker D_3={(a,0,c)}=im D_2`.  This is a sign sanity check, not a substitute for
the topological proof.

## Bounded novelty check

Fresh searches on 2026-08-13 covered:

- exact variants of `H^3_cts(T,T)` and the source's question wording;
- `globally continuous group cohomology`, circle/torus coefficients, and
  `H^3`;
- source title, arXiv id `1305.7269`, author, Question 10.1, and citation
  results;
- local run registry, claim, and attempt indexes;
- primary sources arXiv:1004.4937 (Austin--Moore) and arXiv:1110.3304
  (Wagemann--Wockel).

Those sources define and discuss the same globally continuous theory, and
later search results discuss related measurable, locally continuous, smooth,
or classifying-space cohomology.  No paper explicitly answering Question 10.1
or stating the all-degree torus computation was found.

Novelty confidence is **moderate**: the proof is short enough that the result
could be implicit folklore under different notation, but the exact question
was published as open and no later answer appeared in the bounded search.

## Build and visual QA

- `main.tex` compiled with `latexmk`/`pdflatex`.
- The build log was checked for errors, undefined references, overfull boxes,
  and unresolved citations.
- The final PDF was text-extracted and the theorem, question, proof endpoint,
  limitations, and references were checked.
- Every rendered packet page and the original-resolution source crop were
  inspected visually.

## Human review recommendation

High-priority expert review.  Check the normalized-continuous-cochain lemma
and the smash-product lift.  The rest is an explicit bar-differential and Haar
integration calculation.
