# Verification record

Verified on 2026-08-17 by `agent_lane_09`.

## Source integrity

- `source_paper.pdf`: 342531 bytes; SHA-256 `461b316ee028c68577f454201ecb9b5286def93102662d891c7cf8c7592c8ad5`.
- `assets/source_question_crop.png`: 97179 bytes; SHA-256 `09ccca08bf6ff5878408033ec08f0301b95fcbdc04e9f5cd0f52ff426007bdbe`.
- The crop is a direct image of source PDF page 4 containing Remark 1.2 and its exact natural question. It was inspected at original resolution and is readable.

## Mathematical checks

- The source theorem guarantees at least one seed exponent `a_0>p` with positive polynomial decay and uniform small `exp L^p` norm.
- Choosing `r>max(d/(2 beta),a_0/m)` makes both interpolation targets larger than `a_0` and makes the near-time semigroup singularity integrable.
- The Luxemburg definition, after shrinking the source smallness threshold, uniformly controls the required exponential factor in `L^(2r)`.
- The one-unit restart identity combines fixed-time `L^(a_0)->L^infinity` smoothing with the decaying `L^r` forcing norm to prove `||u(t)||_infinity -> 0`.
- Once the solution is pointwise small, the nonlinear term is bounded by `C delta^(m-1)|u|`; weighted Gronwall against the spectral-gap semigroup gives every rate below `d^beta` in `L^p intersect L^infinity`.
- Interpolation gives every `L^a`, `p<=a<=infinity`, and the source inclusion gives the same exponential decay in `exp L^p`.
- A large-time one-unit restart puts the solution in `L^2` without requiring `u_0 in L^2`.
- For any requested remainder rate `mu<min((d+2)^beta,m d^beta)`, one can choose `alpha<d^beta` with `m alpha>max(mu,d^beta)`. This both makes the ground-state coefficient integral converge and bounds the complementary spectral convolution.
- The linear example `f=0, u_0=epsilon phi_0` attains the leading rate `d^beta`.
- The result is deliberately classified as partial because the short-time endpoint range in the source's exact all-time estimate remains unresolved.

## Packet checks

- `solution_packet.pdf`: 342873 bytes; SHA-256 `5b053dbf97e17ec3b1d52fe0a67624b1f0e05c346783418af585f7cc8ca4da4b`.
- Final PDF has five letter-size pages, is unencrypted, and has no suspect objects.
- Compilation completed without LaTeX warnings, errors, overfull boxes, or underfull boxes.
- Text extraction contains the source question, definitions, proof intuition, theorem, all four proof steps, coefficient formula, novelty audit, limitations, and human-review notice.
- All five pages of the final post-edit 120-DPI render were inspected; no clipping, overlap, overflow, corrupt glyphs, or unreadable content was found.
- The ledger JSON parses successfully and records model `GPT5.6`.

## Review status

Human expert review remains pending. Priority checks are the passage from the
source weak-mild representative to restarted Lebesgue-space identities and the
uniform exponential-moment choice after shrinking the source smallness
constant.
