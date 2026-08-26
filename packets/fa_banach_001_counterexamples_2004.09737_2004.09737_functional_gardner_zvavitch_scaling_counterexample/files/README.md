# Scaling counterexample to the functional Gardner--Zvavitch conjecture

Status: claimed full counterexample; likely valid; pending expert review.

Source: Michael Roysdon and Sudan Xing, *On L_p-Brunn--Minkowski type and L_p-isoperimetric type inequalities for measures*, Transactions of the American Mathematical Society 374 (2021), 5003--5036, arXiv:2004.09737v2.

Target: Conjecture 6.2 on page 29 of the arXiv PDF.

## Result

The functional L_p-Gardner--Zvavitch conjecture is false as stated, already for

- dimension n = 1,
- p = 1 and t = 1/2,
- the standard Gaussian measure,
- smooth, positive, even, strictly log-concave functions.

For M > 0, set

    f_M(x) = M exp(-x^2),
    g_M(x) = M^{-1} exp(-x^2),
    h(x)   = exp(-x^2).

The pointwise hypothesis follows from

    (x^2+y^2)/2 - (x+y)^2/4 = (x-y)^2/4 >= 0.

If A is the Gaussian integral of exp(-x^2), then the proposed conclusion would give

    A >= A(M+M^{-1})/(2C),

which fails for any fixed C when M tends to infinity.

## Mechanism

At p = 1 and t = 1/2 the pointwise premise is invariant under the reciprocal rescaling (f,g) -> (Mf,M^{-1}g), while the proposed arithmetic-mean conclusion is not. The obstruction is therefore structural, not numerical. Equal-height or scale-normalized variants are not disproved.

## Files

- `solution_packet.pdf`: expert-facing counterexample packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:2004.09737v2.
- `figures/open_problem_crop.png`: real crop of Conjecture 6.2.
- `code/make_open_problem_crop.py`: reproducible page render and crop.
- `code/verify_counterexample.py`: exact symbolic verification.
- `verification.md`: verification and novelty-search record.

## Novelty check

Bounded searches on 2026-08-09 covered the exact conjecture name and wording, arXiv:2004.09737, the Roysdon--Xing paper and its visible citation neighborhood, the corresponding 2020 dissertation statement, and later functional Gardner--Zvavitch work. No matching reciprocal-scaling counterexample was found. This supports novelty plausibility but is not a certification.

## Human review

Verify that the source's unqualified term "centered" does not encode a hidden common normalization. The example is centered under both usual readings: every function is even with barycenter zero, and every function attains its maximum at the origin. The source separately imposes equal suprema in Theorem 6.3, whereas Conjecture 6.2 does not.
