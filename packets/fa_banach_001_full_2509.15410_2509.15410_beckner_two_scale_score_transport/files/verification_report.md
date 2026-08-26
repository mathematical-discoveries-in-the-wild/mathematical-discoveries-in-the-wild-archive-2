# Verification report

Verdict: `candidate_full_solution_likely_valid`.

## Claim checked

For every `1 < p <= 2`, the joint and mixture in the Euclidean setup of
arXiv:2509.15410 inherit `Phi_p`-Sobolev inequalities under the packet's
power-divergence score-transport condition. Pointwise bounded scores imply
this condition with the exact bound `L=B`; the source MGF condition implies it
with `L^2=p barL^2`.

## Adversarial step check

| Step | Status | Notes |
| --- | --- | --- |
| Phi-entropy decomposition | valid | Expanding both sides cancels the conditional-mean power exactly. |
| Differentiation of `M(y)` | valid under source regularity | Gives the direct `y` derivative plus `E(psi s_y)`; this is the same differentiation assumption used in the source. |
| Direct derivative estimate | valid | Weighted Cauchy--Schwarz followed by concavity of `1/Phi_p'' = t^(2-p)/p`. |
| Homogeneity identity | valid | With `h=psi/M`, `Ent_{Phi_p}(psi)=M^p D_p(h)` exactly. |
| Score estimate | valid | Multiplication by `Phi_p''(M)=pM^(p-2)` yields `pM^p`; the `2/p` in score transport cancels the `p`. |
| Conditional Beckner insertion | valid | `2L^2 Ent <= beta L^2 E[Phi_p''(psi)|grad_x psi|^2]`. |
| Joint coefficient bookkeeping | valid | The coefficients are `beta+alpha(1+C^-1)beta L^2` and `alpha(1+C)`. |
| Mixture specialization | valid | The test function is independent of `y`, so the direct derivative term vanishes and the coefficient is `beta+alpha beta L^2`. |
| Closed form for `zeta` | valid | Re-derived by equating the two monotone branches and checked numerically on 5,000 positive triples. |
| Sharp power Pinsker | valid | Conditional Jensen reduces to a scalar function with zero value and derivative at zero; its second derivative is at least `4p`. |
| Bounded-score corollary | valid | Score centering plus power Pinsker gives score transport with `L=B`. |
| MGF corollary | valid, conservative | The entropy variational inequality gives mean shift squared at most `2 barL^2 KL`; Jensen and `log z <= z-1` give `KL <= D_p`. |
| Variance obstruction | valid | The constructed score is in `L^2`, while densities concentrating on `A_n` make the score-transport quotient asymptotic to `(p-1)n`. |
| Nonnegative test functions | routine | `psi+epsilon` and monotone convergence handle the singular weight for `p<2`; truncation/smoothing is standard in the source setup. |

No unproved mathematical dependency remains in the stated theorem.

## Computational checks

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2509.15410_beckner_two_scale_score_transport/code/verify_beckner_score_transport.py
```

Output:

```text
power-Pinsker binary cases: 441007
bounded-score random cases: 25000
zeta formula cases: 5000
variance-obstruction ratios: 1.06667 1.50294 2.00003 2.5 3 3.5 4 4.5 5 5.5 6
all finite sanity checks passed
```

These finite checks do not replace the proof.

## Source and rendering checks

- `source_paper.pdf` was compiled locally from the ingested official arXiv
  source and bibliography for arXiv:2509.15410; it has 25 pages.
- The exact Beckner question begins on source PDF page 21 and continues on
  page 22.
- `open_problem_crop_1.png` and `open_problem_crop_2.png` are real crops of
  those rendered source pages, use the full readable text width, and together
  contain the question, the anticipated conclusion, and the complete stated
  proof obstruction.
- `solution_packet.pdf` was compiled with build artifacts confined to `tmp/`.
- The final packet has 8 pages. Every page was rendered at 150 dpi and
  visually inspected after the last mathematical correction. No clipped
  formulas, overlaps, broken glyphs, unreadable evidence, or unresolved
  references were found.
- The final LaTeX log contains no overfull/underfull box warnings or undefined
  references.

## Novelty check

Bounded arXiv/web searches on 2026-08-11 used the exact title, arXiv id,
author, Section 6.1 wording, and close keyword variants. No later paper
explicitly answering the question was found. Agrawal--Horel
(arXiv:2006.05973) is relevant general divergence/IPM context but does not
state this two-scale result. This is evidence of plausible novelty, not a
comprehensive literature certification.

## Scope and verifier focus

- The factor `p` in the MGF proxy is not claimed optimal.
- Variance alone is shown insufficient for this score-transport mechanism,
  not disproved as a hypothesis for every conceivable inheritance proof.
- The abstract score-transport condition is sufficient, not claimed
  necessary.
- The source's separate HMC regularity program remains open.

Recommended human focus: the factor cancellation in the normalized score
estimate and the lower bound on the scalar second derivative in the sharp
power-Pinsker lemma.

