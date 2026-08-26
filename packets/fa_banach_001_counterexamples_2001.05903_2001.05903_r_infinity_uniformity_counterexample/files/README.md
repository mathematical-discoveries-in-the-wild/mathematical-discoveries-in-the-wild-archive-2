# Counterexample to uniformity for finite outer `L^p(ell^infinity)`

Status: `candidate_counterexample_likely_valid`

Source: Marco Fraccaroli, *Duality for outer L^p_mu(ell^r) spaces and
relation to tent spaces*, arXiv:2001.05903; Journal of Fourier Analysis and
Applications 27 (2021), Paper 67. The paragraph after Theorem 1.1 on PDF page
3 asks whether the norm-duality and quasi-triangle constants can be uniform
over all finite settings when `1 < p < infinity` and `r = infinity`.

## Claimed result

The answer is no for every `1 < p < infinity`.

For integers `N > k > 0`, let `X` be the collection of all `k`-subsets of
`{1,...,N}` and set

```text
E_i = { S in X : i in S }.
```

Give every `E_i` pre-measure one and let `mu` be the induced covering outer
measure. Then

```text
mu(E_i) = 1,       mu(X) = N-k+1,
sum_i 1_{E_i} = k 1_X.
```

Because the `r=infinity` outer norm is a Choquet norm,

```text
||1_{E_i}||_{L^p(ell^infinity)} = 1,
||sum_i 1_{E_i}||_{L^p(ell^infinity)} = k (N-k+1)^(1/p).
```

With `N=2m` and `k=m`, the ratio of the left side to the sum of the
individual norms is exactly `(m+1)^(1/p)/2`, which tends to infinity. Thus no
uniform quasi-triangle constant exists.

The proposed dual expression is subadditive, and the already-known uniform
outer Holder inequality bounds it above by a constant times the outer norm.
Applying it to the individual indicators shows that the reverse duality
constant also grows at least as a fixed multiple of `(m+1)^(1/p)`. Therefore
the open uniformity question for both parts (ii) and (iii) has a full negative
answer.

## Verification

The set-cover identity is elementary: a family indexed by `I` covers `X` iff
every `k`-subset meets `I`, iff the complement of `I` has fewer than `k`
elements. The included checker enumerates all generator subfamilies for
`2 <= N <= 10` and verifies the incidence and cover formulas exactly:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2001.05903_r_infinity_uniformity_counterexample/code/verify_set_cover_example.py
```

The computation is only a sanity check; the packet contains a proof for all
`N`, `k`, and `p`.

Verifier focus:

- Confirm that the covering construction is an outer measure allowed by the
  source and is finite and positive on every singleton.
- Confirm the identity `mu(X)=N-k+1`.
- Confirm that failure of the uniform quasi-triangle inequality forces failure
  of the reverse uniform dual estimate using the source's outer Holder half.

## Novelty and scope

A bounded search on August 9, 2026 covered the four local lightweight indexes,
the exact arXiv id and open-question phrase, combinations of `outer L^p`,
`ell^infinity`, `Choquet`, `finite outer measure`, `uniformity`, and
`triangle inequality`, Fraccaroli's later outer-space papers and current
publication list, and his 2022 thesis. The thesis repeats that this exact
endpoint remains open. No later proof or counterexample was found.

The construction settles exactly the arbitrary finite-setting question. It
does not contradict the source's positive result for the geometrically
structured upper half-space setting, and it does not seek the optimal growth
in the cardinality `|X|`.

Human review recommendation: send to an expert in outer measure spaces or
capacitary integration. The argument is short; the main audit point is the
duality implication, while the direct quasi-triangle obstruction is entirely
elementary.

Files:

- `source_paper.pdf`: arXiv:2001.05903.
- `figures/open_problem_crop.png`: source PDF page 3.
- `main.tex`, `solution_packet.pdf`: complete counterexample packet.
- `VERIFICATION.md`: independent step audit.
- `code/verify_set_cover_example.py`: exhaustive small-instance check.
