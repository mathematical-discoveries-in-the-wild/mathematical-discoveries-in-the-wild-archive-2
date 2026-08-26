# Verification report

- The modular estimate uses only 1 <= p(x) <= p^+ < infinity.
- Local L1 limits of functions bounded by M remain essentially bounded by M.
- Integer unit intervals give global essential bounds for both profiles.
- The asymptotic remainder vanishes along every integer subsequence.
- Once both decomposition pieces are bounded, the modular lemma applies.
- The reverse inclusions are Theorem 3.7(i) of the source.

The finite-grid checker reports:

    PASS: 1200 variable-exponent modular checks
    verified rho(u/eps) <= [1+(B/eps)^(p+-1)] ||u||_1/eps

Reviewer focus: verify that the forward translated limit inherits the bound
of f and the reverse almost-automorphic limit transfers it to g.
