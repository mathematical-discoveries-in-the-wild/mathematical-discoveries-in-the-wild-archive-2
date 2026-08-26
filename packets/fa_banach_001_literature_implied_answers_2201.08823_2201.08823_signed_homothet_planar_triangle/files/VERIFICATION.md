# Verification record

## Mathematical identification

- The source statement is Conjecture 4 on PDF page 6 of arXiv:2201.08823.
- The supporting statement is Theorem 1 on PDF page 2 of Dumitrescu--Jiang, EJC 15 (2008), R37.
- On that same supporting page the authors define both positive and negative homothetic copies. Their proof then separates positive and negative cases, so the theorem is genuinely mixed-sign rather than positive-only.
- The affine identity
  \(A(\lambda K+t)=\lambda A(K)+Lt+(1-\lambda)b\) for \(A(x)=Lx+b\)
  was checked directly and preserves coefficient signs and magnitudes.
- The central-symmetry reduction uses \(-K=K-2c\), hence
  \(-\mu K+t=\mu K+(t-2\mu c)\).
- The packet explicitly limits the result to planar triangles and centrally symmetric planar bodies.

## Direct-attack code check

The copied triangle checker was rerun in the `sandbox` environment on the mixed pair \((0.9,-0.9)\), grid denominator 20. It returned an exact LP uncovered margin `0.03333454459723101`, consistent with the earlier searches and demonstrating that the durable checker executes successfully.

## PDF checks

- `latexmk` completed with no errors, overfull boxes, or underfull boxes. The only warning was LaTeX changing a float specifier from `h` to `ht`.
- Final packet: 3 pages, 255,653 bytes.
- All three final pages were rendered to PNG in RGB at 130 dpi and visually inspected. Text, equations, captions, borders, and both genuine source excerpts are legible and unclipped.
- The source excerpt is embedded directly from page 6 of the official arXiv PDF.
- The decisive theorem excerpt is embedded directly from page 2 of the official EJC PDF.

## SHA-256

```text
130e70f2f9db7b57e990a816a28c41ecfb6de7bfa9c06e2dc17a2cf1707277fe  solution_packet.pdf
8d1e265a695c9a87fa995f985fda5c8f65fdee21211d737db64d04c0d647737f  source_paper.pdf
f4ac7e02cf640fa419be3897bfeb2277041ef9274acea3abfc92e9e8df5124c6  supporting_dumitrescu_jiang_2008.pdf
b8135b118f2c1b0e97f472f32169691a7886bd33afbfd3997c75dc7734d754e9  solution.tex
fa2aaadd16f4b253db0c4a5d686a7afd18d4f4c6143810b1c048cb3180bc2123  code/signed_triangle_search.py
95dd9f88971043ad88ff1117e1e50b4e11a349d7b66f939b9d16c358bd0fb38d  code/signed_polygon_search.py
```

