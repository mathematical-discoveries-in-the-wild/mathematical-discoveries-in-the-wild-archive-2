# Davies ratio limit from the zero-threshold spectral measure

## Status

`literature_implied_answer (full for both classes in Remark C.2)`

This packet gives a positive answer to the two cases left open by Grillo,
Kovařík, and Pinchover.  The decisive spectral-measure and threshold-regularity
facts are already in Christiansen--Datchev, but that paper does not mention
Davies' conjecture or identify this application.  This is therefore an
agent-identified literature implication, not an explicit later answer and not
an originality claim.

## Source question

- G. Grillo, H. Kovařík, and Y. Pinchover, *Sharp two-sided heat kernel
  estimates of twisted tubes and applications*, arXiv:1105.0842.
- Exact location: Appendix C, Remark C.2, PDF page 22 of the current arXiv PDF.
- The source asks whether Davies' heat-kernel ratio limit holds for the
  subcritical compactly supported elliptic perturbations in Theorem 3.19 and
  for the locally twisted Dirichlet tube.

## Supporting theorem

- T. J. Christiansen and K. Datchev, *Wave asymptotics for waveguides and
  manifolds with infinite cylindrical ends*, arXiv:1705.08972.
- Exact ingredients: Sections 2.2--2.5; Lemma 2.4 (threshold regularity),
  Lemma 2.5 (generalized-eigenfunction spectral measure, PDF pages 20--21),
  and Lemma 2.6 (threshold-resonance singularity, PDF page 22).

## Identification

For either source class, the shifted operator is a self-adjoint compactly
supported perturbation of a two-ended product cylinder, with transverse
operator `-Delta^D_omega-E_1 >= 0`.  Below the first positive transverse
threshold, the continuous spectral measure is a finite sum of generalized
eigenfunction squares.

The source's fixed-point diagonal estimate `k(t,x,x) asymp t^(-3/2)` excludes
both a zero eigenvalue and a zero-threshold resonance: either would force a
nondecaying or `t^(-1/2)` diagonal contribution.  The zero-channel generalized
eigenfunctions therefore satisfy

```text
Phi_j(lambda) = lambda Psi_j + O(lambda^2).
```

Stone's formula then yields the exact fixed-point asymptotic

```text
k(t,x,y) = t^(-3/2) B(x,y) + O_{x,y}(t^(-2)),
B(x,y) = (1/(8 sqrt(pi))) sum_j Psi_j(x) conjugate(Psi_j(y)).
```

The diagonal lower bound makes `B(x,x)>0`, and fixed-point parabolic Harnack
comparison makes `B(x,y)>0` for every pair.  Hence

```text
lim k(t,x,y)/k(t,x0,y0) = B(x,y)/B(x0,y0) > 0.
```

The common exponential shift cancels for the unshifted twisted-tube
Laplacian.

## Search and scope

Cheap run indexes were searched for the arXiv id and Davies/twisted-tube/ratio
terms.  Bounded direct searches covered the exact source phrase, title, and
later cylindrical-waveguide heat and spectral asymptotics.  No paper explicitly
announcing this consequence was found.  The packet is complete for the
self-adjoint uniformly elliptic class actually stated in source Theorem 3.19
and for the locally twisted Dirichlet tube; it makes no claim for general
nonsymmetric operators or arbitrary noncompact manifolds.

## Files

- `solution_packet.pdf`: rendered proof of the implication.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:1105.0842.
- `supporting_paper_1705.08972.pdf`: decisive supporting paper.
- `verification_report.md`: normalization, hypothesis, and proof audit.
- Ledger: `runs/fa_banach_001/ledger/results/1105.0842_davies_conjecture_threshold_spectral_measure.json`.

## Human-review recommendation

Prioritize the localized Stone normalization, the black-box fit after the
`E_1` shift, and the final Harnack positivity step.  The existence of the
ratio does not depend on the displayed universal scalar normalization, but the
packet audits that factor explicitly.

