# Odd-window Gabor frame on a non-lattice density-two set

Status: `candidate counterexample, likely valid pending expert review`

Source: Markus Faulhuber, *On the Parity under Metaplectic Operators and an
Extension of a Result of Lyubarskii and Nes*, arXiv:1901.01220v2.

## Result

The source asks whether the odd-window non-frame theorem at lattice density
`(n+1)/n` continues to hold for every relatively separated discrete set of
that lower Beurling density. The universal extension is false already at
`n=1`.

Set

```text
g(t) = t exp(-1/(1-4t^2))  for |t|<1/2, and 0 otherwise,
Gamma = Z^2 union ((1/4,0)+Z^2).
```

Then `g` is odd and belongs to `C_c^infinity subset S_0(R)`. The non-lattice
set `Gamma` is uniformly discrete and has both lower and upper Beurling
density 2, but `G(g,Gamma)` is a frame for `L^2(R)`.

## Method

The Zak transform of `g` vanishes exactly on the vertical classes
`x=0,1/2 (mod 1)`. The transform of `T_(1/4)g` vanishes exactly on
`x=1/4,3/4 (mod 1)`. Hence they have no common zero. Critical-lattice Zak
diagonalization makes the two-window frame operator multiplication by the
sum of the two squared Zak transforms, which is continuous and strictly
positive on the compact torus. The two-window system over `Z^2` is precisely
the single-window system over `Gamma`.

## Scope

This is a full negative answer to the first question as a proposed universal
extension: one counterexample at `n=1` suffices. It does not decide separate
fixed-`n` assertions for `n>=2`, and it does not answer the two
higher-dimensional questions in the source.

## Files

- `main.tex`: self-contained counterexample and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_problem_crop.png`: the question on source PDF page 9.
- `code/verify_zak_multiplier.py`: numerical regression check.
- `verification.md`: audit and review priorities.

## Novelty check

The cheap run indexes and bounded arXiv/web searches covered the source title,
odd Gabor windows, relatively separated sets, Beurling density,
Lyubarskii--Nes, compactly supported windows, and shifted integer-lattice
unions. The closely related arXiv:2502.09510 was inspected. It uses the same
standard Zak multiplier for periodic sets but the search did not find this
explicit window, this two-coset counterexample, or an explicit answer to the
2019 question. Novelty confidence is moderate rather than certified.

## Human-review recommendation

Check the source quantifiers, the two-window Zak diagonalization, and the
endpoint zero calculation. The exact proof is independent of the numerical
script.
