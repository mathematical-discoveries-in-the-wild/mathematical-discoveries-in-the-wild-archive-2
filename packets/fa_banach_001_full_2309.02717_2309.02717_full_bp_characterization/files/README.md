# Full Besov characterization for the generalized Cesaro-like operator

Status: `claimed full solution, likely valid, subject to human review`

Source: Pengcheng Tang, “Generalized Cesàro-like operator from a class of
analytic function spaces to analytic Besov spaces,” arXiv:2309.02717. The
introduction asks for boundedness and compactness criteria for
`C_{mu,alpha}: B_p -> B_p`, `p>1`.

## Full result

Let `1<p<infinity`, `alpha>0`, and

`mu_n = integral_0^1 t^n dmu(t)`.

For `N>=2`, put

`Phi_N = log(eN)^(p-1) sum_{n>=N} (n+1)^(p alpha-1) mu_n^p`.

The packet proves:

- `C_{mu,alpha}` is bounded on `B_p` if and only if `sup_N Phi_N<infinity`.
- `C_{mu,alpha}` is compact on `B_p` if and only if `Phi_N -> 0`.

This covers every parameter in the source question, including the previously
untreated regimes `p!=2` and `0<alpha<1`.

For every `p>1` and `alpha>0`, the measure

`dmu_alpha(t)=(1-t)^(alpha-1)/log(e/(1-t)) dt`

gives a bounded but noncompact operator. Its moments satisfy
`mu_{alpha,n} asymp n^(-alpha)/log n`, so `Phi_N asymp 1`.

## Proof mechanism

The factorization

`C_{mu,alpha} = M_mu ((1-z)^(-alpha) .)`

is combined with the dyadic analytic Besov norm

`||f||_{B_p}^p asymp |a_0|^p + sum_j 2^j ||Delta_j f||_{H^p}^p`.

If `x_j=2^(j/p)||Delta_j f||_{H^p}`, the output block sizes are bounded by

`2^(j alpha) mu_(2^(j-1)) sum_{l<=j} x_l`.

The exact discrete weighted Hardy criterion gives the upper bound. Normalized
logarithmic polynomials and positivity on a short boundary arc recover the
same dyadic tail, proving necessity and the compactness criterion.

## Verification and novelty

- The theorem specializes at `p=2` to the previous lane-4 Dirichlet packet.
- At `p=2, alpha=1`, it matches Bao--Guo--Sun--Wang, arXiv:2401.09188.
- A checker evaluates the boundary moments and tail products for several
  `(p,alpha)` pairs.
- The proof packet is compiled and every page is rendered and visually
  inspected before delivery.
- The bounded novelty search covered the run indexes, local arXiv sources,
  arXiv:2305.02717, the source title/id, exact operator formula, and current
  web results. No full self-map characterization for all `p,alpha` was found.

Human review should focus on the dyadic analytic Besov norm and the two cases
of the frequency-separated product estimate. The remaining Hardy and
positive-coefficient arguments are explicit.

Files:

- `main.tex`, `solution_packet.pdf`: full proof packet.
- `source_paper.pdf`: original paper containing the open question.
- `supporting_paper_2401.09188.pdf`: later `p=2, alpha=1` comparison.
- `figures/open_problem_crop.png`: source question.
- `code/check_boundary_measure.py`: general-parameter numerical sanity check.
- `tmp/pdfs/`: LaTeX and rendering intermediates.
