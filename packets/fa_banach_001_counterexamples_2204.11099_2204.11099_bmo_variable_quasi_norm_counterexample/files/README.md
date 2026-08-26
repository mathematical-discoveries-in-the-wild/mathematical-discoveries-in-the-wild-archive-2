# Counterexamples for Questions 6.1 and 6.2

Status: `candidate_counterexample_likely_valid`  
Source: arXiv:2204.11099, Questions 6.1 and 6.2  
Agent: `agent_lane_03`  
Model: `GPT5.6`

## Result

Both questions have negative answers as stated.

1. Question 6.1 already fails for a normalized family of Banach function
   spaces.  On each cube, use a probability-weighted `L^1` norm whose density
   decays exponentially away from the central coordinate hyperplane.  Then
   `f(x)=x_1` has uniformly bounded generalized mean oscillation, whereas its
   classical mean oscillation on a cube of side length `L` equals `L/4`.
2. Question 6.2, including the stronger version explicitly proposed in the
   source, fails for a normalized family of quasi-Banach function spaces.  A
   cube-dependent weighted `L^{p_Q}` construction satisfies

   ```text
   BMO -> BMO_X,
   ```

   while `x_1` belongs even to `BMO_X^*` and is not in classical `BMO`.

The second construction works in every fixed dimension.  Its exponent tends
to zero on large cubes.  A small fraction of the probability mass is put on
an extremely tiny concentric cube; the resulting small-exponent power mean
simultaneously absorbs the logarithmic drift of every BMO average and the
linear oscillation of the affine witness.

## Contents

- `solution_packet.pdf` — complete proof and exact source excerpt.
- `main.tex` — packet source.
- `source_paper.pdf` — arXiv:2204.11099.
- `supporting_2606.01688.pdf` — latest directly related preprint found in the
  bounded literature audit.
- `figures/questions_6_1_6_2_crop.png` — exact source-page crop.
- `code/verify_parameters.py` — stable numerical checks of the scale
  identities and analytic bounds.
- `verification.md` — proof, source, build, and visual-QA record.

## Reproduce the parameter check

```bash
conda run --no-capture-output -n sandbox python code/verify_parameters.py
```

The proof is analytic and does not depend on the numerical samples.

## Literature boundary

The journal version appeared in *Mathematische Annalen* 388 (2024),
4053--4082.  Exact-ID, exact-question, citation, and core-keyword searches
through 2026-08-11 found no prior matching counterexample.  The directly
related arXiv:2606.01688 gives further sufficient testing criteria and still
describes characterization directions as open; it does not contain either
construction here.  This is a bounded novelty audit, not a priority claim.

