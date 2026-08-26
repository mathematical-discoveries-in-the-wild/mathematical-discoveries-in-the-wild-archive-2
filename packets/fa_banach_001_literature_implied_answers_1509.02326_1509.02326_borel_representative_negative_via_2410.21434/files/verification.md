# Verification report

Status: literature-implied full negative answer; human review requested.

## Mathematical audit

- Checked that `d_alpha(x,y)=|x-y|^alpha` is a metric for `0<alpha<1` and
  induces the usual topology on `[0,1]`; hence the space is compact, complete,
  separable, and has the usual Borel sets.
- Proved the no-rectifiable-curve claim using first hitting times of `n`
  equally spaced intermediate values. The resulting length lower bound is
  `L^alpha n^(1-alpha)`, which diverges.
- Rechecked the source definitions: upper gradients are tested only on
  nonconstant compact rectifiable curves. Thus zero is an upper gradient of
  every measurable function on the snowflake.
- Derived exactly `||f||_{N^{1,p}}=||f||_p` and, for measurable `E`,
  `C_p(E)=mu(E)`. The lower capacity bound follows from every admissible
  `h>=1` on `E`; the upper bound uses `h=chi_E` and upper gradient zero.
- Checked that a Bernstein set and its complement have Lebesgue inner measure
  zero: a positive-measure measurable subset would contain a nonempty perfect
  subset.
- Checked that the split sigma-algebra is closed under complements and
  countable unions.
- Checked well-definedness of the averaged measure: differences between two
  coordinate representations lie in a measurable subset of `A` or `A^c` and
  hence are null.
- Checked countable additivity: disjoint split sets have coordinate sets that
  are pairwise disjoint modulo Lebesgue-null intersections.
- Checked completeness: a subset of a null split set is represented by
  Lebesgue-measurable subsets of its two null coordinates.
- Checked that the measure restricts to Lebesgue measure on all Lebesgue sets,
  so it is finite and positive on nonempty open balls.
- Verified `mu(A)=1/2` and the exact identity
  `mu(A triangle B)=1/2` for every Borel set `B`.
- If a Borel function represented `chi_A`, its Borel superlevel set at `1/2`
  would contradict that identity. Since capacity equals measure on measurable
  sets, this also rules out a Borel quasi-everywhere representative.

## Literature and provenance audit

- Cheap indexes searched: `registry_index.tsv`, `solutions/index.tsv`,
  `attempts/index.tsv`, and `proof_gaps/index.tsv`.
- Search terms included the source id, exact open-problem wording, `Newtonian
  Borel representative`, and `measurable p-path`.
- No indexed duplicate or explicit later answer to arXiv:1509.02326 was found.
- arXiv:2410.21434, Theorem 1.1, proves for a metric space with a measure
  finite on balls that Borel regularity is equivalent to every measurable
  function admitting a Borel representative.
- The supporting source has no occurrence of the source authors, source id,
  `Newtonian`, or `quasiopen`. The link to Open Problem 5.3 is therefore an
  inferred consequence, not an explicitly claimed answer in that paper.
- Classification is conservative: `literature_implied_answer`, not a novel
  counterexample.

## Rendering audit

- `source_paper.pdf` has 17 pages; the problem crop was rendered at 180 dpi
  from PDF page 13 and visually inspected.
- `supporting_paper_2410.21434.pdf` has 15 pages; the theorem crop was rendered
  at 180 dpi from PDF page 2 and visually inspected.
- The final packet was compiled with `latexmk`, text-extracted, rendered to
  page PNGs, and every page was visually inspected. Build details and the
  final page count are stored in `tmp/`.

## Reviewer focus

1. Check the completeness and well-definedness of the split measure.
2. Check the first-hitting-time proof excluding rectifiable curves.
3. Confirm that the source convention for a complete Borel measure permits a
   domain sigma-algebra strictly larger than the Borel sigma-algebra, as used
   both in the source setting and explicitly in Theorem 1.1 of the supporting
   paper.
