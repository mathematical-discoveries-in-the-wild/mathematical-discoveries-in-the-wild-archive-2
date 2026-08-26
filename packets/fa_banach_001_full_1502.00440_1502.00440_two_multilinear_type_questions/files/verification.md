# Verification report

Status: `candidate_full_result_likely_valid_needs_human_review`

## Mathematical audit

### 1. Open Question 1

Let `S=sum_i 1/r_i` and `s=1/S`. The hypothesis `S>=1/p` gives
`s<=p`, while `S>=1/r_i` gives `s<=r_i` for every coordinate. Type `p`
of `E` first bounds the output Rademacher norm by the `ell_p` norm of

```text
prod_{i=1}^n |phi_i(x_j^i)| times ||x_j^{n+1}||.
```

The `ell_s` norm dominates the `ell_p` norm because `s<=p`. Generalized
Holder is applicable with exponents `r_i/s`, since their reciprocal sum is
`sum_i s/r_i=1`. This gives exactly the product of the requested
`ell_{r_i}` input norms and the constant
`T_p(E) prod_i ||phi_i||`.

The equality case `S=1/p` uses the assumed attained type `p`. No sign lower
estimate occurs in the proof.

### 2. Boundedness of the coordinate-product map

For `1<=r_i<=2` and `n>=2`, the capacities `1/r_i` sum to at least one.
Hence one can choose `b_i in [0,1/r_i]` with sum one. Setting
`q_i=1/b_i`, with `q_i=infinity` when `b_i=0`, gives `q_i>=r_i` and
`sum_i 1/q_i=1`. Generalized Holder and the contractive inclusions
`ell_{r_i} into ell_{q_i}` prove

```text
||B(x^1,...,x^n)||_1 <= prod_i ||x^i||_{r_i}.
```

Thus `B` is a bounded map into the Banach space `ell_1`; no quasi-Banach
target is used.

### 3. Factorization-ideal membership

The identity of `ell_r` has linear type `r` for `1<r<=2`, and every
Banach-space identity has type one by the triangle inequality. Therefore

```text
B = B(id_{ell_{r_1}},...,id_{ell_{r_n}})
```

is a factorization through type-`r_i` maps exactly in the sense of the
source definition. This includes every endpoint `r_i=1` and `r_i=2`.

### 4. Failure of every proper multilinear type

On common diagonal basis vectors, `B(e_j,...,e_j)=e_j`. Every Rademacher
sum of the first `k` unit vectors has `ell_1` norm exactly `k`, so its
`Rad(ell_1)` norm is `k`. A type tuple with reciprocal sum `S` would imply
`k<=C k^S`. Properness requires `S<1`, which is impossible as `k` tends to
infinity. The same single `B` therefore lies outside the union of all
proper diagonal-type ideals.

## Upgrade-attempt audit

Seven materially distinct passes are recorded in
`attempts/1502.00440_two_type_questions.md`:

1. the generalized-Holder closure of Question 1;
2. the equality and nonattained-type endpoint audit;
3. diagnosis of why the source's one-active-coordinate construction only
   covers a partial exponent range;
4. the all-coordinate `ell_1` product construction closing Question 2;
5. factorization, Banach-target, and endpoint checks;
6. the stronger outside-the-union ideal interpretation;
7. bounded literature and novelty checks.

Both strongest routes close their exact questions, so no partial-to-full
upgrade remains.

## Literature and scope audit

- The run's registry, solution, attempt, and proof-gap indexes had no prior
  treatment of arXiv:1502.00440 or either exact question.
- The current source is arXiv:1502.00440v2, last revised 21 December 2015,
  and contains both question statements.
- Bounded searches through 11 August 2026 for the exact question labels,
  title-plus-question phrases, factorization notation, and coordinatewise
  product counterexamples found no later answer.
- Both arguments are elementary consequences of the definitions and could
  be folklore or overlooked. No priority claim is made.
- The packet addresses the two multilinear type questions only. It makes no
  assertion about the paper's multilinear cotype ideals.

## Rendering audit

- Final PDF: four US-Letter pages, 291290 bytes.
- Two `pdflatex` passes completed without warnings, undefined references,
  overfull boxes, or underfull boxes.
- All four pages were rasterized at 150 dpi and visually inspected. The
  status box, exact question crops, equations, proof endings, citations,
  margins, and page transitions are clean and legible.
- `solution_packet.pdf` and `tmp/main.pdf` are byte-identical.
- Final SHA-256:
  `0dee0ee97e62135fc8ac23ca1d7d7a1bbb51f48f52861c745e9c1faf50302e97`.

## Human-review focus

Independently check the direction of the sequence-space inclusions in both
proofs, then verify the admissible selection of the `b_i` and the exact
diagonal `Rad(ell_1)` calculation. These are the only review-critical steps.
