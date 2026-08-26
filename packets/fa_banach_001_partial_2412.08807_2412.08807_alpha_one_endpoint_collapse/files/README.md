# The alpha=1 Maz'ya endpoint collapses to ordinary inclusion

- Source: Tomáš Beránek, *Optimality of embeddings in Orlicz spaces*,
  arXiv:2412.08807; Mathematische Nachrichten 298 (2025), 2380--2400.
- Selected open branch: the omitted `alpha=1` case in Maz'ya domains.
- Status: `promoted_partial_likely_valid_needs_human_review`.
- Agent: `agent_lane_18`; model: `GPT5.6`; date: 2026-08-12.

The packet proves an exact endpoint theorem. For every integer `m>=1`, every
rearrangement-invariant target `Y`, and every Young function `A`,

`W^m L^A(Omega) -> Y(Omega)` for every `Omega in J_1`

holds if and only if the ordinary representation-space inclusion
`L^A(0,1) -> Y(0,1)` holds. The necessity is forced by disjoint translated
bumps on a bounded, measure-one coiled exponential horn whose isoperimetric
profile is comparable to `t`.

For the formal endpoint family `Y_q=L^{infinity,q;-1-1/q}`, this yields:

- no largest Orlicz domain for `1<=q<infinity`;
- largest Orlicz domain `exp L` for `q=infinity`.

This fully classifies the natural Lorentz--Zygmund alpha-one endpoint, but the
source leaves a broader multi-branch program, so the result is packaged as a
promoted partial rather than a complete resolution of the paper's closing
remark.

Files:

- `solution_packet.pdf`: theorem, proof, checks, and limitations.
- `source_paper.pdf`: current arXiv source paper.
- `figures/open_problem_crop.png`: exact closing open-program remark.
- `main.tex`: packet source.
