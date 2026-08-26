# Quantum sharp Young inequality at the Plancherel endpoint

**Status:** candidate partial result, likely valid; pending human review.

**Source:** G. De Palma, D. Trevisan, V. Giovannetti, and L. Ambrosio,
*Gaussian optimizers for entropic inequalities in quantum information*,
arXiv:1803.02360v2, Conjecture V.16 and Remark V.17, PDF page 28.

## Result

Conjecture V.16 is proved for the full endpoint slice
`(p,q,r)=(2,2,infinity)`, for every number `n` of modes and for both the
beam-splitter (`0<lambda<1`) and two-mode squeezer (`lambda>1`).  The exact
constant is

```text
C_n(2,2,infinity,lambda)
  = [lambda |1-lambda|]^(-n/2).
```

At the degenerate parameters `lambda=0,1`, the constant is infinite.  Thus the
thermal-restriction equality in Conjecture V.16 still holds there, but the
critical-case finiteness claim in Remark V.17 needs the natural restriction to
nondegenerate mixing.  Away from those endpoints the constants are
multiplicative, and thermal Gaussian inputs are asymptotically optimal along an
explicit high-energy ray.

The proof uses only the factorization of Weyl characteristic functions,
Weyl--Plancherel, Cauchy--Schwarz, and the exact thermal-state norms.

## Scope

This is a substantial endpoint subcase, not a solution of Conjecture V.16 at
finite critical exponents and not a solution of the source's three entropy or
`p -> q` conjectures.  The natural finite-exponent extension requires sharp
Hausdorff--Young constants for the Weyl transform; elementary interpolation
has a strictly larger constant than the thermal benchmark.

## Files and verification

- `main.tex` / `solution_packet.pdf`: theorem, proof, limitations, and search.
- `source_paper.pdf`: local copy of the source.
- `figures/open_problem_crop.png`: Conjecture V.16 and Remark V.17.
- `code/check_endpoint.py`: finite-Fock-sector and thermal-asymptotic checks.

Run:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1803.02360_quantum_young_plancherel_endpoint/code/check_endpoint.py
```

The current run checks 900 deterministic random beam-splitter instances and
six thermal asymptotic families, and ends with:

```text
PASS: Plancherel-endpoint sanity checks completed
```

The code is supplementary; the proof is analytic.

## Novelty and human review

Bounded run-index and open web/arXiv searches on 2026-08-11 used the source
id/title/authors, exact conjecture name, `C_n(2,2,infinity)`, Hilbert--Schmidt to
operator norm, Weyl Plancherel, and close variants.  No explicit later answer
to this endpoint was located.  Novelty confidence is moderate because the
argument is short and may be folklore.

Recommended review focus: characteristic-function normalizations, extension
from finite-rank to Hilbert--Schmidt inputs, and the squeezer conjugation sign
(which does not affect the norm estimate).
