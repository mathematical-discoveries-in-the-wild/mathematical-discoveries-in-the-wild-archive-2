# Finite box dimension forces finite-rank Taylor coefficients

Status: **candidate full solution; likely valid; human review recommended**

## Source questions

- Daniel Carando, Carlos D'Andrea, Leodan A. Torres, and Pablo Turco,
  *Entropy numbers and box dimension of polynomials and holomorphic
  functions*, arXiv:2401.12059v1; Math. Nachr. 298 (2025), 567–580.
- Target: Questions 4.4 and 4.5, official arXiv PDF page 15.

If a holomorphic map `f:U -> F` sends `x0 + epsilon B_E` to a set of finite
box dimension, Question 4.5 asks whether every homogeneous Taylor coefficient
`P_m f(x0)` maps `B_E` to a set of finite upper box dimension. Question 4.4
asks for the weaker endpoint conclusion that its dyadic entropy numbers belong
to `ell_1`.

The source questions accidentally print `f:U -> E`; the paper's setup and the
introduction of `F` make `f:U -> F` the intended formulation.

## Full result

Both answers are yes, under the weaker assumption of finite *upper* box
dimension. Put

```text
d = upper_dim_B f(x0 + epsilon B_E),
r = floor(d/2),
V_m = span(P_1(E), ..., P_m(E)).
```

Then

```text
dim(V_m / V_(m-1)) <= (r+m)^m,
dim V_m <= sum_(k=1)^m (r+k)^k.
```

Thus every `P_m` has finite-dimensional range, so `P_m(B_E)` has finite
upper box dimension and geometrically decaying dyadic entropy numbers. In
particular, those entropy numbers lie in `ell_1`.

## Proof mechanism

Finite upper box dimension bounds every complex differential rank of `f` by
`r`: otherwise a finite-dimensional slice and the holomorphic inverse theorem
would put an open subset of `C^(r+1)` inside a Lipschitz image of `f`'s image.

Inductively quotient `F` by the finite span of the lower Taylor ranges. In that
quotient the derivative series along `x0+t x` begins exactly with

```text
t^(m-1) d(P_m)(x).
```

A nonzero `(r+1)`-minor of this leading coefficient remains nonzero for small
nonzero `t`, contradicting the differential-rank bound. Hence the quotient
polynomial has all derivative ranks at most `r`. The polynomial Jacobian
estimate proved in Section 3 of the source then bounds its range-span dimension
by `(r+m)^m`, closing the induction.

## Verification and novelty

Run:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2401.12059_taylor_coefficients_finite_rank/code/verify_rank_induction.py
```

The script checks the exact leading-minor exponent and coefficient on a grid
of matrix sizes and Taylor degrees. The general result is the formal proof,
not a computational inference.

Bounded searches on 13 August 2026 found the 2025 published source and one
indexed citing paper on generalized entropy numbers, but no claimed answer to
Questions 4.4 or 4.5. Novelty confidence is moderate.

## Human-review focus

Prioritize the reduction of the Banach-valued polynomial rank lemma to the
source's Corollary 3.3, and the claim that lower-degree quotienting makes the
Taylor determinant's leading coefficient exact. The inverse-function and
finite-dimensional entropy steps are standard.

## Packet contents

- `main.tex`, `solution_packet.pdf`: quantitative theorem and full proof.
- `source_paper.pdf`: official 17-page arXiv PDF.
- `figures/open_problem_crop.png`: official page-15 source crop.
- `code/make_open_problem_crop.py`: reproducible cropper.
- `code/verify_rank_induction.py`: exact determinant/index sanity checker.
- `verification.md`: proof audit, literature bounds, QA, and hashes.
