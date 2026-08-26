# Verification Report

Candidate: Question 8.2 in arXiv:2512.24575

## Claim checked

For every (N\ge3), positive-entry (A\succeq0), and nonintegral
(alpha>N-2), the derivative matrix (mathcal B(\alpha,A)) is positive
semidefinite. Consequently the exact Jury fractional-power positivity set is
(mathbb Z_{\ge0}\cup[N-2,\infty)).

## Verdict

`likely valid; full-scope literature-implied answer`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Kernel identity (F_A(x,y)=v(x)^TAv(y)) | valid | Direct expansion. |
| Sample matrix (C_h=V_hAV_h^T\succeq0) | valid | Ordinary congruence. |
| Entries of (C_h) are positive and remain in (I) | valid | All coefficients of (F_A) are positive; for the general transfer lemma, continuity at (F_A(0,0)=a_{00}\in I) suffices for small (h). |
| FitzGerald--Horn applies | external, verified | Theorem 2.1 of arXiv:1311.1581 states that entrywise powers preserve (N\times N) positivity for (alpha\in\mathbb N\cup[N-2,\infty)). |
| Difference congruence is positive | valid | (L_h f[C_h]L_h^T\succeq0) for every (h>0). |
| Congruence entries converge to mixed derivatives | valid | They are the standard forward-difference quotients of orders (i,j). |
| Limit remains positive | valid | The finite-dimensional positive semidefinite cone is closed. |
| Exact classification | valid | Sufficiency is the transfer argument; necessity below (N-2) is Theorem E(b) in the source. |

## Counterexample search

The exploratory script tested 390,000 positive-entry Gram matrices:

- (N=3), (alpha=1.01,1.2,1.5,1.9,2.5), 60,000 matrices each;
- (N=4), (alpha=2.1,2.5,3.5), 30,000 matrices each.

It sampled ranks (1,ldots,N). No normalized negative eigenvalue below
(-10^{-8}) occurred. Tiny negative values were at floating-point roundoff
scale for rank-deficient matrices. The computation is not used in the proof.

## External dependencies

- FitzGerald--Horn's entrywise-power theorem, verified through Theorem 2.1 of
  arXiv:1311.1581 and the 1977 article metadata.
- Proposition 8.3 and Theorem E(b) of arXiv:2512.24575.

## Gaps

No mathematical gap located. Novelty is deliberately not claimed: the answer
is classified by provenance as an implication of a known theorem.

## Confidence

Score: 98/100.

Reason: every nonexternal step is an elementary identity, congruence, or
finite-difference limit; the decisive external theorem is quoted explicitly
in both the source and supporting paper.

## Human review recommendation

Send to a human reviewer and check the lower-triangular difference matrix
indices once. If confirmed, record Question 8.2 and the open part of Theorem E
as fully resolved by literature implication.
