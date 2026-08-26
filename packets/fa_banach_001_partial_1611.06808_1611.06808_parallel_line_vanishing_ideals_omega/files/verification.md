# Verification record

Status: `candidate_partial_result_likely_valid`  
Agent: `agent_lane_03`  
Model: `GPT5.6`  
Date: 2026-08-11

## Mathematical audit

- The source statement is Conjecture 2.3 on printed page 6: every
  value-vanishing ideal in `C-infinity(R^d)` has property `(Omega)`.
- For finitely many parallel lines, simultaneous restriction has the explicit
  continuous right inverse built from transverse functions satisfying
  `chi_i(b_j)=delta_ij`. Thus `P=ER` is a continuous projection with kernel
  exactly the ideal vanishing on every carrier line.
- Under this splitting, vanishing on `K` is equivalent coordinatewise to
  membership in the one-dimensional slice ideals `J_i`. This gives the stated
  topological direct sum for `I_K`.
- The packet now proves directly, from the approximation definition, that
  `C-infinity(R^d)` has `(Omega)`: cutoff, mollification at scale `delta`, and
  Taylor/convolution estimates give low-order error `O(delta)` and prescribed
  high-order norm `O(delta^-k)`.
- The packet also proves the two permanence facts used: continuous projections
  transfer the defining decomposition to complemented subspaces, and finitely
  many coordinate estimates combine to give finite-direct-sum stability.
- The source's Theorem 2.1 supplies `(Omega)` for every closed ideal of
  `C-infinity(R)`, including every slice ideal. The conclusion follows.
- Empty slices cause no exception: then `J_i=C-infinity(R)`, covered either by
  the source theorem or by the packet's direct lemma.
- The proof does not use compactness beyond making each slice a compact source
  target; in particular, it imposes no regularity or density assumption on a
  slice.

## Full-upgrade audit

The durable attempt note records eight materially distinct routes. The direct
cutoff, finite-order Whitney correction, multivariate interpolation, union
partition, fiber-product, sparse-sequence counterexample, general carrier
transfer, and parallel-line upgrade were each pursued. The first six expose
specific obstructions; the seventh gives a transfer principle; the eighth
closes the stated higher-dimensional class. The remaining universal step
would require a new controlled multivariate selection/interpolation theorem,
so the result is correctly classified as partial.

## Reproducible structural check

Command:

```text
conda run --no-capture-output -n sandbox python code/verify_parallel_line_splitting.py
```

Output:

```text
exact transverse interpolation matrix: identity
simultaneous restriction/right-inverse checks passed on 303 samples
```

This checks the explicit interpolation and restriction identities, not the
abstract `(Omega)` estimates.

## Literature and source audit

- No duplicate was found in the run registry, solution index, attempt index,
  or proof-gap index.
- Exact source wording, core keywords, the DOI's later citations, and the
  separate union-stability question were checked through 2026-08-11.
- Semantic Scholar returned one later citation, A. Goncharov's 2025 survey
  *Bases and Isomorphisms of Whitney Spaces*; it does not settle Conjecture 2.3.
- The supporting Vogt paper's first page was text-audited and its bibliography
  entry corrected to *Splitting of exact sequences of Frechet spaces in the
  absence of continuous norms*. It supplies background only; the packet proves
  the permanence facts it uses.
- This is a bounded novelty check, not an exhaustive priority claim.

## Build and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully.
- Final log search found no LaTeX warnings, undefined references, overfull
  boxes, or underfull boxes.
- The final three-page PDF was rendered at 1.8x with PyMuPDF.
- Every rendered page was visually inspected. The source crop is legible; no
  text, equations, references, borders, or page numbers are clipped or
  overlapped.

## SHA-256

- `solution_packet.pdf`:
  `0881c65e3db36c17836d9f3c29b267d309916989669756848910d752401205cb`
- `source_paper.pdf`:
  `df291b18ce774f78b4d6157b1031093ddeec441f5869570e1426961b675e18b9`
- `references/vogt_omega_smooth_spaces.pdf`:
  `40533a16ee670fe4fbae796866a1c542992cae1bf7e36ba6dfe716ed2fa33541`
- `question_crop.png`:
  `34934aa4c065424a8be8d2e1e4606df03615180740991372e36f640c7fe8fbb4`

