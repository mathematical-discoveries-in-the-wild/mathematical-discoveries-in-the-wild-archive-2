# All-degree instability of power maps for small `s`

Status: `candidate_partial_solution_likely_valid`

Source question: Katarzyna Mazowiecka and Armin Schikorra, *Minimal
`W^{s,n/s}`-harmonic maps in homotopy classes*, arXiv:2006.07138, PDF page 6.

Immediate context: Dorian Martino, Katarzyna Mazowiecka, and Armin Schikorra,
*Minimizing and non-minimizing degree one `W^{s,1/s}`-harmonic maps between
spheres*, arXiv:2606.15644v1, PDF page 2 and footnote 1.

## Result

For every `s in (0,1/8)` and every nonzero integer `d`, the power map

`u_d(z) = z^d : S^1 -> S^1`

is not a local minimizer of the conformally invariant `W^{s,1/s}` energy in
degree `d`.  More precisely, putting `p=1/s`, `q=|d|`, and

`u_{d,epsilon}(e^{i theta}) = exp(i(d theta + epsilon cos(3q theta)))`,

one has

`(1/p) d^2/d epsilon^2 E_s(u_{d,epsilon})|_0`

`= q(8-p) 2^{p+1} pi^{3/2} Gamma((p+1)/2)/Gamma(3+p/2) < 0`.

Consequently, for all sufficiently small nonzero `epsilon`,

`E_s(u_{d,epsilon}) < E_s(z^d) = |d| E_s(id)`.

This rigorously proves the all-degree statement that arXiv:2606.15644v1 labels
as based only on “AI generated, unverified” trigonometric computations.

## Proof mechanism

The second variation at `z^d` has a translation-invariant kernel.  On the
Fourier mode `cos(3|d| theta)`, partitioning the angular difference into
`|d|` equal arcs and applying

`sum_{j=0}^{q-1} csc^2((x+2 pi j)/(2q)) = q^2 csc^2(x/2)`

reduces the quadratic form exactly to `|d|` times the degree-one form.  A
short beta-integral calculation evaluates the latter and produces the factor
`8-p`.

## Scope

This is a complete theorem, but only a substantial partial result adjacent to
the source question.  It rules out every power map as a minimizer when
`s<1/8`; it does **not** decide whether some non-power degree-one minimizer
exists there.  It also does not decide the endpoint `s=1/8`, other maps, or
higher-dimensional sphere maps.

## Novelty check

The bounded check on 2026-08-11 searched the run indexes, the exact source and
supporting titles, and official arXiv API queries for combinations of
`power maps`, `fractional harmonic`, `second variation`, `degree one`,
`W^s`, and `positive definiteness`.  The exact `degree one`/`W^s` query found
only arXiv:2606.15644v1; the two closest all-degree/second-variation queries
returned zero records.  The supporting preprint itself states the all-degree
claim only in an explicitly unverified footnote.  No rigorous prior proof was
found.  Novelty is plausible and fairly high-confidence, but not certified by
an exhaustive journal search.

## Packet contents

- `main.tex`, `solution_packet.pdf`: exact theorem and proof.
- `source_paper.pdf`: arXiv:2006.07138.
- `supporting_paper_2606.15644.pdf`: the June 2026 preprint containing the
  unverified all-degree footnote.
- `figures/open_problem_crop.png`: source question on PDF page 6.
- `figures/unverified_all_degree_claim_crop.png`: supporting theorem and
  footnote on PDF page 2.
- `code/verify_multiplier.py`: high-precision numerical checks.
- `VERIFICATION.md`: proof, computation, build, and visual-QA report.

Human review should focus on the second-variation kernel, the partition and
cosecant root-sum identity, and the beta-integral normalization.

