# Verification record

Verified at: 2026-08-17T20:41:31Z

Verdict: `candidate_counterexample_likely_valid` — a full counterexample to
the literal question in arXiv:math/0401078 asking for an instance where the
polynomial capacities `Theta` and `Gamma` really differ.

## Mathematical audit

- For every `m>=2`, `0<=k<=m-2`, `1<=p<infinity`, and `alpha>0`, take a
  nonzero `P0 in P_k`, a polynomial `H in P_{m-1}\P_k` with no terms of
  degree at most `k`, and
  `A_epsilon=span{P0+epsilon H}`.
- For sufficiently small positive `epsilon`, every nonzero generator passes
  the `Theta` dominance condition.  Its nonpolynomial remainder and its
  `m`-th derivative both vanish, hence `Theta=0`.
- If `w in U_{P,A_epsilon}`, then on `Q` one has
  `w=P+t(P0+epsilon H)`.  Higher-order Poincare gives
  `||nabla^m w||_{L^p(2Q)} >= c_Q ||w||_{L^p(Q)}`.
- The finite-dimensional angle
  `delta_epsilon=inf_{||P||_p=1,t} ||P+t(P0+epsilon H)||_p` is positive.
  Indeed, convergence to zero in the quotient
  `P_{m-1}/P_k` forces `t epsilon [H]` to zero, hence `t` to zero, and then
  contradicts `||P||_p=1`.  Therefore
  `Gamma >= c_Q^p delta_epsilon^p > 0`.
- A cutoff equal to one on `Q`, with `P=-P0` and
  `w=epsilon eta H`, gives `Gamma <= C epsilon^p`; thus the counterexamples
  can approach the zero-capacity boundary.
- In the explicit example `Q=(-1,1), m=2, k=0, p=2, alpha=1`, and
  `A=span{1+x/2}`, the normalized squared trace distance is
  `(1+t)^2+t^2/12`, whose exact minimum is `1/13`.

## Upgrade record

Six materially distinct stages were completed: a singleton construction,
upgrade to a vector subspace, a uniform Gamma lower bound, a quantitative
upper bound, extension to every nontrivial index, and an exact concrete
audit.  The construction covers precisely `k<=m-2`; the source already
proves equivalence at `k=m-1`.  It answers the capacities question for
arbitrary subsets of `W^{m,p}(Q)` but does not resolve possible equivalence
on narrower geometric families used in spectral synthesis.

## Literature audit

Bounded primary-source searches through 2026-08-17 located the source paper
and the 2004 follow-up arXiv:math/0401253, which repeats the equivalence
question.  No later primary source recording this separation was found.
This is a novelty screen, not a definitive priority determination.

## Computational and packet checks

- `python code/verify_explicit_example.py` passed using exact rational
  arithmetic and returned the minimum `1/13`.
- LaTeX compiled without overfull boxes, underfull boxes, undefined
  references, or warnings matched by the packet log audit.
- The final packet has three A4 pages.  Every page was rendered at 180 dpi
  and visually inspected; all mathematics, the source crop, and references
  are readable and unclipped.

SHA-256:

- `solution_packet.pdf`: `cce0b3104b2429de10e1e4bd60fd7b555850350a260139e5e74abd0105793545`
- `source_paper.pdf`: `99cfb06de5fe95deb3879e3efde4da9d6127d815212fc836f036316f917f2e64`
- `figures/open_question_crop.png`: `427b841d17a159c92525b14d198de4ac113dec2e04d155278bf7af6f852e6b52`
- `code/verify_explicit_example.py`: `12b9c010aaed992a358b642b67c2dd6c29cef1cecbe5c63aa3e230f2aa9ed682`

## Human review priorities

1. Confirm that the source's projection convention identifies the
   degree-at-most-`k` and higher-degree parts of these exact polynomials as
   used here.
2. Confirm that the nonzero-`P` restriction implicit in the quotient
   defining `Gamma` is read exactly as in the packet.
3. Recheck the higher-order Poincare estimate for `W_0^{m,p}(2Q)` and the
   finite-dimensional quotient argument.
4. Repeat the novelty search beyond arXiv before dissemination.
