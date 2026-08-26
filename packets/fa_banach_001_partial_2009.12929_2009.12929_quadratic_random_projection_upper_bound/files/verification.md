# Verification record

Verified on 2026-08-17 by `agent_lane_09`.

## Source integrity

- `source_paper.pdf`: 230745 bytes; SHA-256 `6560e928e63b41ba54dc3e019afb5522bf6767321135aef3139aa5d524da8f1d`.
- `assets/source_question_crop.png`: 174227 bytes; SHA-256 `e82c5e4f765612f7772de9ede349ab68ab876d81e9318c0395bd78d8400abd71`.
- The crop is a direct image of source PDF page 12 containing Remark 4.5, the source upper bound, and the statement that significant improvement is expected. It was inspected at original resolution and is readable.

## Mathematical checks

- On the unit sphere, `<u,x>=1-||u-x||_2^2/2` is exact.
- The support function of `conv(F union -F)` is `max_(x in F)|<u,x>|`; a uniform lower support bound is equivalent to containment of the corresponding Euclidean ball.
- From `rB_2 subset K subset B_2`, the gauges satisfy `||v||_2<=||v||_X<=r^(-1)||v||_2`.
- Applying this comparison to every Euclidean orthogonal hyperplane projection gives the same simultaneous norm bound without a Grassmannian union bound.
- For surface dimension `d=n-1`, the stated normalized cap lower bound follows from the polar-coordinate formula, angular radius `2 arcsin(t/2)>=t`, `sin(theta)>=2theta/pi`, and an upper bound `pi` on the normalizing integral.
- A maximal `t/2`-separated set is a `t/2`-net, and its radius-`t/4` caps are disjoint, giving the asserted covering-number bound.
- Independence and a union bound give the displayed failure probability for random covering radius.
- Substitution of `t_N^d=2^d(A+2)log(N)/(kappa_n N)` was checked algebraically: the exponential contributes `N^(-(A+2))` and the net cardinal contributes `2^d N/((A+2)log N)`.
- For `t_N<=1`, `(1-t_N^2/2)^(-1)<=1+t_N^2`, yielding the theorem.
- Six focused upgrade attempts were recorded; the log-free and matching-lower-bound routes have explicit obstructions.

## Packet checks

- `solution_packet.pdf`: 415085 bytes; SHA-256 `cecd3351df63e1ec1642d7885d74834032227e7f3e0a3729c27aa0d2e8825c9b`.
- Final PDF has five letter-size pages, is unencrypted, and has no suspect objects.
- Compilation completed without LaTeX warnings, errors, overfull boxes, or underfull boxes.
- Text extraction contains the source question, definitions, proof intuition, deterministic lemma, random covering lemma, theorem, comparison, novelty audit, limitations, and human-review notice.
- All five pages of the final 120-DPI render were inspected; no clipping, overlap, overflow, corrupt glyphs, or unreadable content was found.
- The ledger JSON parses successfully and records model `GPT5.6`.

## Review status

Human expert review remains pending. Priority checks are the normalized cap
constant, the support-function containment, and whether an equivalent
projection estimate appears outside the bounded arXiv search.
