# Verification Report

Candidate: quantum (L^2)-KKL for pairwise-anticommuting Pauli sums

## Claim checked

For a real normalized linear combination of distinct nonidentity pairwise
anticommuting (n)-qubit Pauli strings,

\[
 \max_j\operatorname{Inf}_j^2(A)
 \ge \frac{6}{\sqrt{24n+9}+3}.
\]

## Verdict

`likely valid`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| (A) is Hermitian, unitary, and balanced | valid | Pairwise anticommutation cancels all cross terms in (A^2); every nonidentity Pauli string is traceless. |
| Fourier formula for influence | valid | Orthonormality of the Pauli basis gives (q_j=\sum_{s:j\in\mathrm{supp}(\Gamma_s)}c_s^2). |
| Global-to-local pair cover | valid | Two Pauli strings anticommute iff the number of locally anticommuting coordinates is odd, hence nonzero. |
| Per-coordinate weighted count | valid | It is (xy+xz+yz\le(x+y+z)^2/3=q_j^2/3). |
| Lower bound involving (a=\max c_s^2) | valid | (Q\ge a), and (\sum_s(c_s^2)^2\le a\sum_sc_s^2=a). |
| Scalar optimization | valid | The increasing and decreasing branches meet at (a^2=3(1-a)/(2n)), whose positive root is the claimed constant. |
| Implication for KKL | valid | (n^{-1/2}) dominates ((\log n)/n) uniformly. |

## Counterexample search

`code/verify_small_cases.py` exhausts all (2^{15}) subsets of nonidentity
two-qubit Pauli strings, retains every pairwise-anticommuting family, and tests
multiple deterministic weight vectors for each. It also performs deterministic
random greedy tests for three qubits. No violation was found.

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2209.07279_anticommuting_pauli_quantum_kkl/code/verify_small_cases.py
```

The finite computation is not used in the proof.

## External dependencies

None beyond the standard Pauli-basis definition of quantum influence used in
the source paper.

## Gaps and scope

- The theorem is a subcase only. It does not control general Pauli supports
  with commuting-product cancellations.
- The bounded literature search did not find the exact result, but this is not
  a guarantee of novelty.

## Confidence

Score: 94/100.

Reason: the proof reduces to a positive weighted covering count and a
one-variable optimization; the main risk is novelty, not correctness.

## Human review recommendation

Send to a human reviewer, focusing on the pair-cover count and exact influence
normalization.
