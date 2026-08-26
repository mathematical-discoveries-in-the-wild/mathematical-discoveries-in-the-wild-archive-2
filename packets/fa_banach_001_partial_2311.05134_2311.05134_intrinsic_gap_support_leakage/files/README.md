# Intrinsic-gap control of support leakage for sliced-Wasserstein geodesics

Status: `candidate partial result, likely valid`.

Source: Sangmin Park and Dejan Slepčev, *Geometry and analytic properties of
the sliced Wasserstein space*, arXiv:2311.05134; Journal of Functional
Analysis 289 (2025), article 110975. Remark 4.7 on printed/PDF page 26 asks
whether an intrinsic sliced-Wasserstein geodesic between measures supported in
the closed unit ball remains supported there.

## Candidate result

Let `L=ell_SW(mu_0,mu_1)` and `D=SW(mu_0,mu_1)`. For any constant-speed
`ell_SW` geodesic `(mu_t)` between measures supported in the unit ball, define

```text
Leak(mu)^2 = average_theta integral (|r|-1)_+^2 d(R_theta mu)(r).
```

Then, for every `t`,

```text
Leak(mu_t) <= min(tL,(1-t)L, (1/2)sqrt(L^2-D^2)).
```

Consequently every intermediate measure remains in the unit ball whenever
`ell_SW(mu_0,mu_1)=SW(mu_0,mu_1)`. This gives a complete affirmative answer
for pairs with one Dirac endpoint, pairs supported on one affine line, and
pairs related by a positive affine homothety. It also applies to every pair
admitting an extrinsic sliced-Wasserstein geodesic.

The proof uses the quantile isometric embedding of sliced Wasserstein space
into a Hilbert space. Unit-ball support becomes membership in the convex
pointwise box `|q(theta,s)|<=1`. A Hilbert-space projection inequality bounds
the distance of any point on the intrinsic geodesic from that box by the gap
between intrinsic length and the endpoint chord.

## Scope and novelty

The general question remains open here because coordinatewise clipping of
directional quantiles need not satisfy Radon consistency and therefore need
not represent a probability measure. The source paper already describes the
slice interpolation when an intrinsic geodesic attains `SW`, so the qualitative
zero-gap observation is close to implicit there. The main candidate-new part
is the quantitative leakage inequality and its uniform application to every
intrinsic geodesic. Known translation/dilation geodesics are not claimed as
new.

A bounded search through 11 August 2026 found Hopper, arXiv:2407.07219, on
additional extrinsic sliced-Wasserstein geodesics, and Han,
arXiv:2605.25453, on rigidity of the different deficit
`W^2/d-SW^2`. Neither source located in the search states the intrinsic-gap
leakage estimate or resolves the ball-support question.

## Files

- `main.tex` and `solution_packet.pdf`: theorem, proof, upgrade attempts, and
  literature audit.
- `verification.md`: independent proof checklist.
- `source_paper.pdf`: arXiv:2311.05134.
- `supporting_paper_2407.07219.pdf`: later extrinsic-geodesic paper.
- `supporting_paper_2605.25453.pdf`: later sliced-deficit rigidity paper.
- `figures/open_problem_crop.png`: source question on PDF page 26.

Human review focus: check the Hilbert projection lemma and the identification
of distance to the quantile box with the displayed leakage functional.

