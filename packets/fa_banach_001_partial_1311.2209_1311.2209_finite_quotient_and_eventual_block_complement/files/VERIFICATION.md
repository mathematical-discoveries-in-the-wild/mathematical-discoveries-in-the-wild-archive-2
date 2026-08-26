# Verification

Status: proof internally checked; human review pending.

## Symbolic checks

The key convention was recomputed directly.  For

`eta_n=(1/N_n) sum_{r=0}^{N_n-1} delta_{r/P_n}`,

the real zero set is

`P_(n-1) Z \ P_n Z`.

Thus odd-head spectral differences and even-head spectral differences occupy
disjoint first-nondivisibility layers.  Adding a multiple of `P_(2k)` cannot
change a layer below `2k`, which validates the quotient injectivity step.

The head-tail spectrum lemma was checked on the digit product model: addition
of the head and tail digits is one-to-one almost everywhere, frequencies
`P_(2k)u` are trivial on the head grid, and for each head frequency `l` the
tail basis is only translated by `l/P_(2k)`.

## Computational guard

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1311.2209_finite_quotient_and_eventual_block_complement/code/verify_finite_quotients.py
```

The script exhaustively enumerates every normalized finite odd-head spectrum
in four quotients and checks the direct tiling by the negative canonical
even-head spectrum.  Output:

```text
radices=[2, 2, 2, 2]: checked 16 normalized spectra
radices=[2, 3, 2, 2]: checked 24 normalized spectra
radices=[2, 2, 3, 2]: checked 64 normalized spectra
radices=[3, 2, 2, 2]: checked 128 normalized spectra
PASS: 232 finite spectra, no tiling failure
```

This finite search is not used as a substitute for the proof.

## Reviewer checklist

1. Verify that distinct frequencies in a finite spectrum cannot differ by the
   support period.
2. Verify that the cardinalities of the two finite spectra multiply to
   `P_(2k)`.
3. Verify the head-tail tensor-basis argument for an arbitrary finite head
   spectrum, not only the canonical one.
4. Verify that the carry `c_r=(h_r-r)/P_(2k)` is absorbed by the exact tail
   tiling and does not affect uniqueness.
5. Preserve the stated limitation: the proof does not cover a general
   nonterminating spectral tree.
