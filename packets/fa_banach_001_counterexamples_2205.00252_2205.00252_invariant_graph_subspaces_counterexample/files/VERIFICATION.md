# Verification report

## Verdict

`candidate_counterexample_likely_valid`

The formal proof is self-contained.  Exact finite-section calculations pass
and expose no indexing or boundary contradiction.

## Command

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2205.00252_invariant_graph_subspaces_counterexample/code/verify_counterexample.py
```

## Output

```text
all exact finite-section checks passed
checked graph invariance for powers 2 through 6
verified the q=1/2 graph is not invariant for the p=1/3 square
```

## What was checked

- Exact rational backward-shift matrices with weights `w_n=(1/2)^n`.
- Graph invariance for every residue `1 <= r < m`, for `2 <= m <= 6`.
- Full graph rank and properness in each finite section.
- Trivial intersection with the two coordinate residue spaces forming the
  graph.
- Distinct graph subspaces for two different slopes.
- The `m=2`, odd-residue graph omitted by Theorem 3.10.
- The explicit failure of invariance under the `p=1/3` square for the
  `q=1/2` graph.

Finite sections are not the proof.  The proof follows from orthogonality of
residue spaces and the exact commutation identity
`B^m(I+lambda B)=(I+lambda B)B^m`.

