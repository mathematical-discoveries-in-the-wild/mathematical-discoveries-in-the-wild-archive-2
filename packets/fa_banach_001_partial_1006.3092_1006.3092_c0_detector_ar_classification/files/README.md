# Candidate partial result: a noncompact c0 detector forces Hilbert topology

Status: `candidate_partial_result_likely_valid`

Source: Taras Banakh and Robert Cauty, *Topological classification of closed
convex sets in Frechet spaces*, arXiv:1006.3092, Section 4, Problems 1–2.

Main candidate theorem: if a complete linear metric absolute retract `X`
admits a continuous noncompact linear operator `T:X -> c0`, then `X` has SAP,
hence LFAP, and is homeomorphic to `ell_2(dens X)`.

Quasi-Banach consequence: every quasi-Banach AR with infinite-dimensional
Banach envelope is Hilbert-homeomorphic. If the envelope is finite-dimensional,
it splits off, reducing the unresolved infinite-dimensional part to a
complemented AR with trivial dual and trivial Banach envelope.

The proof replaces the source's locally convex barycentric step by a
cover-controlled Banach embedding/retraction construction available for every
complete metrizable AR. The remaining `c0` marker separation is proved by an
independent five-case audit.

Limit: this does not settle the general problems. The residual
trivial-envelope class admits no nonzero continuous linear detector into any
Banach space, so a full solution requires a genuinely nonlinear idea.

Files:

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: source page 8, both open problems.
- `VERIFICATION.md`: audit and novelty-search record.

Human-review focus: the AR approximation lemma, the two-adjacent partition of
unity, and the marker rank bookkeeping.
