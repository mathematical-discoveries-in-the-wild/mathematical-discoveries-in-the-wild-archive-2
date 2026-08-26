# Exact SD-Tuple Classification

Status: `candidate_full_solution_likely_valid`

Source: Benjamin Passer, *Shape, Scale, and Minimality of Matrix Ranges*,
arXiv:1803.09212, Definition 2.5 and the conjectural discussion after (2.27)
(source PDF pp. 7 and 11).

## Claimed contribution

For every positive tuple `(a_1,...,a_d)`, the packet proves

`(a_1,...,a_d) is an SD-tuple iff sum_i 1/a_i <= 1`.

Therefore the uniform SD-constant is `U(d)=d`.  In particular, for every
`d>=2`, the tuple `(sqrt(d),...,sqrt(d))` satisfies the reciprocal `l2`
condition proposed in the source but is not an SD-tuple.

This fully resolves the precise SD-tuple classification question.  It does
not resolve the source's much broader Problem 2.3 for arbitrary convex
factors and target sets.

## Proof mechanism

Minimal matrix-convex membership over a product of diamonds has a product-
vertex POVM representation.  Coarse-graining its signs shows that an SD
inclusion would make `d` POVMs jointly measurable while each dominates
`a_i^{-1}` times a chosen rank-one PVM.  A trace witness bounds the total
dominated sharp weight by the largest norm of a transversal projection sum.
Choose the PVMs from mutually unbiased bases in arbitrarily large prime
dimension.  Gershgorin's theorem makes that norm at most
`1+(d-1)/sqrt(p)`, so passage to large primes forces
`sum_i 1/a_i <= 1`.  The converse is Corollary 2.25 of the source.

Whenever the reciprocal sum is greater than one, the proof also gives an
explicit finite failure witness: any sufficiently large odd prime dimension
works.

## Packet contents

- `solution_packet.pdf`: full proof and review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/sd_definition_crop.png`: rendered source definition.
- `figures/sd_question_crop.png`: rendered source bounds and conjecture.
- `code/verify_sd_tuple_mub.py`: independent MUB and norm-bound verifier.
- `code/verification_output.txt`: saved PASS output.
- `VERIFIER_REPORT.md`: adversarial step-by-step review.
- `main.tex`: packet source; build intermediates and rendered pages are under
  `tmp/`.

## Reproduce the verification

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1803.09212_exact_sd_tuple_l1_characterization/code/verify_sd_tuple_mub.py \
  --suite
```

## Human-review focus

Check the finite-polytope POVM representation, the signed-to-unsigned
coarse-graining lemma, and the product/maximal matrix-convex membership of
the MUB PVM tuple.  The bounded novelty search through 2026-08-13 found no
prior exact classification; novelty remains plausible rather than certified.
