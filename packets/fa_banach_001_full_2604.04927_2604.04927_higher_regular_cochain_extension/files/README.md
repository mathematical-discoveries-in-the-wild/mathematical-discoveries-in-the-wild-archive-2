# Higher-Regularity Cochain Extensions

Result type: `full`

Status: candidate full solution, likely valid pending expert review.

Source paper:

- Erik Nilsson and Silvano Pitassi, “Uniformly Bounded Cochain Extensions
  and Uniform Poincare Inequalities,” arXiv:2604.04927v2 (2026).
- Question location: Section 6, Open question 1, pages 19-20.
- Local source: `source_paper.pdf`.
- Evidence crops: `figures/open_problem_crop_page19.png` and
  `figures/open_problem_crop_page20.png`.

## Claimed contribution

The packet gives an affirmative answer to Open question 1 as literally
stated, for every integer regularity order `m >= 0`, every form degree, and
both variants in the question. For each fixed bounded Lipschitz domain
`Omega`, the harmonic-orthogonal Sobolev de Rham subcomplex admits a bounded
contracting homotopy `h`. If `S` is any bounded degreewise Sobolev extension,
then

```text
E^k = d S^{k-1} h^k + S^k h^{k+1} d
```

is automatically a bounded extension and a strict cochain map. If
`Omega` is compactly contained in `K`, choosing the degreewise extensions
with support compactly contained in `K` makes every `E^k omega` vanish near
the outer boundary, so extension by zero belongs to the same whole-space
Sobolev graph space.

The nontrivial analytic point is exactness of the harmonic-orthogonal
higher-regularity complex. It follows from Costabel-McIntosh maximal
regularity and their smooth finite-dimensional representatives of de Rham
cohomology, together with a finite-dimensional correction that enforces
orthogonality to the source paper's absolute harmonic fields.

## Files

- `main.tex`: full proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: the source arXiv paper.
- `supporting_paper_0808.2614.pdf`: Costabel-McIntosh regularity theorem.
- `figures/open_problem_crop_page19.png`: first page of the source question.
- `figures/open_problem_crop_page20.png`: continuation of the question.
- `verification.md`: proof audit and human-review focus.
- `tmp/`: LaTeX intermediates and rendered QA pages.

No computational code is used; the result is purely functional-analytic.

## Novelty check

Bounded searches on August 9, 2026 used the exact source title and the phrases
“strict higher-regularity analogue,” “higher-regularity cochain extension,”
`H^{(m,m)}` with “cochain extension,” and “bounded contracting homotopy
Sobolev de Rham Lipschitz extension.” The searches found the source paper,
the Hiptmair-Li-Zou degreewise extension theorem, and the
Costabel-McIntosh regularity/homotopy paper, but no paper stating this
arbitrary-ambient higher-regularity cochain section or the displayed
two-term formula as an answer to Open question 1. The run's cheap indexes had
no prior packet for arXiv:2604.04927. Novelty confidence is moderate: the
proof is a short synthesis of established ingredients and should receive a
specialist citation search before any publication claim.

## Scope limitation

The proof gives a bounded operator for each fixed domain pair, exactly as the
displayed question asks. It does not extract a sharp or explicitly uniform
bound for the contracting homotopy over a varying family of Lipschitz
domains. If the authors intended that stronger quantitative requirement as
part of the word “analogue,” that refinement remains open.

## Human review focus

Please check:

- that the absolute harmonic space used in arXiv:2604.04927 represents the
  same de Rham cohomology appearing in Costabel-McIntosh;
- the finite-dimensional correction proving exactness of the subcomplex
  defined by `L^2`-orthogonality to harmonic fields;
- boundedness of the contracting homotopy in the `H^{(m,m)}` graph norm;
- the endpoint degrees and the compact-support/zero-extension argument;
- whether the source authors intended quantitative uniformity over domain
  families beyond the literal fixed-domain bound in Open question 1.
