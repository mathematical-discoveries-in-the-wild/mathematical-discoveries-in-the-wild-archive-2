# The optimized curvelet “length term” vanishes

Status: `candidate_counterexample_likely_valid`

The final-remarks conjecture in arXiv:math/0608124 proposes that, under
`theta_lambda=1/(4 epsilon)`, the adaptive penalty

`sum theta_lambda (rho_lambda-v_lambda)^2`

estimates the length of a rectifiable curved discontinuity.

The paper's own exact minimizer in `v` implies instead

`sum theta_lambda (rho_lambda-v_lambda)^2
 <= epsilon sum ||u_lambda||_q^2
 <= C(M,q) epsilon ||u||_ell2^2`.

Hence the term tends to zero for every uniformly bounded coefficient family,
independently of the thresholds `rho_lambda` and even after restricting to
fine-scale/tangent curvelets.  Taking the curvelet coefficients of the
indicator of a disk gives an explicit signal whose jump set has positive
length but whose proposed length term vanishes.

Files:

- `main.tex`, `solution_packet.pdf`: proof packet;
- `source_paper.pdf`: the source paper;
- `code/check_weight_penalty.py`: finite-dimensional regression verifier.
