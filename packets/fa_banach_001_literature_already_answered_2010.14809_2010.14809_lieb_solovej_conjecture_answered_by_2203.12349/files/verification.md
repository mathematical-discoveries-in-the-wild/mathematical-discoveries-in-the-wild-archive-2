# Verification

Status: `literature_already_answered` (full problem).

## Source evidence

- `source_paper.pdf` has 25 pages.
- The conjecture is equation (1.1), beginning on PDF page 1 and continuing on
  PDF page 2.
- The source states on PDF page 2 that the conjecture concerns non-integer
  values of `s` and that the authors do not know how to prove it in general.

## Supporting evidence

- `supporting_paper_2203.12349.pdf` has 13 pages.
- Its abstract says that the paper proves the Lieb--Solovej Wehrl-type
  conjecture for `SU(1,1)`.
- The introduction on PDF page 2 identifies the Bergman contractivity question
  as the question of Lieb and Solovej and says that the paper confirms it.
- Theorem 1.2 and Corollary 1.3 on PDF page 3 give the required general
  contractivity result.

## Normalization check

Kulikov uses

```text
dm(z) = dx dy / (pi (1-|z|^2)^2)
||f||_(A_alpha^p)^p = integral (alpha-1)|f|^p(1-|z|^2)^alpha dm.
```

Hence

```text
||f||_(A_2^2)^2 = (1/pi) integral_D |f|^2 dx dy,
||f||_(A_(2s)^(2s))^(2s)
  = ((2s-1)/pi) integral_D |f|^(2s)(1-|z|^2)^(2s-2) dx dy.
```

Corollary 1.3 applies because
`2/2 = (2s)/(2s) = 1` and `2 < 2s` for `s>1`. Raising its norm
inequality to the power `2s` and rearranging gives

```text
integral_D |f|^(2s)(1-|z|^2)^(2s-2) dx dy
 <= pi^(1-s)/(2s-1) (integral_D |f|^2 dx dy)^s,
```

which is exactly the source's disk formulation and transfers to equation
(1.1). The omitted endpoint `s=1` is an identity.

## File checks

- Source SHA-256:
  `b783a8a932c6a4d8dcc706f0dc9763e4806815ef1dc52c46ff6fec17220a094f`.
- Supporting SHA-256:
  `703b69593ff0ecea69a9db18dadabc360238bbe6768e663c3f04905cea2e1d3b`.
- The compact note was compiled with `latexmk -pdf -interaction=nonstopmode
  -halt-on-error -outdir=tmp main.tex` and visually checked after rendering.

No computational experiment is used as mathematical evidence.
