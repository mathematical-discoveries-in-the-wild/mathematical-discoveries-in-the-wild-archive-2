# Candidate full solution: all-order C-fraction parity

**Status:** candidate full solution, likely valid; human review requested.

The open problem after Theorem 1 of Hongmin Xu and Xu You,
arXiv:1407.3865, asks whether the fastest continued-fraction coefficients for
the Euler correction satisfy `a_(2k+1)=-a_(2k)` for every `k>=1`.

The packet proves the answer is yes.  The source fraction is the regular
C-fraction of the Euler asymptotic series.  Its nonlinear tail algorithm turns
the evenness beyond the linear term into opposite coefficient pairs, while a
strict Stieltjes moment representation of the Bernoulli coefficients ensures
that the fraction continues nondegenerately to every order.

The exact SymPy verifier reproduces all source coefficients through `a_13`,
checks twelve pairs through `a_26`, and produces new coefficients including

`a_14 = 3754087889491759 / 2440840521848406`, `a_15=-a_14`.

Build with

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

Run QA with

```sh
conda run --no-capture-output -n sandbox python code/check_cfraction_parity.py
```

The main review focus is the identification of fastest finite corrections
with regular C-fraction convergents and the use of strict Stieltjes positivity
to rule out termination.
