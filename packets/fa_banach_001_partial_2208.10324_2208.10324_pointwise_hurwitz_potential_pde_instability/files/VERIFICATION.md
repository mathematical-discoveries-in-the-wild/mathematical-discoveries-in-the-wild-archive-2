# Verification report

Verdict: `candidate_partial_likely_valid`.

## Mathematical checks

The proof is elementary and self-contained.  The key identities were also
checked with SymPy:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2208.10324_pointwise_hurwitz_potential_pde_instability/code/verify_construction.py
```

Output:

```text
cross-product denominator: 9*c**2*d**2 + c**2 + 16*d**2
eta^T u: 1
eta^T w: 0
N^2 is zero: True
PDE residual is zero: True
V(pi/2) for a=lambda=1:
[ 2   0   1]
[ 0  -1   0]
[-9   0  -4]
all symbolic checks passed
```

The strict positivity of the denominator is proof-theoretic, not numerical:
`d=2*c**2-1`, so `c` and `d` cannot vanish simultaneously.

## Packet and visual checks

- `latexmk` completed after two passes with no unresolved references,
  overfull boxes, underfull boxes, or logged warnings in the final build.
- The final PDF has three A4 pages.
- All three pages were rendered at 160 DPI and visually inspected at original
  resolution.  The source crop is readable at normal review zoom; no content
  is clipped; formulas, page numbers, and section transitions are clean.
- Text extraction found the theorem, frozen-stability assertion, and novelty
  limitation in the final PDF.

## SHA-256

```text
d1a6082a6e2b5f821679e8ac3ecc44cc578e7a70d524a7d2c6aefdaa2e7ea474  solution_packet.pdf
a3a55b89be86fa3d51e4b0abce4d456a29d7d43314a4786f46c1237e4dcfa2de  source_paper.pdf
e43a2defdd2a0c114bf3b68119c32603a9ba0703b539808643c1ba68ee916f37  figures/open_problem_crop.png
5f858e4f3726f0c482da7842753e3a3d0d956b4085266aba773a135298ab4b68  code/verify_construction.py
```

## Human-review recommendation

Check the rank-one functional `eta`, the frozen-semigroup bound, and the scope
label.  The construction completely refutes pointwise/frozen spectral
stability as a boundedness criterion, but it is a substantial partial answer
to a broad source direction rather than a full characterization of all
non-dissipative potentials.
