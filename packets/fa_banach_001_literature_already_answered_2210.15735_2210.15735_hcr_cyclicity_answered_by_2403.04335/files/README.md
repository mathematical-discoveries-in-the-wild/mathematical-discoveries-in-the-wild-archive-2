# HCR/corona hypothesis removed by arXiv:2403.04335

Status: `literature_already_answered`

## Source question

Emmanuel Fricain and Sophie Grivaux, *Cyclicity in de Branges--Rovnyak
spaces*, arXiv:2210.15735.

Question 5.2 on arXiv PDF page 20 asks whether Proposition 5.7 remains true
without the hypothesis that the Pythagorean pair `(a,b)` satisfies (HCR),
equivalently the relevant corona condition.  The requested conclusions are:

1. every reproducing kernel `k^b_lambda` is cyclic for `S_b`;
2. if `b` is outer, then `b k_lambda` is cyclic for every `lambda`, and in
   particular `b` is cyclic.

## Explicit later answer

Emmanuel Fricain and Romain Lebreton, *Cyclicity of the shift operator and a
related completeness problem in de Branges--Rovnyak spaces*, arXiv:2403.04335,
answers both parts affirmatively.

- Theorem 4.2 proves that an outer `f in H(b)` is cyclic whenever
  `b/f in L^infinity(T)`.
- Corollary 5.1(i) deduces cyclicity from `inf_D |f|>0`, and Corollary 5.1(ii)
  says that `b` is cyclic exactly when `b` is outer.
- Example 5.2(a) applies the lower bound
  `|k^b_lambda(z)| >= (1-|b(lambda)|)/2` to every reproducing kernel.
- Example 5.2(b) applies Theorem 4.2 to `f=b k_lambda` when `b` is outer.

On arXiv PDF page 16, immediately after these two deductions, the authors
explicitly identify Proposition 5.7 of the earlier paper and state that its
corona-pair assumption can be omitted.  This is a complete literature answer,
not a new result of this run.

Files:

- `source_paper.pdf`: arXiv:2210.15735.
- `supporting_paper_2403.04335.pdf`: separate answering paper.
- `main.tex`, `solution_packet.pdf`: compact literature-status note.
