# Verification report

## Claimed result

For every 0<p<1, with q=p_flat=2p/(2-p), there is a matrix

    W in ell^q(ell^infinity) subset Y_q

that does not belong to ell^infinity tensor_p ell^infinity. This gives a
full negative answer to Remark 1 on page 20 of arXiv:1910.06891.

## Audit table

| Check | Result | Reason |
|---|---|---|
| Critical exponent | pass | 1/q=1/p_sharp+1/2 exactly, so each flat-unitary block contributes c_j^q to the row-envelope mass. |
| Membership in Y_q | pass | The row suprema form a sequence alpha with sum alpha_i^q=sum_j c_j^q<infinity. |
| Singular-value lower bound | pass | Removing rank at most an from c n^{-1/p_sharp}U_n leaves at least (1-a)n singular values at that scale. |
| Far-tail estimate | pass | Monotonicity of lambda_k and lambda in ell^p give sum_{k>bn}lambda_k <= (bn)^{-1/p_sharp}||lambda||_p. |
| Window inequality | pass | Schatten p-subadditivity yields sum_{an<k<=bn}lambda_k^p >= c^p(1-a)-b^{p-1}||lambda||_p^p. |
| Disjoint windows | pass | n_{j+1}>=4b_jn_j makes (n_j/4,b_jn_j] pairwise disjoint. |
| Error absorption | pass | With b_j=c_j^{-2p/(1-p)}, the error is ||lambda||_p^p c_j^{2p}=o(c_j^p). |
| Final contradiction | pass | c_j^p=(j+1)^{-1}, so the mandatory mass over disjoint windows diverges. |

## Independent checks

The script code/verify_exponents.py checks the exact rational exponent
identities for representative rational values of p and verifies numerically
that finite Fourier matrices have flat entries and all singular values equal to
one. It runs under the bundled workspace Python with NumPy.

The proof was also checked through approximation-number language: for any rank
r operator R, the Schatten p error from a scalar unitary is bounded below
by the tail of its constant singular-value list. This reproduces the only
nontrivial lower-bound step without referring to the identity-block geometry in
the source paper.

## Literature and novelty check

Bounded searches through 2026-08-17 used the exact arXiv id, exact title, the
verbatim open sentence, Y_{p_flat}, p-tensor, Pisier sufficient condition,
and later works citing the 2020 JFA paper. Later cited papers found locally and
on arXiv concern triangular projections, Haagerup tensors, smooth Schur
multipliers, or analytic Schur multipliers. None answers this inclusion.
Novelty is therefore a candidate claim pending MathSciNet/zbMATH and specialist
review.

## Scope and human-review priorities

The proof only answers the Y_{p_flat} inclusion question. It does not address
automatic complete boundedness for 1<p<infinity, the spectral-measure problem,
the diagonal ell^{p_sharp,p} conjecture, or equality with the bounded pointwise
closure of the p-tensor product.

Human review should prioritize the scaled-unitary coefficient-window lemma,
especially the conversion of the far tail from ell^p to ell^1, and the
normalization of an arbitrary tensor representation into a decreasing
nonnegative coefficient sequence.
