# Verification report

Status: `candidate_full_likely_valid_positive_answer`.

## Source audit

- Source: Sophie Grivaux, *Frequently hypercyclic operators with irregularly
  visiting orbits*, arXiv:1710.07901, published in JMAA 462 (2018), 542-553.
- Open question: source PDF page 11, Question 3.3. The source defines
  `dens A` as ordinary natural asymptotic density.
- Lemma 2.2, source PDF page 7, gives the exact disjoint decomposition of the
  half-space return set into intervals `I^+_{k,s}` lying within distance
  `2^s+d` of each center `k`.
- Source PDF page 8 puts each center at distance at least
  `2^(s+1+p)` from the complement of its dyadic subblock and assumes
  `2^(s+1+p) >= 2^(s+1)+2d+1`. The entire detecting interval therefore stays
  inside that subblock.
- The same page defines the center sets using only dyadic block indices
  `J = 5N union (5N+2)`. Hence the return set misses the complete consecutive
  blocks with indices `5q+3` and `5q+4`.

## Independent proof checks

1. **Support containment.** The support radius is `2^s+d`, strictly below
   the source's boundary margin. No endpoint can spill into an omitted block.
2. **Gap endpoints.** For
   `N_q=2^(5q+3)-1` and `M_q=2^(5q+5)-1`, any subset `A` of the return set has
   exactly equal counts at `N_q` and `M_q`.
3. **Density conclusion.** Since `N_q/M_q -> 1/4`, existence of a natural
   density `delta` forces `delta=delta/4`, hence `delta=0`. This proves the
   stronger hereditary statement, not merely failure of density for the full
   return set.
4. **Frequent hypercyclicity.** The vector is exactly the vector proved
   frequently hypercyclic in source Lemma 2.1, so the half-space is nonempty
   and its return set has positive lower density.
5. **Explicit witness.** For `T=2B` on `ell^2(N_0)`, the orbit
   `x_{-m}=2^{-m}e_m`, `x_n=0` for `n>=1` satisfies `Tx_n=x_{n+1}`, spans the
   coordinate vectors, has an absolutely norm-convergent bilateral series,
   and is detected only at index zero by the zeroth-coordinate functional.

The exact script `code/check_lacunary_gap.py` was run successfully. It checks
the residue classes, endpoint ratios, and margin implication on representative
finite ranges. The argument in the packet is symbolic and does not rely on
the finite test.

## Novelty bound

On 11 August 2026 the run result/attempt indexes and bounded web/arXiv searches
were checked using the arXiv id, exact title, exact question phrase, and the
terms `positive density subset`, `irregularly visiting orbit`, and close
variants. The search found the source and journal record but no later paper
explicitly answering Question 3.3. This is not an exhaustive specialist
citation review. Novelty confidence is moderate; mathematical confidence is
high.

## Build and visual QA

- `source_paper.pdf` is the locally compiled arXiv source (12 pages).
- `figures/open_problem_crop.png` was rendered from page 11 and contains the
  full readable Question 3.3 statement.
- The final packet was compiled with `latexmk`, all build artifacts were sent
  to `tmp/`, and every rendered output page was visually inspected.
- The LaTeX log was checked for overfull boxes and unresolved references.

## Human-review recommendation

Promote after checking the one-line implication from the source's center
margin to containment in selected dyadic blocks, and confirming that the
source's word `density` is the natural density it defines on page 2. The
remaining steps are elementary exact counting.
