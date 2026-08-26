# Exact low-dimensional constants and a stronger asymptotic bound

Status: `candidate_substantial_partial_solution_likely_valid`

This packet advances Problem 3 on page 5 of Bandeira--Lewis--Mixon,
arXiv:1504.01014.

## Results

For

```text
c(n)=(1/n) sup_(U unitary) inf_(x != 0) [ns(x)+ns(Ux)],
ns(x)=||x||_1^2/||x||_2^2,
```

the first dimensions are exact:

```text
c(1)=2,       c(2)=3/2,       c(3)=4/3.
```

The normalized Fourier matrices `F_2` and `F_3` attain the nontrivial values.
The `F_3` proof uses three phase-weighted sums of the pairwise products of
`F_3x`, which isolate the quadrics `x_i^2-x_jx_k`.

The packet also sharpens the source's random-unitary argument to prove

```text
liminf_(n -> infinity) c(n) >= 3/100000.
```

This improves the source's stated `1/540000` lower bound by a factor of 16.2.
The key is a direct RIP-to-nullspace-width estimate valid for every
`delta<1`, followed by the choices `delta=7/10` and
`k=floor(n/5000)`.

## Scope

This is a substantial partial result.  The exact values for `n>=4` and the
asymptotically optimal constant remain open.  Numerical searches were used
only to assess further routes; they are not part of either proof.

## Files

- `main.tex`: source question, proof intuition, theorem statements, and proofs.
- `solution_packet.pdf`: compiled review packet.
- `VERIFICATION.md`: proof, source, novelty, and rendering audit.
- `source_paper.pdf`: local copy of arXiv:1504.01014.
- `figures/open_problem_crop.png`: full-width crop of Problem 3 and its stated
  bounds.
- Run attempt note:
  `attempts/1504.01014_optimal_numerical_sparsity_constants_attempt.md`.

Human review should focus on the three quadratic identities for `F_3` and the
decreasing-block nullspace estimate used in the asymptotic improvement.
