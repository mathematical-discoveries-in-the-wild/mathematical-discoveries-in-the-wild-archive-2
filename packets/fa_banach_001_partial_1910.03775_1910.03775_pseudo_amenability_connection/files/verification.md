# Verification report

Status: candidate partial result, likely valid, pending human review.

## Analytic checks

- Expanded the forward construction and checked exactly that both tensor
  products equal the adjoined identity.
- Applied the product map to the approximate-diagonal commutator to obtain
  the missing opposite-sided approximate-identity limit.
- Expanded the annihilation identity
  `b(xi_i-eta_i)c = r_i(b)c-r_i(bc)+b r_i(c)` term by term.
- Checked that multiplying a unitized projective tensor on the left and
  right by algebra elements places it in `A tensor_pi A`.
- Checked the centrality-dependent commutator identity used in the converse.
- Checked the order of quantifiers: the two possibly unbounded central
  localizers are fixed first, and only then is the tensor index chosen.
- Checked that local finite-set/tolerance approximants direct to an
  approximate diagonal.

## Upgrade attempts

Four deeper attempts are recorded in
`runs/fa_banach_001/attempts/1910.03775_pseudo_vs_approximate_semi_amenability.md`:
removing centrality, component extraction, finite Schatten-corner diagonals,
and a counterexample search. None supports a stronger honest claim.

## Build and visual audit

The final packet is compiled with `latexmk -pdf` in a temporary build
directory. Every final PDF page is rendered to PNG with `pdftoppm` and
visually inspected. The exact source-question crop is generated from PDF
page 24 by `code/crop_open_problem.py`.

Final outcome on 11 August 2026: `latexmk` completed in two passes with no
remaining warnings, undefined references, overfull boxes, or underfull
boxes. Text extraction found four pages and 7,551 characters. All four pages
were rendered at 150 dpi and visually inspected after the final compile; no
clipping, overlap, illegible formula, or malformed source image was found.
The packet SHA-256 is
`e7abe1399712cad29b61198eaa2ed1b8df8d92548b4489b79e4b5ed18984475f`.
The bundled source paper has 26 pages and SHA-256
`705b02f0ab38203a0e9626f3e2b65e960c37981eabca63cfd44f2af0c14e8e77`.

## Literature check

On 11 August 2026, bounded local-index and web searches used the exact arXiv
id, title, exact question wording, and the principal theorem keywords. They
found the source paper and general pseudo-amenability literature, but no
direct occurrence of the proved implications or commutative equivalence.
This is not an exhaustive novelty guarantee.

## Human-review recommendation

Check Theorem 4.2's local-to-net argument and perform a dedicated historical
search for equivalent statements under approximate-diagonal terminology.
The general noncommutative converse and the Schatten-class question should
remain explicitly excluded.
