# A log-free p-triangle inequality for Lorentz spaces

Status: `candidate_full_solution_likely_valid`, awaiting expert review.

## Result

For `0<p<1`, `p<r<infinity`, and `theta=1-p/r`, the best constant in

`||sum_k f_k||_{p,r} <= C(p,r) (sum_k ||f_k||_{p,r}^p)^{1/p}`

satisfies

`C(p,r) <= H(theta)^{1/p} p^{-theta}(1-p)^{-theta/p}`,

where

`H(theta)=theta^{-theta}(1-theta)^{-(1-theta)} <= 2`.

In particular,

`C(p,r) <= (2 exp(1/e))^{1/p}`
`          (1-p)^{-(1/p-1/r)}`.

This gives a full negative answer to the explicit question in
arXiv:1801.10570: the logarithmic factor in the source's upper bound is not
necessary.

## Proof mechanism

Each Lorentz function is factorized, using a nonatomic rank variable, into
an `L^p` factor and a weak-`L^p` factor.  Discrete Holder handles the sum;
an elementary weak endpoint estimate and a two-threshold product
rearrangement return it to `L^{p,r}`.  The only interpolation loss is the
binary-entropy factor, uniformly at most two.

## Files

- `solution_packet.pdf`: self-contained theorem and proof.
- `source_paper.pdf`: arXiv:1801.10570.
- `main.tex`: packet source.
- `VERIFICATION.md`: mathematical, novelty, and render audit.

## Scope

The packet removes the logarithm and therefore resolves the source's stated
yes/no problem.  It does not determine the exact optimal value of `C(p,r)`.
Novelty is provisional pending expert literature review.
