# Verification report

Status: `full_solution_likely_valid`  
Agent: `agent_lane_03`  
Model: `GPT5.6`

## Source and target

The exact statement is Conjecture 1 on PDF page 12 of arXiv:2001.11614.
The conjecture asks for equivalence of arbitrary representability,
representability by scalar and size-two atoms, and representability with a
single size-two atom. The screenshot in `figures/open_problem_crop.png`
contains the complete statement.

## Proof audit

The following were checked independently while assembling the packet:

1. A finite representing measure is exactly a finite-dimensional real
   tracial direct sum with a normalized tracial state.
2. With `Y^2=1` and `X=[[A,B],[B*,C]]`, direct block multiplication gives all
   displayed moment identities through degree four and
   `Delta=beta_X2-beta_XYXY=4 tau(BB*)`.
3. The proposed size-two atom has density `2 lambda`, diagonal entries equal
   to the two weighted means, and `b^2=tau(BB*)/lambda`; it matches `Delta`
   and cancels every mixed contribution through degree three.
4. Cauchy--Schwarz gives `lambda <= w^2/S <= min(tau(e+),tau(e-))`, so all
   residual masses are nonnegative and the size-two density is at most one.
5. Sherman--Morrison gives the two minimum-fourth-moment formulas. Substitution
   into the fourth-order block identity gives the surplus `G(v)` exactly.
6. The two Cauchy--Schwarz estimates and the elementary two-variable
   inequality give `G(v0)>=0`; continuity and `G(v)->-infinity` produce a
   zero of `G`, hence two flat scalar Hankel extensions.
7. If a base order-one Hankel matrix has rank one, the corresponding corner
   operator is scalar. The formulas reduce to a one-point measure, and all
   `0/0` endpoint terms are harmless limits. If both variance terms vanish,
   the endpoint argument is used directly.

## Computational check

Run:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2001.11614_tracial_y2_single_2x2_reduction/code/verify_random_reduction.py
```

The script generates 5,000 seeded random finite tracial direct sums, verifies
the block moment identities and residual cubic matching, evaluates the exact
Schur-complement surplus, and checks the proved lower bound. It is a
regression check, not part of the proof.

Observed output:

```text
cases=5000 max_identity_error=5.329e-15 min_margin=-1.848e-11
```

The tiny negative minimum is below the script's `2e-7` roundoff tolerance;
the analytic lower bound is nonnegative.

## Novelty check

Search date: 2026-08-09.

- Local parsed arXiv corpus and run registry: exact arXiv id, paper title,
  `tracial moment`, `Y^2=1`, `type (m,1)`, and `atoms of size at most 2`.
- Bounded web/arXiv searches: the same exact phrases, source authors
  Bhardwaj--Zalar, and the source title plus `conjecture`.
- Hits: arXiv:2001.11614, the authors' earlier arXiv:1611.00494, and unrelated
  classical moment papers. No later exact resolution was found.

This is not proof of novelty. The mathematical status remains subject to
expert review and a broader bibliographic search.
