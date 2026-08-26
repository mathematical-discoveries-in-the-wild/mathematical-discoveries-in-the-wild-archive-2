# Higher-Dimensional Ball Frames Answered by arXiv:2607.23953

Status: `literature_already_answered`

## Source question

Kevin Hughes, Arie Israel, and Azita Mayeli, *Wave Packets and Eigenvalue
Estimates for Limiting Operators on the Disk*, arXiv:2601.21224 (2026).

On arXiv PDF page 3, after Theorem 1.2, the authors explain that their
two-dimensional construction answers Open Problem 2 from their SampTA 2025
paper only for `d=2`. The outstanding problem is to construct, in dimensions
`d>=3`, a wave-packet frame on the Euclidean ball with the stated energy
decomposition and a residual family of size

`C R^(d-1) log(R/epsilon)^J`

for some finite exponent `J`.

## Explicit later answer

The same authors' separate later paper, *Localized frames on Euclidean balls*,
arXiv:2607.23953 (July 2026), answers the problem in arbitrary dimension.
The introduction explicitly says that the paper extends the disk framework to
Euclidean balls in arbitrary dimensions.

Theorem 1.2 on arXiv PDF pages 2-3 constructs, for every `d>=2`, a unit-norm
frame for `L^2(B_d(R))` with dimension-dependent frame bounds and the required
energy decomposition. When the frequency boundary has codimension one
(`eta=1`), its exceptional-family estimate is

`#I_3 <= C M^(d-1)(boundary S) R^(d-1) log(R diam(S)/epsilon)^(sd+1)`.

After normalizing `diam(S)` this has precisely the requested form, with
`J=sd+1`. The later theorem is slightly stronger because it also permits
frequency boundaries of fractional codimension.

This is an author-explicit later resolution, not a new result from this run.

## Search evidence and scope

A bounded check on 9 August 2026 searched the run registry and cheap local
indexes for arXiv:2601.21224, then searched arXiv by the exact title, authors,
and the phrases `wave packet frame`, `Euclidean ball`, and `higher dimensions`.
The decisive match was arXiv:2607.23953. Its theorem and provenance were
verified against both the arXiv source and PDF. The higher-dimensional frame
problem recorded by arXiv:2601.21224 is fully answered; no new mathematical
result is claimed here.

Files:

- `source_paper.pdf`: arXiv:2601.21224.
- `supporting_paper_2607.23953.pdf`: the separate later answering paper.
- `main.tex`, `solution_packet.pdf`: compact literature-status note.
