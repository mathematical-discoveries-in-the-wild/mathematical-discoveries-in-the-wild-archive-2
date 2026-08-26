# Verification report

Verdict: candidate full negative answer with a reproducible exact-rational
certificate.

## Structural checks

1. The equation is exactly of the source form
   `X'=f(X)+epsilon P(X,X(t-r(X)))`.
2. `f` and `P` are polynomial. The delay `2*pi-arctan(v)` is real analytic,
   positive, and globally bounded between `3*pi/2` and `5*pi/2`.
3. The unperturbed cycle is checked by substitution. Its Floquet multipliers
   are `1`, `exp(-4*pi)`, and `exp(-2*pi)`, so it is nondegenerate.
4. The scalar periodic problem is a contraction for `|epsilon|<1`; its unique
   fixed point bootstraps to `C-infinity`.
5. The coefficient normalization, recurrence, Cauchy majorant, parity
   restriction, log-convex endpoint reduction, and geometric tail ratio were
   rederived independently from `main.tex`.
6. Local uniform convergence on compact punctured parameter sets makes the
   obstruction holomorphic, so the certified nonzero value at `epsilon=1/10`
   yields nonzero values arbitrarily close to zero.

## Exact certificate

Run from the packet directory:

```bash
conda run --no-capture-output -n sandbox python code/rigorous_certificate.py
```

The script uses exact rational arithmetic for every decisive comparison. Its
expected summary is:

```text
exact Taylor obstruction certificate: PASS
inf_{|y0|<=10/9} |w_30| > 227.03539284378
max_{k<=30, |y0|<=10/9} |w_k| < 734.7284579277
sum_{n>=30} R_n < 1.8829084625232e-08
|w_infinity-w_30| < 1.3834264571374e-05
therefore |w_infinity| > 227.03537900952
```

The displayed decimals are informational conversions performed only after
the exact assertions pass.

## Literature and source checks

- The exact question is on source PDF page 18 and is preserved in
  `figures/open_problem_crop.png`.
- Mallet-Paret--Nussbaum arXiv:1305.0579 treats prescribed time-dependent
  delays and explicitly does not settle state-dependent delays.
- Hu arXiv:1708.08024 treats a special state-dependent system under an
  additional monotone time-map condition not satisfied here.
- Searches through 2026-08-12 found no explicit resolution of Remark 6.5.

## Build and visual QA

- The five-page packet compiled with no warnings, unresolved references,
  overfull boxes, or underfull boxes.
- All five pages were rendered at 130 dpi and visually inspected. The source
  crop is readable, equations are not clipped, and the corrected comparison
  and limit symbols render properly.
- Source PDF SHA-256:
  `adc53a7df79d8b2a50cc571504626ee569a86532518457bb418e6ed7d12fd302`
- Question crop SHA-256:
  `22ac602cd16e54c88551719b11cf72eacbbdb0a40bdf38d633bd90eb265ea1bb`
- Solution packet SHA-256:
  `c71dbf1c6bfadfd84f9888a4a4ad3abc7d11be5baee0e1cb1117fa1bca5ac146`
