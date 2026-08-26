# Verification notes

## Source evidence

- `source_paper.pdf` is arXiv:0707.0427, 30 pages.
- `figures/open_problem_crop.png` is a 180 dpi render of PDF/printed page 24.
  It contains Section 3.3, both definitions, the transposition lower bound,
  the non-even open question, and the even-exponent upper bounds.

## Exact audit

Run:

```sh
conda run --no-capture-output -n sandbox python \
  code/verify_trace_identity.py
```

The script uses integer arithmetic and checks:

1. sampled instances of `S_{2r}=0` in `M_r` for `r=1,...,4`;
2. the explicit chain evaluation `S_{2r}=e_{1,r+1}` in `M_{r+1}`;
3. the marked trace is exactly one before normalization;
4. the boundary coefficient `C_{2r,2r+1,1}=2r` is nonzero.

These are audits only. The packet proves the general statements using
Amitsur--Levitzki and the unique nonzero matrix-unit ordering.

## Proof review gates

- Confirm that finite matrix trace evaluations span the dual of every finite
  cyclic `*`-polynomial space; the packet gives the weighted-cycle argument.
- Confirm the positive/negative splitting: annihilation of the constant makes
  the total masses equal, so both sides become normalized faithful traces on
  finite direct sums.
- Check the one-star coefficient extraction in the unit case. Every ordering
  has transition count one and the coefficient is nonzero exactly under the
  stated `m>=2r` hypothesis.
- Check the paired-brick extraction in the homogeneous case and the need for
  `m>=2r+1` to include a marker brick.
- Confirm that the common tagging summand preserves equality/non-equality and
  makes both spanning tuples linearly independent.

## Literature boundary

Bounded index and primary-source searches through 2026-08-17 found no later
answer to the fixed-level subspace questions and no matching quantitative
lower bounds. Novelty confidence is moderate, not a priority certification.

## PDF build

- `solution_packet.pdf`: 6 letter-size pages.
- Final LaTeX log: no warnings, undefined references, overfull boxes, or
  underfull boxes.
- All six rendered pages were visually inspected; the source crop is legible
  and no content is clipped or overlapped.
- SHA-256:
  `2dfbd7577785f250c3bd85aec568b1afb4ce880767453cf1698e4c0b79f6cb31`.
