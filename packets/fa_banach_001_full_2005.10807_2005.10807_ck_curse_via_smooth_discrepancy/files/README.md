# Candidate full result: the fixed-\(k\) smooth curse of dimensionality

## Source question

E and Wojtowytsch, arXiv:2005.10807, prove that norm-controlled Barron and
tree-like neural-network spaces are poor \(L^2\)-approximators for some
Lipschitz targets.  They conjecture that Lipschitz targets can be replaced by
\(C^k\) targets for every fixed \(k\) that does not scale with dimension.  In
their open-problem section they reduce this to empirical convergence against
test functions with bounded Lipschitz norm and bounded \(k\)-th derivative.

## Result

Let \(X\hookrightarrow L^2(\mathbb T^d)\) be a Banach function space whose
unit ball has the uniform Monte-Carlo estimate
\[
 \mathbb E\sup_{\|f\|_X\le1}|(P_n-P)f|\le C_Xn^{-1/2}.
\]
This includes the Barron and tree-like spaces used in the source paper.  If
\(d>2k\), then
\[
 \sup_{\|g\|_{C^k}\le1}\inf_{\|f\|_X\le t}\|g-f\|_2
 \ge c_{d,k,X}t^{-2k/(d-2k)}.
\]
Moreover, there is one \(g\in C^k(\mathbb T^d)\), \(\|g\|_{C^k}\le1\), such
that for every \(\eta>4k/(d-2k)\),
\[
 \limsup_{t\to\infty}t^\eta
 \inf_{\|f\|_X\le t}\|g-f\|_2^2=\infty.
\]
Thus the source conjecture is proved in its intended high-dimensional regime:
for every fixed \(k\), all sufficiently large dimensions admit a fixed
\(C^k\) target suffering the same norm-controlled curse.

## New ingredients

1. A grid of disjoint \(C^\infty\) bumps gives the deterministic lower bound
   \(n^{-k/d}\) for integration against every \(n\)-point rule.
2. The same construction avoids the source paper's radius-\(n^{-1/d}\) balls,
   so the lower bound survives the ball-averaging operators needed for
   \(L^2\)-continuity.
3. A Baire-category upgrade converts a width lower bound into one fixed hard
   target under the sole condition \(d>2k\).  This improves the direct
   multi-scale lemma's restriction \(d>4k\).

The empirical upper rate itself is not claimed as new: Kloeckner (2018)
proved the matching \(n^{-k/d}\) bound for \(C^k\) observables when \(d>2k\).
The candidate new result is the mollified lower-bound bridge and its
application, together with the Baire fixed-target upgrade.

## Scope

The threshold \(d>2k\) is the natural one for this method: only there is the
smooth empirical exponent \(k/d\) strictly smaller than the hypothesis
class's Monte-Carlo exponent \(1/2\).  At \(d\le2k\), smooth empirical
integration is parametric (up to the critical logarithm), so this separation
mechanism cannot produce a curse.  The theorem does not assert that every
\(C^k\) function is hard.

## Files

- `main.tex`: self-contained proof.
- `solution_packet.pdf`: rendered proof packet.
- `VERIFICATION.md`: proof audit and literature boundary.
- `source_paper.pdf`: arXiv:2005.10807.
- `supporting_kloeckner_1802.04038.pdf`: prior smooth empirical upper bound.

