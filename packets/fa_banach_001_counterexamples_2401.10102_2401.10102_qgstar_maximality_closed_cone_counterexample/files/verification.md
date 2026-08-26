# Verification report

Status: `candidate_counterexample_likely_valid`

## Exact proof audit

1. The weighted successive-difference function
   `p(x)=sup_k 2^(-k)|x_k-x_(k+1)|` is a continuous norm on `c0`.
2. Its epigraph in `c0 ⊕∞ R` is therefore a closed convex cone. The norm
   identity `p(-x)=p(x)` makes the cone pointed.
3. Positivity of `(f,a)` on the epigraph is equivalent to `a>=0` and
   `|f(x)|<=a p(x)` for all `x`.
4. For `s_N=e_1+...+e_N`, `p(s_N)=2^(-N)`. Thus
   `|sum_(k<=N) f_k|<=a2^(-N)`, and `f in ell1` gives `sum_k f_k=0`.
5. Consequently `C*-C*` lies in the proper norm-closed hyperplane
   `{(f,a):sum_k f_k=0}` and is not dense in `X*`.
6. For `n>=2`, `p(e_n)=2^(-(n-1))`; hence `(e_n,p(e_n))` is weakly null in
   `X` and has norm one. It lies in every truncation with `epsilon in (0,1)`.
7. A bounded base would be strongly separated from zero. Boundedness then
   makes the separating functional uniformly positive on every fixed
   truncation, contradicting the weakly null sequence.
8. The source's weak-separation assertion and bounded-base assertion are both
   false, so their equivalence holds for this cone outside `qG*`.

## Source evidence

The published source PDF has 13 pages. Complete printed page 9 was rendered at
170 dpi as `figures/source_problem_page9.png`; it contains the base definition,
Corollary 1, the closed-cone motivation, and Problem 1. The page was visually
inspected at original resolution and is readable and complete.

## Literature audit

On 2026-08-09, exact-phrase and core-keyword web searches, the arXiv record,
the 2019 published version, and later citing papers were checked after the
direct construction. Searches included the problem's exact maximality phrase,
`qG*`, quasi-generating dual cones, bounded bases, weak closures of truncated
cones, `c0`, and epigraph cones. No later solution or occurrence of this
construction was found. This supports plausible novelty only; it does not
certify priority.

## Human verifier focus

- Confirm that the source asks literal maximality of the class for which the
  equivalence holds, so a cone with both assertions false is admissible.
- Check that the source imposes no hidden normality condition; the example is
  closed and pointed in any case.
- Check the dual-cone characterization and the passage from finite partial
  sums to `sum_k f_k=0`.
- Check strong separation of a convex base from zero and the scaling estimate
  on a fixed truncation.

## PDF QA

`solution_packet.pdf` was compiled twice by `latexmk`. The final log has no
overfull/underfull box, undefined-reference, or substantive warning hits. All
five final pages were rendered at 150 dpi and visually inspected individually.
The complete source page is readable; the theorem, proof ending, bibliography,
links, equations, and page numbers are unclipped, with no overlap or missing
glyphs.
