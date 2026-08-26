# Verification Report

Candidate: arXiv:2002.12917, nonexistence of unconditional bases at the
critical first-difference Besov endpoint

## Verdict

`likely valid` (substantial partial result)

## Claims checked

1. A critical dyadic atom has Besov quasi-norm at most its `L1` mass.
2. The Banach envelope of the target space is canonically `L1(I^d)`.
3. An unconditional basis passes to an unconditional basis of an injective,
   dense Banach envelope.
4. The classical nonexistence of unconditional Schauder bases in nonatomic
   `L1` gives the contradiction.

## Adversarial proof audit

| Step | Status | Notes |
| --- | --- | --- |
| Exact target | valid | Source PDF p. 2 asks whether the spaces with `0<p<q<=1`, `s=d(1/p-1)` possess `(unconditional)` Schauder bases. |
| Parameter range | valid | The source also assumes `s<1/p`, equivalently `p>(d-1)/d` here. |
| Approximation quasi-norm | valid | Source Lemma 1 supplies the best-dyadic-approximation norm used in the proof. |
| Atom errors | valid | For a level-`m` atom, `E_k<=||atom||_p` for `k<m` and `E_k=0` for `k>=m`. No claim about the actual best constant is needed. |
| Critical cancellation | valid | `|Delta|^(1/p)2^(ms)=2^(-md/p)2^(md(1/p-1))=|Delta|`. The raw `L_p` term is no larger since `p<1` and `|Delta|<=1`. |
| Envelope lower estimate | valid | The source embedding `X -> L1` applied termwise to every finite decomposition yields `||f||_1 <= C||f||_c`; hence the envelope seminorm is separating. |
| Envelope upper estimate | valid | Cellwise decomposition plus the atom bound gives `||f||_c<=C||f||_1` for every dyadic step function. |
| Completion | valid | Dyadic step functions are dense in `X` by the source and in `L1` classically. Equivalent norms on this common dense subspace identify the completions. |
| Operator extension | valid | `||Tx||_c<=||T||||x||_c` follows directly by applying `T` to each finite decomposition. |
| Basis convergence in envelope | valid | Uniformly bounded ordinary partial sums converge on dense `X`, hence on all of the envelope by the three-term approximation estimate. |
| Finite-dimensional ranges | valid | The extended projection has range in the same finite-dimensional coordinate span because that span is closed and dense approximation of inputs suffices. Projection identities persist by continuity. |
| Unconditionality transfer | valid | All finite coordinate projections have a common bound in `X`; their extensions have the same common bound, which is the standard unconditional-basis criterion. |
| Final contradiction | valid | The source explicitly recalls the classical theorem that `L1(I)` has no unconditional Schauder basis. The same holds for `L1(I^d)`, which is a nonatomic `L1` space and isometrically isomorphic to `L1(I)`. |

## Counterexample and loophole search

- The proof does not assume that the original quasi-norm is convex; it uses
  the finite-decomposition definition of the convexified norm.
- The envelope map cannot kill a basis vector because the continuous
  embedding into `L1` makes the envelope norm separating.
- Merely having uniformly bounded projections on `X` would be insufficient
  if `X` were not dense in the envelope; density is built into the envelope
  completion and is also explicit through dyadic steps.
- A conditional basis is not excluded: it also transfers to `L1`, but `L1`
  has conditional bases. The packet states this limitation prominently.
- Standard wavelet theorems for distributional Besov spaces cannot be
  invoked at equality in the source's strict norm-equivalence range.

## Literature audit

Bounded searches through 2026-08-13 covered the local run indexes, exact
title and arXiv id, the quoted basis question, the critical exponent,
Banach-envelope terminology, later Haar/frame work, and the citations exposed
by Math-Net. No primary source resolving this exact first-difference endpoint
question or stating this envelope argument was found. Novelty is plausible,
not certified, and priority is not claimed.

## Rendering audit

The final packet compiled to 3 US Letter pages with no LaTeX warnings,
overfull boxes, or underfull boxes. All three pages were rendered to PNG and
visually inspected at 130 dpi; no clipping, overlap, illegible mathematics,
or malformed source image was found.

- Packet PDF SHA-256: `f68d8512ad0b6d66a9f11f7d2085251833dd1d45022ea7016303dd18ac8a0c46`
- Source PDF SHA-256: `3be6496a629aa69f35c6d31e88c5d42a72bfd4fa5b3081b867b8de3ad837d27f`
- LaTeX source SHA-256: `3357a37822731319bfdc7463cc834747cce3db379cceb92b628947f65fff95ad`
- Source crop SHA-256: `341eff3c7b822d06518d481662b857028f19d2e05da0baf6888a0c117aae4ecb`

## Confidence

Score before typography audit: 97/100.

Residual uncertainty is literature novelty, not a known mathematical gap.

## Human review recommendation

`send to human`

Primary review focus: the basis-transfer lemma and whether the preferred
definition of Banach envelope in this quasi-Banach category matches the
finite-decomposition norm (the proof establishes the needed completion
directly in either convention).
