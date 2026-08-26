# Invariant graph subspaces omitted from powers of unicellular shifts

**Status:** `candidate_counterexample_likely_valid`

## Source question

Sneh Lata, Sushant Pokhriyal, and Dinesh Singh, *Invariant subspaces of
powers of some unicellular operators*, arXiv:2205.00252; New York Journal of
Mathematics 29 (2023), 231-260.

Remark 4.2 (arXiv PDF page 20; journal page 257) asks whether the lattice
descriptions for invariant subspaces of `T*^2` and `T*^3` in Theorems
3.9-3.11 remain valid for other weight classes.

## Counterexample

Let `B=T*` be any backward weighted shift on `ell^2(N_0)` with positive
bounded weights, and put

```text
H_r^(m) = closed span{e_(mk+r) : k >= 0},   1 <= r < m.
```

For every `m >= 2` and every scalar `lambda`, the subspace

```text
G_(lambda,m,r) = (I + lambda B) H_r^(m)
```

is invariant under `B^m`.  When `lambda != 0`, it is closed, proper, and
infinite-dimensional.  Indeed, `H_r^(m)` and `B H_r^(m)` are orthogonal,
so `I+lambda B` is bounded below there, and

```text
B^m (I + lambda B)x = (I + lambda B) B^m x.
```

For `m=2`, `r=1`, and the Donoghue weights `w_n=2^(-n)`, these graph
subspaces are absent from every form in Theorems 3.9 and 3.10: a nonzero graph meets
both the even and odd coordinate subspaces only at zero, while every listed
form is a coordinate subspace or contains `e_0`.  Thus Theorem 3.10 is false
under its own Condition (3.4).  The same weights satisfy Condition (3.1)
because a product of length `L` gives the uniformly bounded geometric sum
`sum_(k>=0) 2^(-2kL)`, so Theorem 3.9 fails as well.  Continuum many invariant
subspaces are missing.  Taking `m=3`, `r=1` gives the analogous counterexample
to Theorem 3.11.

The lattices can also differ with the weights even inside Condition (3.4).
Let `B_q e_n=q^(n-1)e_(n-1)` and

```text
G_q = (I+B_q) H_odd.
```

For `q=1/2`, `G_q` is `B_q^2`-invariant.  It is not invariant under
`B_p^2` for `p=1/3`: for `g=e_3+q^2e_2`,

```text
B_p^2 g = p^3 e_1 + q^2 p e_0,
```

whereas membership in `G_q` would force the coefficient of `e_0` to be
`p^3`.  This would require `q^2=p^2`, which fails.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2205.00252_invariant_graph_subspaces_counterexample/code/verify_counterexample.py
```

The script uses exact rational matrices.  It checks graph invariance for
powers 2 through 6, trivial intersections with the adjacent residue spaces,
distinct slopes, the explicit Theorem 3.10 counterexample, and the
`q=1/2`, `p=1/3` cross-weight failure.  These checks guard indexing; the
infinite-dimensional proof is algebraic.

## Novelty check

On 2026-08-11, bounded local and web searches used the arXiv id, exact title,
authors, theorem number, the phrase "lattice structure", and combinations of
"weighted shift", "power", and "invariant graph subspace".  They found the
arXiv preprint and the 2023 New York Journal of Mathematics publication, but
no correction, erratum, or later source explicitly recording this graph
counterexample.  This is not a certification of novelty.

## Human review recommendation

Review the two-line invariance identity, the closed-range argument, and the
comparison with the exact lists in Theorems 3.10 and 3.11.  The result is
elementary but contradicts published characterization statements, so the
formulation should be checked especially carefully before external use.
