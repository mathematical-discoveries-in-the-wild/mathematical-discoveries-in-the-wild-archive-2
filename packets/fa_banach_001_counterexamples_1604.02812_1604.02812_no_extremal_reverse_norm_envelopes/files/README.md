# Reverse extremal norm envelopes can fail

Status: `candidate counterexample (full answer)`.

Source target: Mohsen Kian, *C*-convexity of norm unit balls*,
arXiv:1604.02812, the two questions on PDF page 11 after Corollary 3.5.

## Counterexample

On `M_3`, let `omega_*` be the dual numerical-radius norm and define

```text
p(A) = max(||A||_1, (3/4) omega_*(A)).
```

Both component norms are L-norms.  For `E=E_11`, `J=E_23`, and `X=E+J`,

```text
p(E)=1,   p(J)=3/2,   p(X)=9/4.
```

Compressing `X` onto the two diagonal blocks therefore violates the L-norm
inequality: `1 + 3/2 > 9/4`.  Thus `p` is not an L-norm.  If a greatest
L-norm below `p` existed, it would dominate both component L-norms and hence
equal their maximum `p`, a contradiction.

The construction is robust: replacing `3/4` by any `c` in `(1/2,1)` gives
the same contradiction.

Dualizing gives the companion counterexample.  The explicit norm

```text
r(A) = inf_{A=B+C} (||B||_infinity + (4/3) omega(C))
```

has no least M-norm above it.

## Files

- `main.tex` and `solution_packet.pdf`: complete proof and provenance.
- `source_paper.pdf`: source paper.
- `figures/source_question_page11.png`: exact source-question page.
- `code/verify_counterexample.py`: exact matrix-value verifier.
- `VERIFICATION.md`: proof, computation, literature, and PDF audit.
