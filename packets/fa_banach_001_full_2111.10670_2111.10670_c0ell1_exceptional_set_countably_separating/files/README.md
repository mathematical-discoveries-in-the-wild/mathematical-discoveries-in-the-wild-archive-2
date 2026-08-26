# The exceptional set is countably separating (arXiv:2111.10670)

**Status:** candidate full affirmative solution to the converse question after
Corollary 4.10, subject to human review.

Ronchim and Tausk prove that if the exceptional set

\[
E=\{t\in Q:(F_i(t))_{i\in I}\notin c_0(I)\}
\]

admits a countably separating family, then a weak-star-null family
`(F_i)_{i in I}` in `NBV(K)` is of type `c_0 ell_1` over `Q`. They ask
whether the converse holds.

The answer is affirmative. From a `c_0 ell_1` decomposition `F=a+b`, choose
at each `t in E` an index `i(t)` for which `F_i(t)` is large and
`b_i(t) != 0`. Every fiber of `t -> i(t)` is countable because each row
`b_i` has countable support. Right continuity gives a neighborhood `V_t` on
whose right-hand part `F_{i(t)}` stays large.

If a set `M` satisfies `x in V_y` for every `x,y in M`, split it according
to a common lower bound `1/m`. For `y in M`, the selected coordinate is
large on the right tail `J_y={x in M:x>=y}`. When `J_y` is infinite, source
Lemma 4.11 says that only finitely many coordinates can be uniformly large
on it. These finite coordinate sets are nested as `y` increases, so their
union is countable. The selected-coordinate fibers are countable, and the
points with finite right tail are countable as well. Hence `M` is countable.

Combining this converse with source Corollary 4.10 gives the exact
characterization:

\[
(F_i)\text{ is of type }c_0\ell_1\text{ over }Q
\quad\Longleftrightarrow\quad
E\text{ admits a countably separating family.}
\]

## Files

- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: full-width crop of printed page 27,
  containing Corollary 4.10 and the converse question.
- `main.tex`: packet source; build and QA intermediates are in `tmp/`.

## Verification report

The proof was checked dependency-by-dependency. It uses only the definition of
type `c_0 ell_1`, right continuity in `NBV(K)`, the elementary fact that an
absolutely summable row has countable support, and source Lemma 4.11. The two
possible tail cases are exhaustive: points with infinite right tail are
controlled by a countable union of selected-coordinate fibers, while a linear
order has at most one point with each prescribed finite right-tail size. No
computational check is applicable.

## Human-review focus

Verify the one-sided neighborhood construction at non-right-isolated points
and the nested-finite-set argument. In particular, for `y<=z` one has
`J_z subset J_y`, hence the finite set of coordinates large on `J_y` is
contained in the corresponding set for `J_z`.

## Novelty check

The run indexes and targeted web searches through 2026-08-09 used arXiv id
`2111.10670`, the exact converse sentence, `countably separating family`,
`c_0 ell_1`, `c_0(I)-extension property`, the exact paper title, the DOI, and
the authors' names. Searches also checked later compact-line extension work
returned by title/citation queries. No later paper explicitly answering
Corollary 4.10's converse was found. Novelty remains subject to expert review.

Ledger:
`runs/fa_banach_001/ledger/results/2111.10670_c0ell1_exceptional_set_countably_separating.json`.
