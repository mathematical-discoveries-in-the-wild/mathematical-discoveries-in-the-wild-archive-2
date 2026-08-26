# Full candidate: mixed-exponent cb Schur multipliers

Status: `full_solution_likely_valid` (awaiting specialist review).

For `1 <= q <= 2 <= p <= infinity`, set

```text
1/r = 1/q - 1/p.
```

This packet proves that a scalar matrix `phi=(phi_ij)` defines a completely
bounded Schur multiplier `M_phi:S_p -> S_q` if and only if there are
nonnegative sequences `a,b in ell_{2r}` such that

```text
|phi_ij| <= a_i b_j  for all i,j.
```

Moreover, the cb norm is equivalent, with constants depending only on `p,q`,
to the infimum of `||a||_{2r}||b||_{2r}`.  This answers Problem 7.7 of
Quanhua Xu, arXiv:math/0505306, including the off-dual-line range requested
there.  On the dual line it recovers Xu's Corollary 7.6(ii).

The proof factors through `S_2`.  Sufficiency splits the two weights around
`S_2`.  Necessity combines Junge--Parcet's operator-space Maurey
factorization with a squared Hilbert--Schmidt torus average that forces the
first weights diagonal, then uses Xu's operator-space little Grothendieck
theorem on the residual Schur map.  Holder combines the two endpoint weight
pairs into the exponent `2r`.

Files:

- `solution_packet.pdf`: review-ready theorem and proof.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: Problem 7.7 in the source.
- `verification.md`: proof-dependency and endpoint audit.
- `code/check_exponents.py`: exact rational checks of the exponent identities.

Primary verifier focus: check the equivariant extraction in Lemma 4.  After
Junge--Parcet factorization, the proof averages the squared
`S_2^m[S_2^n]=S_2^{mn}` norm over two diagonal tori, obtains the diagonal
conditional expectations of `d_1^2,d_2^2`, and invokes Xu's
`S_2`-amplification criterion to recover a cb residual map.

Novelty status: bounded searches of the run indexes, exact web/arXiv queries,
and the 33 OpenAlex-indexed citing works found the relevant 2009/2010
factorization and endpoint papers, but no paper stating this full mixed
characterization.  Novelty remains subject to expert literature review.
