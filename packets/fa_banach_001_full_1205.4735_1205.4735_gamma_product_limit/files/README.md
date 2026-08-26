# The gamma-product limit for the classical Bohnenblust--Hille estimates

Status: `candidate_full_solution_likely_valid`

Model: `GPT5.6`

Primary source: Diana Marcela Serrano-Rodríguez, *A closed formula for
subexponential constants in the multilinear Bohnenblust--Hille inequality*,
arXiv:1205.4735, PDF page 5; published as *Improving the closed formula for
subpolynomial constants in the multilinear Bohnenblust--Hille inequalities*,
Linear Algebra and its Applications 438 (2013), 3124–3138.

Originating queue target: G. A. Muñoz-Fernández, D. Pellegrino, and J. B.
Seoane-Sepúlveda, arXiv:1107.4814.

## Result

For the corrected even-indexed gamma product `r_n` in equation (2.3) of
arXiv:1205.4735,

```text
log r_n = 1 - gamma/2 - (log 2)/2
          - [psi_1(3/2)/(4n)] log n + O(1/n).
```

Hence

```text
lim r_n = exp(1-gamma/2)/sqrt(2),
```

exactly as conjectured. The original product from arXiv:1107.4814 has the same
asymptotic expansion because the corrected and original logarithms differ by
an explicit fixed constant divided by `n`.

The proof also upgrades the original conditional consequence: the complete
real recursive sequence of classical upper estimates satisfies

```text
C_n / 2^(n/8) -> exp(1-gamma/2) / 2^(1/4),
C_n / C_(n-1) -> 2^(1/8).
```

These are asymptotics for the named classical upper estimates, not for the
unknown optimal Bohnenblust--Hille constants.

## Mechanism

The identity

```text
(6k+1)/(4k+2) = 3/2 - 1/(2k+1)
```

turns the logarithm of the product into a Cesàro average of difference
quotients of `log Gamma` at `3/2`. Exact cancellation of the powers of `pi`
and `2` leaves the digamma value `psi(3/2)`. The next Taylor coefficient is
the trigamma value and supplies the `-(log n)/n` correction.

## Files

- `main.tex`: source statement, proof intuition, theorem, full proof, and
  recursive strengthening.
- `solution_packet.pdf`: compiled review packet.
- `VERIFICATION.md`: source, algebra, numerical, novelty, and render checks.
- `source_paper.pdf`: official arXiv PDF for arXiv:1205.4735.
- `supporting_paper_1107.4814.pdf`: official PDF for the originating target.
- `figures/open_problem_crop.png`: full-width crop from source PDF page 5.
- `code/check_gamma_product_limit.py`: high-precision sanity checker; not used
  as proof.
- Run attempt note:
  `attempts/1107.4814_gamma_product_limit_attempt.md`.

Human review should focus on the exact cancellation, the finite correction
between the two formulas, and the parity-summed recurrence increment.
