# Wavelet completeness is atomic regularity

Status: `literature_implied_answer (exact conceptual characterization)`

The Wavelet Completeness conjecture in Eirik Berge,
*Interpolation in Wavelet Spaces and the HRT-Conjecture*, arXiv:2005.04964,
Section 7 / arXiv PDF page 16, defines a group to be wavelet complete when
the coefficient spaces of all square-integrable irreducible representations
span `L^2(G)`.

Duflo--Moore theory identifies those coefficient spaces with the irreducible
subrepresentations forming the atomic part of the left regular
representation. Therefore

```text
wavelet complete  <=>  atomic regular ([AR]).
```

Keith Taylor's 2008 survey predates the source and records this established
class, noncompact examples, and the exact equivalent criteria that the Fourier
algebra `A(G)` is a dual Banach space or has the Radon--Nikodym property.
The identification is made by this packet; the older authors did not know the
later source terminology. No new theorem is claimed.

Files:

- `source_paper.pdf`: arXiv:2005.04964, with the conjecture on PDF page 16.
- `supporting_paper_taylor_AR_survey.pdf`: Keith F. Taylor's 2008 survey;
  decisive material is on PDF pages 5 and 8.
- `main.tex`, `solution_packet.pdf`: compact status note and identification.

Scope: this is an exact representation-theoretic/Fourier-algebra
characterization, not a simple structural enumeration of every [AR] group.
The separate global HRT conjecture remains open.
