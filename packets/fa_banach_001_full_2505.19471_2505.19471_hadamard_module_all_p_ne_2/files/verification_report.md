# Verification report

Verdict: **likely valid**, suitable for expert review as a candidate full
solution.

## Claim-to-source match

- The source question is the paragraph after Example 5.2 on source PDF p. 18.
- The packet treats exactly the same algebra and the same two-summand
  row–column module.
- It proves non-C*-likeness for every finite \(p\ne2\), and records the known
  positive Hilbertian case \(p=2\). This is the requested classification.

## Analytic audit

1. **Source-column norm below 2.** Grouping the four entries into the pairs
   \((3x\pm y)\) and \((x\pm3y)\), the strict scalar Clarkson inequality gives
   \(\|T\|^p=2^{1-p}(3^p+1)\). Equality is possible only when \(xy=0\), so the
   norming inputs are exactly the two coordinate axes.
2. **Compactness.** Row contractions form a compact set and all spaces are
   finite dimensional. If the recovery supremum equalled \(\|T\|\), a row
   contraction and a norming input would attain the complete equality chain.
3. **Dual smoothness.** For the normalized \(\eta=Te_1/\|T\|\), equality
   supplies a unit \(\phi\) such that \(C=B^*\) satisfies
   \(C\phi=j_p(\eta)\) and \(C^*\eta=j_{p'}(\phi)\). This uses uniqueness of
   support functionals in finite-dimensional \(\ell_r\), \(1<r<\infty\).
4. **Hadamard equations.** Solving the first equality in diagonal coordinates
   determines all four eigenvalues of \(C\). Substitution into the second
   equality yields
   \(-\bar v/\bar u=|v|^{s-2}v/(|u|^{s-2}u)\) when \(uv\ne0\). Hence the only
   projective cases are the two axes and \((1,\pm i)\). The denominators
   \(u\pm v\) cannot vanish because \(q\pm1\ne0\).
5. **Coordinate directions.** The unique structured \(C\) expands \((1,1)\)
   by the strict \(s>2\) Clarkson inequality, so it cannot be a contraction.
6. **Exceptional complex directions.** The displayed \(C_0\) was multiplied
   by \((1,i)\) directly. Along \(\xi_t=(1,i)+it(1,-i)\), the second derivative
   of \(\|C\xi_t\|_s^s-\|\xi_t\|_s^s\) is the stated positive scalar margin.
7. **Scalar margin.** With \(q^{s-1}=3\), the margin reduces to \(h(q)>0\) on
   \((1,3)\). The derivative computation is sign-checked in the packet:
   \(-h'=R>0\), because \(R'<0\) and
   \(R(3)=(10-8\log3)/3>0\).
8. **Above 2.** Matrix adjoints are isometric from operators on \(\ell_{p'}\)
   to operators on \(\ell_p\), preserve the algebra as a set, swap rows with
   columns, and reverse products. Thus the strict first-axiom gap at \(p'<2\)
   is exactly the strict second-axiom gap at \(p>2\).

No step uses the numerical script.

## Computational sanity checks

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2505.19471_hadamard_module_all_p_ne_2/code/check_identities.py
```

The script checks seven exponents from 1.05 through 1.99. It verifies the
normalization \(D^s=2(q^s+1)\), positivity of the scalar margin, strict axis
expansion, the complex matrix identity \(C_0(1,i)=g\), an explicit expanding
perturbation, and 25,000 random complex source-column inputs per exponent.
These checks are non-proof regression tests.

## Novelty audit

- Cheap indexes searched: `registry_index.tsv`, `solutions/index.tsv`,
  `attempts/index.tsv`, and `proof_gaps/index.tsv`.
- Terms: arXiv:2505.19471, exact title, C*-like modules, Example 5.2,
  normalized Hadamard, and simultaneously diagonalizable.
- Web bounds on 2026-08-11: exact-title, exact-question, and core-keyword
  searches. The arXiv and Springer/Annals versions were found; the published
  p. 18 still explicitly says the question is unknown. No separate answer was
  found.
- Limitation: this was not a comprehensive MathSciNet/zbMATH/citation-network
  review. Novelty confidence is moderate.

## Artifact audit

- `source_paper.pdf` is the 19-page arXiv PDF.
- `figures/open_problem_crop.png` is a real 240 dpi full-width crop of source
  p. 18, not a transcription.
- LaTeX build products and rendered pages are confined to `tmp/`.
- Every rendered packet page was visually inspected after compilation.

## Reviewer focus

The highest-value review points are the common-scalar cancellation preceding
the phase equation, the complex exceptional-direction second variation, and
the exact row/column identification under \(p\)-\(p'\) adjoints.
