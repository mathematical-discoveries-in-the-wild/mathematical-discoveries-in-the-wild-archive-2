# Verification report

## Claim checked

For `0<a,s<infinity` and `0<q<2`, neither `HB_0^{a,q}` nor
`HF_0^{a,q}` admits a finite positive measure `mu` satisfying

`||f||_X <= C ||f||_{L^s(mu)}`

for every analytic polynomial `f`. Taking `a=s=p` answers Problem 8.1 of
arXiv:2412.02354.

## Mathematical audit

1. The test polynomial is
   `P_N=N^(-1/2) sum_{j=1}^N z^(M^j)` with fixed `M=64`.
2. On the disjoint interval where `1-r` lies between `M^(-j)` and
   `2M^(-j)`, the `j`th derivative monomial dominates the entire derivative
   pointwise. The lower monomials contribute at most `1/(M-1)` of the
   `M^j` scale; the higher tail contributes at most
   `sum_{ell>=1} M^ell exp(-M^ell+1/M)`; and the main term contributes at
   least `exp(-3)`. A direct numerical check gives main constant
   `0.0497870`, lower-frequency bound `0.0158731`, tail below
   `1.05e-26`, and positive margin `0.0339140`.
3. Integrating over all `N` disjoint radial intervals gives the lower bound
   `c N^(1/q-1/2)` for both the Besov and Triebel--Lizorkin quasinorms. The
   estimate is pointwise in the angular variable, so it remains valid for
   angular exponents below one.
4. For `0<s<=2`, orthogonality gives
   `||P_N||_{H^s} <= ||P_N||_{H^2}=1`. For `s>2`, the Paley--Zygmund
   inequality for Hadamard-lacunary polynomials gives
   `||P_N||_{H^s} <= C_s`. Thus the exact source range `s=p<1` uses no
   external lacunary estimate.
5. Fubini and subharmonicity show that the average over rotations of the
   `s`th power of the `L^s(mu)` quasinorm is at most
   `C_s^s mu(closed disk)`. Thus one rotation has uniformly bounded
   right-hand side, while rotation invariance preserves the analytic-space
   norm.
6. Every test function is a polynomial, so no approximation, boundary-value,
   or density step is used.

## Literature and novelty audit

On 13 August 2026, bounded searches used arXiv:2412.02354, the exact text of
Problem 8.1, and combinations of `reverse Carleson`, `Besov`, `p<1`,
`p<q<2`, and `lacunary`. The current arXiv rendering still states Problem 8.1
as open. No later paper explicitly resolving this range or giving this
rotation-averaged lacunary argument was found. Novelty confidence is moderate,
because the proof uses classical ingredients in a short new combination.

## PDF audit

The final four-page packet was compiled to convergence with `latexmk` and
contains no unresolved references, warnings, overfull or underfull boxes, or
reported errors. It was rendered at 144 dpi, and every page of the final PDF
was visually inspected after the last mathematical and typographic edits.

## Human-review focus

Check the uniform derivative domination on the selected annuli, the use of
the Paley--Zygmund lacunary inequality for all finite exponents, and the
rotation/Fubini argument for arbitrary finite measures with boundary mass.
