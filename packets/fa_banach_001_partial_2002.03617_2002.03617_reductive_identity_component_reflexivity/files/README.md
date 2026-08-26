# Partial solution: reductive identity component

- **Source:** O. Yu. Aristov, *On holomorphic reflexivity conditions for
  complex Lie groups*, arXiv:2002.03617, Conjecture 1.5.
- **Result:** Conjecture 1.5 holds when the identity component is connected
  linearly complex reductive, with no restriction on the number of
  components.
- **Status:** `partial_result_likely_valid; human_review_needed`.
- **Model:** `GPT5.6`.

Let `G` be a compactly generated complex Lie group and suppose `G_0` is
connected linearly complex reductive.  The packet proves

```text
O(G) is holomorphically reflexive
    iff
the Banach-algebra linearizer of G is trivial.
```

The new mechanism is algebraic.  Restriction sends every exponential-type
function on `G` into the regular coordinate Hopf algebra of `G_0`.  Its image
is translation invariant, hence a Hopf subalgebra.  Trivial generalized
linearizer forces that subalgebra to have trivial common kernel.  A
coalgebra/Noetherian argument then produces a faithful finite-dimensional
coefficient representation inside the image, forcing the image to be the
whole regular coordinate algebra.  The source's restriction-density
criterion completes holomorphic reflexivity.

The packet also proves a broader criterion for any connected linear identity
component: it is enough that the **regular** restrictions have trivial common
kernel.

Scope limitation: the full conjecture remains open for identity components
with a nontrivial solvable part.  There, exponential-type functions need not
be regular, and separation by all Banach coefficients need not visibly imply
separation by regular coefficients.

Human review should focus on the algebraic Hopf-subalgebra lemma, the finite
faithful coefficient extraction, and the passage from the generalized
linearizer to the common kernel of the restriction image.

Files:

- `solution_packet.pdf` -- full proof packet.
- `source_paper.pdf` -- arXiv:2002.03617.
- `supporting_paper_1903.08080.pdf` -- reductive equality
  `O_exp(G_0)=R(G_0)`.
- `supporting_paper_2304.00507.pdf` -- density of regular functions in
  `O_exp(G_0)` for connected linear groups.
- `figures/open_problem_crop.png` -- source Conjecture 1.5.
- Ledger: `ledger/results/2002.03617_reductive_identity_component_reflexivity.json`.

