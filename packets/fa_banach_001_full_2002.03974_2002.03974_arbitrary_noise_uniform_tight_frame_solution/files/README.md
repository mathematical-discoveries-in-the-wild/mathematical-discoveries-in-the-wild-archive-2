# Exact arbitrary-noise solution of the optimal-signals problem

Status: candidate full solution to Problem 1 of arXiv:2002.03974, pending
expert review.

For `N>d`, put `alpha=(N-d)/d` and

    c_sigma = clip(sigma/sqrt(alpha), c1, c2).

The packet proves that the exact value asked for in Problem 1 is

    log(1 + 1/(sigma^2/c_sigma + alpha*c_sigma)),

and that every maximizer is a uniform tight frame whose common squared norm
is `c_sigma`.  It also handles the elementary boundary case `N=d`.

The key inequality is obtained by writing `a_i=|v_i|^2`,
`x_i=1/a_i`, and weighting the reciprocal SINR of user `i` by `x_i`.
Each unordered pair then has coefficient

    a_j/a_i + a_i/a_j >= 2.

The Welch/frame-potential bound and Cauchy--Schwarz reduce the whole problem
to minimizing the single scalar function

    sigma^2/c + ((N-d)/d)*c

on `[c1,c2]`.  All equality conditions are simultaneously attained by a
uniform tight frame.

Verification:

    conda run --no-capture-output -n sandbox python code/verify_bound.py

The script checks every algebraic stage on 120,000 seeded random
configurations and checks equality for explicit real harmonic UNTFs over a
grid of dimensions and noise regimes.  With `--global-search`, it also runs
small-dimensional differential-evolution searches; those computations are
sanity checks, not part of the proof.

The main reviewer focus should be the inverse-norm weighting identity and the
equality implications in the cases `sigma=0` and `N=d`.  The packet records a
bounded arXiv/web/citation novelty search; no later solution of the arbitrary-
noise problem was found.

