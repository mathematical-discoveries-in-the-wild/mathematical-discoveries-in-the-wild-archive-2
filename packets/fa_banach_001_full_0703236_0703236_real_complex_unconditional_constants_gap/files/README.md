# A strict real/complex unconditional-constant gap

Status: `candidate_full_likely_valid` affirmative answer to the final open
question in arXiv:0703236.

## Result

For `Lambda={0,1,2,3,5}`, the real and complex unconditional constants of the
character basis satisfy

```text
K_C > 49999/26400 > 1.89 > 1.888 > K_R,
K_C-K_R > 779/132000.
```

The complex lower bound uses one explicit rational polynomial and a rigorous
root-grid plus derivative estimate.  The real upper bound uses explicit
finite representing measures for all 16 normalized sign patterns.  A
six-root discrete Fourier correction repairs the tiny rounded moment
residuals exactly.

## Files

- `main.tex`: self-contained mathematical explanation.
- `solution_packet.pdf`: rendered review packet.
- `code/verify_gap.py`: static outward-interval certificate checker.
- `source_paper.pdf`: compiled source paper arXiv:0703236.
- `supporting_status_paper_2603.28229.pdf`: later same-author status evidence.
- `figures/`: readable crops of the original question and later open status.
- `verification.md`: computational, proof, and rendering audit.

## Reproduce

From the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/0703236_real_complex_unconditional_constants_gap/code/verify_gap.py
```

The checker performs no numerical optimization and uses no external data.
All finite certificates are stored in the script.

## Novelty scope

The source asks whether such a finite set exists.  arXiv:2603.28229, posted in
2026, still calls the real-versus-complex distinction undecided.  A bounded
local and web/arXiv search on 2026-08-13 found no prior separating example.
The result is therefore promoted as a new candidate full answer, subject to
specialist review.
