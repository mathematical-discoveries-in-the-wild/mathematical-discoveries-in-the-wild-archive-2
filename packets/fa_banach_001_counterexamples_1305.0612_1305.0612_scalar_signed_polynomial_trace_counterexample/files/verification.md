# Verification report

status: likely valid candidate full counterexample

## Proof-critical checks

1. The source quantifies over all Hermitian dimensions, all positive integers
   `q`, and every `s>0`; therefore scalar matrices and `q=3` are admissible.
2. With `A=1/100`, `B=-1`, and `C=1`, all three scalar matrices are nonzero
   (hence invertible), while `A-B=101/100>0`.
3. Thus `(A-B)_+=101/100`, `(A-B)_-=0`, `C_+=1`, and `C_-=0`.
4. The exact left side for `q=3` is `1000001/1000000`.
5. The exact right side for `s=1` is `60603/200000000`; it is strictly smaller.
6. The source technical report accidentally omits a trace sign on the
   polynomial right side, while the later published restatement includes it.
   In dimension one the two readings coincide.
7. The uniform parity construction with `A=0`, `B=-1`,
   `C=(-1)^(q+1)`, and `s=q` gives left side `1` and right side `0` for odd
   `q`, or `1/2` for even `q`, for every `q>=2`.

## Exact mechanical check

Run from the packet directory:

```sh
conda run --no-capture-output -n sandbox python code/verify_scalar_counterexample.py
```

The script uses rational arithmetic, checks the invertible `q=3` example, and
checks the uniform family through `q=30`. The proof is the direct exact
substitution, not the computation.

## Literature and novelty check

The run's cheap indexes were searched by arXiv id, title, and the exact signed
mean-value terminology. A bounded primary-source search found the 2013 report,
the 2016 published restatement of the conjecture, and later unsigned
mean-value trace inequalities, but no proof or counterexample to the signed
polynomial statement. The novelty assessment is therefore only "apparently
new within the bounded search."

## Recommended human focus

Check the positive/negative-part allocation in the source display. For the
`q=3` example every nonzero right-side contribution is multiplied by
`|A|^(q-1)=10^(-4)`, whereas the left side sees the unit-sized value of
`-B^q`. This is the entire mechanism.

## Packet QA

- `pdflatex` completed twice with no remaining warnings, undefined references,
  or overfull/underfull boxes.
- Both pages of the final PDF were rendered at 150 dpi and inspected
  individually. The source excerpt and all equations are readable; no content
  is clipped, missing, or crowded.
- The exact-arithmetic script returned `PASS`, and the result ledger parsed as
  valid JSON with model `GPT5.6`.
- Final packet SHA-256:
  `529d5929feeeade7ac6145635261eb1b9aa273f9887ddb5c5ac55b12976053a3`.
