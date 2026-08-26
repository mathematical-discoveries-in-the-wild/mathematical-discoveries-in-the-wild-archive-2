# Full weighted Lp compact Toeplitz characterization

Run: fa_banach_001

Agent: agent_lane_00

Model: GPT5.6

Status: full_solution_likely_valid

## Source question

Stockdale and Wagner, *Weighted theory of Toeplitz operators on the Bergman
space*, arXiv:2107.03457, Open Question 1.13 on PDF page 8, ask for a
characterization of bounded symbols u for which T_u=P M_u is compact on the
full weighted space L^p_sigma, for 1<p<infinity and sigma in B_p.

## Result

Let q=p/(p-1) and let tau=sigma^(1-q) be the dual Békollé-Bonami weight.
For any fixed positive Bergman radius r, the packet proves

    T_u compact on L^p_sigma
      iff lim_{|a|->1} [1/tau(D(a,r))]
          integral_{D(a,r)} |u|^q tau dV = 0.

The route is exact Banach duality:

    T_u^*=M_conj(u) P on L^q_tau.

Since P projects onto A^q_tau, compactness is equivalent to compactness of
multiplication by conj(u) from A^q_tau to L^q_tau. A self-contained weighted
compact Carleson lemma then gives the displayed local-density criterion.

## Verification focus

- Check the standard passage from the tent definition of B_q to its
  fixed-radius Bergman-ball form.
- Check the normalized peak-function estimate. The annular sum is geometric
  after choosing an integer N>n+1.
- Check the adjoint identity first on bounded compactly supported functions,
  then extend by density and boundedness.

The bounded novelty search found arXiv:2501.13571 answering the distinct
analytic-space Open Question 1.14, and general weighted Carleson theory of
Tong--Li, but no exact full-L^p_sigma statement. Novelty confidence is
moderate; validity confidence is high.

## Files

- main.tex: full proof packet.
- solution_packet.pdf: compiled review document.
- source_paper.pdf: arXiv:2107.03457.
- figures/open_problem_crop.png: Open Question 1.13 and context.
- VERIFIER_REPORT.md: independent checklist and proof-risk summary.
