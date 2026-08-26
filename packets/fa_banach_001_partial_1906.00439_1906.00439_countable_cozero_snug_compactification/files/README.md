# Partial Result: Snug Truncs for Countably Cozero-Presented Compactifications

Status: `candidate_partial_likely_valid_needs_human_review`

Run: `fa_banach_001`  
Agent: `agent_lane_07`  
Source: Richard N. Ball, *Structural aspects of truncated archimedean vector
lattices: good sequences, simple elements*, arXiv:1906.00439; published in
*Commentationes Mathematicae Universitatis Carolinae* 62 (2021), 95--134.

## Target

Published Conjecture 6.1.4 asks whether every compactification `q:M->L` of a
Lindelof frame `L` admits a snugly embedded trunc in `E_0 q`.

The arXiv v1 formula defining snugness contains a superseded overline on `G`.
The published version correctly ranges the finite-domain intersection over all
`g in G`; this packet addresses that intended and published statement.

## Result

The conjecture holds for spatial compactifications with a countable cozero
presentation. More precisely, let `(X,*)` be compact Hausdorff pointed and let
`Y` be a dense pointed subspace. Suppose the image sublocale of

    q: O_*(X) -> O_*(Y)

is the intersection of a decreasing sequence of cozero open sublocales
`U_n -> O_*(X)`. Then `q` admits a snugly embedded trunc `G` in `E_0 q`.

The construction is explicit. If `U_n={h_n>0}`, define an increasingly
dominant pole scale by

    R_1=1/h_1,       R_{n+1}=R_n^2/h_{n+1}.

The ratio of every earlier scale to a later one extends by zero across the
later boundary. Consequently every finite lattice-linear expression in the
centered poles has a continuous extended-real lift: its largest nonzero pole
coefficient determines the boundary behavior lexicographically. Adding all
bounded continuous pointed functions makes the cozero/con sets generate
`O(X)`, while the pole domains intersect to the prescribed sublocale.

## Scope

This is not a proof for arbitrary compactifications of Lindelof frames. A
Lindelof subspace need not have countable cozero cofinality in a specified
compactification. The pole hierarchy has no evident continuation through an
uncountable-cofinality limit stage, where one would need a real-valued master
scale dominating all earlier incompatible infinities.

## Files

- `main.tex`: theorem and full proof.
- `solution_packet.pdf`: compiled proof packet.
- `source_arxiv_v1.pdf`: original arXiv version.
- `source_published_2021.pdf`: corrected published version containing
  Conjecture 6.1.4.
- `VERIFICATION.md`: logical, scope, literature, and artifact checks.

## Novelty check

The cheap run indexes were searched for the arXiv id, exact title, snugly
embedded truncs, Madden compactifications, and Lindelof compactification
phrases. Bounded primary-source searches found the source and its published
version but no later resolution or explicit duplicate of the countable-cozero
pole-hierarchy theorem.
