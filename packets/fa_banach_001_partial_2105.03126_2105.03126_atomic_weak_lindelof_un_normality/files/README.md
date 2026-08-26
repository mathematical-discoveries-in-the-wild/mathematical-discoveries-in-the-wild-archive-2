# Partial packet: weakly Lindelof atomic lattices have normal un-topology

- Source: Marko Kandic and Ales Vavpetic, *On separability of the unbounded norm topology*, arXiv:2105.03126; Positivity 27 (2023), Paper 43.
- Target: Problem 7.3 on PDF page 26 asks for conditions under which `(X,tau_un)` is normal and says the answer is unknown even for order-continuous atomic Banach lattices.
- Status: `partial_result_likely_valid`.
- Agent: `agent_lane_04`, lane 4 of 20.
- Model: `GPT5.6`.

## Result

Let `X` be an atomic order-continuous Banach lattice. If `X` is Lindelof in
its weak topology, then its un-topology is Lindelof, paracompact, and normal.
Consequently this holds whenever `X` is weakly compactly generated (WCG), and
also for the usual weakly Lindelof determined class.

There is a further mixed-band upgrade. If `X=Y direct-sum Z` is a band
decomposition where `Y` is an atomic KB-space and `Z` is atomic,
order-continuous, and weakly Lindelof in its weak topology, then `(X,tau_un)`
is again Lindelof, paracompact, and normal.

The theorem covers two genuinely new model families relative to the source:

- `c0(Gamma)` for uncountable `Gamma`, whose un-topology is nonmetrizable and
  which is not a KB-space;
- `l1(Gamma) direct-sum c0(Delta)` for uncountable `Gamma,Delta`, which is
  neither a KB-space nor weakly Lindelof in its weak topology, and whose
  un-topology is nonmetrizable.

## Proof mechanism

For atomic order-continuous lattices, Kandić--Marabeh--Troitsky proved that
un-convergence is exactly coordinatewise convergence along the atoms. The
coordinate functionals are norm-continuous, so `tau_un` is coarser than the
weak topology. Every un-open cover is therefore a weakly open cover. Weak
Lindelofness gives a countable subcover, and a regular Lindelof space is
paracompact and normal.

For the mixed theorem, the un-topology respects the band product. The KB
factor is sigma-compact in un-topology, while the other factor is Lindelof.
A sigma-compact space times a Lindelof space is Lindelof when the compact
pieces are genuinely compact, as they are here.

## Scope

This does not characterize normality for every Banach lattice, nor does it
settle every atomic order-continuous lattice. The remaining class consists of
arbitrary atomic order-continuous Banach sequence ideals that are neither KB
nor weakly Lindelof and need not admit the displayed two-band decomposition.

## Evidence and verification

- `source_paper.pdf`: original open-problem paper.
- `supporting_paper_1608.05489.pdf`: the coordinatewise un-convergence result.
- `figures/open_problem_crop.png`: full-width crop of source PDF page 26.
- `main.tex` and `solution_packet.pdf`: formal packet.
- `verification.md`: proof audit and artifact checks.
- `novelty.md`: bounded duplicate/literature search.
- `code/make_open_problem_crop.py`: reproducible crop generator.
- `code/verify_packet.py`: mechanical consistency checker.

## Human review focus

Check the topology direction in Lemma 1 (`tau_un` is coarser than weak), and
the product identification for the two complementary bands. The rest is the
standard compact-times-Lindelof and regular-Lindelof argument.
