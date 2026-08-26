# A Berger-Five-Sphere Counterexample to Spectral and Contraction Comparison

Status: `counterexample_likely_valid`

Source: Emanuel Milman, *Spectral Estimates, Contractions and
Hypercontractivity*, arXiv:1508.00606v4, Conjectures 3 and 4 on PDF pages 8
and 9.

## Claimed contribution

Both conjectures are false. On the unit round `S^5` split the tangent bundle
into the horizontal distribution of the complex Hopf fibration and its
one-dimensional vertical distribution. Define the Berger metric

```text
g_a = g_horizontal + a g_vertical,    a = 5/4.
```

Its Ricci eigenvalues are `7/2` horizontally and `5` vertically, hence
`Ric(g_a) >= (7/2) g_a`. The round comparison metric therefore has spectral
scale `(7/2)/4 = 7/8` relative to the unit round sphere.

The positive Laplacian of `g_a` has eigenvalue

```text
k(k+4) - (p-q)^2/5
```

on harmonic polynomials of bidegree `(p,q)`, where `p+q=k`. There are exactly
714 modes of total degrees 0 through 6. All of them have eigenvalue at most 60,
whereas every mode of degree at least 7 has eigenvalue at least `336/5`.
Thus, in the source paper's indexing with `lambda_1=0`,

```text
lambda_715(S^5,g_a) = 336/5.
```

On the round comparison sphere, the first 714 modes again have degrees at most
6 and

```text
lambda_715(round comparison) = (7/8)*7*11 = 539/8.
```

Since `336/5 < 539/8` by exactly `7/40`, Conjecture 3 fails. A contraction as
in Conjecture 4 would imply the conjectured spectral ordering by pulling test
spaces back through the map, so Conjecture 4 fails as well.

## Verification

Run the dependency-free exact checker:

```bash
python3 runs/fa_banach_001/solutions/counterexamples/1508.00606_berger_s5_spectral_contraction_counterexample/code/verify_spectrum.py
```

It checks the Ricci and comparison scales, bihomogeneous multiplicities, the
714-mode count, exact spectral ordering through degree 7, and the `7/40`
violation.

## Novelty and scope

A bounded search through 11 August 2026 covered all four run indexes, the
exact source title and arXiv id, exact conjecture phrases, Milman's name with
`Berger sphere` and `counterexample`, citation-oriented queries, and the 2018
journal page. It found no prior counterexample. It also checked the relevant
recent positive results: arXiv:2607.11544 proves the spectral comparison on
`S^2`, and arXiv:2508.13688 proves near-round contractive transport on `S^2`.
Neither covers this five-dimensional example. This is not a claim of priority.

The example refutes the universal statements but does not classify the
dimensions or metric families where either comparison remains true.

Human review recommendation: very high priority. Verify the standard Berger
Ricci and scalar-Laplacian formulas in the stated fiber-scaling convention.
After those two formulas, the counterexample is a short exact count.

