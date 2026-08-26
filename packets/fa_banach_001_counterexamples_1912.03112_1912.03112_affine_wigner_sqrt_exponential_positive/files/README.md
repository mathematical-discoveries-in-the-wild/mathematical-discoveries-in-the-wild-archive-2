# Square-root exponential counterexamples to affine positivity

status: counterexample_likely_valid

source_arxiv: 1912.03112

source_paper: Eirik Berge, Stine Marie Berge, and Franz Luef, *The Affine
Wigner Distribution* (2019), subsection “Affine Positivity Conjecture,”
printed pages 25–26 (PDF pages 25–26).

## Claimed Result

The source conjectures that every nonzero function in
`L^2(R_+, dr/r)` with an everywhere nonnegative affine Wigner distribution is
a generalized Klauder wavelet. The packet disproves this classification.

For every `p > 0` and `beta > 0`, normalize

```text
psi(r) = r^p exp(-beta sqrt(r)).
```

Then `psi` belongs to `L^2(R_+, dr/r)` (indeed to the source paper's
log-Schwartz class), its affine Wigner distribution is nonnegative at every
point of the affine group, and it is not a generalized Klauder wavelet.

## Proof Mechanism

For a fixed scale `a > 0`, the affine Wigner distribution is the Fourier
transform of its slice kernel. With

```text
h(u) = u / (2 sinh(u/2)),
f(u) = sqrt(u coth(u/4)) - 2,
```

the slice kernel, divided by its positive value at zero, is

```text
h(u)^(2p) exp(-beta sqrt(a) f(u)).
```

Both factors are positive definite:

- Euler's product for `sinh` writes `h^(2p)` as a limit of products of
  Gaussian mixtures.
- A partial-fraction expansion for `coth` makes
  `q(u) = u coth(u/4) - 4` conditionally negative definite. Since
  `f(u) = sqrt(4 + q(u)) - 2`, the subordination formula for the square root,
  together with Schoenberg's theorem, makes `exp(-c f)` positive definite for
  every `c > 0`.

The full kernel is also integrable. Bochner's theorem and Fourier uniqueness
therefore imply that its Fourier transform is a continuous nonnegative
function.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered human-review packet.
- `verifier_report.md`: adversarial proof audit.
- `code/check_counterexample.py`: independent algebra, Gram-matrix, and FFT
  diagnostics over 60 parameter triples.
- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_context_crop.png` and `figures/open_problem_crop.png`:
  the two-page source conjecture evidence.

## Novelty Check

Bounded local-index and arXiv-focused web searches on 2026-08-09 covered the
paper/arXiv id, the exact phrase `Affine Positivity Conjecture`, combinations
of `affine Wigner`, `nonnegative`, `generalized Klauder`, `counterexample`,
and the square-root-exponential family. The searches returned the source
paper and older background on positive Morse/Klauder states, but no later
paper explicitly resolving the conjecture and no occurrence of this family as
a counterexample. This is a bounded search, not a priority claim.

## Human Review Recommendation

Send to expert review as a full counterexample. The main points to check are
the conditional-negative-definiteness partial fraction, the square-root
subordination step, and the passage from an integrable positive-definite slice
kernel to pointwise nonnegativity of its Fourier transform.
