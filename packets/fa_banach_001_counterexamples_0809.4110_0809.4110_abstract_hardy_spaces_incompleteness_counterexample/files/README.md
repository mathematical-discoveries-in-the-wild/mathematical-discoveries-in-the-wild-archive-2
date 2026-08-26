# Abstract Hardy spaces can be incomplete

Status: `candidate_counterexample_likely_valid`

Source: Frederic Bernicot, *Use of abstract Hardy spaces, Real interpolation and Applications to bilinear operators*, arXiv:0809.4110v1, Remark 2.6(1), page 6.

## Result

Under exactly the minimal hypotheses used in the source definition, the abstract atomic and molecular Hardy spaces need not be complete. For every molecular decay parameter `epsilon`, the packet constructs a doubling metric-measure space and a uniformly `L^2`-bounded family `(B_Q)` for which

`H^1_{epsilon,mol} = H^1_ato`

is isometric to

`{b in ell_2 : sum_n |b_n|/n^2 < infinity}`

with the weighted `ell_1` norm `sum_n |b_n|/n^2`. This is a genuine norm, but the space is incomplete: the truncations of `(1,1,...)` form a Cauchy sequence while `(1,1,...)` is not in `ell_2`.

Thus the completeness question in Remark 2.6 has a negative answer at the paper's stated level of generality. The counterexample does not conflict with Proposition 2.8, which adds a continuous embedding into `L^1_loc`.

## Mechanism

On `(0,1)`, let `r_n` be the Rademacher functions and let `Q_n` have measure `n^-4`. Define the rank-one operator

`B_{Q_n} f = <f, n^2 1_{Q_n}> r_n`

and set all other `B_Q` equal to zero. The normalized atoms and molecules are precisely scalar multiples of `a_n=n^2 r_n` of modulus at most one.

Almost-everywhere convergence of an atomic series forces its Rademacher coefficient vectors to be Cauchy in `ell_2`. This follows from the fourth-moment estimate and Paley-Zygmund inequality. Conversely, every square-summable coefficient vector gives an almost-everywhere convergent Rademacher series. The atomic gauge is therefore exactly the weighted `ell_1` norm above.

## Novelty check

A bounded search on 2026-08-09 covered the exact sentence from Remark 2.6, the title and arXiv id, `Bernicot abstract Hardy spaces complete atoms molecules`, and `H^1_{epsilon,mol} complete`. It found the source paper and related abstract Hardy-space papers, but no later paper explicitly resolving this completeness question or giving this Rademacher/rank-one counterexample. Novelty confidence is moderate, not definitive.

## Files

- `main.tex`: full counterexample and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: page 6 crop containing Remark 2.6(1).
- `code/finite_rademacher_check.py`: finite sanity checks; it is not part of the proof.
- `VERIFICATION.md`: verifier report and review focus.

## Human review recommendation

Prioritize checking that the source permits an arbitrary uniformly bounded family indexed by balls, that the selected `Q_n` are legitimate balls in `(0,1)`, and that convergence in probability of finite Rademacher sums forces `ell_2`-Cauchy coefficient vectors. If those points pass, promote from candidate to verified counterexample.
