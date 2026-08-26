# An adjoint Gabor system which is not a type-I R-dual

Status: `candidate_counterexample_likely_valid` — claimed full negative answer,
pending specialist human review.

Source: Diana T. Stoeva and Ole Christensen, *On various R-duals and the
duality principle*, arXiv:1509.06263.  The open question appears on PDF page 6,
immediately after Theorem 1.4.

## Result

For every integer `q >= 2`, the packet constructs a window `g in L2(R)` such
that

```text
{E_{m/q} T_n g}_{m,n in Z}
```

is a Gabor frame, but its normalized adjoint system

```text
{sqrt(q) E_m T_{qn} g}_{m,n in Z}
```

is not an R-dual of type I.

Start with `h=q^(-1/2) 1_[0,1)`.  Its primal system is Parseval and its
normalized adjoint is orthonormal.  Under the `q`-step Zak transform,

```text
L2(R) = L2(T^2; C^q),
adjoint span = L2(T^2) e_0.
```

Choose a bounded Borel injection `phi:T^2->[1,2)` and define `g` by

```text
(Z_q g)(t,theta) = q^(-1/2) sqrt(phi(t,theta)) e_0.
```

The primal frame operator is `M_phi tensor I_q`, whereas the adjoint frame
operator on its span is `M_phi`.  The latter is cyclic because `phi` is
essentially one-to-one; the former has no cyclic vector because its fiber
multiplicity is `q>=2`.  Hence the two operators are not antiunitarily
equivalent.  Lemma 1.3(iii) of the source then rules out type-I R-duality.

## Scope and novelty

This is a full negative answer to the universal question as printed.  The
construction is deliberately measurable rather than regular; it does not
decide whether the conclusion might hold for windows in a smaller smoothness
or localization class.

The run's lightweight indexes were searched by arXiv id, title, `R-dual of
type I`, `adjoint Gabor system`, and spectral/Zak keywords.  Focused arXiv/web
searches through 11 August 2026 found no counterexample or solution.  In
particular, arXiv:2408.14952 (2024) still calls this the famous problem and
develops weak R-duality as a possible route.  Novelty confidence is moderate
to high, subject to a specialist search beyond the bounded audit.

## Packet contents

- `main.tex`: self-contained construction and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: readable source crop.
- `verification.md`: adversarial proof and render audit.

Human review recommendation: **review as a full counterexample**, focusing on
the joint Borel functional-calculus step and the source's antiunitary
characterization.

