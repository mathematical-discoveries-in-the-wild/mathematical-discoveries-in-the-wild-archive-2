# The Hopf-bundle commutative JB*-triple fails condition (*)

Status: `candidate_counterexample_likely_valid`

Source: Osamu Hatori, *The Mazur-Ulam property for a Banach space which
satisfies a separation condition*, arXiv:2205.01888; RIMS Kokyuroku Bessatsu
B93 (2023), 29--82.

Target: Final Remarks, page 45 of the arXiv PDF.  Hatori asks whether every
commutative JB*-triple satisfies his separation condition (*).

## Result

The answer is no.  More generally, for a compact principal circle bundle
`pi:L->X`, the commutative JB*-triple

```text
C^T(L)={a in C(L): a(lambda t)=lambda a(t)}
```

satisfies condition (*) if and only if `pi` admits a continuous global
section, equivalently if and only if the principal bundle is trivial.

The key point is that the norm-one evaluation functionals form a copy of
`L` in the weak*-topological extreme boundary, and a representative family
for maximal sphere faces is exactly a set-theoretic transversal of the circle
orbits.  Condition (*) forces such a transversal to be closed.  For compact
`L`, a closed transversal is compact and projects homeomorphically onto `X`,
so it is a continuous section.  Conversely, a continuous section trivializes
the bundle and Urysohn functions on `X` verify condition (*) directly.

Apply this to the nontrivial Hopf bundle `S^3->S^2`.  The resulting space
`C^T(S^3)` is therefore an explicit commutative JB*-triple which does not
satisfy condition (*).  It still has the complex Mazur-Ulam property by the
known theorem of Cabezas--Cueto-Avellaneda--Hirota--Miura--Peralta, so the
counterexample separates Hatori's sufficient condition from the property it
implies.

## Files

- `solution_packet.pdf`: review-ready theorem and proof.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: Hatori's source paper.
- `supporting_paper_2201.06307.pdf`: the principal-bundle representation and
  maximal-face identification used in the proof.
- `figures/open_problem_crop.png`: page-45 crop containing the question.
- `VERIFICATION.md`: proof audit and reviewer focus.

## Novelty and review

The cheap run indexes had no entry for arXiv:2205.01888.  Bounded searches on
2026-08-09 used the exact question, source title, author, condition (*),
commutative JB*-triples, principal circle bundles, and the Hopf fibration.
They found Hatori's paper and the known complex Mazur-Ulam theorem, but no
later answer or the bundle-triviality characterization.  Novelty remains
subject to expert review.

Human review should focus on the closed-transversal lemma and on the exact
identification of representative functionals with the circle orbits of
evaluations, for which the packet cites arXiv:2201.06307.
