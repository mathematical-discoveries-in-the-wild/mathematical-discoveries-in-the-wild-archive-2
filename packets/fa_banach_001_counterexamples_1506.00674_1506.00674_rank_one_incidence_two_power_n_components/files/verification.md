# Verification report

Candidate: `1506.00674_rank_one_incidence_two_power_n_components`

## Claim checked

For `M>=2` and `N>=1`, the complex incidence variety from Edidin's proof has
exactly `2^N` irreducible components when all projection ranks are one.  If
`r>=1` of the ranks are one, it has at least `2^r` irreducible components.

## Verdict

`likely valid`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Rank-one parametrization | valid | A symmetric rank-one idempotent has nondegenerate image line and equals `uu^T/(u^Tu)`. |
| Incidence factorization | valid | Direct multiplication gives `y^TP_ux=(u^Ty)(u^Tx)/(u^Tu)`. |
| `2^N` closed cover | valid | Over a field, every product is zero iff at least one factor is zero; the alternatives are the polynomial conditions `P_i x=0` and `P_i y=0`. |
| Irreducibility of each piece | valid | Each one-sided incidence space is a nonempty open subset of an iterated projective bundle over projective space; a pattern piece is a product of two such spaces. |
| Exact component count | valid | The real witness `x=e_1,y=e_2`, with image line `e_2` for an `x` choice and `e_1` for a `y` choice, belongs to exactly one pattern piece.  Hence no piece is contained in another, and the finite irreducible cover is the component decomposition. |
| Dimension | valid | The base contributes `M-1`; each constrained line contributes `M-2`.  Every piece has dimension `2M-2+N(M-2)`, equal to the source formula for `k_i=1`. |
| Mixed-rank corollary | valid | Coordinate projections of every allowed remaining rank make `e_2^TPe_1=0`; the same pattern-separating witnesses force at least `2^r` distinct ambient components. |

## Counterexample search

The exact-rational checker was run for dimensions `2` through `6`, several
integer vectors, and all rank-one patterns through `N=4`.  It verified
idempotence, symmetry, the factorization identity, and uniqueness of every
pattern witness.  This is a sanity check, not the irreducibility proof.

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1506.00674_rank_one_incidence_two_power_n_components/code/check_rank_one_factorization.py
```

## External dependencies

- Edidin, arXiv:1506.00674, for the definition and exact source uncertainty.
- Standard facts about projective bundles and irreducible varieties.  The
  packet gives the needed bundle construction explicitly.

## Gaps

- No gap found in the component proof.
- Novelty is bounded rather than exhaustive: exact-phrase and close-variant
  web/arXiv searches were performed, but no citation-database proof of novelty
  is claimed.

## Confidence

Score: `96/100`.

The algebraic factorization is exact, and the component proof reduces to a
standard projective-bundle argument.  Human review should focus on the claim
that the rank-one projection parametrization is an isomorphism of varieties
and on the mixed-rank component-count corollary.

## Human review recommendation

`send to human`
