# Verification report

Verdict: **candidate full counterexample to the natural formulation, likely
valid**.

## Source verification

- `source_paper.pdf` is the five-page arXiv PDF for 2509.16386v2.
- The closing assertion and future-work scope occur on PDF page 5.
- `figures/operator_claim.jpg` contains the complete operator condition,
  uniqueness assertion, and future-work paragraph.

## Formulation audit

The source does not formally define entropy of an operator.  The packet uses
the direct extension supplied by its existing definition: compare the
`S*`-entropy of the output top forms, `S*(D omega,M)`.  Under that natural and
explicit formulation, the asserted uniqueness is false.  If a different
operator entropy is intended, it must be specified before an extremal claim
has a truth value.

## Mathematical audit

1. The coefficient
   `a_e(x)=1+e(1-cos(2 pi x))/(2 pi x)` extends smoothly at zero and has
   `a_e(0)=a_e(1)=1`.
2. Therefore `D_e g=d(a_e g)` is a local first-order linear operator and
   `integral D_e g=g(1)-g(0)` for every smooth `g`.
3. For `omega(x)=x`, differentiation gives exactly
   `D_e omega=(1+e sin(2 pi x))dx`.
4. For `0<e<1`, this density is positive and has normalization constant
   `C=1+e`.  The entropy integrand is nonnegative and strictly positive away
   from the measure-zero maximum set, so its integral is strictly positive.
5. The exterior derivative gives the constant density one, whose source
   entropy is zero.  This reverses the claimed maximizing inequality.
6. A derivation on smooth functions has the form `Dg=a(x)g'(x)dx`.  Applying
   global Stokes compatibility to compactly supported test functions forces
   `a` to be constant; applying it to `g=x` forces `a=1`.  Thus imposing the
   Leibniz rule collapses the class to `{d}`.

## Verifier

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2509.16386_operator_entropy_extremality_fails/code/verify_counterexample.py
```

SymPy checks the endpoint values, output density, and Stokes integral exactly.
High-precision quadrature independently confirms strict positive entropy at
`e=1/2`; the proof itself uses pointwise positivity and does not depend on
quadrature.

## Novelty and upgrade audit

- Cheap run indexes contained no prior result for the paper.
- Current arXiv/web searches using the title, author, exact operator wording,
  and entropy-extremizing-duality terminology found only the source.
- The first counterexample used a nonlocal boundary functional.  The deep
  upgrade above is stronger: it is a smooth local first-order differential
  operator, obeys Stokes globally for every input, and belongs to a full
  one-parameter family.  The distinct derivation avenue identifies the exact
  condition that removes the counterexample, at the cost of making the
  variational assertion tautological.
- Novelty confidence: moderate, pending author/specialist review.

## Rendering audit

The final `solution_packet.pdf` builds without LaTeX warnings or overfull
boxes.  Both pages were rendered to RGB PNGs and inspected at full
resolution: the source assertion is readable, all formulas and symbols render
correctly, and the two-page layout has no clipping or transparency artifacts.
