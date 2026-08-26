# Verification report

## Algebraic audit

- The common-left-inverse lemma was checked directly from `[X w]^{-1}`.
- The cycle indexing uses `Q_j=X_{j-1}` and the last endpoint
  `X_n=Q_1 H^{-1}`; hence the last common inverse satisfies `P_n Q_1=H`.
- The backward determinant coefficient is the `j`th leading principal minor.
- The strong-leading-minor induction uses the invertible Schur complement.
- The lower-bound rounding is strict when `H != I`: `d <= n-2` makes the
  source bound larger than `n-1`, so integral rank is at least `n`.

## Computational audit

Command:

```text
conda run --no-capture-output -n sandbox python code/verify_frame_path.py
```

Observed checks:

```text
k=1 p=3 reached=8 qualifying=1 distances={2: 1} missing=0
k=2 p=2 reached=42 qualifying=2 distances={3: 2} missing=0
k=2 p=3 reached=624 qualifying=27 distances={3: 27} missing=0
k=3 p=2 reached=2520 qualifying=48 distances={4: 48} missing=0
constructive validation k=2 p=2: all 6 invertible endpoints passed
constructive validation k=2 p=3: all 48 invertible endpoints passed
constructive validation k=3 p=2: all 168 invertible endpoints passed
```

The computation is supporting evidence only; the proof is field-uniform.

Final PDF: 5 pages, visually inspected page by page. SHA-256:
`e0dff770e59d225fdb8ed7fca7f1d2e3b4a693645f1514054d8a958df7ea0a0d`.

## Literature caveat

The Cohen--Pereira article was not available as an open full text. The
literature implication is supported by the source author's thesis, which
states the exact relevant upper bound and cites that article. Human review
should inspect the original theorem before upgrading the provenance status.
