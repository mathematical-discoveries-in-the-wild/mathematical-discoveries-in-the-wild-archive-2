# Verification report

## Claim checked

For every `1 < p <= 2` in the abstract setting of arXiv:2007.10209,
`alpha_p^opt >= rho_0^opt / 2`, and the symmetric two-point form attains
equality. Hence `K_p^opt = 1/2`.

## Checks performed

- Verified the exact source normalization:
  `rho_0 Ent(f) <= E(f,log f)` and
  `alpha_p H_p(f) <= (p/2) E(f,f^(p-1))`.
- Derived both Stieltjes identities twice: from the beta integral and by
  differentiating the proposed antiderivatives.
- Ran `code/check_identities.py` at p = 1.1, 1.37, 1.8; all quadrature checks
  passed.
- Audited integrability at s=0 and s=infinity using nonnegative Bregman
  remainders.
- Audited the abstract-domain step. Truncated mixture kernels are Lipschitz on
  the bounded range of f. Positive Riemann sums converge uniformly at the
  derivative level; Assumption 1 supplies the needed energy squeeze. No
  continuity of E is presumed.
- Audited the full-kernel energy comparison pointwise using the source's exact
  comparison axiom.
- Checked p=2 separately through the Poincare linearization of mLSI.
- Checked the two-point constants by exact power series and near-constant
  asymptotics.
- Compiled the packet without LaTeX errors and visually inspected every page
  after the final render.

## Scope and residual risk

- The proof targets precisely Assumption 1 and the definitions in the source.
- The originality search was bounded, not exhaustive. Human review should
  specifically check whether the positive shifted-entropy mixture has appeared
  in later citation literature.
- The most delicate proof point is the Riemann-sum energy squeeze; it is stated
  explicitly in the packet so a reviewer can test it independently.

Verdict: full proof likely valid, pending human review.

## Interrupted-lane recovery audit (2026-08-21)

The Stieltjes identities, positivity of the mixture, use of Assumption 1, and
the sharp two-point constants were rechecked independently. The checker was
rerun in the `sandbox` environment and again printed `all identity checks
passed`; the source crop was regenerated from PDF page 12. `main.tex` was
force-rebuilt to four pages. The log has no LaTeX errors, undefined
references, or overfull boxes. All pages were rendered at 120 dpi and visually
inspected without finding clipping, overlap, malformed formulas, or unreadable
evidence.

## Protocol structure QA (2026-08-21)

An explicit `Proof intuition` section now precedes the theorem and the
Stieltjes-mixture proof. The packet was force-rebuilt to four pages; the final
log has no LaTeX errors, undefined references, or overfull boxes. All four
pages were rendered with Poppler at 130 dpi and visually inspected. The source
crop, new section, theorem, proof, and page breaks are readable and unclipped.
SHA-256 of the final `solution_packet.pdf`:
`82592b1480f448f670d6e26bc32169a05bf3813b4e62710ffd794df7bbd7fcd6`.
