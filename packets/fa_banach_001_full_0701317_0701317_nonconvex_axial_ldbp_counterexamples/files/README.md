# Candidate full solution: nonconvex axial LDBP counterexamples

Status: **candidate full solution, likely valid, needs expert review**

Source: Boris Rubin, *The Lower Dimensional Busemann-Petty Problem for
Bodies with the Generalized Axial Symmetry*, arXiv:math/0701317v2 (2007),
published in *Israel Journal of Mathematics* 173 (2009), 213-233. The
conjecture is on PDF page 4, after Theorem 1.1.

## Result

For every parameter choice in Rubin's Theorem 1.1(b), namely

\[
1\leq \ell\leq n/2,\qquad i+\ell\leq n,\qquad
i\in\{\ell+1,\ell+2\},
\]

the packet constructs smooth origin-symmetric star bodies \(A,B\subset
\mathbb R^n\), with \(A\) and \(B\) both \(K_\ell\)-symmetric and
nonconvex, such that

\[
\operatorname{vol}_i(A\cap\xi)\leq
\operatorname{vol}_i(B\cap\xi)\quad(\xi\in G_{n,i}),
\qquad
\operatorname{vol}_n(A)>\operatorname{vol}_n(B).
\]

This proves Rubin's conjecture, subject to expert review.

Let \(k=n-i\), write \(\theta=(\theta',\theta'')\in
\mathbb R^{n-\ell}\oplus\mathbb R^\ell\), and set

\[
\rho_B(\theta)^k=1+\varepsilon
\left(|\theta''|^2-\frac\ell n\right),
\qquad
\frac{kn}{i(n-\ell)}<\varepsilon<\frac n\ell.
\]

The quadratic term is a degree-two spherical harmonic. Under the inverse
generalized cosine transform \(M^{1-i}\), its multiplier relative to the
constant harmonic is \(-i/k\). The unique representing density of \(B\)
therefore becomes negative near the \(\ell\)-dimensional block axis, so
\(B\) is not a \(k\)-intersection body. The same parameter inequality gives
negative curvature in a two-dimensional coordinate section, proving directly
that \(B\) is nonconvex. A small smooth perturbation supported where the
representing density is negative is exactly Rubin's Section 4 negative-result
mechanism; it produces \(A\), the section inequalities on the full
Grassmannian, and the strict volume reversal. Smallness preserves the strict
negative curvature, so \(A\) is also nonconvex.

## Files

- `solution_packet.pdf`: theorem, proof, source evidence, verification, and
  novelty bounds.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_crop.png`: source PDF page 4 crop containing the full
  conjecture.
- `code/verifier.py`: finite parameter and sign sanity checks.
- `VERIFICATION.md`: verification transcript and reviewer checklist.

## Human-review priority

Review the generalized cosine-transform multiplier normalization and the
distribution-level uniqueness of the representing density first. Then check
that Rubin's Lemmas 4.1-4.2 justify the pairing identity and the full
Grassmannian section comparison with the stated indices.

## Novelty status

A bounded search on 11 August 2026 covered the run's four lightweight indexes,
the exact arXiv id and title, the source conjecture's distinctive phrases, the
published DOI, and later symmetry literature including arXiv:1307.3206. No
explicit later resolution or this degree-two construction was found. This is
provisional evidence, not an exhaustive originality determination.
