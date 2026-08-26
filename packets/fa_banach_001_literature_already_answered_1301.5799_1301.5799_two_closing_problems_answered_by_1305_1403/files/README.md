# Literature-Already-Answered: both closing problems in arXiv:1301.5799

Status: `literature_already_answered (both closing problems; dense-only branch carries the exact countable-compactness condition)`

Run: `fa_banach_001`

Agent: `agent_lane_12`

## Source questions

Marek Cuth, *Noncommutative Valdivia compacta*, arXiv:1301.5799,
PDF page 13, ends with two problems.

- Problem 1 asks for a topological property `(T)` of
  `(C(K), tau_p(D))` characterizing when a dense (respectively dense and
  countably closed) subset `D` of a compact space `K` is induced by a
  retractional skeleton.
- Question 1 asks whether three conditions involving a 1-projectional
  skeleton on `C(K)` and convex symmetric sets induced by retractional
  skeletons in the weak-star dual ball or in `P(K)` imply one another in the
  specified directions.

The official source PDF is included as `source_paper.pdf`.

## Answer to Problem 1

Marek Cuth and Ondrej F. K. Kalenda, *Monotone retractability and
retractional skeletons*, arXiv:1403.4480, J. Math. Anal. Appl. 423 (2015),
18--31, says explicitly that it answers the source problem. Theorem 1.4
(PDF page 2; proof on page 11) states, for compact `K` and dense `D subset K`,
that the following are equivalent:

1. `D` is induced by a retractional skeleton in `K`;
2. `D` is countably compact and `(C(K), tau_p(D))` is monotonically Sokolov.

Thus the sought function-space property is monotone Sokolovness. For the
source's dense-and-countably-closed alternative, countable compactness of `D`
is automatic. For merely dense `D`, the exact later characterization retains
countable compactness as an additional condition on `D`; this packet does not
erase that hypothesis.

The official answer PDF is included as
`supporting_paper_problem1_1403.4480.pdf`.

## Answer to Question 1

Marek Cuth, *Simultaneous projectional skeletons*, arXiv:1305.1438,
J. Math. Anal. Appl. 411 (2014), 19--29, says explicitly that Theorem 4.1
answers the source question. Theorem 4.1 (PDF page 6) proves that the following
are equivalent:

1. `C(K)` has a 1-projectional skeleton;
2. a convex symmetric set is induced by a retractional skeleton in the
   weak-star dual ball;
3. a convex set is induced there;
4. a convex set is induced by a retractional skeleton in `P(K)`.

This is stronger than requested: the source's condition in `P(K)` assumes
symmetry, whereas condition (4) does not. Consequently `(iii)=>(ii)`,
`(ii)=>(i)`, and `(iii)=>(i)` in the source are all affirmative.

The official answer PDF is included as
`supporting_paper_question1_1305.1438.pdf`.

## Scope and provenance

This packet records direct later-literature answers, not an original run
proof. The two answer papers explicitly identify the source's numbered
problem/question. Cheap run indexes contained no existing packet for
arXiv:1301.5799.

## Human review notes

- Check the dense-only nuance in Theorem 1.4: monotone Sokolovness is paired
  with countable compactness of `D`.
- Check that source Question 1 asks only implications among the three listed
  conditions and that Theorem 4.1 gives the stronger four-way equivalence.

