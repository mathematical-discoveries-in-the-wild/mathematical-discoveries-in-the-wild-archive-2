# Verification report

Status: `candidate_full_solution_likely_valid`

## Mathematical audit

- Confirmed from the source that the cut norm is the supremum over arbitrary
  complex `L_infinity`-bounded one-variable functions, not merely indicators.
- Checked the conditional-expectation identity with the source inner-product
  convention `(<a,b>) = integral conjugate(a)b`.
- Checked that the `L_infinity(B)` unit ball is closed and bounded in
  `L2(B)`, hence weakly compact; source separability makes the restricted weak
  topology metrizable.
- Checked that the definition gives sequential continuity of the identity
  into cut norm, which is ordinary continuity on that metrizable domain.
- Checked the Arzela--Ascoli hypotheses: weak continuity, uniform pointwise
  boundedness, and equicontinuity of the indexed linear functionals.
- Checked the isometry to `L1`: the measurable complex phase of a
  `B`-measurable difference attains the dual supremum.
- Checked the layer-cake and complex positive/negative-part decomposition
  establishing equivalence with conditional rectangle indicators.
- Checked finite sigma-algebras and the atomless full-product Rademacher
  obstruction as opposite sanity examples.

## Reproducible checks

Run from the packet directory:

```bash
conda run --no-capture-output -n sandbox python code/make_crop.py
conda run --no-capture-output -n sandbox python code/verify_finite_models.py
```

The finite verifier enumerates all real sign tests for 348 randomized
partitions of product spaces of sizes 2, 3, and 4.  It checks both the
projected cut-test identity and the `L1` dual identity.  This does not prove
the infinite-dimensional compactness theorem.

## Literature and duplicate checks

The run registry, solution paths, target indexes, exact question wording, and
the combinations `weakly random sigma-algebra` / `cut norm` /
`characterization` were searched.  No duplicate packet or explicit later
answer was found as of 11 August 2026.

## Build and visual QA

- Built with `latexmk -pdf -interaction=nonstopmode -halt-on-error` into a
  temporary directory and copied only the final PDF into the packet.
- The final log has no warnings, undefined references, overfull boxes, or
  underfull boxes.
- The final PDF has 3 pages.  Every page was rendered at 1.7x resolution and
  visually inspected; the source crop is legible, equations and proof endings
  are intact, the reference fits cleanly, and no content is clipped.
- `solution_packet.pdf` SHA-256:
  `264b0a6edec0f67eb9ae6cdfc437d27f6cd90ada120758c4a61dcb93917e5117`.
- `source_paper.pdf` SHA-256:
  `0b670baec59a94f47e389e45933a2c8ede482a82ad3e7cb374270c284a7ed629`.
