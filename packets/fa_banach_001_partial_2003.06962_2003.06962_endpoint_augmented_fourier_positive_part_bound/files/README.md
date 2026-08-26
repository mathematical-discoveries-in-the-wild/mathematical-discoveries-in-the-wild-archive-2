# Endpoint-augmented Fourier positive-part bound

**Status:** `candidate_partial_result_likely_valid_needs_human_review`

**Source:** Jose Madrid and Joao P. G. Ramos, *On optimal autocorrelation
inequalities on the real line*, Communications on Pure and Applied Analysis
20 (2021), 369--388, DOI 10.3934/cpaa.2020271, arXiv:2003.06962. The selected
open direction follows Theorem 4.1 on source PDF page 17.

## Candidate result

If `phi` is even, nonnegative, smooth, supported in `[-1,1]`, and has
integral one, then

`||(hat phi)_+||_1 >= 72/(96+sqrt(2929)) = 0.4796155513...`.

The source theorem gives `1/(2(1+theta_0)) = 0.410767...` and explicitly
states that the sharp form is unknown in every dimension. The exact
one-dimensional infimum remains open, so this is a substantial explicit
lower-bound improvement rather than a full solution.

The proof retains the endpoint identity `phi(1)=0`, which is absent from the
source estimate, and combines it with normalization through a nonnegative
Cusa--Huygens Fourier multiplier.

## Contents

- `solution_packet.pdf` - theorem, complete proof, scope, and search audit
- `source_paper.pdf` - local arXiv source PDF
- `figures/open_problem_crop.png` - source Theorem 4.1 and open-status text
- `verification.md` - adversarial proof and rendering checks
- `code/verify_constant.py` - exact rational checkpoint and numerical sanity
  scan; the scan is not used as proof
- `code/make_open_problem_crop.py` - reproducible source-page crop

**Human-review focus:** Check the sign in the combined Fourier identity,
the global bound for the multiplier `K`, and the monotonicity argument on
`[3*pi/2,144/25]`.
