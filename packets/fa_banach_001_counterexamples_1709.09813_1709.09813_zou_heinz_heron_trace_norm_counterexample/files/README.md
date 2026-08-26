# A 2×2 Counterexample to Zou's Heinz–Heron Norm Conjecture

Status: `full_counterexample_pending_human_review`

## Result

The Conjecture in Remark 4.2 of L. Zou, *Inequalities related to Heinz and Heron means*, J. Math. Inequal. 7 (2013), is false.

For the trace norm, take

- `nu = 17/20`, so `alpha(nu) = 49/100`;
- `A = diag(exp(3/5), exp(13/5))`;
- `B = diag(1, exp(9/5))`;
- `T = (1/10) [[5,-8],[-1,4]]`;
- `X = A^(-1/2) T B^(-1/2)`.

Then

`(1/2)||A^nu X B^(1-nu) + A^(1-nu) X B^nu||_1`

is strictly larger than

`(1-alpha)||A^(1/2) X B^(1/2)||_1 + alpha||(AX+XB)/2||_1`.

Exact rational interval arithmetic proves a gap greater than `1001/10^6`. Direct numerical evaluation gives a gap about `0.0011933767`.

## Important source correction

The lane target arXiv:1709.09813 misquotes Zou's second Heinz term as `B^nu X A^(1-nu)`. Zou's original Conjecture (4.2) has the standard `A^(1-nu) X B^nu` term. The packet refutes that correctly stated original conjecture; it does not exploit the transcription error.

## Files

- `main.tex`, `solution_packet.pdf`: complete proof, exact certificate, intuition, provenance, and scope.
- `verify_counterexample.py`: dependency-free exact-rational interval verifier.
- `source_paper.pdf`: lane target arXiv:1709.09813.
- `supporting_zou_2013.pdf`: original primary statement of the conjecture.
- `supporting_gao_ma_2018.pdf`: related later norm-inequality paper checked during provenance review.
- `references.md`, `verification_report.md`: evidence and QA records.

## Human review

- [ ] A human expert has independently checked the proof and novelty status.
