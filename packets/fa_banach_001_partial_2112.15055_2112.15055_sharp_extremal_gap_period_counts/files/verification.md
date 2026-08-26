# Verification report

**Verdict:** PASS as a candidate partial result, likely valid, pending expert
review.

## Mathematical checks

1. The source question was checked against arXiv:2112.15055, Section 5.1,
   PDF page 21. The crop includes the complete statement and the source's
   `p-1` example.
2. Corollary 4.5 and Corollary 6.4 of arXiv:0810.3273 were inspected in the
   supporting PDF. They identify periodicity of the finite-gap isospectral
   torus with rational band harmonic measures and linearize shift by those
   masses.
3. For `E_s=[-1,0] union [s,1]`, continuity of equilibrium measures under
   monotone endpoint convergence gives a continuous right-band mass. Its
   limits are `1/2` as `s` decreases to zero and `0` as `s` increases to one,
   so the intermediate-value construction of mass `1/p` is valid.
4. If the constructed matrix had a smaller period `q`, the mass `1/p` would
   equal `k/q` for an integer `k`; hence `q=kp`, excluding `0<q<p`.
5. Börg's theorem supplies the nonzero-gap lower bound for least period
   greater than one. Floquet theory supplies at most `p` bands, and hence at
   most `p-1` gaps. The source gives a least-period-`p` example attaining
   `p-1`.

No numerical experiment is used as evidence.

## Literature and duplicate checks

The run indexes and a bounded arXiv/web search on 2026-08-17 used the phrases
listed in the README. No exact statement of the sharp min/max theorem was
found. The finite-gap input itself is established literature; the application
to the source's extremal question is agent-identified.

## Artifact checks

- LaTeX compilation: PASS, four pages.
- Final LaTeX log: no warning/error matches.
- PDF text extraction: PASS; theorem, exact-period argument, limitations, and
  human-review recommendation are present.
- Visual inspection: PASS on all four rendered pages; no clipping, overlap,
  or unreadable evidence text.

SHA-256:

```text
source_paper.pdf                    85a371fc9447dac0f68f72cd21401197a270aaab53f960c553a1667c4f42ecf5
supporting_paper_0810.3273.pdf      3a4a43e997ae4b0ac8be82cb846db95b2d47419714a8a8691cb02cf0583d7e37
solution_packet.pdf                 cb98242e188602e4528c040fabe9dd819928199551d0d8d9dac7922f7a99d1ce
figures/open_problem_crop.png       421f187d140d63b141cee964db2ee4e98eeefffefd7d6db3342598a5677171c9
main.tex                            e365fda710b1324d6e5df27bbfa9707afc38933c937a45c0bd8790e8099c5e4a
```

## Human reviewer focus

Confirm the endpoint-continuity argument for the right-band equilibrium mass
and that the CSZ period criterion applies to *least* period exactly as used.
Those are the only nontrivial external-theory junctions.
