# Additive–XOR counterexample for arXiv:math/0308091

Status: **candidate full counterexample, likely valid**, to the conjecture
`#B_n^sigma <= 3^n`.

An explicit normalized permutation `q` of `[32]` has 249 good ordered pairs,
whereas the identity has `3^5=243`.  The exact 32 fibre counts are printed in
the proof and reconstructed independently by the verifier.

For every `n>=5`, the block lift

`sigma_n(32*b+a)=32*b+q(a)`

has exactly `249*3^(n-5)` good pairs.  A carry out of the low five-bit block
would force `b xor d=b+d+1`, impossible by parity; without a carry, the base
condition separates from the `3^(n-5)` carry-free high-bit choices.

Scope: this disproves the source's three-term `B_n^sigma` conjecture.  It does
not resolve the separate four-term maximality conjecture for `A_n^sigma`; the
same permutation scores below the identity on that statistic.

Files:

- `main.tex` / `solution_packet.pdf`: full proof and finite certificate
- `source_paper.pdf`: original paper
- `figures/b_conjecture.png`: exact source-question crop
- `code/verify_counterexample.py`: independent exact verifier
- `VERIFIER_REPORT.md`: verification record

Ledger: `runs/fa_banach_001/ledger/results/0308091_walsh_additive_xor_counterexample.json`
