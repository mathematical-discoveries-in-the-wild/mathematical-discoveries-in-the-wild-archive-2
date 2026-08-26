# Complete Euclidean-Domain Classification Packet

Run: `fa_banach_001`  
Agent: `agent_lane_05`  
Model: `GPT5.6`  
Status: `partial_result_likely_valid (complete I=R^n classification)`

## Source question

- A. Chavez, K. Khalil, M. Kostic, and M. Pinto,
  *Multi-dimensional almost periodic type functions and applications*,
  arXiv:2012.00543.
- Source location: page 26, immediately after Proposition 2.24.
- Local PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

The paper asks for conditions under which Bohr `B`-almost periodicity, or
Bohr `(B,I intersect Delta_n)`-almost periodicity, implies strong
`B`-almost periodicity.

## Result

For `I=R^n`, the parameter condition is exact. Given any family `B` of
subsets of a Banach space `X`, the following are equivalent:

1. Every member of `B` is relatively compact.
2. For every Banach target `Y`, every continuous Bohr `B`-almost periodic
   map `R^n times X -> Y` is strongly `B`-almost periodic.
3. The same implication holds for scalar-valued maps.

Consequently:

- For all compact parameter sets, Bohr and strong notions coincide.
- For all bounded parameter sets, the universal implication holds exactly
  when `X` is finite-dimensional.
- The same exact criterion holds on the full-dimensional convex polyhedral
  cones used in the source.
- When `n>=2`, diagonal almost periods alone never give a parameter-only
  converse: `exp(i(t_1-t_2)^2)` is bounded and exactly diagonal-invariant but
  not strongly almost periodic.

## Proof mechanism

If `K=closure(B)` is compact, the map `t -> F(t,.)|_K` is a continuous
`C(K;Y)`-valued Bohr function. Banach-valued Bohr approximation supplies
coefficients on `K`, and Dugundji extends those coefficients continuously to
`X`.

If `B` is not precompact, choose a uniformly separated sequence `x_m` in
`B`, place disjoint bumps `phi_m` around it, and define

`F(t,x)=sum_m phi_m(x) exp(i m t_1)`.

This is bounded, jointly continuous, and exactly `2 pi` periodic. At `x_m`
it equals `exp(i m t_1)`. A finite trigonometric polynomial has only finitely
many frequencies, and a character-mean calculation shows its uniform error
on `R^n times B` is at least one.

## Scope

This is a complete classification for `I=R^n` and for the source's
full-dimensional convex polyhedral cones. Arbitrary additive domains may have
additional temporal extension obstructions and are not classified, so the
packet remains in `solutions/partial/` rather than overclaiming a solution of
every domain geometry.

## Novelty check

On 2026-08-09 the run indexes, local arXiv source corpus, and bounded web
searches were checked for the arXiv id, exact question, strong/Bohr
`B`-almost-periodicity terminology, relative compactness, and later metrical
or Stepanov variants. They found the source and related generalizations, but
no later answer or matching iff criterion. Novelty is plausible, not
certified.

## Verification

The proof is analytic and uses no numerical experiment. See
`verification.md` for the proof and packet audit.

## Files

- `main.tex`: theorems and complete proofs.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: source-question crop.
- `verification.md`: mathematical and rendering audit.
- `code/crop_source_page.py`: reproducible crop script.
- `tmp/`: build and rendering intermediates.

## Human-review recommendation

Check the `C(K;Y)` reduction, the vector-valued Dugundji extension, the
separated-bump construction for arbitrary non-precompact sets, the character
mean obstruction, and the application of source Theorem 2.36 to
`C(K;Y)`-valued maps on convex polyhedral cones. No conditional lemma remains.
