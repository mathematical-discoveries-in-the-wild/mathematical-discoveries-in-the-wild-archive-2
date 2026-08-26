# Full result: Heisenberg quantum channels are operator-norm closed

status: `candidate_full_likely_valid`

model: `GPT5.6`

source: Frederik vom Ende, *Reachability in Controlled Markovian Quantum
Systems: An Operator-Theoretic Approach*, arXiv:2012.03496v2 (2020),
Section 2.3.2, printed pages 46--48.

packet: `runs/fa_banach_001/solutions/full/2012.03496_heisenberg_channels_norm_closed/`

## Result

For separable complex Hilbert spaces `G,H`, the Heisenberg quantum channels

```text
Q_H(G,H) subset B(B(G),B(H))
```

form an operator-norm closed subset of the full Banach space of bounded linear
maps. This answers the explicit question immediately following Proposition
2.3.13 in the source.

## Proof mechanism

The source proves all inputs directly before asking the question:

- `Q_S(H,G)` is operator-norm closed in the bounded maps between trace-class
  spaces (Proposition 2.3.13(i)); hence it is complete.
- The adjoint correspondence `T -> T*` is a bijection from `Q_S(H,G)` onto
  `Q_H(G,H)` (Corollary 2.3.12).
- The same correspondence is an isometry for the ambient operator norms
  (the paragraph and footnote 33 preceding Proposition 2.3.13).

An isometric image of a complete metric space is complete, and every complete
subset of a metric space is closed. Therefore `Q_H(G,H)` is closed in the full
mapping space, not merely in the subspace of adjoint/normal maps.

Equivalently, if `S_n=T_n*` are Heisenberg channels and `S_n -> S` in operator
norm, then the isometry makes `(T_n)` Cauchy. Its limit `T` is a Schrödinger
channel, and continuity of the adjoint operation gives `S=T*`.

## Verification and novelty

- The exact open-question screenshot is from printed page 48 (physical PDF
  page 62); the preceding source inputs are reproduced from printed page 47.
- The proof was audited both as a completeness argument and as the explicit
  sequential lifting argument above.
- No computation is relevant: the claim follows from metric completeness and
  the source's stated norm-isometric bijection.
- Exact local-index searches and bounded primary-arXiv searches on 2026-08-11
  found the thesis and later quantum-control work, but no paper explicitly
  recording this closure corollary. Novelty confidence is moderate because the
  proof is a short overlooked consequence of results already adjacent in the
  source.

## Human-review focus

Confirm that the star map in Corollary 2.3.12 is onto the source's full
`Q_H(G,H)` and that footnote 33 uses the same operator norms as the ambient
spaces in the question. Both points are stated explicitly in the source.

