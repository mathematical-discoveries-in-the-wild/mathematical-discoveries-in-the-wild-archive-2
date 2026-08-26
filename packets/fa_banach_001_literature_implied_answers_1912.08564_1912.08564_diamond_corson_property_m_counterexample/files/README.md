# Consistent negative answer to the Corson Property (M) equivalence

## Source question

- Source: Claudia Correa, *On the c_0-extension property*,
  arXiv:1912.08564.
- Location: Remark 3.6, PDF page 9.
- Question: for every Corson compactum K, is it true that `C(K)` has the
  c0-extension property if and only if K has Property (M)? The remark also
  asks specifically about Kunen's Corson compactum without Property (M).

## Status

`literature_implied_answer (consistent negative under diamond)`

Plebanek's later paper *Monolithic spaces of measures*, arXiv:1912.13297,
Theorem 2.9 (PDF page 4), constructs under Jensen's diamond a Corson compact K
such that `P(K)` is aleph_0-monolithic while K supports a probability measure
of Maharam type omega_1. Plebanek records in the introduction that `P(K)` is
aleph_0-monolithic exactly when the dual ball of `C(K)` is weak-star
aleph_0-monolithic. Correa's Theorem 2.5 (PDF page 6) then gives the
2-c0-extension property for `C(K)`.

The measure's support is nonseparable. If it were separable, Corson
monolithicity would make the closed support metrizable, and every measure on a
compact metrizable space has countable Maharam type. This contradicts type
omega_1. Hence K fails Property (M), while `C(K)` has even 2-c0-EP.

The supporting paper connects its measure-space problem to Correa's work, but
does not state the resulting c0-extension corollary. The answer is therefore a
direct literature implication, not an explicitly advertised solution.

## Scope

- This proves that the universal equivalence is false under diamond and hence
  cannot be a theorem of ZFC if ZFC plus diamond is consistent.
- It does not give a ZFC counterexample; Plebanek states that even deriving the
  construction from CH was unknown.
- It does not decide whether Kunen's particular compactum has c0-EP.
- It does not answer Correa's separate question whether c0-EP for an arbitrary
  Banach space forces its dual ball to be weak-star monolithic. Plebanek's
  example has a monolithic dual ball and therefore is not a counterexample to
  that converse.

## Search evidence

The bounded check covered the run registry, solution, attempt, and proof-gap
indexes for both arXiv ids and the terms c0-extension, weak-star monolithic,
Corson, Property (M), and Kunen. Web searches covered the exact source title
and both question formulations. The decisive hit was the locally ingested
arXiv:1912.13297; its Theorem 2.9 and introductory equivalence supply the
result after combination with Correa's Theorem 2.5.

## Files

- `solution_packet.pdf`: compact rendered status note.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: Correa, arXiv:1912.08564.
- `supporting_paper_1912.13297.pdf`: Plebanek, arXiv:1912.13297.

## Human review recommendation

Verify the three-link implication `P(K) monolithic -> dual ball monolithic ->
2-c0-EP` and the short Maharam-type argument forcing nonseparable support.
The result should be read as a consistent counterexample to the general
Corson equivalence, with the ZFC and Kunen-specific questions left open.

