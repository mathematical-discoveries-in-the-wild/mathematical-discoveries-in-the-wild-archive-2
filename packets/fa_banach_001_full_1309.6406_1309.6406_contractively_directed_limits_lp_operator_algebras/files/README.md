# Contractive direct limits preserve Lp-operator algebras

Status: `candidate_full_likely_valid`

Source: N. Christopher Phillips, *Crossed products of Lp operator algebras
and the K-theory of Cuntz algebras on Lp spaces*, arXiv:1309.6406.

Target: PDF page 35, immediately after Proposition 6.1.  The paper asks
whether a direct limit of Lp-operator algebras with contractive connecting
homomorphisms is again an Lp-operator algebra.

## Result

Yes, for every fixed `1 <= p < infinity`, the range used in the source paper.
No injectivity, isometry, nondegeneracy, separability, countability, or complete
contractivity assumption on the connecting maps is needed.

Choose an ultrafilter on the directed index set containing every final segment,
and choose an isometric Lp-representation of every stage.  An element from one
stage gives a tail family of operators at all later stages.  This family acts on
the Banach-space ultraproduct of the stage Lp-spaces.  The norm of the induced
operator is the ultralimit of the stage norms, which is exactly the direct-limit
norm from Phillips's Proposition 6.1.  The resulting representation of the
dense algebraic direct limit is therefore isometric and extends to the Banach
direct limit.  Finally, an ultraproduct of Lp-spaces is an Lp-space when
`1 <= p < infinity`.

## Prior-art boundary

Phillips's 2014 GPOTS talk summary states a theorem for direct limits whose
connecting maps are *completely contractive*, also using ultraproducts.  The
source question assumes only ordinary contractivity.  The proof in this packet
works at matrix level one and removes the complete-contractivity hypothesis.
Bounded exact-phrase, title, author, ultraproduct, and direct-limit searches on
2026-08-09 found the talk special case and later special direct-limit
constructions, but no result for arbitrary contractive connecting maps.

## Files

- `solution_packet.pdf`: theorem, proof, scope, and references.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `supporting_talk_phillips_2014.pdf`: prior completely-contractive subcase.
- `figures/open_problem_crop.png`: source page-35 question and context.
- `VERIFICATION.md`: proof audit and reviewer focus.
- `code/crop_source.py`: reproducible source-question rendering and crop.

Human review should focus on the well-defined tail representation on the
operator ultraproduct and confirm that no matrix-norm compatibility is silently
needed.  The proof explicitly uses only ordinary operator norms.
