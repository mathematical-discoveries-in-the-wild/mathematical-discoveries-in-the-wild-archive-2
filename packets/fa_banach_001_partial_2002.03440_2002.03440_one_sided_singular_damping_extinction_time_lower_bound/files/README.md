# Sharp two-traversal lower bound for one-sided singular damping

Status: `candidate partial result; likely valid`.

For the second open problem in Section 4 of arXiv:2002.03440, this packet
proves that no damping which is regular away from at most one endpoint can
make the Dirichlet energy semigroup on the unit interval vanish before time
2. In the standard form class

`a in C^1((0,1]), a >= 0, sup_{x>0} x a(x) < infinity`,

every `T < 2` admits energy data whose wavefront survives to time `T`.
Consequently, the known damping `a(x)=1/x` has the optimal universal
extinction time 2 throughout this one-sided-singularity class.

The proof follows one isolated jump of a Riemann invariant. Its amplitude is
a nonzero exponential until the jump reaches a singular set. It travels from
an interior point to the regular endpoint, reflects, and survives on the
return trip until time `2-x0`. Choosing `x0 < 2-T` excludes every `T<2`.

The unrestricted source problem remains open for damping with critical
nonintegrable singularities at both endpoints or at an interior interface.
Eight focused upgrade attempts are recorded in the packet; none supplied the
missing singular-interface or spectral classification.

Files:

- `solution_packet.pdf`: review-ready partial-result packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original arXiv:2002.03440 PDF.
- `figures/open_problem_crop.png`: genuine crop of the second problem on PDF page 10.
- `code/verify_broken_ray.py`: finite geometry and critical-amplitude sanity check.
- `VERIFIER_REPORT.md`: proof, scope, literature, and rendering audit.
- Ledger: `runs/fa_banach_001/ledger/results/2002.03440_one_sided_singular_damping_extinction_time_lower_bound.json`.

