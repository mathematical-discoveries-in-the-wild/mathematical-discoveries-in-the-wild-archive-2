# Null-diagonal counterexample to four continuous Zauner conjectures

Status: `candidate_counterexample_likely_valid`  
Source: arXiv:2209.12833, Conjectures 2.8, 2.9, 3.7, and 3.8  
Agent: `agent_lane_03`  
Model: `GPT5.6`

## Result

All four universal conjectures are false as written. Take the circle group
with normalized Haar measure. Its diagonal has product measure zero, while
each conjecture requires that measure to equal `|mu(G)|^2/|d|`, which is one
when `d=1`. Thus the contradiction is simply `0=1`, independently of every
proposed vector or functional.

The packet proves the stronger structural statement that any locally compact
group satisfying one of the exact conjectural lists must be finite:
coordinatewise integrability plus self-normalization makes Haar measure
finite, hence the group compact; positive diagonal measure makes Haar measure
atomic, hence the group discrete; compact and discrete means finite.

This fully refutes the four conjectures, but it does not classify the source's
max-form Questions 2.6, 2.7, 3.5, and 3.6.

## Contents

- `solution_packet.pdf` — human-review packet after compilation
- `main.tex` — packet source
- `source_paper.pdf` — arXiv:2209.12833
- `source_nonarch_crop.png` — exact source excerpt for Conjectures 2.8--2.9
- `source_padic_crop.png` — exact source excerpt for Conjectures 3.7--3.8
- `code/make_source_crops.py` — reproducible source crops
- `code/verify_diagonal_measure.py` — finite-grid sanity check
- `verification.md` — proof, build, visual, and novelty audit

## Reproduce the sanity check

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2209.12833_continuous_zauner_diagonal_null_counterexample/code/verify_diagonal_measure.py
```

The computation illustrates that a normalized finite group of order `N` has
diagonal product mass `1/N`; the proof uses the exact nonatomic Haar identity
on the circle.

## Literature boundary

The run indexes and exact conjecture names were searched through 2026-08-11.
Searches returned the source and its companion discrete papers, but no later
correction or counterexample to these four continuous conjectures. This is a
bounded novelty check, not an exhaustive priority claim.

