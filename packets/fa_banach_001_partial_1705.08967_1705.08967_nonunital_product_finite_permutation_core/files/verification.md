# Verification

Status: passed as a candidate partial result.

## Mathematical checks

- On a finite topological space, connected components are clopen and real
  continuous functions are exactly the functions constant on components.
- Norm and weak continuity coincide for the finite-dimensional function spaces.
- The four displayed families of equality relations are exactly the
  continuity, `C_r`, translation-orbit, and iterated-translation-orbit
  conditions in the source definition.
- The generated equality relation is stable under right multiplication by
  associativity, so every right map descends to the quotient.
- A deterministic map preserving a finite probability permutes its support:
  the support maps onto itself, hence bijectively.
- The uniform probability on a common permutation core is invariant under
  every descended right map.
- Iterated cyclic-point deletion is exact: every valid core survives, and a
  nonempty fixed point of the deletion operator is itself a common core.
- The general-product claim is explicitly not asserted.  The packet clearly
  separates exhaustive computations, randomized evidence, and the remaining
  analytic/core-lifting obstruction.

## Computational checks

- Exhaustive order-at-most-three rerun:
  - labelled semigroups: `1, 8, 113`;
  - amenable semigroup/partition candidates: `1, 15, 534`;
  - total candidates: `550`;
  - all `72,010` unordered pairs of nonunital amenable candidates had amenable
    product.
- Independent core/linear-program verifier:
  - `582` factor cases agreed;
  - `500` sampled product cases agreed.
- Local order-four extension rerun:
  - `2,235` distinct labelled associative tables containing the distinguished
    three-element subsemigroup;
  - `1,870` canonical amenable nonunital topology candidates;
  - all `1,870` self-products amenable.
- The order-four table file is generated locally by the checked-in C++ source;
  no failed external database query is used as evidence.

## Source verification

- The locally compiled source paper has 16 A4 pages.
- Rendered source page 14 was visually inspected.  It contains Proposition
  5.1(E), the exact statement that products of unital SGTs are amenable, and
  the immediate question whether unitality can be dropped even for a finite
  family.

## Build and visual QA

- The final packet LaTeX log contains no warnings, overfull boxes, underfull
  boxes, undefined references, or errors.
- Final packet: 3 US-letter pages, 163706 bytes.
- All three pages were rendered at 130 dpi and visually inspected.  The title,
  theorem statements, table, formulas, scope boundary, reference, and margins
  are clean; nothing is clipped or overlapped.
- PDF text extraction finds all three section headings, the permutation-core
  theorem, and the references.

## Artifact hashes

```text
source_paper.pdf                         72124af49e20ee1e39520013ab17f62ecb85e4459ab039f0f9c84df970618d21
source_question_page.png                 d7d91646787566c18f64f4f8c14660c547a13b2ba3c7e9a0c5ad03087783a7b8
order4_extension_tables.txt              bd90116b3402246d78a45818ae799c1fa30b427a80054a44c861abc3cc09a925
solution_packet.pdf                      bfb05ed8e19e84641cec4710f60c07d87079abf6d945a91b2a59b9187d7146f2
finite_product_counterexample_search.py  ec6dfdf353d8c2162eb8a11610a16fbc0737a78b8099aad28a9fd770e3c92c17
order4_extension_enumerator.cpp          1b59f351514f82162bd0528025c3ff06b28f8c3506445fdb4a5db64434cdb97f
order4_extension_product_search.py       bcf2b38c70e47c152450ee92b2b85a817024bc07aef2c67102951f873bc93fe2
verify_permutation_core.py               44a5c6c0c90f23ae5bb269c3c50479b4476f734d133d4cb5c521faedad110e2a
```
