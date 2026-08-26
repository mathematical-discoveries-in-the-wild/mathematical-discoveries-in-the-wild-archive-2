# The complement-layer obstruction for nested spherical designs

Status: **candidate full counterexample — likely valid, pending human
review**.

Source: Ruigang Zheng and Xiaosheng Zhuang, *On the existence and estimates
of nested spherical designs*, arXiv:2405.10607; Applied and Computational
Harmonic Analysis 73 (2024), 101672.

The source conjectures that, for every `t1<t`, a spherical `t1`-design of
size `C_d t1^d` can be nested in a spherical `t`-design of size `C_d t^d`
with one constant independent of `t1,t`. This packet refutes that
identical-constant clause.

The key fact is elementary but decisive: the newly added multiset in any
nested pair is itself a `t1`-design. Hence it needs at least the
Delsarte--Goethals--Seidel lower-bound number `Omega(t1^d)` of points. For
adjacent strengths `t=t1+1`, the conjectured identical cardinality formulas
leave only `C_d((t1+1)^d-t1^d)=O(t1^(d-1))` added points, a contradiction.

The packet also proves:

- no common asymptotic leading coefficient is possible along adjacent
  strengths;
- a strict every-degree nested chain through strength `T` needs
  `Omega(T^(d+1))` points;
- on the circle, the weaker pairwise optimal-order question is true: every
  `t1<t` has an explicit regular-polygon nested pair with at most `2t1` and
  `2t` points.

The weaker higher-dimensional conjecture with merely comparable cardinalities
and unrelated constants remains open.

Files:

- `solution_packet.pdf`: review-ready counterexample packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original arXiv PDF.
- `figures/order_definition_crop.png`: the source's exact meaning of “order”.
- `figures/conjecture_crop.png`: the exact conjecture.
- `code/crop_source.py`: reproducible crop script.
- `verification.md`: analytic, literature, build, and visual checks.

Human-review focus: confirm the source's exact-coefficient interpretation and
the applicability of its quoted cardinality lower bound to the multiset
convention adopted in the paper.
