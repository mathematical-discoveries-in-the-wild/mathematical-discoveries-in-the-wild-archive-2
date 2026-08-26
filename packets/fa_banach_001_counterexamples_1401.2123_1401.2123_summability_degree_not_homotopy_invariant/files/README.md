# Summability degree is not a homotopy invariant

Status: `candidate_counterexample_likely_valid`.

Source: Magnus Goffeng and Bram Mesland, “Spectral triples and finite
summability on Cuntz--Krieger algebras,” arXiv:1401.2123, Documenta
Mathematica 20 (2015), 89--170.

## Result

There are separable homotopy-equivalent C*-algebras with different odd
degrees of summability.  In fact, the example has the maximal possible gap:

```text
sd_1(A)   = infinity,
sd_1(M_f) = 0.
```

Take the source paper's algebra

```text
A = c0-direct-sum_{j>=1} C(S^{2j-1}),
```

which has an odd K-homology class of infinite degree.  Let `D=O_Q` for

```text
Q = [[0,1,1],
     [1,1,0],
     [1,0,1]].
```

Then `D` is a simple purely infinite Cuntz--Krieger algebra,
`K_0(D)=K_1(D)=Z`, and the source theorem gives `sd_1(D)=0`.  The UCT and
Kirchberg's realization theorem give homomorphisms

```text
f_j:C(S^{2j-1}) -> D
```

which are KK-equivalences.  Their c0 sum `f:A -> B`, where
`B=c0-direct-sum D`, induces an isomorphism on odd K-homology.

The mapping cylinder

```text
M_f = {(a,h) in A + C([0,1],B) : h(0)=f(a)}
```

is homotopy equivalent to `A`.  Evaluation at 1 maps `M_f` onto `B` and is
surjective on odd K-homology.  Pullback along a surjective *-homomorphism
preserves p-summability because inverse images of dense smooth subalgebras
remain dense.  Every odd class of `B` is p-summable for every `p>0`, so the
same is true for `M_f`.

This is a full negative answer to the homotopy-invariance question for the
odd summability degree.  It does not address the source's separate request
for general obstructions to finite summability, nor does it assert an even
counterexample.

## Files

- `solution_packet.pdf`: complete proof and review notes.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `supporting_dadarlat_2007.pdf`: primary source for Kirchberg's
  KK-class realization theorem.
- `figures/open_problem_crop.png`: Definition 4, the exact question, and
  the source's infinite-degree example on PDF page 6.
- `figures/source_extremes_crop.png`: the source's lower-bound conclusion
  and Theorem 7 giving Cuntz--Krieger odd degree zero.
- `figures/kirchberg_realization_crop.png`: Dadarlat's Theorem 2.3(i).
- `code/verify_ck_matrix.py`: exact finite checks of the chosen 0--1 matrix.
- `novelty.md`: bounded duplicate and literature search.
- `verification.md`: mathematical, computation, build, and rendering checks.

Human review should focus on the UCT-to-homomorphism realization step, the
countable direct-sum Fredholm module, and the K-homology diagram for the
mapping cylinder.
