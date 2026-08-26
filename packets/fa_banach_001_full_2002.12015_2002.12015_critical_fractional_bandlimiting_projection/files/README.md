# Critical fractional bandlimiting projection

Status: `candidate_full_solution_likely_valid`.

This packet answers the bounded-projection question in Section 8 of
Monguzzi–Peloso–Salvatori, *Fractional Paley–Wiener and Bernstein spaces*
(arXiv:2002.12015), for every critical index
`s - 1/p ∈ N_0` and `1 < p < ∞`.

The key result is

`Pi_{a,s,p} = (Delta^{s/2})^{-1} Q_a Delta^{s/2}`,

where `Q_a` is the interval Fourier projection on `L^p`. The critical
fractional Laplacian is an onto isometry from the BMO-normalized Sobolev
realization to `L^p`; compact spectral support then gives an entire
representative by Paley–Wiener–Schwartz. The projection norm is exactly the
`L^p` multiplier norm of `Q_a`, and for `p=2` the operator is orthogonal.

The packet treats both the canonical homogeneous quotient and the source's
critical BMO realization. A Taylor-normalized entire model is obtained
isometrically after bandlimiting. The separate interpolation question—whether
a preferred concrete critical normalization is the interpolation space
between neighboring noncritical spaces—is not claimed.

Files:

- `main.tex`, `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: arXiv:2002.12015.
- `supporting_realization_paper_1910.05980.pdf`: the cited critical
  homogeneous Sobolev realization theorem.
- `figures/open_problem_crop.png`: source page 23.
- `tmp/`: build and render intermediates.

Novelty check (2026-08-11): the four run indexes, exact title/arXiv id,
critical-projection phrases, the published Springer page, and visible citing
followups were searched. No later resolution of the exact question was found;
the published article still presents it as open. Novelty confidence is
moderate. Human review should focus on the distributional support lemma and
the normalization comparison.
