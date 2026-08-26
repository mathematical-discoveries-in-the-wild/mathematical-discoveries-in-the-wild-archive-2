# Verification

## Claim-to-source audit

- Source problem: `source_1604.05072.tex`, around line 1410, displays the
  normalized reciprocal sum from `k=2` to `N+1` and calls its validity open.
- Source convention: the same section defines `mu_1=0` and `mu_2` as the
  first nontrivial Neumann eigenvalue.
- Exact proof: `supporting_2606.08271.tex`, Theorem 1.2 (label
  `thm:main-euclidean`), proves the `N`-term reciprocal inequality for smooth
  bounded domains and characterizes equality by balls.
- Lipschitz formulation: `supporting_2607.19008.tex`, Theorem 1.1 (label
  `thm:HLT`), states that the same result remains valid for every bounded
  Lipschitz domain.
- Normalization: the packet algebraically expands
  `R_Omega=(|Omega|/omega_N)^(1/N)` and verifies that the later normalized
  deficit is exactly the source's scale-invariant display.
- Scope audit: the source's independent planar Steklov sharp-bound question
  is expressly excluded.

## Mechanical checks

Run from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Then inspect the log for undefined references, citations, and overfull boxes;
render every page of `solution_packet.pdf` and inspect the page images.

Completed on 2026-08-11: `latexmk` converged in two runs with no undefined
references, citation warnings, or overfull boxes. Both pages were rendered at
150 dpi and visually inspected. The final PDF SHA-256 is
`b08249bcc05eed8a395ceeb1ddf75b9b7142f2026e8d08c972cc43da20a14736`.

## Literature lookup

Primary-source searches on 2026-08-11 located arXiv:2606.08271 and the
follow-up arXiv:2607.19008. The included TeX sources were checked directly,
not merely their abstracts.
