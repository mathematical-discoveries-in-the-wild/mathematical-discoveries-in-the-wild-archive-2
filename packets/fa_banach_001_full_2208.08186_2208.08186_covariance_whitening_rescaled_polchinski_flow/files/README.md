# Covariance-whitening rescaling of the Polchinski flow

**Status:** likely valid full answer to the rescaling question in Section 3
of arXiv:2208.08186.

Let `Sigma_t=C_infinity-C_t` and choose `M_t` so that
`M_t C_infinity M_t^T=Sigma_t`.  The blow-up

`mu_t=(M_t^{-1})_# nu_t`

has density `rho_t(y)=exp(V_infinity(0)-V_t(M_t y))` relative to the fixed
Gaussian `gamma_{C_infinity}`.  It evolves by the explicit inhomogeneous
Ornstein--Uhlenbeck kernels

`Q_st f(y)=E f(M_s^{-1}M_t y+Z_st)`,

where

`Cov(Z_st)=C_infinity-(M_s^{-1}M_t)C_infinity(M_s^{-1}M_t)^T`.

These kernels preserve `gamma_{C_infinity}`, satisfy the two-parameter
composition law, and give `rho_t=Q_st rho_s`.  The rescaled laws converge in
total variation to `gamma_{C_infinity}`.  The associated continuity velocity
is explicit and contains only the interaction score plus a Gaussian-
preserving rotation; the collapsing Gaussian Hessian
`(C_infinity-C_t)^{-1}` no longer appears.  For the exponential heat-kernel
schedule this reduces exactly to Shenfeld's established Langevin transport.

The packet also proves that scalar rescaling is impossible in general, even
for an anisotropic Gaussian: different covariance directions collapse at
different exponential rates.

Files:

- `solution_packet.pdf` — review packet
- `main.tex` — packet source
- `source_paper.pdf` — original arXiv source PDF
- `figures/open_problem_crop.png` — exact source passage
- `code/check_covariance_conjugacy.py` — noncommuting-matrix identity check
- `verification.md` — build and audit notes

Human review should focus on semigroup direction conventions, the
continuity-equation sign, and the exact intended meaning of removing the
source's `alpha_t` correction.
