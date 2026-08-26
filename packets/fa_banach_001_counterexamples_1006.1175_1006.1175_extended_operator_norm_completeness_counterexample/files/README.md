# 1006.1175 — extended operator completeness need not imply range completeness

Status: candidate full negative answer in the source's stated generality, with an exact positive repair; likely valid, human review requested.

Model: GPT5.6.

Source: S. Cobzaș, *Functional analysis in asymmetric normed spaces*, arXiv:1006.1175v1 (2010), Remark 3.8(2) on source PDF page 19.

## Result

The source asks whether completeness of the extended-norm operator space `(L(X,Y), ||.||*_{p,q})` forces `(Y,q)` to be biBanach. The answer is no.

Take `X=R` with `p(t)=max(t,0)` and take the incomplete ordinary normed space `Y=c_00` with its `ell^2` norm. Every operator is `A_y(t)=ty`. If `y` is nonzero, then

`||A_y||* = sup_{t<=1} ||ty||_2 = infinity`.

Thus every two distinct operators are at infinite distance. Every Cauchy operator sequence is eventually constant, so the extended operator space is complete although `Y` is incomplete.

The packet proves the exact positive repair. Let `D_p` be the space of linear functionals whose absolute value is bounded on the one-sided unit ball `{p<=1}`. If `D_p` is nonzero, the classical rank-one argument works and completeness of the operator space forces `Y` to be biBanach. If `D_p=0`, Hahn–Banach implies that zero is the only finite-extended-norm operator into any range, so completeness is automatic.

## Files

- `main.tex`: self-contained theorem, dichotomy proof, and counterexample.
- `solution_packet.pdf`: rendered expert-facing packet.
- `source_paper.pdf`: official arXiv PDF.
- `source_question_crop.pdf`: readable crop of source Remark 3.8(2).
- `crop_question.tex`: reproducible crop source.
- `verification_report.md`: proof, source, PDF, and novelty checks.

No computational experiment is used; the proof is analytic and explicit.

## Reviewer focus

Please check:

1. that the source's completeness convention is completeness for the symmetric extended metric;
2. that `p(t)=max(t,0)` lies in the source's allowed class (it is also a recurring source example);
3. the Hahn–Banach step proving that a nonzero finite-norm operator creates a nonzero bilaterally bounded functional;
4. whether a `T_1` or finite-valuedness hypothesis was tacitly intended but unstated;
5. the bounded novelty search before external dissemination.

## Novelty bound

Bounded searches through 13 August 2026 covered all four run indexes, the exact source title, arXiv id, and question wording, plus close variants involving extended operator norms, completeness, biBanach ranges, and asymmetric norms. They found the source, its later book version, and adjacent operator theory, but no answer to the remark or the domain-dual dichotomy proved here. Novelty remains provisional.
