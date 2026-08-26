# Literature Answer: Translation-Invariant Min–Max Formula

Status: literature_already_answered

Run: fa_banach_001
Agent: agent_lane_07

## Source question

Section “Some Questions” of N. Guillen and R. W. Schwab,
*Min-max formulas for nonlocal elliptic operators*,
arXiv:1606.08417, asks whether a translation-invariant operator
\(I:C_b^2(\mathbb R^d)\to C_b^0(\mathbb R^d)\) can be represented using
only translation-invariant linear operators in the paper’s min–max formula.

## Direct later answer

The same authors answer this affirmatively in
*Min-max formulas for nonlocal elliptic operators on Euclidean space*,
arXiv:1812.09642 (final version, Nonlinear Analysis 193 (2020), 111468).

Theorem 1.10 states that if \(I\) is Lipschitz, has the global comparison
property, and is translation invariant, then
\[
  I(u,x)=\min_a\max_b\{f_{ab}+L_{ab}(u,x)\},
\]
where the \(f_{ab}\) are constants and all \(L_{ab}\) are linear
translation-invariant Lévy operators with constant coefficients.

The proof is exactly tailored to the source question: apply the scalar
min–max theorem to \(F(u)=I(u,0)\), represent its supporting functionals by
Lévy functionals at \(0\), and use \(I(u,x)=F(\tau_xu)\) to translate them
to constant-coefficient operators at every \(x\).

## Scope

This packet records a direct same-authors literature resolution. It does not
claim a new proof from this run. The other broad questions in the source’s
final section are not resolved by Theorem 1.10.

## Files

- main.tex: theorem-level comparison of the question and later answer.
- solution_packet.pdf: compiled status packet.
- source_paper.pdf: arXiv:1606.08417.
- supporting_1812.09642.pdf: later answering paper.
- VERIFICATION.md: source and artifact checks.
