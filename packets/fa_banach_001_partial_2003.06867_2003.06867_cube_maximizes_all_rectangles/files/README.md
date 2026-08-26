# The cube maximizes the exit-time/eigenvalue functional over rectangles

Status: **candidate full proof of the rectangular subcase of Conjecture 5.4;
substantial partial result for the full convex-domain conjecture; likely valid,
novelty uncertain; send to human review**.

For an axis-aligned rectangle

```text
R_a = product_k (-a_k,a_k)
```

and every `d>=2`, `p>0`, the packet proves

```text
lambda_1(R_a)^p E_0[tau_{R_a}^p]
    <= lambda_1(Q_d)^p E_0[tau_{Q_d}^p].
```

Equality holds exactly when all `a_k` are equal, i.e. when the rectangle is a
homothetic cube (and, under the source normalization `a_1=1`, exactly for
`Q_d`).  The proof gives the stronger stochastic domination

```text
lambda_1(R_a) tau_{R_a} <=_st lambda_1(Q_d) tau_{Q_d}.
```

The key new observation is that the exit time `T` of one-dimensional Brownian
motion from `(-1,1)`, started at zero, is log-concave as a probability law.
Indeed,

```text
E exp(-sT) = sech(sqrt(2s))
           = product_{n>=0} lambda_n/(lambda_n+s),
lambda_n = (2n+1)^2 pi^2/8,
```

so `T` is an infinite sum of independent exponential variables.  Its survival
function `S` is therefore log-concave.  Jensen gives
`product_k S(b_k t) <= S(average(b)t)^d` for `b_k=a_k^{-2}`.

Files:

- `solution_packet.pdf`: self-contained proof packet.
- `main.tex`: packet source.
- `problem.md`: exact source transcription and scope.
- `solution.md`: plain-text proof companion.
- `verification.md`: adversarial mathematical and computational checks.
- `references.md`: source and bounded novelty audit.
- `source_paper.pdf`: arXiv:2003.06867.
- `figures/open_problem_crop.png`: readable excerpt spanning source pages
  19--20.
- `code/check_rectangle_inequality.py`: non-proof numerical sanity check.

The full conjecture over arbitrary coordinate-symmetric convex domains is not
claimed.
