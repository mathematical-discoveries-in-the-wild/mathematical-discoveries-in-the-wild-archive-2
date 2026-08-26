# Verification

Status: candidate full answer to the stated trace problem, likely valid, subject to human review.

Mathematical checks:

- Checked the exact open statement in Remark 3.5 of arXiv:2302.00721v3.
- Checked Definition 2.4: the distribution projection is applied to the modulus of an affiliated operator.
- Verified by functional calculus that `exp(itL)` is unitary and hence has modulus `I`.
- Derived the distribution function, generalized singular numbers, and weak Lorentz norm directly from the definitions, including finite- and infinite-trace cases.
- Separately computed the literal normal-operator spectral projection as the pushforward of the spectral measure of `L`.
- Stress-tested both readings for `G = R^n`, `L = -Delta`: the distribution trace is infinite below threshold 1, while the literal resonant projection has trace zero for nonzero time.
- Compared this degeneracy with the direct Euclidean Schrödinger kernel to isolate the missing mechanism: phase cancellation.

Novelty/literature check:

- Searched `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and `proof_gaps/index.tsv` for arXiv:2302.00721 and the central trace/unitary-propagator phrases; no exact prior run result was found.
- Searched the current arXiv record, exact title, exact open-problem phrase, arXiv id, and close variants through 11 August 2026.
- The source was last revised on 16 February 2026 and still labels the trace problem open.
- No later paper explicitly making this computation was found in the bounded search. This is not an exhaustive priority claim.

Artifact checks:

- `source_paper.pdf` was compiled locally from the official ingested arXiv v3 TeX source because the cached artifact was a source archive rather than a PDF.
- The source evidence is the full rendered page 14, not an OCR reconstruction.
- The packet was compiled with `latexmk`, rendered page by page, and visually inspected.

Human-review focus:

1. Confirm that Remark 3.5 intends the distribution projection from Definition 2.4; if so, the modulus computation is decisive.
2. If the omission of the modulus was intentional, confirm the literal pushforward formula for the resonant eigenspace.
3. Decide whether the repository should label this as a full answer to the exact trace problem or as a sharp obstruction relative to the broader goal of all classical dispersive estimates.
