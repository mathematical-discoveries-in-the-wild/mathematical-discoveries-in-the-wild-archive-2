# Sharp spectral gap for the large-block unitary measure

Status: `candidate_full_solution_likely_valid`.

Source: Gilles Pisier, *Spectral gap properties of the unitary groups:
around Rider's results on non-commutative Sidon sets*, arXiv:1607.05674v7,
Remark 2.11 on printed/PDF page 17.

## Answer

Let `mu_{k,n}` be the conjugation average of Haar measure on the embedded
copy `U(k) -> U(n)`, and put `ell=n-k`.  If `ell <= k`, then, with respect
to the defining representation and its conjugate, `mu_{k,n}` has the sharp
spectral-gap parameters

`delta_{k,n}=ell/n`,

`gamma_{k,n}=ell(ell+1)/(n(n+1))`.

Thus, for `k=[theta n]` and `1/2<theta<1`,

`delta_{k,n} -> 1-theta` and
`gamma_{k,n} -> (1-theta)^2`.

This answers the source's stated unknown range affirmatively with exactly the
same asymptotics as in the range it calls known.  The off-target maximum is
attained by the symmetric-square representation and its conjugate, so the
constant is optimal.

## Key point

The source's Lemma 2.8(ii) is itself stated under `n-k <= k`, which is the
range called unknown in Remark 2.11; the remark reverses that inequality.
Those estimates already imply some strict spectral gap.  To obtain the sharp
constant, only one loose mixed-weight case remains.

In that case the skew Young diagram disconnects.  Writing
`alpha_i=lambda_i-1` gives

`s_{lambda/(1^k)}(1^ell)=ell s_alpha(1^ell)`.

After cancelling `s_alpha(1^ell)` in Weyl's dimension product, every
remaining factor is coordinatewise nondecreasing in `alpha`.  Its minimum is
at `alpha=(1,0,...)`, yielding the bound `ell^2/(n^2-1)`, which is at most
`gamma_{k,n}`.  The source's remaining cases are already bounded by
`gamma_{k,n}`.

## Provenance and nearby literature

The inequality-direction inconsistency and the sharp completion were not
found in the four works indexed as citing the published chapter.  The closest
later primary source is Alon--Puder, arXiv:2603.00353, which studies different,
noncentral hypergraph measures obtained by averaging coordinate-block Haar
measures.  Its mean-field spectral theorem concerns the smallest eigenvalue
of a noncentral Laplacian, not the normalized fixed-space dimension (the
Fourier coefficient) of Pisier's conjugation-averaged measure.  It neither
cites arXiv:1607.05674 nor states the result here.

## Files

- `main.tex`: complete sharp proof and novelty/scope audit.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv:1607.05674v7.
- `supporting_alon_puder_2603.00353.pdf`: closest 2026 comparison paper.
- `figures/source_question_page_17.png`: source remark and surrounding proof.
- `figures/source_lemma_2_8_page_14.png`: the source lemma's decisive
  `n-k <= k` hypothesis.
- `verify_small_ranks.py`: exact Jacobi--Trudi/Weyl sanity check in small
  ranks; it is supplementary and not used in the proof.
- `verification.md`: reproducibility and visual-QA record.

Human review recommendation: check the disconnected-skew-diagram identity,
the displayed cancellation formula in Lemma 2 of the packet, and the
exhaustiveness of the source-lemma case split.  If those pass, retain as a
full sharp answer.
