# Stable Sampling and Endpoint Obstructions for Riesz--Feller Bernstein Spaces

Status: `candidate_partial_result_likely_valid`

Source: Swanhild Bernstein and Nelson Faustino, *Paley-Wiener Type Theorems
Associated to Dirac Operators of Riesz-Feller Type*, arXiv:2405.04989,
Section 6 outlook (source PDF p. 29).

## Claimed contribution

The packet advances both directions in the source outlook.

1. It gives the complete Hilbert-space (`p=2`) RKHS and sampling answer. The
   boundary space has the explicit scalar Bessel reproducing kernel, the full
   spacetime solution space has an operator-valued multiplier kernel, and one
   cubic lattice of boundary samples reconstructs both Riesz--Feller
   half-space solutions.
2. The sampling formula has an exact Parseval identity and explicit uniform,
   slice-`L2`, truncation, and additive-noise bounds. It is therefore already
   a stable numerical reconstruction scheme, not just a uniqueness theorem.
3. Two exact one-dimensional counterexamples show why the source framework
   cannot extend to `p=1` or `p=infinity` merely by retaining the same
   `f_+=(f+Hf)/2`, `f_-=(f-Hf)/2` splitting. One bandlimited `L1` function has
   a nonintegrable Hilbert transform, and one bounded bandlimited function has
   a logarithmically unbounded Hilbert transform.
4. On bandpass data whose Fourier support stays away from the origin, the
   endpoint obstruction disappears because the localized Riesz multiplier
   has a Schwartz convolution kernel.

The packet does not claim a general `p`-sampling theorem or the full
Hardy/BMO and Morrey--Campanato endpoint theory.

## Packet contents

- `solution_packet.pdf`: formal source-to-result packet.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/source_outlook_crop.png`: rendered crop of the exact live outlook.
- `code/verify_sampling_endpoints.py`: normalization, convergence, and
  endpoint-asymptotic checks.
- `code/verification_output.txt`: saved PASS output.
- `VERIFIER_REPORT.md`: adversarial mathematical review.
- `main.tex`: packet source; build artifacts and rendered pages are in `tmp/`.

## Reproduce verification

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2405.04989_riesz_feller_sampling_rkhs_endpoints/code/verify_sampling_endpoints.py \
  --suite
```

## Human-review focus

Check the left/right Clifford multiplication order in the sampling kernel,
the operator-valued RKHS adjoint convention, and the exact endpoint Hilbert
transform formulas. Novelty is bounded: Clifford ball sampling itself is
classical; the promoted contribution is its explicit stable propagation
through the Riesz--Feller solution multiplier together with the endpoint
obstruction/repair.

