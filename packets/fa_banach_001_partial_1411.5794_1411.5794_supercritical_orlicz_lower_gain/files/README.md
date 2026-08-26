# Partial Result: A Supercritical Orlicz Lower Gain for Discrepancy

Status: candidate_substantial_partial_likely_valid_needs_human_review

Run: fa_banach_001  
Agent: agent_lane_07  
Target: Dmitriy Bilyk and Lev Markhasin, *BMO and exponential Orlicz
space estimates of the discrepancy function in arbitrary dimension*,
arXiv:1411.5794.

## Exact target

The source proves optimal-order upper bounds in
exp(L^(2/(d-1))) and interpolated upper bounds in exp(L^beta).
It explains that corresponding lower bounds beyond the critical endpoint are
closely tied to the higher-dimensional star-discrepancy problem.

The critical lower bound itself is not open: the source's norm equivalence
for exp(L^alpha), evaluated at p=2, turns Roth's L_2 lower bound into the
matching critical exp(L^(2/(d-1))) lower bound. The later sequence paper
arXiv:1604.08713 makes this baseline explicit and says that the matching
supercritical scale remains beyond reach.

## New partial result

For every dimension d>=3, there is eta_d>0 such that every N-point set and
every beta>2 satisfy

    ||D_P||_{exp(L^beta)}
      >= c_{d,beta}
         (log N)^((d-1)/2 + eta_d(1-2/beta))
         (log log(e^e N))^(-1/beta).

Thus every fixed beta>2 admits a genuine polynomial-in-log N gain over
Roth's exponent (d-1)/2. As beta tends to infinity, the exponent tends to
the Bilyk--Lacey--Vagharshakyan star-discrepancy exponent
(d-1)/2+eta_d.

The proof extracts growing-p information from the 2008 short Riesz product.
Its strongly-distinct test has bounded L_1 norm and pairing
q^(1/4) n^((d-1)/2) with discrepancy. The full product has
L_2 <= exp(C sqrt(q)); the coincidence-graph summability used in the
original L_1 proof, combined with uniform partial-product L_4 control,
gives

    ||Psi_sd||_2 <= exp(C sqrt(q) log q).

Interpolation bounds the dual norm once p >= C sqrt(q) log q. Choosing that
moment in the Orlicz norm equivalence gives the theorem.

## Scope

This does **not** prove the conjectural matching lower bound
(log N)^(d-1-1/beta). It improves the known baseline only for beta>2.
The short-product parameter balance shows why the present method stops there:
the maximal admissible gain is q^(1/4), while the available coincidence
control costs moments at scale sqrt(q), up to logarithms.

## Files

- main.tex: theorem and full proof.
- solution_packet.pdf: compiled proof packet.
- source_target_1411.5794.pdf: official target paper.
- source_small_ball_0705.4619.pdf: official short Riesz-product source.
- source_sequence_context_1604.08713.pdf: later primary-source context.
- VERIFICATION.md: logical, exponent, novelty, and artifact checks.

## Novelty check

The cheap run indexes were searched for arXiv:1411.5794, its title, star
discrepancy, small-ball, subgaussian, and exponential-Orlicz lower-bound
phrases. Bounded searches of primary arXiv sources found the target, the 2008
small-ball paper, and the 2016 sequence paper, but no later statement of the
growing-moment extraction or the displayed beta>2 lower bound. This is not
an exhaustive literature certification and the result needs expert review.
