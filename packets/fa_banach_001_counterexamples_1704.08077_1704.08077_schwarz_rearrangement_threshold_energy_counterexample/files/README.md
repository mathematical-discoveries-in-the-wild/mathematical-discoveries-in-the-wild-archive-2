# Schwarz rearrangement can increase the threshold energy

Status: `counterexample_likely_valid` (new result; subject to human review)

## Source problem

Hoai-Minh Nguyen and Marco Squassina, *Some remarks on rearrangement for
nonlocal functionals*, arXiv:1704.08077v2 (2017).

Open Problem 2.2 on arXiv PDF page 5 asks whether

```text
I_delta(u*) <= I_delta(u)
```

for every nonnegative measurable function, where `u*` is the Schwarz
rearrangement.  The exponent `p` is implicit in `I_delta`.

## Counterexample

Take `N=1`, `p=3/2`, and `delta=1`.  Define the nonnegative step function

```text
u = 1 on [-15,-14] U [14,15],
    2 on [-14,7] U [11,14],
    3 on [7,8] U [10,11],
    4 on [8,10],
    0 elsewhere,
```

with endpoint choices immaterial.  Its Schwarz rearrangement is

```text
u* = 1 on [-15,-14] U [14,15],
     2 on [-14,-2] U [2,14],
     3 on [-2,-1] U [1,2],
     4 on [-1,1],
     0 elsewhere.
```

Every adjacent jump is exactly one, while the threshold is strict.  Hence
the singular kernel is never integrated across a touching pair with an
active value gap, and both energies are finite.  Exact interval integration
gives

```text
I_1(u*) - I_1(u) = 0.0431325097966... > 43/1000.
```

Thus Schwarz rearrangement increases this threshold energy.

## Scope

This gives a full negative answer to Open Problem 2.2 under its universal
reading, already in dimension one and at `p=3/2`.  It does not settle the
paper's separate Open Problem 4.1 about distributional Riesz fractional
gradients, nor the fixed-`p` variants outside the exhibited exponent.

Files:

- `source_paper.pdf`: arXiv:1704.08077v2.
- `figures/open_problem_crop.png`: Open Problem 2.2 on source PDF page 5.
- `main.tex`, `solution_packet.pdf`: full exact proof and novelty audit.
- `verification.py`: independent finite-sum and rational-bound check.

