# A nondense diagonal counterexample to Remark 2.11

Status: candidate full counterexample to the open problem as stated, likely valid, requiring expert review.

Source: Charles Batty and Chuang Chen, *Besov spaces associated with non-negative operators on Banach spaces*, arXiv:2006.07008v1 (2020). The target is Lemma 2.10 and Remark 2.11 on source PDF p. 16, with the limit defined in (2.37) on p. 15.

## Result

Let (X=\ell^\infty(\mathbb N)) and

\[
 D(A)=\{x=(x_k): (kx_k)\in\ell^\infty\},
 \qquad (Ax)_k=kx_k.
\]

Then (A) is a positive (hence non-negative) closed operator and
\(\overline{D(A)}=c_0\). For every \(\alpha\in\mathbb C\) with
\(\operatorname{Re}\alpha>0\), its fractional power is

\[
 D(A^\alpha)=\{x:(k^\alpha x_k)\in\ell^\infty\},
 \qquad (A^\alpha x)_k=k^\alpha x_k.
\]

Fix the exceptional exponent asked about in Remark 2.11,
\(\alpha=n+it\), where \(n\in\mathbb N\) and \(t\ne0\), take
\(\beta=\alpha+1\), and put \(x_k=k^{-\alpha}\). Then
\(x\in D(A^\alpha)\) and \(A^\alpha x=\mathbf 1\). However, the
truncated expression in (2.37) is exactly

\[
 \left(\left(\frac{N}{N+k}\right)^\alpha\right)_{k\ge1}.
\]

For each fixed (k) this tends to (1), but for each finite (N) it
belongs to (c_0). It therefore cannot converge in \(\ell^\infty\): any
norm limit would be the constant-one sequence coordinatewise, whereas
\(c_0\) is norm closed. Thus the limit asserted in Lemma 2.10 does not
exist.

The same construction works for every \(\alpha\in\mathbb C_+\), not only
when \(\operatorname{Re}\alpha\in\mathbb N\) and
\(\operatorname{Im}\alpha\ne0\). This stronger failure is possible because
the source explicitly allows non-densely defined non-negative operators.

## Scope

The counterexample answers Remark 2.11 negatively in the source paper's
stated generality. It does **not** decide a modified version in which (A)
is required to be densely defined. The earlier Chen--Li theorem cited by the
source was formulated for densely defined operators; this packet does not
claim to contradict that dense-domain result.

## Packet contents

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv source-question paper.
- `figures/limit_formula_crop.png`: source PDF p. 15, including (2.37).
- `figures/open_problem_crop.png`: source PDF p. 16, including Lemma 2.10 and Remark 2.11.
- `figures/source_generality_crop.png`: source PDF p. 2, documenting that nondense domains are allowed.
- `VERIFICATION.md`: structural proof audit and novelty-search record.
- `code/verifier.py`: optional finite-coordinate numerical check of the exact integral evaluation.

## Novelty check

On 11 August 2026, bounded searches covered the four run indexes; the exact
arXiv id and source title; the phrases “mystery of imaginary powers,”
“n + i t,” and “characterizations of domains of fractional powers”; the cited
Chen--Li paper; later title/citation searches; and searches combining
non-densely defined fractional powers with diagonal operators on
\(\ell^\infty\) and \(c_0\). Searches found background literature on
fractional powers of non-densely defined operators, but no later paper
explicitly answering Remark 2.11 and no occurrence of this diagonal
counterexample. Novelty is provisional.

## Human-review recommendation

Verify the source's intended scope (especially whether Remark 2.11 inherits
the paper's explicit allowance of non-densely defined operators), the
identification of (A^\alpha) via the bounded inverse (A^{-1}), and the
coordinatewise evaluation of the truncated integral. If the intended question
is silently restricted to densely defined operators, reclassify this as a
sharp obstruction showing that density is indispensable rather than as a full
counterexample to that restricted variant.

