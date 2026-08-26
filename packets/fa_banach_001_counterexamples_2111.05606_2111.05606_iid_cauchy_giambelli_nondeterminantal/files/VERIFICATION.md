# Verification report

Status: **candidate counterexample, likely valid; expert review recommended**.

## Hypothesis audit

- `E = R` is one of the two ambient cases allowed immediately before the
  source conjecture.
- Cauchy measure is atomless, so two iid samples define a simple two-point
  configuration almost surely.
- `|(x+iR)^(-1)| <= R^(-1)`. Every image of a symmetric function under the
  centered specialization is therefore a bounded polynomial of two bounded
  variables. This proves the full `L^1`-specialization requirement, not just
  integrability of the individual Newton sums.

## Giambelli audit

The parametrization `x = R cot(theta/2)` gives Cauchy density and sends
`t=(x+iR)^(-1)` to `c + r zeta`, where `c=-i/(2R)`, `r=1/(2R)`, and `zeta`
is uniform on the unit circle. For every polynomial `F(t1,t2)`, independence
and the one-variable mean-value identity give `E F(t1,t2)=F(c,c)`.

The centered Newton sums are `t1^k+t2^k-2c^k`. Evaluating at `(c,c)` makes
all of them zero. Hence the expected specialization equals the counit on the
entire symmetric-function algebra. Every nonempty Schur function, including
every hook in a Giambelli determinant, has expectation zero. The Giambelli
identity follows in every degree.

## Non-determinantal audit

Relative to Cauchy probability measure, the ordered factorial correlation
densities are `rho_1=2`, `rho_2=2`, and `rho_m=0` for `m>=3`. A change from an
arbitrary dominating reference measure to Cauchy measure is implemented by
dividing `K(x,y)` by the square root of the two Radon--Nikodym densities; this
divides each determinant by exactly the required product density.

For a conull quadruple, the hypothetical kernel matrix has diagonal `2`,
two-by-two principal minors `2`, and all three- and four-by-four principal
minors zero. Diagonal similarity normalizes the first row/column. The
three-minor containing the base point forces every remaining oriented entry
to be `1+i` or `1-i`. The remaining three-minor forbids the cyclic tournament,
so the three vertices can be transitively ordered. The resulting full matrix
has determinant `-4`, contradicting its required zero four-minor. This proof
does not assume Hermitian symmetry or positivity of the kernel.

## Exact verifier

Command:

```bash
conda run --no-capture-output -n sandbox python code/verify_counterexample.py
```

Output:

```text
checked 66 nonempty partitions through degree 8
all exact checks passed
```

The script checks the determinant normal forms exactly in `Q(i)` and verifies
the centered Schur vanishing through degree eight. The all-degree statements
are proved analytically in `main.tex`; the finite computation is only a sanity
check.

## Visual/PDF audit

- LaTeX compiled without errors to a five-page packet.
- All five rendered pages were inspected at 120 dpi.
- The source crop is a real, full-width crop of printed page 5 and contains
  the complete Conjecture 1 statement.
- No clipping, overflow, missing glyph, or unreadable formula was observed
  after the final crop and spacing correction.

Recommended review focus: the two applications of the holomorphic mean-value
property, the reference-measure rescaling, and the conull-quadruple selection.

