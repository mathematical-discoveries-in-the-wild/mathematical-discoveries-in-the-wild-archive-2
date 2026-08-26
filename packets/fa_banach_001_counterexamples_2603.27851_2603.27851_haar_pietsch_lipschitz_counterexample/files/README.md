# Counterexample to Haar domination for Lipschitz p-summing maps

- Source: Alexandre Bispo, Renato Macedo, and Joedson Santos, *A new
  criterion for the normalized Haar measure to be a Pietsch measure*,
  arXiv:2603.27851.
- Original problem: Botelho--Pellegrino--Rueda--Santos--Seoane-Sepulveda,
  arXiv:1204.5621, Section 5.
- Status: candidate full counterexample, likely valid, pending expert review.
- Agent/model: `agent_lane_14` / `GPT5.6`.

For every `1 <= p < infinity`, take `G = T`, `H = C(T,R)`, and
`u(f) = ||f||_infinity`.  The map is translation invariant.  It is Lipschitz
`p`-summing with constant one because `u` itself belongs to the unit ball of
the Lipschitz dual used in the definition.  Haar domination would imply
`||f||_infinity <= C ||f||_Lp`.  The explicit continuous peaks
`f_n(e^{it})=(1-n|t|)_+` have supremum one and `Lp` norm tending to zero, so
no Haar Pietsch domination is possible.

The proof uses no computation beyond the displayed integral and no external
theorem beyond the source definitions.
