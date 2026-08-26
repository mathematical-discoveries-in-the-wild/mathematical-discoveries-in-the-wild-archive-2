# Verification

Status: candidate_substantial_partial_likely_valid_needs_human_review

## Target and source checks

- arXiv:1411.5794 genuinely identifies higher-dimensional star discrepancy
  and matching supercritical exponential-Orlicz lower estimates as open.
- Its Proposition 2.2 gives the equivalence between the exp(L^beta) norm and
  the supremum of p^(-1/beta)||f||_p over p>1.
- The critical lower bound follows immediately by taking p=2 and applying
  Roth; the later arXiv:1604.08713 explicitly records this baseline and
  distinguishes it from a matching lower bound.
- arXiv:0705.4619 supplies the short Riesz-product construction, bounded
  L_1 norm of the strongly-distinct test, its discrepancy pairing, uniform
  partial-product L_2 and crude L_4 estimates, and the coincidence-graph
  summability estimate used here.

## Quantitative proof checks

- With b=1/4, the source's partial-product second moment is
  exp(C q^(2b)) = exp(C sqrt(q)).
- In the coincidence expansion Psi_neg=sum_G A_G B_G, the original proof
  establishes sum_G ||A_G||_s <= C for s=q^(2b)=sqrt(q).
- For 1/2=1/s+1/r, one has r=2s/(s-2) and, for s>=4, 2<=r<=4.
- The interpolation parameter between L_2 and L_4 is exactly 4/s:
  1/r=(1-4/s)/2+(4/s)/4.
- Uniform L_2 <= exp(C sqrt(q)) and L_4 <= (Cq)^q therefore give
  L_r <= exp(C sqrt(q) log(2q)).
- Hölder and graph summability give the same L_2 bound for Psi_neg, hence
  for Psi_sd=Psi-1-Psi_neg.
- Interpolating Psi_sd between L_1 and L_2 at p'=p/(p-1) uses parameter
  2/p and yields a bounded dual norm when p >= C sqrt(q) log(2q).
- Duality then yields
  ||D_P||_p >= c q^(1/4) n^((d-1)/2) at that growing moment.
- Multiplication by p^(-1/beta) gives
  q^(1/4-1/(2 beta)) (log q)^(-1/beta).
- Since q~n^epsilon, eta_d=epsilon/4, and n~log N, this is precisely
  the exponent and the log log N factor stated in the theorem.
- The improvement over Roth is positive exactly when beta>2.

## Scope and obstruction checks

- The packet does not call the critical Roth consequence novel.
- It does not claim a matching supercritical lower bound.
- Allowing a general short-product exponent b<=1/4 gives test gain q^b
  and coincidence moment cost at least q^(1-2b) with the available
  estimates. The condition for an Orlicz gain is
  b>(1-2b)/beta, whose best threshold at b=1/4 is beta>2.
- Reaching beta<=2 requires new coincidence control or a different test;
  iterating the same parameter balance cannot do it.

## Literature and artifact checks

- Cheap run indexes contain no prior packet or ledger entry for
  arXiv:1411.5794.
- Bounded primary-source searches found no later duplicate of the theorem.
- All three official arXiv PDFs open as valid PDFs.
- main.tex compiled without errors.
- solution_packet.pdf was rendered page by page and visually inspected.
