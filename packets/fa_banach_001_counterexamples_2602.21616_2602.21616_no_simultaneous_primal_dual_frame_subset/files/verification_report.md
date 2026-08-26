# Verification report

## Verdict

Likely valid full negative answer to Remark 3.4(b) of arXiv:2602.21616.
Human review is recommended before dissemination.

## Claim audited

There exists a normalized unconditional Schauder-frame pair `(x_n,y_n)` in a
separable infinite-dimensional Hilbert space, with all `y_n` nonzero, such
that no subset `J` makes both `(x_n/||x_n||)_{n in J}` and
`(||x_n||y_n)_{n in J}` frames.

## Adversarial checks

1. **Definition and orientation.** The source defines associated coefficient
   vectors by `z = sum_n <z,y_n>x_n`. The construction uses
   `x_{k,j}=e_k` and `y_{k,j}=e_k/k`, so each of the `k` summands in block `k`
   is exactly `(z_k/k)e_k`. There is no swap of analysis and synthesis roles.

2. **Ordinary sequence indexing.** The triangular index set
   `{(k,j): k>=1, 1<=j<=k}` is countable. Any fixed bijection with the natural
   numbers gives a sequence of precisely the kind used in the source.

3. **Semi-normalization and nonzero vectors.** Every primal vector has norm
   one, so the sequence is normalized (hence semi-normalized). Every
   coefficient vector has norm `1/k>0`; no reconstruction is hidden in zero
   functionals.

4. **Unconditional convergence.** A finite partial sum has `k`th diagonal
   multiplier `r_k(F)/k`, always in `[0,1]`. Once a finite set contains every
   index in the first `K` blocks, its error is supported after `K` and has norm
   at most the `l2` tail norm of `z`. This proves convergence of the net over
   finite subsets, the standard unconditional convergence criterion.

5. **Exact primal frame form.** Selecting `r_k` copies of `e_k` gives
   `sum r_k|z_k|^2`. If this is a frame with upper bound `B`, the test `z=e_k`
   gives `r_k<=B` for every `k`. (Its lower bound would additionally require
   `inf r_k>0`, but that is not needed for the contradiction.)

6. **Exact coefficient frame form.** Because `||x_{k,j}||=1`, the selected
   rescaled coefficient vectors are `e_k/k`, repeated `r_k` times. Their frame
   form is `sum (r_k/k^2)|z_k|^2`. A lower frame bound `A'>0` would require
   `r_k/k^2>=A'` for every `k`.

7. **The contradiction uses compatible quantifiers.** If both selected
   sequences were frames, the same multiplicities would satisfy
   `A' <= r_k/k^2 <= B/k^2` for all `k`, impossible as `k` tends to infinity.
   No uniformity across different subsets is assumed.

8. **Consistency with the source theorem.** Selecting one copy in every block
   makes the normalized primal vectors an orthonormal basis. Hence the example
   respects, rather than challenges, the paper's theorem that a normalized
   primal frame subsequence exists. The obstruction is solely simultaneous
   control of the paired coefficient vectors.

9. **No finite-dimensional loophole.** The failure occurs along infinitely
   many coordinates. Every finite truncation could have a positive lower
   coefficient-frame bound, but these bounds decay as the truncation grows;
   the source asks for a frame on the full infinite-dimensional space.

## Literature and novelty check

The four cheap run indexes had no entry resolving this arXiv id or the exact
question. Targeted searches on 11 August 2026 for the exact wording of Remark
3.4(b), the paper title, and simultaneous normalized-primal/rescaled-dual frame
subsets returned the source paper and unrelated frame literature, but no later
resolution. This bounded search is not a substitute for expert review, and the
novelty status is provisional because the source is recent.

## Recommended verifier focus

Confirm the source convention `sum <z,y_n>x_n` and the unconditional-net
criterion. Once those are fixed, the diagonal frame-bound contradiction is
exact and immediate.
