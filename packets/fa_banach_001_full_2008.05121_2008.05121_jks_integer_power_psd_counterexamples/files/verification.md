# Verification report

Verdict: `candidate_full_likely_valid`

## Exact proof audit

1. For `n=m+3`, the interval
   `pi/(2(n-1)) < delta < pi/(2(n-2))` is nonempty.
2. The total angle span `L=(n-1)delta` is in `(pi/2,pi)`, so every angle lies
   in `(-pi/2,pi/2)` and `x_j=tan(u_j)` is strictly increasing.
3. Every non-endpoint separation is at most `(n-2)delta<pi/2`; only the pair
   `{1,n}` is truncated by the positive part of cosine.
4. The binomial Fourier expansion of `cos(t)^m` has `m+1=n-2` positive
   weights. Hence the untruncated matrix `C` is PSD of rank at most `n-2`.
5. The middle block `B` is positive definite: its evaluation matrix is,
   after nonzero row factors, a square Vandermonde matrix on distinct nodes
   `exp(-2 i u_j)`.
6. In the two-corner determinant expansion, the constant and linear terms
   vanish by `rank(C)<=n-2`. The quadratic coefficient is `-det(B)`, giving
   `det(A)=-cos(L)^(2m) det(B)<0`.
7. Positive diagonal congruence converts `A` to the JKS Gram power and
   preserves the determinant sign.
8. At `m=0`, the source convention `0^0=0` gives the same formula with
   `C` all ones, `B=[1]`, and determinant `-1`.
9. For `m<=p-3`, the negative `(m+3)`-minor violates `TN_p`; Theorem C of the
   source handles all noninteger exponents below `p-2` and all positive cases
   at or above `p-2`.

No unproved lemma or numerical dependency remains.

## Computational audit

Command, run from the packet directory:

```bash
conda run --no-capture-output -n sandbox python code/verify_jks_family.py
```

Scope: `m=0,...,16`, with 180 decimal digits.

Checks: `det(B)>0`, `det(A)<0`, and the relative error in
`det(A)=-c^2 det(B)` is below `1e-70`.

Result: all 17 cases passed. The largest observed relative discrepancy was
below `5e-151`; this is much smaller than the asserted tolerance. This audit
does not replace the exact proof.

## Source and evidence audit

- `source_paper.pdf` is the official arXiv PDF for 2008.05121v2 (32 pages).
- Question 5.5 is on PDF/printed page 19.
- `figures/open_problem_crop.png` is a 1530-by-625 full-width readable crop
  containing the complete question, surrounding classification statement,
  both source examples, and the `0^0=0` convention.

## Novelty audit

The cheap run indexes were searched for `2008.05121`, the exact title, JKS,
Jain--Karlin--Schoenberg, and `max(1+xy,0)`, with no prior run result found.

Bounded web/arXiv searches through 2026-08-17 used:

- exact `Question 5.5` plus the kernel name;
- `K_JKS`, `alpha+3`, `positive semidefinite`, and integer powers;
- the exact formula `max(1+xy,0)` with determinant/PSD terminology;
- close later papers arXiv:2103.12550, 2110.08206, and 2411.03391;
- the author publication page and current author-hosted source PDF.

No later paper explicitly resolving the question or containing this
one-corner-pair determinant construction was found. The current author PDF
still presents the problem as Question 5.5. This supports but does not certify
novelty.

## Render audit

`latexmk` completed without undefined references, overfull boxes, or LaTeX
warnings. The resulting `solution_packet.pdf` has four pages. All four pages
were rendered at 140 dpi to `tmp/qa-page-01.png` through
`tmp/qa-page-04.png` and visually inspected: no text, equations, figure
content, page numbers, or bibliography entries are clipped; the source crop is
readable at normal review zoom.

## Human-review recommendation

Review the sign in the two-corner determinant coefficient, then the
Vandermonde nonsingularity and the classification corollary. If those checks
pass and a specialist search finds no prior answer, promote as a full
solution of Question 5.5.
