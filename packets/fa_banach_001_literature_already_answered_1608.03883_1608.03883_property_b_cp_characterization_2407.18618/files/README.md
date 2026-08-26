# Literature answer: property (B) for `C_p(X)`

**Status:** `literature_already_answered`.

## Original question

Mikołaj Krupski and Witold Marciszewski, *On the weak and pointwise
topologies in function spaces II*, arXiv:1608.03883, Problem 5.10 on PDF page
12, ask:

> Characterize the property (B) of `C_p(X)` in terms of the topology of a
> Tychonoff space `X`.

Here a space has property (B) if it has a countable family of closed nowhere
dense sets such that every compact subset is contained in one member.

## Explicit later answer

Mikołaj Krupski, Kacper Kucharski, and Witold Marciszewski,
*Characterizing function spaces which have the property (B) of Banakh*,
arXiv:2407.18618, explicitly cite `[4, Problem 5.10]`, state that they settle
it, and prove in Theorem 1.1 on PDF page 2:

`C_p(X)` fails property (B) if and only if `X` has property `(kappa)`, meaning
that every pairwise disjoint sequence of finite subsets of `X` has an infinite
subsequence admitting a point-finite open expansion.  Equivalently,
`C_p(X)` has property (B) exactly when `X` fails property `(kappa)`.

This is an explicit answer recognized by the supporting authors, so the packet
belongs in `literature_already_answered`, not in a new-result folder.

## Scope

This settles only Problem 5.10.  It does not settle Problems 1.1 or 1.2 about
homeomorphisms between `C_p(K)` and `C_w(L)`, nor the concrete Hilbert-cube and
Cech--Stone questions in Section 4 of the source paper.

## Files

- `source_paper.pdf`: arXiv:1608.03883.
- `supporting_paper_2407.18618.pdf`: arXiv:2407.18618.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- Ledger: `ledger/results/1608.03883_property_b_cp_characterization_2407.18618.json`.

## Search evidence

The exact arXiv id, title, phrase `Characterize the property (B) of C_p(X)`,
and citation trail were searched.  The supporting paper's introduction names
the source problem and says, "In this note we settle this question," followed
immediately by Theorem 1.1.
