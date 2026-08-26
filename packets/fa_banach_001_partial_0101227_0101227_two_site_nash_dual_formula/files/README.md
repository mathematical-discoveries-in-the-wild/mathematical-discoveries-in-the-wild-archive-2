# Exact two-site nonlinear dual formula for the Sobolev partner of Nash

Status: `candidate_substantial_partial_likely_valid`

For every `p>2`, this packet gives a complete sup-inf/inf-sup formula for the
sharp `ell^p` Sobolev constant of the first nontrivial Dirichlet birth-death
chain (two live sites, unit conductances). This is a rigorous finite-chain
subcase of Open Question 4 in arXiv:math/0101227.

It also proves two complementary facts:

- every finite Dirichlet birth-death chain has the exact nonlinear
  `sup_f min_i J_i(f)` half-formula;
- at `p=4`, the simpler Banach tail-norm upper functional from Chen's later
  Poincare-type theory is strictly nonsharp: the true constant is below
  `2.08`, while that functional is above `2.13`.

This does **not** solve the original centered ergodic Nash or logarithmic
Sobolev question. Their Euler sources change sign, so the positive-tail
comparison behind this packet does not extend directly.

Key files:

- `solution_packet.pdf`: reviewer-facing theorem and proof.
- `main.tex`: packet source.
- `code/verify_two_site.py`: exact symbolic and rational certificate for the
  `p=4` strict gap, plus numerical sanity checks across exponents.
- `verification.md`: reproduced output and review checklist.
- `source_paper.pdf`: arXiv:math/0101227.
- `figures/open_questions_crop.png`: source PDF page 6.
- Attempt record:
  `runs/fa_banach_001/attempts/0101227_nash_variational_formula_upgrade_attempts.md`.

Run the verifier from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/0101227_two_site_nash_dual_formula/code/verify_two_site.py
```

Human review should focus on the identification of the two-site model as a
Dirichlet Sobolev/Nash-type subcase, the summation-by-parts half-formula, and
the distinction between the nonlinear source-tail functional `J_i` and
Chen's Banach tail-norm upper functional.

