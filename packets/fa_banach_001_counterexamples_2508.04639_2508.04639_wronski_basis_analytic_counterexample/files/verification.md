# Verification record

Date: 2026-08-12

## Mathematical checks

- The coefficient map `(a,b) -> a+b x^2` is an isometric bijection from
  `R^2` to `H`; hence `H` is complete and `{1,x^2}` is orthonormal.
- Substituting `1` into an arbitrary regular second-order HODE forces
  `p_0=0`.
- Substituting `x^2` then forces `2p_2+2xp_1=0`, so at `x=0` one obtains
  `p_2(0)=0`, contrary to regularity.
- Direct determinant expansion gives `W(1,x^2)=2x` and
  `W(1,x^2,y)=2xy''-2y'`.
- Reordering or nonzero rescaling of the basis does not remove the zero of
  its Wronskian.

## Source alignment

- The source's Remark 1 assumes continuous coefficients and a leading
  coefficient nonzero everywhere on the interval.
- Immediately after Conjecture 8, the source explicitly specializes a
  finite basis of size `N` to its proposed `N`th-order Wronskian equation.
- The example therefore targets the source's asserted finite case rather
  than relying on any undefined infinite-order formalism.

## Scope

- Global domain: `R`.
- The example does not obstruct the equation on an interval avoiding zero.
- A corrected finite theorem needs, at minimum, an everywhere-nonvanishing
  basis Wronskian.

## Artifact QA

- `latexmk` completed successfully after two passes.
- Final PDF: 3 A4 pages, 341,378 bytes.
- The final log contains no overfull/underfull boxes, undefined references,
  or LaTeX/package warnings.
- All three pages were rendered at 150 dpi and visually inspected; the source
  crop is legible, equations fit, and there are no clipping or overlap defects.
- SHA-256 of `solution_packet.pdf`:
  `4fdc0342c7a2e2b818233b7cb8a942b4fa38c09d24f835e6b6f63923e9cdee79`.
