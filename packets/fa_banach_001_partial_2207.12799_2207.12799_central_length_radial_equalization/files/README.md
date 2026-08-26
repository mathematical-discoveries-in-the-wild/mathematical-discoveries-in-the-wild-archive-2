# Partial Result: Optimal radial equalization for central modular lengths

- **Source:** K. Mahesh Krishna, *Modular Paulsen Problem and Modular Projection Problem*, arXiv:2207.12799.
- **Target:** Problem 2.10, asking for the closest equal-inner-product modular frame to a given nearly equal-inner-product modular frame.
- **Status:** `candidate_full_solution_central_length_subcase_likely_valid; general_noncommutative_problem_open`.
- **Model:** `GPT5.6`.

## Result

Let `A` be a unital C*-algebra, let `{tau_j}_{j=1}^n` be an epsilon-nearly equal-inner-product frame for the standard left module `A^d`, put

```text
c = sqrt(d/n),    p_j = <tau_j,tau_j>,
omega_j = c p_j^(-1/2) tau_j.
```

Then `{omega_j}` is an equal-inner-product modular frame over every `A`. If `{tau_j}` has frame bounds `a,b`, the new bounds are `a/(1+epsilon), b/(1-epsilon)`, and

```text
dist(tau,omega)^2 = || sum_j (p_j^(1/2)-c)^2 ||
                  <= d(1-sqrt(1-epsilon))^2
                  <= d epsilon^2.
```

If every `p_j` is central in `A`—in particular if `A` is commutative—this radial normalization is globally closest among all equal-inner-product modular frames. The proof actually compares it with every equal-length collection, whether or not that collection is a frame.

## Proof idea

Functional calculus gives the equal-length identity and exact distance formula. Frame preservation follows by inserting the bounded positive coefficients `c^2 p_j^(-1)` into the original frame inequalities. For optimality, normalize a competitor to two unit module vectors `v_j,u_j`. Their cross inner product is a contraction. Centrality lets the positive factor `p_j^(1/2)` commute through the cross term, turning the contraction inequality `q_j+q_j^* <= 2` into the pointwise lower bound

```text
<tau_j-nu_j,tau_j-nu_j> >= (p_j^(1/2)-c)^2.
```

Summing and taking the C*-norm proves global minimality.

## Scope

The packet fully solves Problem 2.10 for commutative C*-algebras and, more generally, for frames whose squared lengths are central. For arbitrary noncentral lengths it gives a canonical feasible frame with an exact distance and a uniform bound, but no general lower bound matching that distance is proved. The obstruction is genuinely noncommutative: the two cross terms place `p_j^(1/2)` on opposite sides, while the modular distance uses a nontracial C*-norm.

## Files

- `main.tex` — theorem, proof, scope, and novelty audit.
- `solution_packet.pdf` — compiled proof packet.
- `source_paper.pdf` — official arXiv source PDF.
- `figures/problem_2_10_crop.png` — source question and definitions.
- `VERIFICATION.md` — mathematical and presentation checks.
