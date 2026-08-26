# Faithful cocycle action without ordinary Podles density

Status: `counterexample`

The direct density analogue suggested after Definition 5.1 of arXiv:0807.2827
is false.  For `A = C*(S_3) = C + C + M_2` and `B = M_2`, exterior-perturb
the trivial action by a unitary that is the tensor flip on the `M_2` block and
the identity on the counit block.  The resulting cocycle action is normalized
and faithful, but its usual Podles span has distinguished block only
`M_2 tensor C1`, not `M_2 tensor M_2`.

The packet also proves the exact corrected statement for a stabilizable
cocycle action: if `beta = X alpha(.) X*` is ordinary, faithfulness is
equivalent to density of `alpha(B) X* (A tensor 1)`.

The source's phrase “some natural density conditions” is informal, and its
display (5.3) is typographically malformed.  The claimed scope is therefore
precise: a full counterexample to the unchanged Lemma 2.2 density condition,
plus a stabilizer-twisted replacement.  The example has `V = 1` and
`(epsilon tensor id) alpha = id`, so it is independent of the typo.

Files:

- `source_paper.pdf`: arXiv:0807.2827.
- `figures/source_question.png`: source question on PDF page 16.
- `main.tex`, `solution_packet.pdf`: complete construction and proofs.
- `verification.md`: algebraic and rendering checks.
