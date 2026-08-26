# Verifier report

Verdict: `candidate partial result; likely valid`.

## Mathematical audit

- Re-derived `p_t-p_x=-a(p+q)` and `q_t+q_x=-a(p+q)` from
  `p=u_t+u_x`, `q=u_t-u_x`; the factor is `a`, not `2a`.
- Distributional jump balance on a right-going characteristic forces
  `[p]=0` and gives `[q]'=-a[q]`.
- The Dirichlet trace gives `p+q=2u_t=0` at `x=1`, hence reflection with
  coefficient `-1`.
- Checked both path integrals in the reflected amplitude and confirmed that
  they are finite because the entire tracked ray remains in `[delta,1]`.
- Checked the initial-data correction: `integral(q0)=0`, so
  `u0(x)=-(1/2) integral_0^x q0` belongs to `H_0^1`; `u1=q0/2` is in `L2`;
  the correction is smooth and does not create a second jump.
- For every `T<2`, the choice `0<x0<min(1,2-T)`, `x0 != 1-T`, leaves the
  jump at an interior point at time `T`.
- For `a=1/x`, the reflected amplitude simplifies exactly to
  `-J*x0*(2-x0-t)`, which is nonzero for `t<2-x0`.
- Audited eight focused upgrade routes. The remaining unrestricted regime
  requires critical damping at both endpoints or at an interior interface;
  no justified semigroup/interface classification was obtained.

## Computational sanity check

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2002.03440_one_sided_singular_damping_extinction_time_lower_bound/code/verify_broken_ray.py
```

The script checks 399 rational test times in `(0,2)`, constructs an allowed
`x0`, verifies that the broken ray is interior at the test time, and checks
positivity of the explicit `a=1/x` amplitude. It is not used as proof.

## Literature and scope check

- Cheap run indexes had no duplicate for arXiv:2002.03440 or this route.
- Exact-title, quoted-question, minimal-time, singular-damping, and citation
  searches through 13 August 2026 found no later answer to the `T<2` question.
- arXiv:2310.19911 and Ann. PDE 12 (2026), Article 6 rule out finite-time
  extinction for broad subcritical unbounded-damping classes, but explicitly
  leave the critical `2/x` phenomenon outside that regime.
- The packet is explicitly partial: it does not settle two-endpoint or
  interior critical singularities and does not address the source's first,
  norm-constrained optimization problem.

## Source and rendering audit

- `source_paper.pdf` is the 11-page arXiv:2002.03440 PDF.
- `figures/open_problem_crop.png` is a genuine full-width raster crop of PDF
  page 10 and contains the complete second open problem.
- The final packet has 5 pages. Every page of the final PDF was rendered at
  review resolution and visually inspected for clipping, overlap, broken
  glyphs, unreadable mathematics, and crop legibility.
- The final LaTeX log has no warnings, overfull boxes, underfull boxes, or
  undefined references.
- Final packet SHA-256:
  `ce78cdfd2e1af082ce741f1554181ec6c60679daf658dfd2d1cfbb81b6574e41`.
- Source-paper SHA-256:
  `6e7257e2bc1be58761f08d2987413f09f7505c9cd13a7a12d48c0efd4a9af3b1`.
- Source-crop SHA-256:
  `ec9c4c7418c3af0ef2f2844645a97f9326e48a12458a2a2e070e552bbf54df1d`.
