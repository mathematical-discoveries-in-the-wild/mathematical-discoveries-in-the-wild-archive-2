# Verification report

Verdict: `candidate_partial_likely_valid`.  The packet fully removes the extra
smoothness unit for the Métivier class of arXiv:2605.02556; the source's
broader arbitrary two-step formulation remains open.

## Proof audit

- Every positive character on a step-two group has the form
  `chi(x,u)=exp(<a,x>)`, with `|a|=2 b_X`, because it annihilates the
  commutator layer.
- If a horizontal curve of length at most `r` ends at first-layer coordinate
  `x`, writing its velocity as `x/r+q` gives
  `integral |q|^2 <= (r^2-|x|^2)/r`.  Subtracting the straight path in the
  step-two endpoint formula yields
  `|u| <= C r sqrt(r^2-|x|^2)`.
- Hence the central fiber above `x` in the Carnot--Carathéodory ball has
  volume at most `C r^d2 (r^2-|x|^2)^(d2/2)`.
- On the exponentially dominant cap, `x=t e_1+z`, `t>r/2`, integration in
  `z` gives `(r^2-t^2)^((d1+d2-1)/2)`.  Setting `y=r-t` proves the character
  integral power `(d1+3d2-1)/2-2 beta`.  The complementary half-ball has an
  extra factor `exp(-b_X r)`, which absorbs its larger polynomial power.
- Cauchy--Schwarz and the source's first-layer weighted Plancherel estimate
  give the 2019 abstract assumption with
  `theta=(d1+3 d2-1)/4-beta` and `a=Q/2-beta-1/2`.
- The three abstract endpoint parameters are `sigma`, `theta+1`, and
  `a+1/2`.  Letting `sigma` decrease to `d/2` and `beta` increase to `d2/2`
  makes them tend to `d/2`, `(d+3)/4`, and `d/2`.  Since `d>=3`, their maximum
  tends to `d/2`.
- The Martini--Ottazzi--Vallarino theorem multiplies that endpoint by
  `2|1/p-1/2|`, yielding exactly `d|1/p-1/2|` and all three endpoint/interior
  mapping conclusions.

## Upgrade attempts and boundary

1. The source proof was traced to its global Claim 3; the local estimates
   already have the desired threshold.
2. An `ell^2` summation of Fourier-time pieces was explored but no weighted
   `L^1` square-function inequality justifying it was found.
3. An abelian radial necessity test indicated cap localization rather than a
   genuine extra derivative.
4. The cap estimate was proved and supplies the successful improvement.
5. The cap exponents were inserted into the full 2019 abstract theorem,
   including the `d=3` edge case.
6. The cap lemma extends to all step-two groups, but the arbitrary-group
   upgrade stops at the unavailable first-layer weighted Plancherel estimate
   up to `beta<d2/2` and the corresponding sharp local theorem.  The packet
   therefore does not claim the unrestricted question.

## Literature audit

- The exact question and Theorem 1.2 were checked in the official
  arXiv:2605.02556 PDF, source pages 3--4.
- The parameter formula was checked directly in the source of
  arXiv:1705.04752 (the 2019 Martini--Ottazzi--Vallarino paper), including its
  Paley--Wiener lemma and conditional multiplier theorem.
- Bounded primary-source searches used the exact title, arXiv id, threshold
  phrase, Métivier/drift/topological-dimension keywords, and cap terminology.
- The searches found the source, the 2019 abstract theorem, and sharp
  no-drift papers, but no later primary paper removing the extra unit in the
  drift theorem.  Novelty confidence is moderate because the source is recent
  and external expert/database review remains appropriate.

## Reproducibility and visual checks

- `code/verify_thresholds.py` uses exact rational arithmetic to check the
  parameter selection for six dimension pairs.  It includes `(d1,d2)=(2,1)`,
  where `(d+3)/4=d/2`; all assertions passed.
- `latexmk` completed after resolved cross-references.  The final log has no
  overfull boxes, underfull boxes, undefined references, or warnings.
- The packet contains three A4 pages.  Every page was rendered at 180 DPI and
  inspected at original resolution after the final source edit.  The source
  crop, theorem, cap proof, formulas, scope statement, references, margins,
  and page numbers are readable and unclipped.
- PDF text extraction confirms the optimal-form theorem, cap exponent,
  abstract parameter maximum, and arbitrary-two-step caveat.

## SHA-256

```text
c04380edd5f1a5ed23553c43aa5dec641afbbc1bc4333968e0f7ecf97e7d1906  solution_packet.pdf
e4fe68130a39434b2609f5f7540706e0c931390fc71ef94bf5c2b0fa65804836  source_paper.pdf
9141e0bc3846bab5c4df4be161476a0d24089ccdd1ff459973568d36bf49d648  figures/open_question_crop.png
a91ef72e235d88d287bd8fc687f9fb682f7e618c349f51446290ac51b0a3e48f  figures/source_dplus1_theorem_crop.png
0d30e0de061380a5420690bac6a5957335a932c835cc870f42be1c41da8f1221  code/verify_thresholds.py
```

## Human-review recommendation

Prioritize an expert audit of the horizontal-path fiber inequality, the
character-cap integration, and the identification of `(theta,a)` with
Assumption (C) in arXiv:1705.04752.  Also independently check the source's
fractional first-layer weighted Plancherel estimate in the small `d2` cases
and repeat the novelty search beyond arXiv before dissemination.
