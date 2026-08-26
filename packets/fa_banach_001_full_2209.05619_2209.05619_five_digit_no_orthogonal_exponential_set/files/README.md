# The five-digit irrational-mask example is never spectral

This packet gives a candidate full proof of the belief stated in Example 5.2
of An--He--Lai, *Classification of spectral self-similar measures with
four-digit elements* (arXiv:2209.05619, source PDF page 23).

## Result

For

```text
D = {0,1,3,5,6}
```

and every contraction `0 < rho < 1`, the equal-weight self-similar measure
`mu_(rho,D)` is not spectral. More strongly, its `L^2` space contains no
infinite orthogonal family of exponentials.

The proof generalizes: the same conclusion holds for every finite integral
digit set whose mask has no rational zero phase.

## Mechanism

The Fourier zero set is a finite union of families
`q^k(theta+Z)`, where `q=rho^(-1)`. Infinite Ramsey makes one phase `theta`
control all differences in an infinite subfamily. Gelfond--Schneider makes
that phase transcendental. Algebraic `q` is excluded by lacunarity of its
powers. Transcendental `q` lifts all difference identities to `Q(X)`, where a
degree-at-infinity lemma rules out an infinite clique in
`{X^k(R+n)}`.

## Files

- `main.tex`: source problem, generalized theorem, formal lemma, and proof.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: locally compiled arXiv source.
- `figures/open_problem_crop.png`: Example 5.2 and the authors' belief.
- `code/sanity_checks.py`: non-proof symbolic stress checks.
- `verification.md`: proof and render audit.
- `tmp/`: LaTeX build files and rendered pages.

Status: candidate full negative answer, likely valid. Independent expert
review should focus on the rational-function clique lemma.
