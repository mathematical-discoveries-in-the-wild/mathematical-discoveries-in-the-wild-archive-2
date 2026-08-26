# Critical Besov norm of white noise has a deterministic low-p lower bound

Status: `candidate_full_likely_valid`

Source: Mark Veraar, *Regularity of Gaussian white noise on the
d-dimensional torus*, arXiv:1010.6219, Theorem 3.4(2) and Remark 3.5(i), PDF
page 7.

## Result

The source proves that, for `p >= 2`, the critical random Besov norm

`||W||_{B^{-d/2}_{p,infinity}(T^d)}`

is bounded below almost surely by a deterministic positive constant. It asks
whether this also holds for `1 <= p < 2`.

This packet proves it for every `1 <= p < infinity`. Normalize the dyadic
blocks by `Z_j=2^{-jd/2}W_j` and put `Y_j=||Z_j||_p^p`. Pointwise Gaussian
scaling and the annular multiplier bounds give a uniform positive lower bound
for `E Y_j` and a uniform upper bound for `E Y_j^2`. Paley--Zygmund therefore
gives a fixed positive probability that `Y_j` exceeds a fixed positive
constant. Every third block uses a disjoint set of independent Fourier
coefficients, so the second Borel--Cantelli lemma makes this happen infinitely
often almost surely.

## Evidence and verification

- `source_paper.pdf`: the complete canonical arXiv TeX source, locally
  rendered because the environment blocked a fresh PDF download.
- `figures/open_problem_crop.png`: full-width crop of source PDF page 7.
- `main.tex`, `solution_packet.pdf`: complete proof packet.
- `VERIFICATION.md`: proof audit, scope, and build log.

Eight materially progressive attempts are recorded in
`attempts/1010.6219_low_p_white_noise_besov_upgrade_attempts.md`.

A bounded novelty check on 2026-08-17 searched the run indexes and the web/
arXiv by exact remark text, title and author, and the phrases `low p critical
Besov white noise lower bound` and `Paley-Zygmund dyadic white noise Besov`.
It found the source and published version but no explicit later answer.
Novelty confidence is moderate-high pending expert review.

Human review should focus on confirming that the `3n` multiplier supports are
disjoint under the source's convention and on the bounded novelty search.
