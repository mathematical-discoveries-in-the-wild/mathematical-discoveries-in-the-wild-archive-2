# 0909.0692 — Green-circle Möbius/dilation endpoint

## Outcome

Candidate new full positive answer, likely valid and requiring specialist review.

Adimurthi and Tintarev ask for a sharp critical nonlinearity invariant under
the product symmetry suggested by Möbius shifts on the disk and the nonlinear
radial dilations
\[
  h_su(r)=s^{-1/2}u(r^s).
\]
The packet constructs a Green-circle maximal norm on all of \(H_0^1(B)\).
It is invariant under every disk automorphism and, on radial functions, is
exactly the source's sharp dilation-invariant endpoint
\[
  \sup_{0<r<1}\frac{|u(r)|}{\sqrt{\log(1/r)}}.
\]
It therefore supplies the requested common critical nonlinearity in the
literal setting where the source defines the two actions.

## Main formula

For
\[
  \phi_a(w)=\frac{a+w}{1+\bar a w},
\]
put
\[
 \|u\|_{\mathcal G}
 =
 \sup_{a\in B,\ t>0}
 \left[
 \frac1{2\pi t}\int_0^{2\pi}
 |u(\phi_a(e^{-t+i\theta}))|^2\,d\theta
 \right]^{1/2}.
\]
The curves are Green-function level circles and the angular average is their
harmonic measure at the center.

The packet proves:

- \(\|\cdot\|_{\mathcal G}\) is a norm on \(H_0^1(B)\);
- \(\|u\|_{\mathcal G}\le(2\pi)^{-1/2}\|\nabla u\|_2\), with exact constant;
- \(\|u\circ T\|_{\mathcal G}=\|u\|_{\mathcal G}\) for every disk
  automorphism \(T\);
- for radial \(u\), the norm is exactly the source endpoint and is invariant
  under every \(h_s\);
- the same endpoint/dilation statement holds for functions radial about any
  Möbius center;
- the embedding is noncompact along the Moser/dilation orbit;
- no nonzero local functional
  \(\int_B F(u)\,dx/(1-|x|^2)^2\) can be invariant under any fixed
  \(h_s\) with \(s\ne1\).

## Files

- main.tex — theorem, proof, obstruction, verification, and limitations.
- solution_packet.pdf — compiled review packet.
- source_paper.pdf — arXiv source paper.
- figures/open_problem_crop.png — exact source question and definitions.
- verify_green_circle_norm.py — deterministic numerical/algebraic checks.
- tmp/ — build and render artifacts.

## Verification

Run:

    conda run --no-capture-output -n sandbox python verify_green_circle_norm.py

The checker tests the off-center Jensen identity, the Möbius
circle/rotation factorization, the radial endpoint bound, the dilation
scaling, the sharp constant, and the local-integral obstruction.

## Novelty and review

Targeted exact-phrase and arXiv searches, the run indexes, and related later
papers did not locate this construction or a prior answer.  The source uses
“nonlinearity” for its radial \(L^\infty\)-type norm, which is exactly the
interpretation extended here.  A specialist should:

1. confirm that this is the intended meaning of “product group”;
2. check the trace/extension step and the Jensen identity;
3. search more broadly for Möbius-invariant Green-circle maximal norms;
4. contact the source authors if the result and novelty are confirmed.

