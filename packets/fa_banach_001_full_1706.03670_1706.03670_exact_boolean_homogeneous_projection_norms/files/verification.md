# Verification report

Verdict: `candidate full solution, likely valid, human review requested`.

## Mathematical dependency audit

1. Every real Boolean-cube function has a unique multi-affine Fourier-Walsh polynomial; its supremum on `[-1,1]^n` is attained at a vertex.
2. The sharp one-variable Markov coefficient theorem identifies `M_{m,d}` with the relevant coefficient of `T_d` or `T_{d-1}`. This is stated explicitly in source equations (12)–(13).
3. Reducing ordinary monomials modulo `x_j^2=1` gives the unique Fourier-Walsh polynomial on the cube.
4. In the reduction of `(sum x_j)^k`, the degree is the cardinality of the odd-multiplicity support of the ordered index tuple.
5. A tuple with odd support `m` and `r` distinct indices satisfies `k >= m + 2(r-m)`, yielding the required lower-order collision bound.
6. The standard closed formula for Chebyshev polynomials at `i` gives exponential coefficient rate `1+sqrt(2)`.

No unproved lemma or numerical premise remains.

## Scope audit

- Fully answered: source Section 4.3, including the exact sharp norm for every fixed `(m,d)` after taking the supremum over dimensions.
- Not claimed: finite-dimensional attainment of the supremum.
- Not addressed: the Aaronson–Ambainis conjecture and subexponential growth of the source's Lorentz Bohnenblust–Hille constants.

## Computational sanity check

`code/check_chebyshev_limits.py` evaluates the symmetric Fourier formula. For `(d,m)=(6,2),(7,3),(10,6)`, the values converge toward the predicted Chebyshev coefficients `18`, `56`, and `1120`. This check is not used in the proof.

## Novelty audit

On 13 August 2026, searches covered the exact title/arXiv id and close variants combining “homogeneous parts”, “Boolean cube”, “Fourier level projection”, “Markov coefficient/numbers”, and “Chebyshev”. The search found the original open question, standard Markov coefficient estimates, and later general dimension-free bounded homogeneous projection work, but no exact formula `Lambda_{m,d}=M_{m,d}` and no explicit solution of Section 4.3. Novelty confidence remains provisional pending expert review.

## Human-review focus

- Confirm that the multilinear reduction of `T_{d'}((sum x_j)/n)` is exactly the Fourier-Walsh polynomial of its restriction to the cube.
- Confirm the exponent `(k+m)/2` in the parity-support collision count.
- Confirm that asymptotic attainment over increasing dimensions is sufficient for the source's uniform best-constant question.

## Artifact verification

- `latexmk` completed successfully; the final log has no warnings, undefined references, overfull boxes, or underfull boxes.
- `solution_packet.pdf` is a four-page A4 document and parses successfully with Ghostscript.
- All four pages were rendered at 170 dpi and inspected at original detail; the source crop, prose, equations, references, and page boundaries are clean and legible.
- `code/check_chebyshev_limits.py` ran successfully in the run's sandbox environment.
- SHA-256 of `solution_packet.pdf`: `57406aadae2c6e7e914a6c06531800b6a3197db433133f6c0c66ca02746185f9`.
- SHA-256 of `source_paper.pdf`: `312f3f2106f27dd7be6830b4a6e01a2f6decc6e0377dc7c44ea432baa34ced31`.
- Ledger JSON validation and `git diff --check` passed before archival.
