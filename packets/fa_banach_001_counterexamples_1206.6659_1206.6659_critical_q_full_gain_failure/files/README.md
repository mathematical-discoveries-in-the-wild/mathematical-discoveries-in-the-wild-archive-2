# The critical `q=1` velocity-averaging threshold is sharp

Status: `candidate_full_counterexample_likely_valid_human_review_needed`

Source: Diogo Arsénio and Nader Masmoudi, *A new approach to velocity
averaging lemmas in Besov spaces*, arXiv:1206.6659, Theorem 3.2 and the open
question immediately following it (PDF page 8).

## Answer

The answer is negative in general.  For every `q in (1,infinity]`, the packet
constructs real tempered distributions, compactly supported in velocity,
with the admissible parameters

```text
D=1, p=1, beta=1, a=b=0, alpha=1/2,
```

such that

```text
f in B^{0,1/2}_{1,1,q},
g=v partial_x f in B^{0,1}_{1,1,q},
```

but

```text
rho(x)=integral_R f(x,v)dv  is not in B^1_{1,q}(R).
```

Thus the full derivative asserted at the critical index for `q=1` cannot be
extended to any `q>1`; the source's arbitrarily small loss is genuinely
needed in this scale.

## Mechanism

At spatial scale `lambda_m`, place `m` shrinking velocity atoms.  Their
transported versions have uniformly bounded `B^1_{1,q}` cost after the
normalization `m^{-1/q}`, but all atoms have the same nonzero integral.
Velocity averaging therefore produces the sharp accumulation factor
`m^{1/q'}`.  A sequence in `ell^q` is then chosen so the two input mixed Besov
norms converge while the output `B^1_{1,q}` norm diverges.

## Files

- `solution_packet.pdf`: complete counterexample proof.
- `source_paper.pdf`: arXiv:1206.6659.
- `figures/open_problem_crop.png`: the source question.
- `code/sequence_check.py`: nonessential finite-truncation check of the
  convergent input and divergent output sequences.
- Attempt log:
  `runs/fa_banach_001/attempts/1206.6659_critical_q_velocity_averaging_counterexample.md`.

Human review should focus on the elementary dyadic estimate for
`a_j(v)=v 2^j psi(2^jv)` and on the tensor-product bookkeeping in the mixed
Besov norm.  No numerical claim is used in the proof.
