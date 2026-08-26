# Verification report

Verdict: **likely valid; candidate full resolution; specialist review
required**.

## Scope checked

The audit covers the theorem as stated in `main.tex`: an asymptotic upper
bound for all $p\ge C_0\log n$, with absolute constants, under the source
paper's probability threshold greater than $3/4$.

## Lemma-by-lemma audit

1. **Soft maximum.** The truncated-moment calculation is correct. With
   $b_n$ defined by $P(|Z|>b_n)=1/(2n)$, Mills' lower bound gives
   $E\sum |Z_i/b_n|^p1_{|Z_i|\le b_n}
   \le (b_n^2+1)/(2(p-b_n^2))$. For $p\ge C_0\log n$ this is an arbitrarily
   small absolute constant. Combining Markov with the exact probability
   $(1-1/(2n))^n$ yields the claimed lower probability $1/2$.

2. **Chi amplification.** Integrating the $\chi_d$ density over
   $[r,r+1/r]$ is legitimate when $r^2\ge2d$. After comparison with the
   scalar Gaussian tail at $b_n$ and Stirling's upper bound, the logarithm
   of $nP(\chi_d>r)$ has leading term
   $(d/2)\log(e\log n/d)$, while the threshold displacement costs only
   $O(c_1d\log(e\log n/d))$. The leftover prefactor costs
   $O(\log(e\log n/d))$. Choosing $c_1$ small leaves positive growth,
   uniformly down to $d=2$.

3. **Conditioning.** Given the unique longest row, the remaining Gaussian
   rows are independent and conditioned to a Euclidean ball. A fixed
   one-dimensional absolute projection under this conditioning has density
   obtained from the unconditioned $|Z|$ density by a nonincreasing weight.
   Hence it is stochastically dominated by $|Z|$. Choosing the comparison
   direction measurably in the orthogonal complement of the longest-row
   direction preserves rotational invariance. The longest row contributes
   zero in that direction.

4. **Ambient normalization.** Standard Gaussian singular-value estimates
   make every coefficient direction Euclidean to relative error
   $o(a_d)$, uniformly for $2\le d\le c_0\log n$. Therefore the
   coefficient-space $\ell_p$ gap survives after dividing by ambient
   $\ell_2$ norms.

5. **Probability accounting.** The chi event has probability above $9/10$.
   Conditional on it, the comparison direction succeeds with probability at
   least $1/2$. Subtracting a singular-value failure below $1/100$ leaves
   probability above $1/4$ for non-sphericity. This contradicts a good-event
   probability greater than $3/4$.

6. **Dimension inversion.** Sphericity passes to subspaces, and the marginal
   of a Haar subspace chosen inside a Haar subspace is Haar. Selecting
   $d=\max\{2,\lceil A\varepsilon\log n/
   \log(1/\varepsilon)\rceil\}$ makes
   $d\log(e\log n/d)/\log n\gtrsim A\varepsilon$. When the selected scale is
   below two, $d=2$ gives the stronger gap
   $\asymp\log\log n/\log n$; the condition defining that case contributes
   the compensating factor $1/A$.

## External dependencies

- Standard extremal singular-value bounds for a rectangular Gaussian matrix.
- Tikhomirov's sharp randomized cube theorem only for the terminal
  fixed-distortion case; the small-distortion logarithmic-$p$ wedge is proved
  directly.

## Human-review priorities

The most delicate points are the regular-conditional formulation in the
longest-row lemma, constant-uniformity of the chi-tail calculation at $d=2$,
and presentation of the very-small-$\varepsilon$ cutoff in the final
inversion. No gap was found in this audit, but those three points merit an
independent specialist derivation before the result is treated as verified.

## Novelty check

The bounded search covered the run indexes, local arXiv sources, exact and
close-variant arXiv/web queries, and 24 OpenAlex citing records for the source
DOI. No later resolution or the present soft-max/longest-row argument was
found. This does not establish novelty.
