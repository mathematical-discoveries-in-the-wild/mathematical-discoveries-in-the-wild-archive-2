# Candidate full solution: optimal gamma-plus-one tail loss

Status: candidate full solution, likely valid, pending human verification.

Source: E. Ostrovsky and L. Sirota, *Maximal and other operators in
exponential Orlicz and Grand Lebesgue Spaces*, arXiv:1706.07539 (2017),
Example 3.2 and the open question following (3.19b), pp. 17–18.

## Result

The optimal universal exponent in (3.19b) is exactly `gamma + 1`.

The paper supplies the upper bound. The packet proves sharpness by constructing
a positive linear operator that is contractive on every `L^p`, `1 <= p <= b`,
and a function with source tail

`y^{-b} (log y)^gamma L(log y)`

whose image attains the `gamma + 1` logarithmic power along a sparse sequence.
The mechanism is an equal-mass atomic block operator that gathers the block's
`ell^b` energy into one atom; the harmonic sum supplies the extra logarithm.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop_page17.png`: assumptions and (3.19a).
- `figures/open_problem_crop_page18.png`: (3.19b) and the exact open question.
- `code/check_finite_blocks.py`: finite-block consistency check.

## Verification and novelty

The formal proof is analytic; the script only checks representative finite
blocks. Run it from the packet directory with
`python code/check_finite_blocks.py`. For `b=2`, `gamma=0.5`, `L=1`,
`alpha=0.8`, and `R=4,6,8,10,12`, the norming vector had `ell^{b'}` norm one
to twelve displayed decimals, every tested `ell^{p'}` norm was at most one,
the normalized `gamma+1` output scale stayed between 0.66 and 0.70, and the
obstruction ratio for `beta=gamma+0.5` increased from 1.51 to 2.56. This is a
consistency check, not a proof.

A bounded novelty search covered the local run indexes and exact-title,
exact-question, and core formula/keyword web searches. No later arXiv or other
primary-source answer to the exact question was found. This does not replace a
definitive citation review.

Human review should focus on the regular-variation tail bookkeeping across
blocks and the simultaneous `L^p` contraction argument.

Ledger:
`runs/fa_banach_001/ledger/results/1706.07539_optimal_gamma_plus_one_tail_loss.json`
