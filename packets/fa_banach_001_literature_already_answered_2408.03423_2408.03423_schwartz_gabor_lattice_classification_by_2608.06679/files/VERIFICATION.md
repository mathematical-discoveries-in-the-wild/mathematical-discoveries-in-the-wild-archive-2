# Verification

## Claim-to-source audit

- `source_arxiv_2408.03423.tex`, lines 115--185, contains Problem A, the
  rational-lattice reduction, Definition B of `n_Gamma`, and Theorem C with
  `covol(Gamma) < 1-(d-1)/n_Gamma`.
- The same source near its final examples says no Schwartz Gabor frame was
  known over a lattice violating that inequality.
- `supporting_arxiv_2608.06679.tex`, Theorem 1.2, gives the iff condition
  `covol(Gamma)<1` and, in the symplectically rational case,
  `nu(Gamma) >= nu(Gamma^circ)+d`.
- Its Theorem 1.3 gives the stronger obstruction in the Feichtinger algebra
  `S_0`; Theorem 1.4(e) restates the resulting nonexistence.
- Its equation (1.8) gives
  `covol(Gamma)=nu(Gamma^circ)/nu(Gamma)` in the rational case.
- Since `nu(Gamma)=n_Gamma` and the two invariants are integers, the source
  strict inequality is equivalent to the later arithmetic gap. This verifies
  that the later theorem proves sharp necessity for the source criterion.
- Its Example 1.5(ii) takes
  `M=diag(1,1,1,1/2)`, records covolume `1/2`, `nu(Gamma)=2`, and
  `nu(Gamma^circ)=1`, and notes failure of the criterion. The later
  nonexistence theorem therefore rules out every `S_0` window. Because
  `Schwartz` is contained in `S_0`, this is a counterexample to Problem A.

## Mechanical checks

Run from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Then inspect the log for undefined references, citations, and overfull boxes;
render every page of `solution_packet.pdf` and inspect all page images.

Completed on 2026-08-11: `latexmk` converged with no undefined references,
citation warnings, duplicate destinations, or overfull boxes. Both pages were
rendered at 150 dpi and visually inspected. The final PDF SHA-256 is
`3221b44ff6e665f62ffffae02812fe24019ccbb451d41f633751f9d982c30778`.

## Search record

The cheap run indexes contained no entry for arXiv:2408.03423. Exact-title,
problem-phrase, and rational-lattice searches on 2026-08-11 located
arXiv:2608.06679, posted four days earlier. Its abstract advertises an exact
classification for general phase-space lattices; source inspection confirms
that its iff condition is precisely the sharp form of the 2024 criterion.
