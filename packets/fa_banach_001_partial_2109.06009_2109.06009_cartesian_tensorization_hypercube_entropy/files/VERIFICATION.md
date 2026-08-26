# Verification

## Analytic audit

The packet uses the source normalization

    E_G(f) = (2/|V|) sum_{x,y} c_xy ent_xy(f).

For the Cartesian product, splitting the ordered edge sum into the two
coordinate directions gives exactly

    E_product(F)
      = average_u E_G(F(.,u)) + average_x E_H(F(x,.)).

There is no missing vertex-cardinality factor.  Entropy tensorization follows
from the entropy chain rule and convexity of entropy under averaging.  Applying
the factor inequalities on every fiber gives the lower product bound, and
one-coordinate test functions give both upper bounds.

For K_2 with edge conductance w, the ordered edge sum counts the sole
undirected edge twice.  Thus the entropy energy is 2w times the global
two-point entropy, agreeing with the nonzero Laplacian eigenvalue 2w.

## Computational audit

Run from the repository root:

    conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/partial/2109.06009_cartesian_tensorization_hypercube_entropy/code/verify_tensorization.py

The script deterministically checks random positive functions on random
weighted graph products, exact energy decomposition, the weighted K_2
quotient, and the claimed hypercube inequality.

## Novelty check

The run indexes were searched by arXiv identifier, exact title, entropy
constant, Cartesian product, tensorization, hypercube, path, cycle, and
rectangular box.  A bounded web search using the exact title and close
Cartesian-product/tensorization phrases found the source and general
background material, but no exact statement of this graph-constant product
formula or its weighted-hypercube corollary.  The result should nevertheless
be treated as potentially folklore until expert review.

## Remaining scope

The computation through graph sizes ten found no credible counterexample for
the general path/cycle conjecture, but it is exploratory evidence only.  The
packet deliberately claims only the exact product theorem and Boolean-box
corollary.

