# Kamke Delta-functions: non-product examples and derivative redundancy

Result type: `full`

Status: candidate full answer, likely valid pending expert review.

Source paper:

- Dušan Oberta, “On the existence of solutions of dynamic equations on time
  scales in Banach spaces,” arXiv:2512.13602v2 (2026), DOI
  `10.1002/mma.70827`.
- Question location: Section 5, page 29, final Kamke Delta-function paragraph.
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

The packet answers both example directions raised in the source:

1. It constructs a large family of non-product Kamke Delta-functions. In
   particular,

   ```text
   w(t,x) = x + (t-a)x^2
   ```

   works on every nondegenerate compact time-scale interval and cannot factor
   as `q(t)h(x)`.
2. It proves that the requested example in which the endpoint derivative
   clause is essential cannot exist. Every nonnegative continuous solution of

   ```text
   u(t) <= integral_a^t w(s,u(s)) Delta s
   ```

   automatically is Delta-differentiable at `a` with derivative zero under
   axioms (ii) and (iii) of the definition. Hence axiom (iv) is equivalent to
   zero being the unique nonnegative continuous solution without any endpoint
   derivative restriction.

The second conclusion is structural: it applies to every Kamke
Delta-function, not only to the displayed example.

## Files

- `main.tex`: full proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: full-width crop of the page-29 question.
- `verification.md`: proof audit and review focus.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

On August 11, 2026, cheap run indexes were searched for arXiv:2512.13602 and
the core Kamke Delta-function terms. Exact-title and close-phrase web searches
found no independent answer. OpenAlex listed one 2026 citing work, concerning
fractional retarded dynamic equations; its indexed title and abstract do not
state either observation here. Novelty confidence is moderate pending a
specialist search.

## Human review focus

Please check:

- the use of uniform equicontinuity at `x=0` in the right-dense endpoint case;
- the one-step Delta-integral identity in the right-scattered case;
- the endpoint convention that `[a,b]_T` is the ambient time scale;
- the time-scale Gronwall comparison for polynomial coefficient
  `Q_M(t)`.
