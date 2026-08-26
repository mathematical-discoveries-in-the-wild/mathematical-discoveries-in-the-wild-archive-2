# A strongly forward isometric noncontractive representation of finite `L_d`

**Status:** claimed full negative resolution / counterexample; likely valid,
pending human review.

**Source:** N. Christopher Phillips, *Analogs of Cuntz algebras on $L^p$
spaces*, arXiv:1201.4196v1 (2012), 60 pages.

Definition 2.12 and Remark 2.13 on source page 10 ask whether a strongly
forward isometric representation of the finite Leavitt algebra $L_d$ can fail
to be contractive on generators. The source gives such behavior for
$L_\infty$ but states that the finite-$d$ case is unknown.

The packet gives a negative answer for every $d\ge2$ and every
$1\le p<\infty$. Let $(V_j,W_j)_{j=1}^d$ be the standard spatial Leavitt
family on $\ell^p$, put $\alpha=2^{-1/p}$, and define

\[
S_1=V_1,\qquad S_2=\alpha(V_1+V_2),\qquad
T_1=W_1-W_2,\qquad T_2=\alpha^{-1}W_2,
\]

leaving the remaining generators unchanged. These operators satisfy the
Leavitt relations exactly. Every $S_j$ is an isometry and every linear
combination $\sum_j\lambda_jS_j$ is a scalar multiple of an isometry, because
the ranges of the $V_j$ are disjoint. Thus the representation is strongly
forward isometric. But $\|T_2\|=\alpha^{-1}=2^{1/p}>1$, so it is not
contractive on generators.

Files:

- `solution_packet.pdf`: expert-facing statement and proof.
- `source_paper.pdf`: the arXiv source paper.
- `figures/open_problem_crop.png`: Definition 2.12 and Remark 2.13 on page 10.

Novelty check (bounded, 2026-08-09): the run registry and solution/attempt/gap
indexes were searched by arXiv id, title, and the core terminology. Exact
phrase searches for “strongly forward isometric” plus “contractive on
generators,” the exact open sentence, title/citation searches, and searches
for finite-$d$ Leavitt representations found the source paper and later
general $L^p$-operator-algebra literature, but no later answer to this exact
question. This is evidence, not a guarantee, of novelty.

**Human-review focus:** check the four displayed Leavitt-relation identities
and the norm formula for a linear combination of the mixed forward
generators.

