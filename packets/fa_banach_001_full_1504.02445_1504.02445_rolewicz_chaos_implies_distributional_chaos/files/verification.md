# Verification report

Verdict: `likely valid candidate full solution`, pending expert review.

## Mathematical audit

1. **Tail factor.** For `k>=m`, pairwise almost disjointness makes all
   coordinates `f_i(k)` distinct over `(i,k)`.  Hölder gives the exact tail
   norm `C=||(c_i)||_{p'}` (or the maximum norm for `p=1`).  The tail is a
   factor because every strictly increasing self-map of `N` satisfies
   `f_i(k)>=k`.  A hypercyclic factor cannot have operator norm at most one,
   so `C>1`.
2. **Escape from the exceptional prefix.** If the `T*`-orbit of an initial
   coordinate functional never reaches the tail, its cyclic span is a
   nonzero finite-dimensional invariant subspace.  The corresponding
   finite-dimensional factor would inherit a dense orbit, contradicting the
   standard impossibility of finite-dimensional hypercyclicity.
3. **No hidden collisions.** Equal-depth descendants of distinct starting
   rows are disjoint.  Once a path reaches an index at least `m`, distinct
   continuation words are also disjoint.  Thus an escape coefficient
   `beta_k` is simply multiplied by `c_sigma`; no unaccounted cancellation is
   possible after escape.
4. **Right inverse.** Duality gives a vector of norm
   `(|beta_k| C^(N-r_k))^{-1}` pairing to one with row `k` of `T^N`.
   Disjoint supports make these columns a bounded operator `R_N`, with
   `T^N R_N=I` and `||R_N||<=K C^{-N}<1` for large `N`.
5. **Shadowing.** For `A R=I`, `||R||<1`, the convergent correction series
   `x_0 + sum R^(j+1)e_j` traces every positive pseudo-orbit.  A direct
   `N`-block estimate transfers positive shadowing from `T^N` to `T`.
   Positive shadowing trivially implies finite shadowing.
6. **Final implication.** Bernardes--Peris, arXiv:2305.02714, Theorem 11 is
   stated for continuous linear operators on Fréchet spaces and says that
   Devaney chaos plus finite shadowing implies dense distributional chaos.
   It therefore applies to `ell_p` without a compactness mismatch.

## Computational check

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1504.02445_rolewicz_chaos_implies_distributional_chaos/code/verify_right_inverse.py
```

The script uses exact rational arithmetic for two disjoint branches, depth
four, and eight starting rows.  It checks pairwise disjoint column supports,
the exact identity `T^N R_N=I`, recovery of a nontrivial rational vector, and
the predicted contracting column norm.  This is a sanity check of the
normalization, not evidence replacing the general proof.

## Adversarial checks

- The compact-space theorem arXiv:1609.03168 was rejected as the decisive
  final step after its phase-space hypothesis was checked.  The packet uses
  the later linear Fréchet-space theorem instead.
- Zero coefficients cause no problem: hypercyclicity forces the dual norm
  `C` of the remaining coefficient vector to exceed one.
- The argument covers finite coincidences and cancellations before the tail;
  it does not assume the source paper's nonzero condition.
- The conclusion is conditional only on the exact hypothesis in the source
  conjecture (Devaney chaos), not on the source paper's separate construction
  theorem.

## Novelty audit

Search date: 2026-08-12.  Sources: arXiv full-text/web search and the run's
`registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and
`proof_gaps/index.tsv`.  Search phrases included the exact title and id,
“Rolewicz-type chaotic operators distributionally chaotic”, “Rolewicz-type
shadowing”, “finite shadowing”, “weighted pseudo-shifts”, and “generalized
backward shift shadowing distributional chaos”.  The search found the source,
compact-space shadowing results, and Bernardes--Peris 2023, but no explicit
answer to the source conjecture and no occurrence of the contracting-power
right-inverse argument for this almost-disjoint family.

Novelty confidence: moderate.  Mathematical confidence: high, subject to an
expert checking the escape-coefficient lemma and the `T^N`-to-`T` shadowing
transfer.

Human-review recommendation: **prioritize review**; this is a short full
resolution with a stronger dense-chaos conclusion.
