# Infinite-product counterexamples to Questions 5.2 and 5.3

Status: candidate full counterexamples, likely valid, requiring expert review.

Source: Eusebio Gardella, *Rokhlin dimension for compact group actions*, arXiv:1407.1277v2; Indiana Univ. Math. J. 66 (2017), 659--703. The targets are Questions 5.2 and 5.3 on source PDF p. 28.

## Result

Let

\[
G=\prod_{j=1}^{\infty}\mathbb Z/2\mathbb Z,
\qquad
X=\prod_{j=1}^{\infty}S^1,
\]

and let each coordinate of \(G\) act on the corresponding circle by multiplication by \(\pm1\). The action is free. The induced action on \(C(X)\) has the \(X\)-Rokhlin property because the identity map \(C(X)\to C(X)\) is already equivariant, central, and unital. Nevertheless its Rokhlin dimension is infinite. Since \(C(X)\) is commutative, its ordinary and commuting-tower Rokhlin dimensions agree.

For the tail subgroup \(N_i=\prod_{j>i}\mathbb Z/2\mathbb Z\), the quotient \(H_i=G/N_i\cong(\mathbb Z/2\mathbb Z)^i\) acts on \(X/N_i\). After identifying both \(X/N_i\) and \(X/G\) with the infinite torus, the principal-bundle map \(X/N_i\to X/G\) squares its first \(i\) coordinates. The first \(i\) degree-one mod-2 cohomology classes all pull back to zero, while their cup product is nonzero. The standard sectional-category cup-length bound gives Schwarz genus, hence \(H_i\)-index, at least \(i\). Corollary 5.15 of Gardella--Hajac--Tobolski--Wu, arXiv:1801.00767, identifies the original Rokhlin dimension with the supremum of these finite-quotient indices, so it is infinite.

Thus the same action answers both source questions negatively:

- it is \(X\)-Rokhlin but does not have finite Rokhlin dimension with commuting towers;
- it is free on its maximal ideal space but does not have finite Rokhlin dimension.

The source itself suggested a closely related varying-order product. The packet supplies the missing dimension computation for a simpler constant-order version.

## Packet contents

- "solution_packet.pdf": review-ready proof packet.
- "main.tex": LaTeX source.
- "source_paper.pdf": official source-question paper.
- "supporting_paper_1801.00767.pdf": official arXiv PDF containing the inverse-limit formula used in the proof.
- "figures/open_problem_crop.png": source PDF p. 28, including both questions and the suggested construction.
- "VERIFICATION.md": structural proof audit and novelty-search record.

## Novelty check

On 11 August 2026, bounded searches covered the four run indexes; the exact source title and arXiv id; exact wording of Questions 5.2--5.3; “arbitrary compact groups,” “X-Rokhlin,” “coordinate-wise rotation,” “infinite Rokhlin dimension,” and “Schwarz genus”; the source author's thesis; the published source; arXiv:1801.00767; and later papers/citations returned by those searches. The original suggestion and the later general inverse-limit formula were found, but no source explicitly computing this product action or announcing answers to Questions 5.2 and 5.3 was located. Novelty is provisional.

## Human-review recommendation

Verify (i) the identification of \(X/N_i\to X/G\) with squaring in the first \(i\) coordinates, (ii) the mod-2 sectional-category lower bound, and (iii) the hypotheses and convention of Corollary 5.15 in arXiv:1801.00767. Also check that “the \(X\)-Rokhlin property” in Question 5.2 permits the underlying free \(G\)-space \(X\), as in the cited definition.
