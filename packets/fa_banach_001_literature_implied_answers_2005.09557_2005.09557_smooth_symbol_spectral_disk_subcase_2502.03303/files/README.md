# Smooth-symbol partial answer to the spectral open-disk question

Status: `literature_implied_answer (partial smooth-symbol subcase)`

Original question:

- E. Abakumov, A. Baranov, S. Charpentier, and A. Lishanskii,
  *New classes of hypercyclic Toeplitz operators*, arXiv:2005.09557.
- PDF page 3, immediately after the spectrum formula: does hypercyclicity of
  `T_Phi` imply `sigma(T_Phi) intersect D != empty`?

Supporting theorem:

- E. Fricain, S. Grivaux, and M. Ostermann,
  *Hypercyclicity of Toeplitz operators with smooth symbols*,
  arXiv:2502.03303.
- Theorem 3.2, PDF page 14: under hypotheses (H1)--(H3), every connected
  component of the interior spectrum of a hypercyclic Toeplitz operator meets
  the unit circle.

## Identification

For a source symbol `Phi(z)=R(1/z)+phi(z)` of degree `N`, hypercyclicity gives
`N`-valence by the source's Proposition 1.1.  If the boundary symbol is
`C^{1+epsilon}`, has nonvanishing derivative, and has finitely many simple
self-intersections, the argument principle gives

```text
wind_Phi(lambda) = n_Phi(lambda) - N <= 0.
```

Thus the later theorem applies.  The immersed boundary has a bounded face;
crossing a regular arc from the unbounded face changes the winding from zero
to `-1`, so the interior spectrum is nonempty.  Theorem 3.2 makes one of its
components meet the unit circle.  Since that component is open, it also
contains points of the open unit disk.  Hence the original question has a
positive answer in this smooth finite-self-intersection subcase.

This implication is identified by the present run.  The supporting paper
cites and systematically compares with the original source, but does not
present this exact source question as a named corollary.

## Scope limitation

The arbitrary `phi in H^infinity` case remains open in the checked literature.
The later theorem relies on a bounded `H^infinity` functional calculus supplied
by smooth Toeplitz model theory.  Radial smoothing does not remove the
hypothesis because hypercyclicity is not stable under strong or norm
approximation.

Files:

- `solution_packet.pdf`: compact identification note.
- `source_paper.pdf`: arXiv:2005.09557.
- `supporting_paper_2502.03303.pdf`: arXiv:2502.03303.

Ledger:
`runs/fa_banach_001/ledger/results/2005.09557_smooth_symbol_spectral_disk_subcase_2502.03303.json`.
