# Verification

## Source audit

- The source question occurs at TeX lines 835--850 and PDF page 16.
- Its first display has the typo `Is T^{-1} invertible?`; the surrounding
  discussion and following proposition show that `frequently hypercyclic` is
  intended.
- Grosse-Erdmann's Corollary 17 and following paragraph on PDF page 13 give
  the invertible product characterization and retain the non-symmetric
  condition as open.
- Menet's arXiv:1910.04452 is a general-operator counterexample, not a
  bilateral weighted shift.

## Proof audit

1. Swapping an ordered pair in the published condition yields simultaneous
   bounds on `W_|n-m|` and `L_|n-m|`.
2. Fixing one point in a high-label witness set shows that a translate of
   `E_1` lies inside every prescribed simultaneous-product good set. The
   translate preserves the lower density of `E_1`.
3. For nested sets with a common lower-density bound, the diagonal selector
   `A={n:n in S_{q(n)}}` contains `S_{q(N)}` up to every prefix `N`; this proves
   both the density estimate and eventual containment in each `S_j`.
4. A positive-lower-density set can be partitioned into countably many such
   sets by assigning its `k`-th element according to the 2-adic valuation of
   `k+1`.
5. In the tail-rich theorem, one common translation preserves every
   pairwise difference. Labels tending to infinity supply the missing
   individual inverse-product convergence.
6. For the reflected inverse weights, the cumulative products are exactly
   `W'_r=1/L_r` and `L'_r=1/W_r`.
7. The tail-union corollary is a direct second application of the density
   diagonal lemma.
8. If `L_r` is eventually nonincreasing, subsequential convergence to zero
   on an unbounded set forces global convergence to zero.

## Scope audit

- No converse to the density-escape theorem is claimed.
- A single positive-density product-escape set does not control its pairwise
  differences and is not claimed to prove frequent hypercyclicity.
- Tail-richness is not claimed to follow from the published hypotheses.
- The general inverse question is already negative; only the bilateral
  `c_0(Z)` specialization is treated as open.
- Human review remains unchecked.

## Artifact audit

- `solution_packet.pdf` has 4 pages and 1,436 extracted words.
- The packet compiled with no warnings.
- All four final pages were rendered and visually inspected after the final
  build; no clipping, overlap, stale extra page, or malformed mathematics was
  found.
- Packet SHA-256:
  `35f18e85682ba8759a222a872631ce3e07ff0f710cec32ac16301b1b7fe896d7`.
- Source-paper SHA-256:
  `f5de1711f4504acb52b95dd894e642618ded060b5ac8755796b3c8cd55b61c8f`.
- Later-characterization SHA-256:
  `b9cfc1d17e67373424e8a9012d505ee614ee24435dfe5a34d87e6e14bb0cdfdf`.
- General-counterexample reference SHA-256:
  `7efd4db4fd247a4188aaf91544f38fb11d50c9b3eb58757b609acce578bd4cab`.
- Audit timestamp: `2026-08-13T14:45:07Z`.
