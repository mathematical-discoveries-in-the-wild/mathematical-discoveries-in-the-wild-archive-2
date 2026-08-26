# Hilbert classification of second-order Besov trace spaces

Status: `candidate_major_partial_likely_valid`

Source: Charles J. K. Batty, Ralph Chill, and Sachi Srivastava,
*Maximal regularity in interpolation spaces for second order Cauchy problems*,
arXiv:1404.2967, Section 5, Example 5.3, printed page 13.

## Results

For a complex Hilbert space `H`, `p=q=2`, `0<theta<1/2`, and arbitrary
dense closed operators `A,B` with `D(A)` continuously embedded in `D(B)`,
the source trace space has an exact operator-range description. If `Q_tau`
is the positive form operator associated with

```text
q_tau[x] = (tau^4+tau^2+1)||x||^2 + tau^2||Bx||^2 + ||Ax||^2
```

and

```text
K_j = integral_R tau^(2j)(1+tau^2)^(-theta) Q_tau^(-1) dtau,
```

then the trace is exactly

```text
Ran(K_0^(1/2)) x Ran(K_1^(1/2)),
```

with the corresponding operator-range norm. No commutativity or
self-adjointness of `A,B` is required for this theorem.

For strongly commuting nonnegative self-adjoint `A,B`, this becomes a closed
joint-spectral formula `D(M_0) x D(M_1)`. In particular, for every fractional
damping `A=G`, `B=c G^epsilon`, `0<=epsilon<=1`,

```text
Tr = D((I+G)^gamma_0) x D((I+G)^gamma_1),

epsilon <= 1/2:
  gamma_0 = 3/4 + theta/2,
  gamma_1 = 1/4 + theta/2;

epsilon >= 1/2:
  gamma_0 = (1+epsilon)/2 + theta(1-epsilon),
  gamma_1 = epsilon(1/2+theta).
```

The earlier critical-damping theorem is the case `epsilon=1/2`.

## Scope

This is a full classification for the Hilbert class `D(A) -> D(B)` and for
the entire nonnegative self-adjoint fractional-damping family. It remains a
major partial answer to the source problem because arbitrary Banach spaces,
arbitrary `p,q`, and unrelated operator domains remain untreated. The packet
also gives a diagonal example explaining why the whole-line pencil cannot be
naively extended to unrelated domains.

## Files

- `main.tex`: operator-range theorem, commuting spectral formula, fractional
  phase diagram, proofs, obstruction, and novelty audit.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_problem_crop.png`: source statement on printed page 13.
- `verification.md`: mathematical, numerical, literature, and render audit.
- `code/check_integrals.py`: numerical critical- and two-scale integral guard.
- `code/crop_source.py`: reproducible source-evidence crop.
- `tmp/`: compilation and page-render intermediates.

## Novelty status

Bounded local-index, source-corpus, official-arXiv, and web searches did not
locate the operator-range theorem, the commuting formula, or the full phase
diagram. This is not a novelty certificate; specialist review remains
necessary.

Human review should focus on the common interval-extension lemma, the
form-pencil adjoint and range calculation, and the uniform two-scale lemma.
