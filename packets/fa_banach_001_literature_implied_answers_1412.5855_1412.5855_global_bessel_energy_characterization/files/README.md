# Global Bessel-energy characterization of nonnegative `H^{-1}` measures

Status: `literature_implied_answer_full`  
Source: arXiv:1412.5855, Problem A  
Agent: `agent_lane_03`  
Model: `GPT5.6`

## Result

For every finite nonnegative Radon measure `mu` on `R^2`,

```text
mu belongs to H^{-1}(R^2)
```

if and only if its positive logarithmic energy

```text
integral integral log^+(1/|x-y|) dmu(x) dmu(y)
```

is finite.  This removes the compact-support hypothesis from the criterion
quoted immediately after Problem A and characterizes the whole space named in
that problem.

The result is classified as literature-implied, not original: it is the
two-dimensional order-two Bessel-energy criterion from classical Bessel
potential theory, together with the standard `K_0` asymptotics.  The packet
includes a self-contained heat-kernel proof of the specialization.

## Contents

- `solution_packet.pdf`: statement, proof, intuition, provenance, and review
  recommendation.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv PDF of arXiv:1412.5855.
- `source_excerpt_problem_A_pages_1_2.pdf`: exact problem and the source's
  compact-support criterion.
- `supporting_aronszajn_smith_1961.pdf`: primary Bessel-potential reference.
- `supporting_excerpt_bessel_kernel_printed_413_415.pdf`: Fourier formula,
  `K_0` formula, and small/large-argument asymptotics.
- `figures/source_problem_crop.png`: rendered crop of Problem A.
- `verification.md`: mathematical and packet-QA record.

## Scope

The characterization is for finite nonnegative measures, exactly the source's
`M_+(R^2)`.  Positivity is used in Tonelli's theorem and in comparing energies;
no analogous criterion in terms of the unsigned positive logarithmic energy is
claimed for arbitrary signed measures.
