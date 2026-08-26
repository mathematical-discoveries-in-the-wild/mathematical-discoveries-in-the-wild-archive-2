# Verification report

## Mathematical checks

- `b` is square summable because `sum_j (1-r_j^2) < infinity`.
- The pseudohyperbolic product for `r_j = 1 - 2^{-j}` has the uniform positive lower bound
  `prod_{m>=1} ((1-2^{-m})/(1+2^{-m}))^2`.
- Theorem 2.9 of the source paper therefore applies to the full integer orbit.
- A subfamily of a Bessel sequence is Bessel.
- On `e_j`, prime-suborbit analysis energy is `(1-r_j^2) sum_p r_j^(2p)`.
- Prime density zero plus Abel's theorem forces that energy to zero, so no lower frame bound exists.
- Euler's divergence of `sum_p 1/p` verifies the exact Müntz–Szász hypothesis.
- A single-vector example in arXiv:2606.20848 refutes the universally quantified `G` statement by taking `G={g}`.

## Provenance checks

- The first counterexample is explicitly present in arXiv:2605.29671, Example 3.4.
- The second counterexample explicitly identifies Conjecture 3 of arXiv:2511.10769 in arXiv:2606.20848.
- arXiv:2607.18491 explicitly cites the survey and gives the later natural-density classification.

## Artifact checks

- [x] LaTeX compiled without errors (TeX Live 2026, `latexmk`).
- [x] No undefined references, LaTeX warnings, or overfull/underfull boxes remain.
- [x] Extracted PDF text contains the theorem statements and provenance notice.
- [x] Every rendered page was visually inspected at 135 dpi.
- [x] PDF page count and file types were recorded: the solution packet has 4 US-letter pages; all five bundled artifacts identify as PDF files.

SHA-256 for `solution_packet.pdf`:

`2453338c89c465503318dbd25de885045736452eb5ad6bac63db48fd528d41f6`

## Human review

- [ ] Human expert review completed.
