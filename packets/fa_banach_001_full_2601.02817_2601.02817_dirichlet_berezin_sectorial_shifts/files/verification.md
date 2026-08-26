# Verification report

Status: candidate full result, likely valid; human review requested.

## Mathematical audit

- Re-derived the Dirichlet coefficient norm from the source definition:
  `||sum a_n z^n||^2=sum (n+1)|a_n|^2`.
- Checked the weighted-shift formula
  `D e_n=n sqrt(n/(n+1)) 2^(1-n)e_(n-1)` directly.
- Checked the kernel-coordinate calculation yielding
  `D~(lambda)=conj(lambda)F(|lambda|^2)/K(|lambda|^2)`.
- Checked that the radial modulus extends continuously by zero at both radial
  endpoints and therefore produces the entire closed Berezin disk.
- Verified the geometric tail majorant `F<=N` and truncation lower bound
  `K>=P` on `[0,1]`.
- Verified the three-dimensional compression radius
  `(1/2)sqrt(alpha_1^2+alpha_2^2)=sqrt(7/24)`.
- Verified rotational covariance `U_theta^*DU_theta=e^(i theta)D`, so the
  compression value gives a full numerical circle; convexity fills its disk.
- Checked `||D||=sqrt(2/3)<1`: the second weight attains this value and every
  weight from index three onward is at most `3/4`.
- Checked the tangent-disk sector angles and the negative-real obstruction for
  every `9/20<a<sqrt(7/24)`.

## Exact certificate

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2601.02817_dirichlet_berezin_sectorial_shifts/code/verify_radius_gap.py
```

Observed output:

```text
q degree: 17
Bernstein elevation degree: 32
positive Bernstein coefficients: 33 of 33
minimum coefficient index: 28
minimum coefficient (exact): 55075026511/201587097600000
minimum coefficient (decimal): 0.0002732071008844169
7/24 - (9/20)^2: 107/1200
CERTIFIED: b < 9/20 < sqrt(7/24)
```

The proof-critical checks use exact rational arithmetic.  The printed decimal
is informational only.

## Literature and duplicate audit

- Cheap run indexes searched: `registry_index.tsv`, `solutions/index.tsv`,
  `attempts/index.tsv`, `proof_gaps/index.tsv`.
- Terms: source arXiv id, `Berezin sectorial`, `composition-differentiation`,
  `Dirichlet space`.
- Bounded arXiv web searches on 2026-08-12 used the source id and close phrase
  combinations.  Only the source problem was found; no later answer appeared.
- Novelty remains subject to a human database/citation review.

## Source evidence and rendering audit

- `source_paper.pdf` was compiled from the ingested arXiv source and has 25
  pages.
- `figures/open_problem_crop.png` was rendered at 180 dpi from PDF page 23,
  full text width, and visually checked for complete readable wording.
- The final packet was compiled with `latexmk`, text-extracted, rendered to
  page PNGs, and visually inspected.  Build details and final page count are
  recorded in `tmp/`.

## Reviewer focus

1. Confirm the inner-product convention only conjugates the displayed
   Berezin symbol and does not affect its disk.
2. Re-run the exact Bernstein checker.
3. Confirm that the source's “similar constructions” refers to the scalar
   shifts explicitly described on PDF page 22.
