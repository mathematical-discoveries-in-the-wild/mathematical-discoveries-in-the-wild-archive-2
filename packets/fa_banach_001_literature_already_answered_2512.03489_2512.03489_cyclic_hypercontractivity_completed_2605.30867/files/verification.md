# Verification record

## Primary-source statements

- arXiv:2512.03489, abstract and printed pp. 1–2: the sharp result is proved
  on the `2^k` and `3*2^k` towers and the general arbitrary-order case is
  explicitly left open.
- arXiv:2605.30867, Theorem 1.1, printed p. 1: for every `n>=4` and every
  `1<p<=q<infinity`, the hypercontractive inequality holds exactly at and
  after the threshold `(1/2)log((q-1)/(p-1))`.
- arXiv:2605.30867, Theorem 1.2, printed p. 2: the word-length LSI has optimal
  constant `2` for every `n>=4`.
- arXiv:2606.02847, Theorem 1 and Corollary 2, printed pp. 2–3: independent
  sharp constant-2 LSI and the same if-and-only-if hypercontractive threshold
  for every `n>=4`.
- arXiv:2602.17248, Theorem 1.2, printed p. 3: exact `Z_3` constant from the
  unique solution of the displayed two-equation system.

## Convention checks

- Both the source and arXiv:2605.30867 use
  `psi_n(k)=min(k,n-k)` and normalized counting measure.
- arXiv:2602.17248 uses the multiplier `T_r` with `r^{psi_n(k)}`. Hence the
  source semigroup satisfies `P_t=T_{exp(-t)}`, so `t_{p,q}(3)=-log r_{p,q}`.
- The case `p=q` has threshold zero and is treated separately from the
  strict `p<q` system for `Z_3`.

## Packaging checks

- Compilation and warning scan: passed.  A clean `latexmk` build produced no
  warning, overfull/underfull-box, or undefined-reference lines in the final
  log scan.
- PDF parse/page count: passed.  Ghostscript parsed the final PDF successfully;
  the packet has three letter-size pages.
- Visual inspection of every packet page: passed.  All three rendered pages
  were inspected at high detail; equations, boxes, references, margins, and
  page breaks are legible and unclipped.
