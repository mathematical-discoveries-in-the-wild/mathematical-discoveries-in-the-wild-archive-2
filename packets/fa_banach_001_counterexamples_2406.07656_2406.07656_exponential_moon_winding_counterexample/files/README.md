# 2406.07656 — exponential moon winding counterexample

Status: candidate full counterexample to the entire-symbol winding-number
question, plus a sharp one-parameter classification.

Model: GPT5.6.

For `phi(z)=exp(pi i z)`, every point of `phi(D)` has winding number one,
but `M_phi` does not have the double commutant property. The image is the
exact moon domain

    {r exp(i theta): theta^2 + (log r)^2 < pi^2}.

Its inner and outer Jordan boundaries touch only at `-1`. Filling the inner
hole produces a proper larger domain `B`, and every crosscut of `B` meets
the moon. Sarason's full relative-hull criterion (which includes generators
of transfinite weak-star order) therefore proves that `phi` is not a
weak-star generator. The source paper's univalent-symbol criterion then
rules out the double commutant property.

The upgrade classifies the full family:

    M_{exp(a z)} has the double commutant property
    iff a=0 or |a|<pi.

Verification:

- `code/verify_exponential_family.py` passed 20,000 polar inverse checks.
- Five numerical boundary integrals, each with 200,001 samples, returned
  winding number one to about 1e-14.
- The script checks critical boundary contact and the supercritical
  one-versus-multiple-preimage witnesses.
- `source_paper.pdf` is a locally compiled copy of arXiv:2406.07656.
- `figures/open_question_crop.png` records the exact source passage on page 20.

Novelty: bounded run-index and exact web searches found no later resolution.
Confidence is moderate pending expert literature review, especially of the
application of Sarason's relative-hull criterion.

Ledger:
`runs/fa_banach_001/ledger/results/2406.07656_exponential_moon_winding_counterexample.json`
