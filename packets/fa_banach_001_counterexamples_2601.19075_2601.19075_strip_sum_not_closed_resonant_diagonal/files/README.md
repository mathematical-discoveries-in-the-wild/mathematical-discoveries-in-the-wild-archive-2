# Counterexample: the strip-type sum need not be closed

**Status:** candidate counterexample, likely valid; full negative answer to the
closedness uncertainty in Remark 6.3(iii) of arXiv:2601.19075.

## Source question

Nikolaos Roidos, *Strip-type operators and abstract Cauchy problems*,
arXiv:2601.19075 (current source dated 26 May 2026), Remark 6.3(iii), PDF page
29, says that it is not known whether the sum `+/- iA+B` is closed.  Here `B`
is differentiation on `L^p(0,T;X)` with domain `W_0^{1,p}(0,T;X)`, and `A`
acts pointwise.  The surrounding Remark 6.3(v) emphasizes that positive
self-adjoint operators on Hilbert space satisfy the paper's sectorial and
`R`-strip-type hypotheses.

## Result

The sum need not be closed, even in that Hilbert/self-adjoint setting.  Let
`X=ell_2`, let `Ae_n=n e_n`, fix any `1<p<infinity` and `T>0`, and let `B` be
the source derivation operator.  For either sign `sigma in {+1,-1}`, the
operator

`S_sigma = B + sigma i A`

on `W_0^{1,p} intersect L^p(D(A))` is not closed in `L^p(0,T;ell_2)`.

Take `a_n=1/n`, and set

`u_n(t)=t a_n exp(-sigma i n t)` and
`f_n(t)=a_n exp(-sigma i n t)`.

Finite-coordinate truncations satisfy `S_sigma u^(N)=f^(N)`.  Both truncation
sequences converge in `L^p`, but the limit `u` is not in `L^p(D(A))`, because
`(Au(t))_n=t exp(-sigma i n t)` is not square summable for any `t>0`.  Hence
the graph has a limit outside the original domain.

The example works for every time exponent in the paper and for both signs.
Moreover, `A` is positive definite and self-adjoint, belongs to `P(0)`, and
belongs to `RZ_c` for every `c>0` by a direct diagonal resolvent estimate.

## Scope

This resolves the stated closedness uncertainty negatively.  It does not give
a full Sobolev description of the closure domain `D(overline{+/- iA+B})` or of
the spaces `E_2^+/-`.  Instead, it shows that the passage to the closure in
Section 5 is genuinely necessary under the paper's general hypotheses.

## Verification and novelty

The proof is exact and uses no numerical evidence.  The main reviewer checks
are the sign cancellation, the pointwise extension domain of `A`, and the
interpretation of Remark 6.3(iii).  A bounded search used the exact title,
arXiv id, quoted sentence, `+/- iA+B closed`, `derivation operator`, and
`strip-type`; it found the source and adjacent operator-sum literature but no
later paper or exact answer to this May 2026 uncertainty.

## Files

- `source_paper.pdf`: arXiv:2601.19075.
- `figures/open_problem_crop.png`: Remark 6.3(iii) and the Hilbert/self-adjoint
  context in Remark 6.3(v).
- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered and visually verified packet.
- `code/make_crop.py`: reproducible evidence crop.
