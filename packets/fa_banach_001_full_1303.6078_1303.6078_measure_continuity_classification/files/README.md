# Atomic measures or finite compacta

Status: **full answer; likely valid; pending human review**.

Choi--Kim--Lee--Martín ask for which compact Hausdorff spaces `K` every
operator `T:L1(mu)->C(K)` satisfies their condition (1): the map

```text
s -> T* delta_s
```

is continuous from `K` to `L_infinity(mu)` for convergence in measure.

For a fixed finite measure `mu`, the complete classification is:

- if `mu` is purely atomic modulo null sets, every compact Hausdorff `K`
  works;
- if `mu` has a nonatomic part of positive measure, exactly the finite
  compact Hausdorff spaces work.

Atomic sufficiency follows by reading weak-star continuity one atom at a
time and using that finitely many atoms cover all but arbitrarily small
measure. For the converse, every infinite compact Hausdorff space has an
infinite compact metrizable continuous image. A convergent sequence in that
image supports a weak-star continuous `L_infinity(mu)`-valued bump map whose
values are a weak-star-null Rademacher sequence on the nonatomic part. Those
values do not converge in measure. The standard correspondence between
bounded weak-star continuous fields and operators into `C(K)` then gives the
counterexample.

Files:

- `solution_packet.pdf`: self-contained classification and proof.
- `source_paper.pdf`: arXiv:1303.6078.
- `figures/condition_context_crop.png`: source definition of condition (1).
- `figures/open_problem_crop.png`: exact source question.

The novelty check covered the run indexes and parsed arXiv corpus, exact-id
and exact-question searches, title/citation searches, and close keyword
searches involving Iwanik's condition, weak-star continuity, convergence in
measure, atomic measures, and compact spaces. No prior statement of this
classification was found. This is a bounded search, not a definitive
bibliographic claim.

Primary review focus: the topological lemma producing an infinite metrizable
continuous image of every infinite compact Hausdorff space, and the
weak-star continuity of the bump/Rademacher field at its unique accumulation
point.
