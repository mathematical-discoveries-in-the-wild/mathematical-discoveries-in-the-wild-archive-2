# Verification record

## Claim under review

Source Theorem 1.5 improves from residual
`exp(-C/h^(1/7))` to `exp(-C/h^(1/4))` under the same hypotheses.  This fully
answers the source's literal optimality question negatively, without claiming
that `1/4` is the final sharp exponent.

## Source crosswalk

- The exact question is on source PDF page 4 and is preserved in
  `figures/open_question_crop.png`.
- The analytic WKB amplitudes and common local domain are supplied by source
  Theorem 3.2.
- The only recursion used is source equation (3.13), with its displayed
  definitions of `T_j` and `G_j`.
- The old `j^(7j)` estimate is source Lemma 3.9.
- The cutoff, phase positivity, vanishing `a_j(x0)=0` for `j>=1`, and exact
  final transport remainder are taken unchanged from the proof of source
  Theorem 1.5.

## Decomposed mathematical checks

1. **Centered Cauchy estimate.**  If a point has coordinate margins
   `(delta_1,delta_2)` inside a polydisc, Cauchy's formula on circles centered
   at that point gives derivative cost
   `delta_1^(-alpha) delta_2^(-beta)`, with no extra denominator power.

2. **Common analytic neighborhood.**  Theorem 3.2 constructs the amplitudes on
   one real neighborhood, and the proof of Lemma 3.9 fixes uniform complex
   radii in (3.19) before estimating every index.  Thus `2R_1,2R_2` can be
   chosen so that all amplitudes are holomorphic there and `J`, `1/(JV)`,
   `a_0`, `1/A_0`, the coefficients in `G_j`, and the characteristic-curve
   derivative are uniformly bounded.

3. **Curve geometry.**  After shrinking, the source bound
   `|omega(z)|<=C|z|` satisfies `C R_1<R_2`.  For nested radii
   `r_{nu,k}=(2-k/n)R_nu`, a point of the `(k+1)`-st polydisc has margins
   `R_1/n,R_2/n` in the `k`-th polydisc.  Both the segment from `omega(z)` to
   `w` and the segment from `0` to `z`, together with all inserted points,
   stay in the `(k+1)`-st polydisc by convexity and `C R_1<R_2`.

4. **Derivative bookkeeping.**  `T_k` uses only `d_z d_w^2 a_k`.  `G_k` uses
   only `d_z d_w^2 a_k`, `d_z^2 d_w^2 a_k`, and
   `d_z d_w^3 a_k`.  Their total orders are `3,4,4`.  No derivative falls on
   `a_k` outside this list; all other factors are fixed analytic coefficients.

5. **One-step estimate.**  Centered Cauchy at each recursion sample gives
   `||T_k||<=C n^3||a_k||` and `||G_k||<=C n^4||a_k||`.  The two path lengths
   and all fixed coefficients are uniformly bounded, hence
   `||a_{k+1}||_{r_{k+1}}<=C n^4||a_k||_{r_k}`.

6. **Iteration.**  Multiplication over `k=0,...,n-1` yields
   `||a_n||_{R_1,R_2}<=(C n^4)^n||a_0||_{2R_1,2R_2}`.  A final fixed-margin
   Cauchy estimate on half the polydisc gives the same growth, after changing
   the constant, for `a_n`, its gradient, and its Laplacian on a fixed real
   disk.

7. **Optimal truncation.**  With `N=floor((eMh)^(-1/4))`, every `j<=N`
   satisfies `Mh j^4<=e^(-1)`.  Therefore all amplitude/derivative sums used
   in the cutoff proof are uniformly controlled, and the terminal transport
   term is at most `M h^2 e^(-N)`.

8. **Normalization.**  Positive-definite quadratic behavior of `Re P` and the
   amplitude lower bound imply `||u_h||>=c h^(1/2)` in two real dimensions.
   The Gaussian factor in the transport remainder has matching `O(h^(1/2))`
   norm.  The polynomial factors cancel or are absorbed into the exponential.

9. **Cutoff term.**  On `supp grad(chi)`, `Re P` is bounded below by a positive
   constant, while the optimally truncated amplitude and its first derivative
   are uniformly bounded.  The commutator is `O(exp(-c/h))` up to polynomial
   factors, hence smaller than the claimed `exp(-C/h^(1/4))` term.

10. **Gauge restoration.**  Source identity (3.14) already returns from the
    local gauge to the original operator and defines the final phase as
    `P=S+i theta`.  The packet starts from this identity, so it does not assume
    that the generally complex gauge factor has modulus one.

## Deterministic bookkeeping check

Run:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2410.01377_local_cauchy_pseudomode_exponent_improvement/code/verify_exponent_bookkeeping.py
```

The script checks the exhaustive multi-index list, reproduces the source's
combined origin-centered loss `7`, verifies the centered total-order loss `4`,
and checks the truncation inequality over a deterministic grid of parameters.

## Literature audit

- Cheap run indexes and the local parsed full-source corpus contain no prior
  result for arXiv:2410.01377.
- Exact and close official arXiv searches found the source paper but no
  exponent improvement.
- The current source download is the September 2025 revision; the source is
  published in SIAM Journal on Mathematical Analysis 58 (2026), 66--91, DOI
  `10.1137/24M1703628`.  The optimality question and `1/7` bound remain in the
  current source.

## Build and render checks

- `code/verify_exponent_bookkeeping.py`: PASS on 11 August 2026.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error`: PASS.
- Log audit: no warnings, overfull/underfull boxes, undefined references, or
  multiply-defined labels.
- PDF metadata: 4 A4 pages, unencrypted, no JavaScript.
- All four pages rendered at 150 dpi and inspected individually: no clipping,
  collisions, illegible text, broken equations, or malformed source crop.
- Final packet SHA-256:
  `ac276c1503439e53b272840697644f1a06c45aa94865c12ff3c2047d10094f2e`.
- Source PDF SHA-256:
  `e4ad73726e9c3115a6c8fa98da8f106049564b6a25b7c3e75b478c519d4f3c1b`.
