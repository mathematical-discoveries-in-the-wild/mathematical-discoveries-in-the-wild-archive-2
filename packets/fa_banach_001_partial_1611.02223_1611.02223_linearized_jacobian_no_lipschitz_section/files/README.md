# Linearized Jacobian obstruction for arXiv:1611.02223

**Status:** candidate substantial partial result, likely valid; human review
requested.

The source's Conjecture 7.1 asks whether

```text
J : dot W^{1,np}(R^n,R^n) -> H^p(R^n)
```

has a continuous right inverse for every `n>=2` and `1<=p<infinity`.

This packet proves two negative regularity results:

1. `DJ(u)` is not surjective for any base map `u` and any `p>=1`.
2. Therefore every hypothetical right inverse is Gâteaux-differentiable
   nowhere, and no locally Lipschitz right inverse exists even locally over a
   nonempty open subset of the target.

The proof translates a fixed target-dual bump into disjoint regions where the
`L^{np/(n-1)}` mass of `cof(Du)` tends to zero. Thus the adjoint of `DJ(u)` is
not bounded below. Phelps's differentiability theorem converts any locally
Lipschitz section into an impossible Gâteaux-differentiability point.

This includes the exponent `p=2`, which is not covered by the general
submersion obstruction in arXiv:2010.10497. It does **not** rule out a merely
continuous right inverse or settle bare surjectivity.

Files:

- `solution_packet.pdf`: review-ready partial-result packet.
- `main.tex`: complete LaTeX source.
- `source_paper.pdf`: original source paper.
- `figures/open_conjecture_crop.png`: source PDF crop containing Conjecture 7.1.
- `code/crop_open_question.py`: reproducible crop script.
- `tmp/`: build and rendered-page verification files.

Novelty confidence is moderate after bounded index and web searches. Expert
comparison with the published nonlinear-open-mapping literature is advised.
