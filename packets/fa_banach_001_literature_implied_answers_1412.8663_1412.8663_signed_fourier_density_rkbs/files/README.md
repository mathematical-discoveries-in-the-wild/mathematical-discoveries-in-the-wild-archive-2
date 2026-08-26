# Signed Fourier densities give reproducing-kernel Banach spaces

Status: `literature_implied_answer (full existential conjecture; stronger
Wiener-class family)`.

Source: Yuesheng Xu and Qi Ye, *Generalized Mercer Kernels and Reproducing
Kernel Banach Spaces*, arXiv:1412.8663.  Remark 4.6, printed page 69 (PDF page
75), conjectures that a non-positive-definite function can construct an RKBS
through the Fourier transform.

Supporting theorem: Rongrong Lin, Haizhang Zhang, and Jun Zhang, *On
Reproducing Kernel Banach Spaces: Generic Definitions and Unified Framework of
Constructions*, arXiv:1901.01002, Theorem 2.3 (PDF pages 5--6).

## Identification

The supporting authors do not state that they are answering Xu--Ye's
conjecture.  The implication is obtained by a direct feature-map
identification.  If a nonzero real even density `h` belongs to `L^1(R^d)`, put
`E={h!=0}` and, for conjugate exponents `p,q`, factor

`h = |h|^(1/q) sgn(h)|h|^(1/p)`.

The two factors times opposite Fourier characters are feature maps into
`L^q(E)` and `L^p(E)`.  Their bilinear pairing is

`K(x,y) = integral h(xi) exp(2 pi i (x-y).xi) dxi`.

Fourier uniqueness verifies the two density hypotheses in Lin--Zhang--Zhang,
Theorem 2.3.  Consequently `K` is the reproducing kernel of a pair of RKBSs.
This works for every `1 <= p <= infinity`, including real forms obtained by
restricting to Hermitian Fourier coefficients.

Taking

`h(xi)=exp(-pi xi^2)-2 exp(-16 pi xi^2)`

gives the explicit real kernel

`phi(t)=exp(-pi t^2)-(1/2)exp(-pi t^2/16)`.

The density changes sign, so Bochner's theorem shows that `phi` is not positive
definite.  Thus the source's existential conjecture follows, and the same
argument gives a broad signed Wiener-class family.

## Scope and novelty

This is a known-theorem implication, not a new full solution.  Exact and
close-variant searches covered the four run indexes, the parsed arXiv corpus,
the source paper, arXiv:1901.01002, and arXiv:2006.00247 (*Fast Learning in
Reproducing Kernel Krein Spaces via Signed Measures*), plus bounded arXiv web
queries for non-PD/signed-Fourier RKBSs.  No earlier run packet or paper
explicitly stating the all-`p` RKBS corollary was found, but Theorem 2.3 already
contains the needed abstract construction.  The packet is therefore filed by
literature provenance.

## Files

- `main.tex`: compact mathematical status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1412.8663.
- `supporting_paper_1901.01002.pdf`: decisive supporting theorem.

Human review recommendation: confirm the application of Theorem 2.3 and retain
this packet as duplicate/status memory rather than counting it as a new proof.
