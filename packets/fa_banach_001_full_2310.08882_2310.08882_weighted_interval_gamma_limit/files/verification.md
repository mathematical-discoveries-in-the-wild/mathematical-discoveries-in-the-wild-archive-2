# Verification record

Date: 2026-08-12

## Source evidence

- Official source PDF: `figures/source_2310.08882.pdf`.
- Published Gamma-convergence program: PDF page 4, rendered as
  `figures/source_page4-04.png`.
- Fat-Cantor construction and incompatible pointwise constants: PDF pages
  23--24, rendered as `figures/source_example-23.png` and
  `figures/source_example-24.png`.
- Euclidean input: Brezis--Nguyen (2016), Proposition 15, archived as
  `figures/brezis_nguyen_2016.pdf`. Its radial mollifier convention is
  `integral_0^infinity rho_i(r) dr = 1` in dimension one, so
  `rho_i(r)=i 1_[0,1/i](r)` has limit constant `2^(1/q)`.

## Mathematical checks

The proof was audited along four independent axes:

1. Weight comparison: both the outer weight and the `q`-root of the inner
   weight contribute, giving the sharp lower factor `m^(1+1/q)`.
2. Metric variation: strict step-function approximation followed by moving
   finitely many jumps into the open dense minimum-weight set proves
   `||Du||_mu = m |Du|`.
3. Locality: for a fixed recovery function whose derivative is supported
   compactly inside that open set, all sufficiently short nonconstant pairs
   have both endpoints in it; the weighted and Euclidean energies are then
   exactly related by the same factor.
4. Normalization: Proposition 15 of Brezis--Nguyen applies after renaming the
   two integration variables and gives the one-dimensional constant
   `gamma_(q,1)=2^(1/q)`.

Run:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2310.08882_weighted_interval_gamma_limit/code/verify_weight_scaling.py
```

The script verifies the global weight lower bound for deterministic and
random grid functions, exact equality when all short nonconstant interactions
are confined to a minimum-weight interval, and numerical convergence of the
Euclidean affine energy to `2^(1/q)`.

## Review focus

The highest-value human checks are the strict finite-jump approximation in
Lemma 2, the passage from compact derivative support to the exact locality
identity (11), and the precise match between the source's metric variation
convention and the relaxation used in equation (5).

## Final artifact checks

- Analytic verifier: passed.
- LaTeX build: passed with no warnings, undefined references, or overfull or
  underfull boxes in the final log.
- Rendered-page inspection: all 7 pages of the final packet inspected at 150
  DPI; no clipping, overlap, illegibility, or malformed mathematics found.
- Packet SHA-256:
  `92e3da7c8fb061680692ee2c5728a93c210db6f80da42818a8acdfeaef4237b1`.
- Source PDF SHA-256:
  `da9286026b2f6b38e5bef106d7b5cf62beb30e01ca1be785b441a6cd55412f04`.
- Brezis--Nguyen PDF SHA-256:
  `bf22e8c349f8074f96f59a2b350a42f9ec3377d927fb8699e2947b3e5218dc25`.
