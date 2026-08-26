# Verification

## Mathematical checks

The proof was checked term by term.

1. `g(x)=|x|^(-(n+2)/4)` lies in `L^2` exactly because `n>2`.
2. `theta >= 1-R^(n-1)>0`, while `(1-theta)^(-1)=|x|^{-(n-1)}`
   is integrable on an `n`-ball.
3. The normalization gives `T u_r = 1` exactly.
4. The weighted quadratic cost is a positive constant times `r^(n/2)`.
5. `W_{0,theta}(u_r) <= J_0(u_r)` is bounded by a positive constant times
   `r^((n-2)/4)`.
6. Zero total objective would force both `u=0` and `Tu=1`, a contradiction.
7. For `n<=2`, BV boundedness implies L2 boundedness via the continuous
   critical embedding; compactness is not needed because weak compactness in
   reflexive `L^2` suffices.

## Automated scaling check

```text
conda run --no-capture-output -n sandbox python code/verify_scaling.py
PASS: dimensions 3..100 and the normalized n=3 formulas agree.
```

## Source evidence

`references/source_crop_theorem_2_8.pdf` contains exact physical pages 7--8
of the arXiv PDF: the theorem has no dimension restriction and its proof
explicitly invokes compact embedding of `BV(Omega)` into `L^2(Omega)`.

## PDF checks

The final PDF was compiled with `latexmk` into `tmp/` and copied to the packet
root.  The final log has no warning, overfull, underfull, or undefined-reference
messages.  Ghostscript `nullpage` validation passed.

```text
Pages: 3
Page size: 612 x 792 points (letter)
solution_packet.pdf SHA-256:
dcd2941e1855d55f2a4ff724f3f77cd5b115b54218759e24a53f61af378bec96
```

All three pages were rendered at 180 dpi to `tmp/render-01.png` through
`tmp/render-03.png` and visually inspected.  Equations, theorem statements,
page breaks, links, and the bibliography are legible and unclipped.
