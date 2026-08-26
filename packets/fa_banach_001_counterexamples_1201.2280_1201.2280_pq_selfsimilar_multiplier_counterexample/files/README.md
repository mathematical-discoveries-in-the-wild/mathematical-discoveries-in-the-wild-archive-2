# The `p != q` selfsimilar Besov multiplier question

Source: Cornelia Schneider and Jan Vybíral, *Non-smooth atomic
decompositions, traces on Lipschitz domains, and pointwise multipliers in
function spaces*, arXiv:1201.2280.

Status: candidate full counterexample in a full parameter region, likely
valid.

## Result

On the line, for every `0<q<p<=1` and `s>=1/p`, there is

```text
m in B^s_{p,q,selfs} \ M(B^s_{p,q}).
```

The function is an infinite sum with one normalized compactly supported
wavelet at every scale, with scale-`j` component placed near `2^j`.
Exponential separation makes every rescaled unit localization see at most
one component.  Smooth cutoff tests have input norm `O(N^(1/p))` but their
products with `m` have norm comparable to `N^(1/q)`, contradicting
multiplier boundedness.

Together with Nguyen--Sickel, arXiv:1703.03246, this gives the
high-smoothness phase split: for `s>1/p`, equality with the selfsimilar
space holds when `p<=q` and fails when `q<p`.

## Files

- `main.tex` -- complete proof and phase split
- `solution_packet.pdf` -- rendered proof packet
- `source_paper.pdf` -- official arXiv:1201.2280 PDF
- `supporting_paper_1703.03246.pdf` -- official later multiplier paper
- `VERIFICATION.md` -- source, proof, literature, build, and visual checks

Related attempt:

- `runs/fa_banach_001/attempts/1201.2280_pq_multiplier_selfsimilar_counterexample.md`

Ledger:

- `runs/fa_banach_001/ledger/results/1201.2280_pq_selfsimilar_multiplier_counterexample.json`

## Human review recommendation

Accept as a candidate full negative answer in the stated range.  Check the
dilated support-separation lemma, the `j<J` endpoint estimate, and the
finite-difference bound for the separated test cutoffs.
