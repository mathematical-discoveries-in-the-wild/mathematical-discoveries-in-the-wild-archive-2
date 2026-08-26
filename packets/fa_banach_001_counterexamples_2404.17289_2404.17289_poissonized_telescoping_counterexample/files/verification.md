# Verification report

Verdict: candidate full counterexample, likely valid.

## Proof audit

- The series telescopes exactly because (a_k=s(k)-s(k+1)) and (s(k)\to0).
- Three differentiations of (s) give the uniform decay bounds used for
  (h=s-s(\cdot+1)), including (h''(x)=O(x^{-3}/\log x)).
- The Poisson expectation estimate uses only a second-order Taylor formula on
  (|N_t-t|\le t/2), the exact variance (t), and an exponential Chernoff
  bound off that event.
- The leading term is nonintegrable in absolute value on the positive-density
  logarithmic set (|\cos u|\ge1/2).
- The index conversion (x_{k+1}=(k+1)a_k) makes the paper's series and
  integral expressions exactly the constructed ones, and (x_k\to0).

## Computational regression

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2404.17289_poissonized_telescoping_counterexample/code/verify_poisson_counterexample.py
```

The script checks finite telescoping identities, the Poisson-smoothing error,
and the normalized leading asymptotic on logarithmic periods.  This guards
against indexing and sign errors but is not part of the proof.

Result: `PASS: telescoping identities, Poisson smoothing, and asymptotic sign`.
The four-page packet was rendered and visually inspected page by page.  Its
SHA-256 digest is
`07f8b8ec9579a503b8c5c59b828849fbc77d10cb22adf4eeebd6e62e6002c158`.

## Human-review focus

Review the central-event/tail decomposition in the Poisson lemma and the exact
index shift from (a_k) to the sequence (x\in c).  These are the only places
where an otherwise elementary construction could conceal an error.
