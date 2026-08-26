# Two-point counterexample to the nonlinear factorization converse

Status: candidate_counterexample_likely_valid.

Source: Geraldo Botelho, Mariana Maia, Daniel Pellegrino, and Joedson
Santos, *A unified factorization theorem for Lipschitz summing operators*,
arXiv:1902.02569, Open problem after Corollary 2.5, PDF page 6.

## Result

The converse of Corollary 2.5 is false for `p=2`. In fact it is false for
every `1 <= p < infinity`, even when:

- `K` is a singleton;
- `X` and the complete metric target `Y` both have two points; and
- the summing constant is exactly one.

Take `K={*}`, identify `C(K)` with `R`, put `X=Y={-1,1}` with the inherited
metric, and define `Psi(x)=x` and `u(x)=x`. For every finite family of pairs,
the two sides of the defining `Psi`-Lipschitz `p`-summing inequality are
identical.

There is only one probability measure on `K`, and `L_p(K)` is `R`. The
converse would therefore produce a Lipschitz map `R -> {-1,1}` fixing both
`-1` and `1`. This is impossible because a continuous image of connected
`R` is connected.

## Scope and novelty

This answers the source problem exactly as stated for arbitrary metric
targets. It does not settle a strengthened variant in which the target is
required to be a Banach space or an absolute Lipschitz retract.

On 2026-08-09, the run registry, solution/attempt/proof-gap indexes, and the
local parsed arXiv corpus were searched using the source id, title, exact open
problem phrase, and Lipschitz 2-summing factorization terms. Bounded web
searches used the same exact phrase and close variants. They found the source
and papers citing it, but no later answer or matching two-point counterexample.
Novelty confidence is moderate pending expert review.

## Files

- `main.tex`: self-contained counterexample packet.
- `solution_packet.pdf`: rendered review copy.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source open problem on PDF page 6.
- `figures/corollary_context_crop.png`: Corollary 2.5 context.
- `VERIFICATION.md`: proof, literature-search, and render audit.
