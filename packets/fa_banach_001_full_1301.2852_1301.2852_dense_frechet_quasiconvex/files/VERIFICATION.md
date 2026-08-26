# Verification audit

## Exact source match

The Introduction on source PDF page 5 asks whether every densely continuous
quasiconvex real-valued function on a separable Banach space is continuous and
classically Gâteaux differentiable at the points of a dense subset. The
source explicitly says that its affirmative result uses a weakened,
“essential” notion in which only a residual set of directions is tested.

Source PDF page 25 revisits the layered ℓ² construction and says that its
classical Gâteaux differentiability outside the first-category convex set
remained difficult irrespective of the level sequence. Thus this is not a
same-paper ask-and-answer extraction.

## Imported source results

The proof uses only the following results already proved in arXiv:1301.2852.

1. **Theorem 3.1 (TeX label `th4`).** For a densely continuous quasiconvex
   function, every strict lower sublevel `F_α={f<α}` with `α<m` is nowhere
   dense.
2. **Theorem 3.2(ii) (TeX label `th5`).** If `F'_m={f≤m}` is of second
   category, its interior `V` is nonempty. Since `F'_m` is convex, `V` is
   dense in `F'_m`.
3. **Theorem 3.2(iii).** `X\F'_m` is semi-open.
4. **Theorem 4.2 (TeX label `th9`).** Outside `F'_m`, `f` is Hadamard
   differentiable except on an Aronszajn-null set. The source immediately
   combines this with semi-openness to state relative density there.
5. **Corollary 4.3 (TeX label `cor10`).** The case `m=-∞` is already settled.
6. **Theorem 5.2 (TeX label `th12`).** If `F'_m` is of first category, it is
   nowhere dense and the source gives the needed dense Hadamard points.

## New proof obligations

### 1. Uniform convex-hole lemma

Let `C` be closed and convex with empty interior, and start with a closed ball
of radius `R`. Pick `z` within `R/4` of its center but outside `C`. Strong
separation gives a norm-one functional `ℓ` with
`ℓ(z)>sup_C ℓ`. Choose a unit vector `v` with `ℓ(v)>3/4` and move from `z` by
`(R/2)v`. Every point in the resulting closed `R/8`-ball remains inside the
original ball because

`R/4 + R/2 + R/8 = 7R/8 < R`,

and its functional value exceeds `sup_C ℓ` by more than

`(3/4)(R/2) - R/8 = R/4`.

Because `||ℓ||=1`, the latter also proves distance greater than `R/4` from
`C`. Strong separation is valid here even when `C` is unbounded: a point and
a disjoint closed convex set in a normed space can be strictly separated.

### 2. Nested construction

In any closed ball `B_0⊂V`, set `q=1/8`, `R_k=R_0q^k`, and
`α_k=m-R_0q^{2k}`. The closures `C_k=closure({f<α_k})` are closed, convex,
and have empty interior by source Theorem 3.1. Repeatedly applying the lemma
inside `B_{k-1}` gives nested closed balls `B_k` of radius `R_k` with

`dist(B_k,C_k)>R_{k-1}/4=2R_k`.

Completeness and `R_k→0` give a unique common point `x`. It is outside every
`{f<α_k}` but lies in `V⊂{f≤m}`, so `f(x)=m`.

### 3. Fréchet estimate

For `y→x`, eventually `y∈V`, so `f(y)≤m`. If
`R_{k+1}≤||y-x||<R_k`, then `y∉C_k` by the distance margin, hence
`f(y)≥α_k`. Therefore

\[
0\le \frac{f(x)-f(y)}{\|y-x\|}
\le \frac{m-\alpha_k}{R_{k+1}}
=q^{k-1}\longrightarrow0.
\]

This is the full norm-uniform estimate, not merely a directional limit, so
`f` is Fréchet differentiable at `x` with derivative zero.

### 4. Density and case assembly

Because `B_0⊂V` was arbitrary, these Fréchet points are dense in `V`. A
convex set with nonempty interior is contained in the closure of its
interior, so they are dense in `F'_m`. Source Theorems 3.2(iii) and 4.2 give
dense Hadamard points in `X\F'_m`. The union is dense in `X`; both Fréchet
and Hadamard differentiability imply continuity and classical Gâteaux
differentiability.

## Computational and visual verification

`code/check_nested_holes.py` uses exact rational arithmetic for 30,003
checks of the `1/8`, `1/4`, and quadratic-level-gap schedule. It guards
against constant and indexing mistakes; it does not replace the proof.

The source evidence is rendered directly from `source_paper.pdf`. The final
solution PDF is compiled with a halting LaTeX build, checked for warnings,
rendered to RGB PNG images, and every page is visually inspected.

## Upgrade history, novelty, and review focus

Five materially distinct attempts were made. After literature triage, the
source's ℓ² construction was tested as a counterexample; a sparse-spike
argument instead showed a broad positive phenomenon for that construction.
A general distance-rate reformulation isolated the missing quantitative
input. The final strong-separation argument supplied uniform relative holes
and upgraded the result from directional differentiability to Fréchet
differentiability in the hard region.

Four cheap run indexes and bounded exact-phrase, exact-title,
author-plus-question, and core-keyword searches found no duplicate or later
resolution through 11 August 2026. Because the decisive lemma is elementary,
unindexed-folklore risk remains and novelty confidence is moderate.

Human review should focus on the strong-separation form for unbounded closed
convex sets, the distance margin in the nested balls, and the final assembly
of the source's relative-density statements. The mathematical verdict is
`likely valid`; promotion as a full solution remains subject to expert review.
