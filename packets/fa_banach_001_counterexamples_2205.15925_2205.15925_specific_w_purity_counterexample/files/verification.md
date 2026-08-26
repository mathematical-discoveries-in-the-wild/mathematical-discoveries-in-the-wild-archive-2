# Verification record

Date: 2026-08-12

## Source evidence

- Official arXiv PDF: `figures/source_2205.15925.pdf`.
- Exact open problem: PDF page 2, rendered as
  `figures/source_open_problem.png`.
- Specific zero-integral restriction of `A^{-1}`: PDF page 6, rendered as
  `figures/source_construction.png`.

## Mathematical checks

The counterexample was audited along five independent axes:

1. Operator hypotheses: `A e_k=k^{-1}e_k` is bounded, self-adjoint,
   injective, non-invertible, and has simple spectrum.
2. Exact source model: the cyclic vector `(1+k^2)^(-1/2)` makes the source's
   Herglotz measure counting measure on the nonzero integers, so the displayed
   restriction is literally the one used in the proof.
3. Domain legitimacy: `Dom M_k` embeds into `ell1` by Cauchy--Schwarz, hence
   the zero-sum constraint is well-defined; odd sequences satisfy it.
4. Form splitting: multiplication by `k` reverses parity, forcing the closed
   form of the restriction to split orthogonally. Its positive square root is
   therefore multiplication by `|k|` on the odd sector.
5. Polar computation: surjectivity of multiplication by `|k|` from its odd
   domain gives `V=J` and hence `W=I` on the entire odd sector.

Run:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2205.15925_specific_w_purity_counterexample/code/verify_parity_model.py
```

The script checks the parity reversal and orthogonality identities on several
finite sections, verifies `T=V|T|` and `JV=I` on every odd basis vector, and
checks Herglotz summability.

## Review focus

The highest-value human checks are that the chosen cyclic vector produces
exact counting measure under the source's normalization, that the form
decomposition indeed implies equation (9) by uniqueness of closed-form
representation, and that the source's `V` is exactly the polar isometry of
the displayed restriction.

## Final artifact checks

- Analytic verifier: passed.
- LaTeX build: passed with no warnings, undefined references, or overfull or
  underfull boxes in the final log.
- Rendered-page inspection: all 5 final pages inspected at 150 DPI after the
  last edit; no clipping, overlap, illegibility, or malformed mathematics.
- Packet SHA-256:
  `1ffca937954c632206b4e49aca9095d5f48f08de28c27f093ab397d78d4ab74a`.
- Source PDF SHA-256:
  `c1fa19b36ba4175c29b58362a7723c9421d2d4445c2c9dcb8e56c58763450d60`.
