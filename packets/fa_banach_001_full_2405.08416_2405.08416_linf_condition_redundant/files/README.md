# The `L^infinity` condition is redundant in the compact `T(1)` theorem

Status: `full_solution_likely_valid`

Source target: Árpád Bényi, Guopeng Li, Tadahiro Oh, and Rodolfo H. Torres,
*Compact T(1) theorem à la Stein*, arXiv:2405.08416v2, Theorem 1 and
Remark 3.6, PDF page 8.

Remark 3.6 asks whether the theorem's `L^infinity` condition (ii) can be
removed. This packet gives an affirmative answer: the normalized-bump
`L^2` decay in condition (i) is by itself necessary and sufficient for
compactness.

The new step is a cube-localized representation of `T(1)`. For a cube `Q`
of side length `ell` and a cutoff equal to one near `Q` at scale `A ell`,
the standard kernel estimate gives

```text
MO_Q(T(1)) <= C A^(d/2) omega(x_Q,A ell) + C A^(-delta),
```

where `omega` is the normalized-bump decay from condition (i). Letting `A`
tend to infinity sufficiently slowly proves the three small-cube,
large-cube, and far-translation vanishing conditions characterizing `CMO`.
The same argument gives `T*(1) in CMO`. The source already proves that
condition (i) implies the weak compactness property, so its quoted compact
`T(1)` theorem finishes the proof.

A bounded official-arXiv search through 11 August 2026 used arXiv id
2405.08416, the exact title, and combinations of `L^infinity condition`,
`removed`, `normalized bump`, and `CMO`. No later paper removing condition
(ii) was found. The result is agent-produced and should receive expert proof
and novelty review.

Files:

- `solution_packet.pdf`: full statement, proof intuition, proof, and review
  notes.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: Remark 3.6 and its immediate context.
