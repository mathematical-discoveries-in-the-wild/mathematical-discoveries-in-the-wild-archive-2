# Full convergence of the projected Menger-curvature Hilbert flow

Status: **candidate full solution, likely valid pending specialist review**

Source: Jan Knappmann, Henrik Schumacher, Daniel Steenebruegge, and Heiko von
der Mosel, *A speed preserving Hilbert gradient flow for generalized integral
Menger curvature*, arXiv:2103.10408; Adv. Calc. Var. 16 (2023), 597--635.

## Claimed result

For every `p in (7/3,8/3)` and every regular embedded initial curve in the
natural Hilbert space `H^s`, `s=3p/2-2`, the source paper's global projected
flow converges strongly in `H^s` to a projected critical knot as time tends to
infinity.  The limit remains in the initial knot class and has the prescribed
initial speed and barycenter.

This answers the explicit convergence question immediately before Corollary
1.4 on source PDF page 5.  It does **not** settle global existence or
convergence for the ordinary unprojected ambient Sobolev gradient flow.

## Proof mechanism

The preserved speed and barycenter define a Hilbert submanifold, and the
source vector field is its intrinsic gradient.  Three ingredients close the
problem:

- a normalized-chord factorization proves that `intM^(p,2)` is real analytic
  on its natural Hilbert energy space;
- the Blatt--Reiter first-variation splitting has an elliptic Fourier
  multiplier of order `2s`, while the differentiated remainder is compact at
  a smooth critical knot, so the constrained Hessian is Fredholm of index
  zero;
- the same splitting gives the Palais--Smale property on the fixed-speed
  level set, upgrading the source's weak accumulation to strong `H^s`
  accumulation.

The abstract Lojasiewicz--Simon theorem and finite-length argument then force
the entire trajectory, rather than merely subsequences, to converge.

## Files

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: self-contained proof source.
- `source_paper.pdf`: original arXiv source.
- `supporting_paper_1308.2499.pdf`: Blatt--Reiter principal/remainder splitting.
- `supporting_paper_2505.02719.pdf`: Palais--Smale framework for knot energies.
- `supporting_paper_2511.07214.pdf`: abstract Lojasiewicz--Simon and convergence argument.
- `figures/open_problem_crop.png`: complete source-page evidence.
- `verification.md`: verification and novelty record.
- `tmp/`: LaTeX and rendered-page QA artifacts.

## Human review focus

Please check especially:

1. the weighted `L^2` normalized-chord analyticity lemma;
2. the one-derivative compact-remainder estimate obtained by differentiating
   the Blatt--Reiter structural formula;
3. the projection-defect estimate in the Palais--Smale proof; and
4. the pullback from arbitrary fixed speed to constant speed.

Those are the energy-specific points.  The final Lojasiewicz--Simon
finite-length argument is standard and is written out in the packet.
