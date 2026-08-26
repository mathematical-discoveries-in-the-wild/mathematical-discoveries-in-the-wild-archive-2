# Verification report

Status: candidate substantial partial result, likely valid.

## Analytic audit

1. If `x` is supercyclic and `f(Tz) = mu f(z)` with nonzero `f`, then
   `f(x) != 0`; otherwise the whole projective orbit lies in `ker(f)`.
2. Every tail of a projective orbit of a supercyclic vector is dense. In
   dimension greater than one, otherwise a nonempty open set would have its
   dense projective-orbit intersection contained in finitely many proper
   complex lines. The one-dimensional case is immediate.
3. For a target `y` outside `ker(f)`, choose `alpha_k T^(n_k)x -> y` with
   `n_k -> infinity`. Applying `f` gives
   `alpha_k mu^(n_k) -> f(y)/f(x)`, a nonzero scalar.
4. Tail universality supplies `gamma_k in Gamma` with
   `gamma_k mu^(n_k) -> f(y)/f(x)`. Therefore
   `gamma_k/alpha_k -> 1`, which transfers the vector convergence.
5. The complement of `ker(f)` is dense, so capturing all targets with
   nonzero `f` already makes the Gamma-projective orbit dense in `X`.
6. In the explicit construction, nearest Gaussian-lattice rounding gives an
   error at most `sqrt(2)/(2n)` and the rounded point lies in `F_n` for all
   sufficiently large `n`.
7. If `r=|mu|>1`, the nth block has outer radius at most `n r^(-n)`,
   which tends to zero. If `0<r<1`, every nonzero point in the nth block has
   modulus at least `r^(-n)/n`, which tends to infinity. Either way the
   countable scalar set is non-dense.

## Numerical checker

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1509.04912_nonunit_eigenvalue_tail_scalars/code/verify_tail_scalars.py
```

Recorded output:

```text
lambda modulus: 2
maximum lattice recovery error: 0.025
block outer radii: 0.03125, 0.000244141, 7.45058e-09, 3.46945e-18
lambda modulus: 0.5
maximum lattice recovery error: 0.025
nonzero block inner radii: 32, 4096, 1.34218e+08, 2.8823e+17
all finite sanity checks passed
```

The script is only a finite sanity check; it is not used in the proof.

## Novelty bounds

A bounded search on 9 August 2026 covered the run indexes, the source paper
arXiv:1509.04912, arXiv:1711.10932 on hypercyclic subsets,
arXiv:2005.11230 on Gamma-supercyclic families of translates, and
arXiv:2411.03179 on Furstenberg-family Gamma-hypercyclicity. Exact and close
queries used `Gamma-supercyclicity`, `nonunit adjoint eigenvalue`,
`mu^n Gamma`, `scaled scalar sets`, and `point spectrum`. No explicit
tail-universal condition or countable non-dense construction for the source's
nonunit residual problem was found. Novelty confidence is moderate.

## PDF review

The four-page packet was built from `main.tex` without LaTeX warnings,
overfull boxes, underfull boxes, or unresolved references. Every final page
was rendered to PNG and visually inspected at full-page scale. The source
crops, theorem displays, proof, construction, references, margins, and page
boundaries are readable and unclipped. The PDF is 522469 bytes, version 1.7.

SHA-256:

```text
ee7b678a30cb596cf8bbcdc1a0fe29e33489f9c7660e4183f0df295984346b43
```

## Human verifier focus

1. Check the tail-density lemma for projective orbits.
2. Check that convergence after applying the eigenfunctional really forces
   `gamma_k/alpha_k -> 1` because the limiting scalar is nonzero.
3. Check the two non-density cases for the lattice construction.
4. Assess novelty relative to later scalar-set and hypercyclic-subset work.
