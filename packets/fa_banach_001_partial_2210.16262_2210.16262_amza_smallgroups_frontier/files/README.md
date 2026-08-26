# Exact SmallGroups frontiers for arXiv:2210.16262

Status: `candidate_partial_computational_likely_valid`

This packet gives exact exhaustive affirmative answers through order 383 to
Questions 6.2, 6.3, and 6.4 of John Sawatzky, *Amenability constants of
central Fourier algebras of finite groups*, arXiv:2210.16262v1.

## Claim

For every finite group `G` of order at most 383:

1. `AMZA(G/N) <= AMZA(G)` for every normal Hall subgroup `N`;
2. `AMZA(G)=7/4` implies that `G` is nilpotent;
3. `AMZA(G') <= AMZA(G)` for the derived subgroup `G'`.

This is a computational finite theorem, not a full solution of any
unrestricted source question.

## Evidence

- GAP 4.15.1 and SmallGrp 1.5.4 enumerate all isomorphism types in scope.
- The source character-table formula is evaluated with exact algebraic values.
- Six known/source values, including the order-192 quotient counterexample,
  are reproduced exactly.
- 7,747 relevant normal Hall quotients, 6,892 nonnilpotent groups, and 976
  nonabelian derived-subgroup cases were checked with no violation.
- `code/2210_16262_amza_scan.g` is the complete verifier.
- `code/verification_output.txt` records commands, chunk counts, and summaries.

## Files

- `solution_packet.pdf`: human-readable proof and verification packet.
- `source_paper.pdf`: local copy of arXiv:2210.16262v1.
- `figures/open_problem_crop.png`: source Questions 6.2--6.4 on PDF page 16.
- `code/2210_16262_amza_scan.g`: exact GAP verifier.
- `verification_report.md`: mathematical, computational, novelty, and render QA.

## Human review recommendation

Re-run every command in `code/verification_output.txt`, confirm that the GAP
absolute-value operation remains exact on every encountered character sum,
and independently inspect the Hall-subgroup completeness argument.  Treat the
result as a substantial bounded partial unless a structural extension or
prior computation is located.

