# Verification record

## Mathematical checks

1. For every irreducible unitary corepresentation `U^alpha`, the slice
   `A_alpha=(id tensor phi)(U^alpha)` is a contraction, and convolution turns
   into matrix multiplication. Hence the transform of `phi^{*n}` is
   `A_alpha^n`.
2. Unit-circle eigenvalues of a finite-dimensional contraction are semisimple;
   their eigenspaces are mutually orthogonal and reducing. The remainder has
   spectral radius below one. This proves the displayed block asymptotic.
3. The coefficient Hopf *-algebra is norm dense in `C(G)`. Since all states
   have norm one, convergence of all Fourier matrices implies weak-star
   convergence on the whole C*-algebra.
4. The closure of the simultaneous peripheral-phase powers in the product
   torus is a compact group. Nets realizing its points, weak-star compactness
   of the state space, and Fourier uniqueness give exactly one state per group
   point. Orthogonality of the spectral projections proves the convolution
   law.
5. Cesaro averaging kills every peripheral phase other than one and every
   strict-disk spectral component. Its limit has Fourier matrices
   `P_{alpha,1}`, is idempotent, and is absorbing for the cluster group. It is
   generally **not** the cluster-group identity, whose Fourier matrices are
   the sums of all peripheral spectral projections. The two coincide exactly
   in the ordinary-convergence regime.
6. Convergence of a scalar sequence `lambda^n` on the unit circle forces
   `lambda=1`, proving the ordinary-power criterion in both directions.
7. Haar has Fourier transform zero on every nontrivial irreducible block.
   Therefore convergence to Haar is equivalent to absence of peripheral
   spectrum on every nontrivial block.
8. On a coefficient polynomial, convolution-map convergence is
   finite-dimensional norm convergence. Contractivity and Peter--Weyl density
   extend this point-norm to `C(G)`. The Schwarz inequality and Haar
   preservation make the maps contractions on the Haar GNS `L^2` space, where
   coefficient density gives strong convergence.
9. Writing the Fourier matrix as the compression of the GNS-lifted unitary,
   equality in the contraction estimate proves the deterministic-vector
   characterization of every peripheral eigenpair.
10. Classical check: for `phi=delta_g`, the construction gives all point
    masses on the compact cyclic closure of `g` as the cluster group, with
    identity `delta_e`, while the Cesaro state is Haar on that closure.

## Source and literature checks

- The exact source is Uwe Franz and Adam Skalski, *On ergodic properties of
  convolution operators associated with compact quantum groups*,
  arXiv:0802.1256, Section 4. The question explicitly removes symmetry and
  points to Fourier analysis while warning that atypical idempotent states
  obstruct a literal subgroup-only answer.
- J.P. McCarthy, arXiv:2004.01234, Theorem 4.6, gives the exact finite quantum
  group criterion using proper quasi-subgroups and cyclic cosets of proper
  quasi-subgroups. It does not cover arbitrary compact quantum groups.
- Matthias Neufang, Pekka Salmi, Adam Skalski, and Nico Spronk,
  arXiv:1907.07337, study fixed points and limits of Cesaro averages for
  contractive quantum measures on locally compact quantum groups. The bounded
  source search found no statement there of the ordinary-power compact
  monothetic cluster group or the all-block convergence criterion packaged
  here.
- A bounded search through 2026-08-13 used the source id/title, `compact
  quantum group convolution powers`, `Fourier transform`, `peripheral
  spectrum`, `cluster point`, and the run indexes. It found finite, central,
  discrete-dual, and fixed-point/Cesaro results but no exact all-compact theorem
  matching this packet. This is not an exhaustive priority determination.

## Artifact and PDF checks

- The original source PDF is archived as `source_paper.pdf`.
- The Section 4 question was rendered and cropped as
  `figures/open_question_crop.png`; the crop was visually inspected.
- The packet was compiled with `latexmk`; every final page was rendered to PNG
  and visually inspected.
- The LaTeX log was checked for undefined references, missing citations,
  overfull boxes, and fatal warnings.

## Human review recommendation

The proof is likely valid as a full analytical classification. A specialist
should first check conventions for left versus right Fourier slicing (powers
are unaffected), the net argument realizing every product-torus phase point,
and the Haar-GNS operator extension in the chosen reduced realization. Mathematical
confidence is high. Novelty confidence is low-to-moderate: the theorem is a
short synthesis of standard Peter--Weyl and finite contraction theory, and may
be folklore even though the bounded search found no exact published statement.
