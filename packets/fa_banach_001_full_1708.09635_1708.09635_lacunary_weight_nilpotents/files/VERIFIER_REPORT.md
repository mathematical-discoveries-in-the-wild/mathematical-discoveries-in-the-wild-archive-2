# Verification report

## Mathematical checks

- Confirmed the source defines `Z+={0,1,2,...}`, so `q_0=1` and the displayed
  generating set really generates `Z`.
- Proved an exact strict-balanced mixed-radix lemma for the variable even
  radices `R_i=2^{2i+1}`.
- Checked the two threshold inequalities from the choice
  `d_i=floor(R_i/(2m))+1`, using `R_i>=4m^2`.
- Checked that carry locations are disjoint because selected positions have
  gap two.
- Checked exact nonvanishing of every power below `m` by pairing with the
  norm-one functional `omega`.
- Checked uniform norm decay at the `m`-fold product, not merely diagonal
  decay; this is what makes all iterated Arens limits vanish.
- Checked products of `m` distinct arbitrary left multiples, giving a
  nilpotent principal left ideal rather than only a nilpotent element.

## Computational checks

`code/verify_mixed_radix.py` was run in the `sandbox` conda environment with
SciPy 1.16.3.  It independently solved finite integer word-length
minimization problems and reported:

```
verified 32 exact MILP word-length identities
verified 69632 local normalization inequalities
m=2,...,8: all carry thresholds and exact nilpotency formulas pass
```

The program is corroborative; the packet's proof is uniform in `m` and does
not rely on computation.

## Literature checks

- Local result and attempt indexes.
- Exact source title and exact open-question sentence.
- Variants using “nilpotent elements of every/arbitrarily high index,”
  “Beurling algebra,” and weighted `l1(Z)`.
- Jared T. White's current publication list and doctoral thesis listing.
- arXiv:2602.02764, the author's 2026 sequel on distinct Arens radicals.
- OpenAlex record for DOI `10.1093/qmath/hay003` (zero indexed citations at
  audit time).

No exact prior resolution was located.  This supports but does not certify
novelty.

## Artifact checks

- `solution_packet.pdf`: 5 US Letter pages.
- LaTeX completed without warnings, undefined references, overfull boxes, or
  underfull boxes.
- All five final PDF pages were rendered to PNG and visually inspected.
- The source-question crop is legible and displays the exact page-2 question.
- Final packet SHA-256:
  `e431dbef68984c6ba6094c1c23addb9fc12e447fc902f0509290fb2422411513`.
- Source PDF SHA-256:
  `162436cdd650be11b7e38c5f8e4b2d5ff303766b547ebfc1784b727b8ec9e0e3`.
