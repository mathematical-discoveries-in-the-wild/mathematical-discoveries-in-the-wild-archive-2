# Verification report

## Mathematical checks

1. **Exact source scope.** The current arXiv v3 source was checked at Problem
   1, Theorem A, the injectivity-set definition, the Fourier representation,
   the counterexample perturbation, and the low-dimensional disk proof.  The
   negative-p, complex-dimension-two theorem is stated only for `C=D`.

2. **Ellipse injectivity.** For `p=-2s`, `s>0`, the coefficient of frequency
   `2j` in `(A+B cos(2 theta))^{-s}` was reduced by the Laplace transform to a
   nonzero signed integral of `I_j(|B|t)`.  Since the integrand is strictly
   positive for `t>0`, every even multiplier is nonzero.  The source's exact
   multiplier criterion then makes the injectivity set all origin-symmetric
   convex bodies.

3. **Kernel measure.** The linear-change formula for the Fourier transform of
   `|Bx|^p` gives a positive continuous density proportional to
   `|B^{-T}c|^{-2-p}`.  Hence its normalized second angular moment has modulus
   strictly below one.

4. **Angular witness.** For `Q(u)=|P_Eu|^2`, the global phase orbit has only a
   constant and a second harmonic of amplitude at most `1/2`.  Therefore
   `T_nu Q <= M(1+r)/2`.  The interval `1<a<2/(1+r)` is nonempty and makes
   `phi=1-aQ` negative on `S(E)` while `T_nu phi` is uniformly positive.

5. **Concentration.** The Fourier density of
   `L_delta=(delta P_E+P_{iE})B_2^4` was checked by a linear change of
   variables.  With `t=|P_Eu|^2`, uniform measure on `S^3` makes `t` uniform
   on `[0,1]`.  Outside a fixed neighborhood of `t=1` the weighted mass is
   `O(delta^2)`, while the last interval of width `delta^2` has mass bounded
   below by a constant times `delta^{-p}`.  Their ratio is
   `O(delta^{2+p}) -> 0` precisely because `p>-2`.

6. **Perturbation and membership.** `psi=F_p phi` is even and smooth.
   The source radial perturbation lemma, applied to exponent `-(4+p)`, makes
   the body defined by
   `rho_K^(4+p)=rho_L^(4+p)-epsilon psi` smooth and convex for small epsilon;
   strict positive curvature follows by `C^2` openness around an ellipsoid.
   Full even injectivity puts both bodies in the exact source domain.

7. **Inclusion sign.** The source transform formula and
   `F_{-4-p}F_p=(2pi)^4 Id` subtract a positive multiple of `T_nu phi` from
   `rho_{I K}^{-p}`.  Since `-p>0`, this gives the claimed strict inclusion in
   the stated direction.

8. **Volume sign.** Self-adjointness changes the perturbation pairing into
   `<phi,F_p rho_L^{-p}>`, which is negative.  Multiplication by `p<0` makes
   the mixed-volume change positive.  The source's dual `L_p` Minkowski
   inequality then yields `Vol_4(K)>Vol_4(L)`.  No equality case is needed.

## Computational sanity check

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2404.05630_noncircular_ellipse_dichotomy/code/numerical_sanity.py
```

For an ellipse of semiaxis ratio 2, `delta=0.1`, and
`p=-1.9,-1.5,-1,-0.5,-0.1`, the program checks that the lower bound for
`T_nu phi` is positive and the normalized ellipsoid pairing is negative.
This is a regression check only; neither finiteness nor sampling is used in
the proof.

## Literature and novelty bounds

- searched the run indexes by arXiv id, exact title, operator terminology,
  ellipse, and noncircular ellipse;
- checked current arXiv v3 HTML/source and published-paper metadata;
- searched exact title plus ellipse/noncircular terms, both authors, close
  complex Busemann--Petty terms, the authors' current publication page, and
  their MathOverflow errata/discussion page through 2026-08-11;
- found no later treatment of the ellipse case or the stated dichotomy.

Novelty confidence is moderate pending expert review, because the proof is a
new recombination of tools already developed in the source.

## Artifact QA

- The numerical script completed with positive transform margins and negative
  normalized pairings at all five listed exponents.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully.  The final log contains no warnings, undefined
  references, underfull boxes, or overfull boxes.
- `solution_packet.pdf` has 6 A4 pages.  Ghostscript text extraction produced
  231 lines, including the theorem, proof, review focus, and references.
- All six pages were rendered at 150 dpi and individually inspected.  The two
  source crops are readable at normal zoom, all displayed formulas fit, and
  there is no clipping or overlap in the packet layout.
- Packet SHA-256:
  `173be9b247bae335dee67621b916f008fd9b492cb2495845facfd7e352f27c84`.
- Source PDF SHA-256:
  `b97cab8e0e31c781aacf6038426ebbf36f000764b5f5f521d0c5bd9ee803d9b9`.
