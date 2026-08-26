# Complete classification of geometrically regular weighted shifts

Status: **candidate full solution; likely valid; human review recommended**

## Source and target

- Chafiq Benhida, Raúl E. Curto, and George R. Exner,
  *Geometrically regular weighted shifts*, arXiv:2309.05888v2.
- Target: Conjecture 1.3, official v2 PDF page 7.
- Family:

      alpha_n^2 = (p^n+N)/(p^n+D),
      p>1,  -1<N,D<1.

The conjecture asks for the missing necessity directions in the sector
classification for Bernstein interpolation, moment infinite divisibility
(`MID`), subnormality, and complete hyperexpansivity.

## Full result

The packet proves all three parts of Conjecture 1.3 and strengthens them to
the following global equivalences:

1. The squared weights are interpolated by a Bernstein function iff
   `D=N` or `N<D<=0`.
2. The shift is `MID` iff `D=N` or `N<0` and `N<D<=-N`.
3. The shift is subnormal iff
   `D=N`, or `N<=0` and `D>N`, or
   `0<N<D` and `D=p^k N` for an integer `k>=1`.
4. The shift is completely hyperexpansive iff
   `D=N`, or `N<0` and `pN<=D<N`.

These conditions exactly fill the source's sector diagram.

## Proof mechanism

Put `q=1/p`.  Two explicit signed atomic Hausdorff representations settle
the difficult necessity statements.

For `N<D` and `D>0`,

    1-alpha_n^2
      = sum_{k>=1} (D-N)(-D)^(k-1)(q^k)^n.

The atom at `q^2` is negative.  Uniqueness of compactly supported moment
measures therefore prevents `1-alpha^2` from being completely monotone, so
`alpha^2` is not completely alternating and cannot be Bernstein-interpolated.

In Sector III, write `N=-u`, `D=v`, with `0<=u<v`.  Then

    -log(alpha_n^2)
      = sum_{k>=1} [u^k+(-1)^(k+1)v^k]/k * (q^k)^n.

Every even coefficient is negative.  The same uniqueness argument rules out
complete monotonicity and hence `MID`.  On the boundary `v=u`, the even
coefficients vanish, explaining exactly why `MID` survives there.

Finally, if `delta_n=gamma_{n+1}-gamma_n` for the moment sequence `gamma`,
complete hyperexpansivity requires `delta` to be completely monotone and thus
log-convex.  The source's exact ratio

    delta_(n+1)/delta_n
      = (1/p)(p^n+N)/(p^n+D/p)

can be nondecreasing only if `D>=pN`.  Together with the necessary
expansivity condition `D<N`, this is exactly Sector VIIIA, which the source
already proves sufficient.

## Verification

Run from the repository root:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2309.05888_complete_grws_sector_classification/code/verify_q_series.py
```

The script symbolically checks the two q-series coefficient formulas, the
weight-monotonicity factorization, and the complete-hyperexpansivity ratio
factorization.  Hausdorff uniqueness and the operator-theoretic implications
are proved in `main.tex`; they are not inferred from finite computation.

See `verification.md` for the proof audit and artifact hashes.

## Novelty check and limitations

The local run registry, attempts, solution index, and cheap full-source index
were searched for the exact arXiv id, title, Conjecture 1.3, and the core GRWS
sector terms.  Fresh web/arXiv searches on 2026-08-13 used the exact title,
exact conjecture label, Sector II/III phrases, `MID`, `Bernstein`, and
`Sector VIIIA`.

The closest later sources were the same authors' safe-quotients paper
arXiv:2312.06390/JMAA 538 (2024) and signed Berger-charge paper
arXiv:2405.15000 (published 2025).  Both repeat the partial GRWS classification
but do not claim the necessity arguments here or solve Conjecture 1.3.  The
official arXiv v2, updated in 2026, still states the conjecture.  This is a
bounded search, so novelty confidence is moderate.

The Bernstein statement follows the source's intended convention: it concerns
the squared-weight sequence, as explicitly stated in Theorem 1.2 and the
discussion immediately following it.  The conjecture's shorthand “no
`alpha` is interpolated” is read in that established sense.

## Human-review recommendation

Prioritize:

1. the compact signed-measure uniqueness lemma;
2. the equivalence between Sector-III `MID` and complete monotonicity of
   `-log(alpha^2)`;
3. the use of log-convexity of `delta` to make `D>=pN` necessary;
4. the assembly of the source's Theorems 2.8, 2.9, 2.10, and 2.16 into the
   global subnormal classification.

No unproved dependency is currently known.

## Packet contents

- `main.tex`, `solution_packet.pdf`: theorem and complete proof.
- `source_paper.pdf`: official 26-page arXiv-v2 PDF.
- `figures/open_problem_crop.png`: real full-width crop of the proved sector
  list and all of Conjecture 1.3.
- `code/verify_q_series.py`: exact symbolic checker.
- `code/make_open_problem_crop.py`: reproducible source-page renderer/cropper.
- `verification.md`: verifier report, novelty bounds, and hashes.
- `tmp/`: LaTeX and render intermediates.
