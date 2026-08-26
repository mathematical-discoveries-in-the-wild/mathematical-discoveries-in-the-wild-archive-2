# Verification Report

Candidate: arXiv:1511.09045, compactoid/von-Neumann Mackey convergence without nuclearity.

## Claim checked

Over every nontrivially valued field, topological convergence, von-Neumann-bornological Mackey convergence, and compactoid-bornological Mackey convergence agree for sequences in every metrizable locally convex space. Over trivially valued fields the all-Frechet-space statement fails for `k^N`.

## Verdict

`candidate_full_solution_human_review_needed`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Exact source target | valid | Current source PDF page 29, Remark 3.69, conjectures Lemma 3.68 for all Frechet spaces without nuclearity and identifies the non-Archimedean/non-locally-compact gap. |
| Logical direction | valid correction | Since every compactoid set is von Neumann bounded (stated earlier in the source), compactoid-Mackey convergence automatically implies von-Neumann-Mackey convergence. The substantive missing direction is topological to compactoid-Mackey convergence. |
| Slow scalar rescaling | valid | A fixed element `pi` with `0<|pi|<1` and a diagonal choice of cutoffs `N_r` produce `a_n=pi^(-r)`, with `|a_n|->infinity` while every fixed seminorm of `a_n x_n` tends to zero. |
| Compact null-sequence set | valid | A convergent sequence together with its limit is compact in every topological space: an open set containing the limit covers the entire tail, leaving finitely many terms. |
| Compact implies compactoid | valid | Compact gives a finite translate cover for every zero-neighborhood, hence precompact; precompact is compactoid directly from the source definition. No local compactness of the field is needed in this direction. |
| Absolutely convex hull | valid | If `K subset U+F` and `U` is absolutely convex, then the absolutely convex set `U+Gamma(F)` contains `K`, hence contains `Gamma(K)`. Thus the hull remains compactoid. |
| Mackey scalar quantifier | valid | From `x_n=a_n^(-1)y_n`, for each fixed nonzero `lambda`, eventually `|a_n^(-1)/lambda|<=1`; absolute convexity yields `x_n in lambda B`. |
| Reverse to topology | valid | If Mackey convergence is witnessed by bounded `B`, then for each zero-neighborhood `U`, choose `c` with `B subset cU` and use the Mackey condition at scalar `c^(-1)`. |
| Trivial-valuation example | valid | `k^N` is a complete metrizable locally convex product of discrete one-dimensional spaces and `e_n->0` coordinatewise. Any nonzero vector is excluded from bounded sets by the open subspace forcing one nonzero coordinate to vanish; scalar multiples do not change it under a trivial valuation. |
| Scope strengthening | valid | The positive proof uses metrizability but not completeness, nuclearity, local compactness, or spherical completeness. |

## Stress tests and rejected overclaims

- The packet does not claim `Cpt(E)=E^b`; only sequential convergence agrees.
- The scalar sequence is chosen from powers of one field element, so no density assumption on the value group is used.
- Initial finitely many terms do not matter for Mackey convergence and can be absorbed into the compactoid hull.
- In the trivially valued example, the open subspace `U_j={z:z_j=0}` is a genuine zero-neighborhood because each factor is discrete.
- The counterexample concerns the literal any-valued-field statement. It does not weaken the affirmative theorem in the nontrivially valued analytic setting used later in the source.

## Novelty check

On 2026-08-11, the exact arXiv id/title and the terms `compactoid bornology`, `Mackey convergence`, `Frechet`, `non-Archimedean`, and `null sequence` were checked against the run registry, solution, attempt, and proof-gap indexes. Bounded arXiv primary-source searches did not return a later resolution. This is not a guarantee of novelty.

## Artifact verification

- `source_paper.pdf` is the official 54-page arXiv PDF.
- `figures/conjecture_crop.png` is rendered from source PDF page 29 and includes the exact lemma and conjecture.
- The proof packet uses only definitions stated in the source and elementary metrizable locally convex arguments.
- No computation is used as mathematical evidence.

Confidence: 96/100.

Recommended action: high-priority review by a non-Archimedean functional analyst or bornological geometer. The main audit is convention-level: compactoid absolute convex hulls and Mackey scalar quantifiers.
