# Two-phase generalized Ewens counterexample

- **Source:** P.-M. Samson, *Transport-entropy inequalities on locally acting
  groups of permutations*, arXiv:1609.07315v3, PDF page 6.
- **Question:** generalize the paper's preceding transport--entropy
  inequalities to generalized Ewens distributions.
- **Status:** candidate full counterexample to the parameter-uniform direct
  extension; likely valid, wording-scope review requested.
- **Model:** `GPT5.6`.

On `S_64`, set

```text
theta_1 = 1,
theta_k = 10^(-200)       (2 <= k <= 63),
theta_64 = 1/63!.
```

The identity has raw weight one, and the whole class of 64-cycles also has
raw weight one.  Every other permutation has total raw mass
`r <= 64! 10^(-200) < 10^(-100)`.  The law is therefore an arbitrarily clean
half-identity/half-long-cycle mixture while all weights remain strictly
positive.

Taking the first marginal to be the identity point mass and the second to be
this generalized Ewens law makes all couplings unique.  The Hamming and
transposition costs are order `64`, while the only entropy is
`log(2+r) < 0.7`.  Direct substitution shows that each of the source's
displayed inequalities (7), (8), and (9) fails with its stated constant.

This disproves any extension uniform over arbitrary positive cycle weights
with the source constants (indeed, the construction scales to defeat every
universal `O(n)` constant).  It does not rule out inequalities whose constants
depend on quantitative regularity of the weight sequence.

Files:

- `solution_packet.pdf`: source-backed construction and proof.
- `source_paper.pdf`: arXiv:1609.07315v3.
- `code/verify_bounds.py`: high-precision audit of all five strict failures.
- `VERIFICATION.md`: hypothesis and constant audit.
- Attempt record:
  `attempts/1609.07315_generalized_ewens_transport_upgrade.md`.
