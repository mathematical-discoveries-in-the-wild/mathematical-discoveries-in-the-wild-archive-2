# A binomial sharpening of the cube-BMO rearrangement bound

Status: `partial_result_likely_valid`

Source: Almut Burchard, Galia Dafni, and Ryan Gibara, *Mean oscillation
bounds on rearrangements*, arXiv:2011.09111, Trans. Amer. Math. Soc. 375
(2022), 4429-4444. The open problem is on source PDF page 3.

## Result

Put

```text
beta_m = E|Bin(m,1/2)-m/2|
       = m 2^(-m) binom(m-1,floor((m-1)/2)),

K_n = max_{1<=m<=n-1} min{1+4 beta_m, 2^(n-m)}.
```

Then every rearrangeable `f in BMO(R^n)` satisfies

```text
||f*||_{BMO(R+)} <= 2 K_n ||f||_{BMO(R^n)}.
```

In particular,

```text
C_n <= 2(1+4 beta_(n-1))
    = sqrt(32 n/pi) + O(1),
```

with the harmless replacement of `n-1` by `n` in the displayed asymptotic.
This improves the source bound
`C_n <= 2(1+2 sqrt(n-1))`: the leading coefficient is multiplied by
`sqrt(2/pi)`, approximately `0.797885`.

The key new lemma is sharp. If `g` is a function of independent unbiased bits
and changing coordinate `i` changes `g` by at most `a_i`, then

```text
E|g-Eg| <= E |(1/2) sum_i a_i epsilon_i|.
```

More generally the same comparison holds for every even convex loss. It
replaces the Cauchy-Schwarz bounded-differences step in the source proof.

## Scope

This does **not** settle the source question of whether `C_n` is
dimension-free, nor does it determine the sharp constants. The discrete lemma
is attained by an additive Hamming-weight function, so further improvement
cannot come from coordinatewise neighboring-cube bounds alone; it must use
additional geometric compatibility among cube averages or a different
decomposition.

## Files

- `solution_packet.pdf`: expert-facing statement and complete proof.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: open question from source PDF page 3.
- `code/verify_binomial_bound.py`: exact constant checks and small exhaustive
  linear-program tests (evidence only; the proof is analytic).
- `verification.md`: build and verification record.

## Novelty check

A bounded search on 2026-08-11 covered the run indexes; exact title,
inequality, author, citation, `dimension-free`, `false cube`, `binomial`, and
`mean absolute deviation` queries; the authors' later VMO paper
arXiv:2201.05130; and related semigroup-BMO work. No later resolution of the
cube-BMO question or use of this binomial sharpening in the rearrangement
bound was located. Novelty confidence is moderate: the martingale lemma is an
elementary sharp bounded-differences fact, but its application here appears
absent from the searched literature.

## Human review recommendation

Review as a likely valid substantial partial result. The main checks are the
backward convex-domination induction, the normalization converting the
Rademacher deviation to `4 beta_m`, and the subset-to-container factor
`2^(n-m)`. Do not label this a full answer to the dimension-free question.
