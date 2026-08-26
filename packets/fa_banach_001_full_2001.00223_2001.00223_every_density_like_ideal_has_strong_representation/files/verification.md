# Verification report

## Result checked

The proposed result is a negative answer to Question 5 of arXiv:2001.00223: every density-like ideal is `Exh(psi)` for some strongly-density-like lower semicontinuous submeasure `psi`.

## Analytic audit

1. **Choice of scales.** For every target `t_n`, density-likeness supplies a positive threshold `d_n`. Choosing `t_{n+1} < min(d_n,t_n/4)` is possible and forces `t_n` to decrease to zero.
2. **Concavity.** On `[t_{n+1},t_n]`, the piecewise-affine gauge has slope
   `s_n = 2^(-n-1)/(t_n-t_{n+1})`. The quarter-scale separation gives `s_{n+1}>s_n`. Thus slopes decrease from left to right; adjoining the constant part above `t_0` preserves concavity.
3. **Submeasure property.** A nonnegative, increasing, concave function vanishing at zero is subadditive. Hence `psi=f composed with phi` is monotone and subadditive. Continuity of `f`, including its saturation at infinity, transfers lower semicontinuity.
4. **Same exhaustive ideal.** Tail values satisfy `||A||_psi=f(||A||_phi)`. Since `f(t)=0` exactly when `t=0`, the two exhaustive ideals agree.
5. **Strong-density constant.** If `2^(-n) <= epsilon < 2^(1-n)`, then `psi(F_k)<epsilon/4` implies `phi(F_k)<t_{n+1}<d_n`. The density-like conclusion at target `t_n` yields a union with `psi`-value below `2^(-n)<=epsilon`. For `epsilon>1`, boundedness of `psi` makes the conclusion automatic.

No circular appeal to the desired strong-density property occurs. The construction uses only the original density-like modulus one dyadic scale at a time.

## Computational sanity check

Command:

```sh
conda run --no-capture-output -n sandbox python code/check_concave_gauge.py
```

The script constructs 41 separated scales, checks all 39 comparisons between adjacent interval slopes, tests concavity on 50,000 deterministic random triples, tests subadditivity on 50,000 deterministic random pairs, and checks the dyadic threshold inequalities at 31 scales. The recorded run returned `result=PASS`; the script exits nonzero on failure.

This does not prove the theorem. It guards against reversed slope inequalities, endpoint mistakes in the piecewise definition, and incorrect factors in the dyadic estimate.

## Source verification

- Source: Adam Kwela and Paolo Leonetti, *Density-Like and Generalized Density Ideals*, arXiv:2001.00223, Journal of Symbolic Logic 87 (2022), 228-251.
- Target: Section 6, Question 5, source PDF p. 25.
- The screenshot in `figures/open_problem_crop.png` contains the complete question and immediate context.

## Bounded literature screen

Search date: 2026-08-09.

Queries included the exact question sentence, `strongly-density-like ideal submeasure`, the paper title together with `open question`, and an arXiv-domain search for `strongly-density-like`. The source paper was the only mathematical result found. OpenAlex work `W2998427436` reported one citation, but inspection showed that record to be the journal issue's cover/back matter rather than a later mathematical paper.

Conclusion: no later answer was located in this bounded screen. This is not an exhaustive priority determination.

## Human review focus

- Confirm that monotonicity of the interval slopes is in the correct direction for concavity.
- Confirm lower semicontinuity when the original submeasure may take value infinity.
- Confirm the strict inequalities at the dyadic endpoints.
- Check the bounded literature screen against MathSciNet/Zentralblatt or a broader citation database before any priority claim.
