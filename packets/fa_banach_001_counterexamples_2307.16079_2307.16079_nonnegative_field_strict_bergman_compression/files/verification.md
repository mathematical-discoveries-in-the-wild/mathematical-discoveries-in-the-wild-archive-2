# Verification report

Verdict: **likely valid candidate counterexample**

## Exact target match

The source's Proposition 5.2 gives

    N(H^O_{A,g},0) >= dim(E_V intersect gamma_0(B(Omega)))

and an analogous antiholomorphic inequality.  Remark 5.3 asks whether the
inequalities are equalities when `B>=0`.  The packet constructs `B>0` for
which the displayed first inequality is strict.  A single strict inequality
disproves the universal equality proposal.

## Assumption and sign audit

- Domain: the smooth bounded unit disc.
- Boundary condition: `g=0` (Neumann), allowed by the source.
- Potential: `phi` is a Cartesian polynomial and vanishes on the boundary.
- Vector potential: `A=(-phi_y,phi_x)`, exactly the gauge used in the source.
- Orientation: the source uses counterclockwise tangent and inward normal.
  On the circle this gives `A_tau=partial_r phi`.
- Field: `curl A=Delta phi=2a+16b r^3 cos(3theta)`.
- Positivity: `B>=2a-16b=3/20>0` on the closed disc.
- Flux: the oscillatory term integrates to zero, so the normalized flux is
  `a`, agreeing with the mean of `A_tau`.

## Negative-subspace audit

For holomorphic polynomials, direct Fourier integration gives the form matrix
`q^O/(2pi)` with diagonal `n-a` and coupling `-b` between indices differing
by three.  It is block diagonal modulo three.  The `z^0` and `z^1` directions
are negative because `a>1`.  The `z^2,z^5` block has positive trace and exact
determinant

    (2-a)(5-a)-b^2 = -1703/40000 < 0,

so it has one negative direction.  The three residue blocks are mutually
form-orthogonal; their negative vectors span a three-dimensional negative
subspace.  The min--max/Glazman conclusion `N(H^O,0)>=3` is therefore exact
and does not depend on a finite-truncation approximation.

## Comparison-dimension audit

With `V=-A_tau`, the source's eigenvalue formula gives eigenvalues `m-a` and
eigenfunctions `z^m E`.  Since `1<a<2`, the negative modes have `m<=1`.
The factorization

    E=exp(delta z^3) exp(-delta z^(-3)),  delta=b/3,

is by bounded invertible analytic/coanalytic factors.  Multiplying a
holomorphic boundary vector by the inverse analytic factor preserves the
Hardy space.  The remaining condition is

    T_{conj(alpha)} G in span{1,z},
    alpha(z)=exp(delta z^3).

Both `alpha` and `alpha^{-1}` are in `H^infinity`, and multiplication of
coanalytic Toeplitz operators gives

    T_conj(alpha) T_conj(alpha^{-1}) = I.

Hence the preimage has dimension exactly two.  Conversely `G=1,z` produces
two smooth intersection vectors, so there is no trace-regularity loss.  The
source itself shows the intersection lies in `H^(1/2)`, which embeds in the
`L^2` Hardy setting used for the upper bound.

## Computational check

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2307.16079_nonnegative_field_strict_bergman_compression/code/exact_symbolic_check.py
```

Observed output:

```text
Delta(phi) = 96*x**3/25 - 288*x*y**2/25 + 399/100
global lower bound for B = 3/20
2x2 compression determinant = -1703/40000
q(1)<0, q(z)<0, and the 2x2 block has one negative eigenvalue
all exact checks passed
```

The script uses exact SymPy and `fractions.Fraction` arithmetic.  It checks
identities and arithmetic only; it is not evidence for the functional-
analytic factorization, which is proved separately.

## Eight-attempt upgrade and novelty audit

The attempt record is
`runs/fa_banach_001/attempts/2307.16079_nonnegative_field_equality_counterexample_upgrade/upgrade_attempts.md`.
Its eight materially distinct stages cover target matching, positive-field
realization, exact finite compression, the three-dimensional negative
subspace, boundary-Dirac diagonalization, exact Toeplitz intersection,
parameter-family robustness, and novelty/version screening.

The bounded literature search performed on 2026-08-13 found the original
preprint and journal publication but no later source claiming to resolve the
question and no matching positive-field counterexample.  The current source
TeX retains the question (renumbered Remark 6.4).  Novelty confidence:
moderate.

## Remaining human checks

There is no known mathematical dependency.  Human review should focus on the
orientation sign, the Toeplitz equivalence, and whether the source intended
the two equalities jointly or separately.  Under either reading, strictness
of the first equality is a valid negative answer to the universal proposal.

## Artifact hashes (SHA-256)

- `source_paper.pdf`:
  `45616b953f2f1ff62bf91f9a2ec5d70158e441f151d668ac9054a90aba4b462d`
- `figures/open_problem_crop.png`:
  `b43b877b0f9e3685cbc907b8b43007762585d1415c06c646ef245e746be0f9fc`
- `main.tex`:
  `ed693d6730e078fdf2d486db5e9cd2d15a6c9ed6976a6e315a59b101ecd83874`
- `solution_packet.pdf`:
  `2c7b5335c74d733e0dabdd8dbc2d74cc8a1ea39e4fb075b435217293e6c6c104`
- `code/exact_symbolic_check.py`:
  `1caa79b543695739e58c50f0c60ae1932c34b8e4401ee8cdbecec84a34caa2f7`

The final PDF has five pages.  Ghostscript text extraction succeeded, all
five pages were rendered at 150 dpi, and every rendered page was visually
inspected.  No clipping, missing glyphs, unresolved references, or layout
defects affecting review were found.
