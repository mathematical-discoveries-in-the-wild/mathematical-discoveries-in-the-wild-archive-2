# Counterexample packet for arXiv:2305.09234

Status: **candidate counterexample / full negative resolution of the intended
finite-normalization conjecture; likely valid, pending human review**.

For two independent uniform samples on `[0,1]`, the packet proves

    E M_{1/2} = Theta(sqrt(n) log n).

Consequently

    E M_{1/2} / sqrt(n log n) = Theta(sqrt(log n)) -> +infinity.

This contradicts the finite `limsup` asserted as equation (1.2) of Goldman and
Trevisan and refutes the intended finite-limit conjecture immediately following
it.  The wording caveat matters: as an extended-real limit, the displayed
quantity *does* exist for the uniform law and equals `+infinity`.

The upper bound is equation (12) of Bobkov--Ledoux's published 2024 correction.
The new lower bound is obtained from a sample-adapted signed dyadic-tent witness
in Kantorovich--Rubinstein duality.  Every dyadic level through scale `1/n`
contributes a constant multiple of `sqrt(n)` in expectation.

Contents:

- `solution_packet.pdf`: complete review packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original open-question paper.
- `supporting_bobkov_ledoux_2024_correction.pdf`: decisive published correction.
- `figures/open_problem_crop_part1.png`, `open_problem_crop_part2.png`: the
  two-page source question.
- `figures/correction_notice_crop.png`, `corrected_bound_crop.png`: correction
  notice and corrected critical upper bound.
- `code/verify_multiscale_witness.py`: deterministic regression checker.
- `verification.md`: commands, outputs, hashes, and reviewer checklist.

Human review should focus on the uniform Hoelder estimate for arbitrary tent
signs, the moment-to-absolute-moment lower bound, and the interpretation of the
source's word “exists” in light of its explicitly asserted finite limsup.
