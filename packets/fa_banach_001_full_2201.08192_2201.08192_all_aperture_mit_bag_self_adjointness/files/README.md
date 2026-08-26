# Full result: all-aperture self-adjointness for the MIT bag cone

Status: `candidate_full_solution_likely_valid` (pending expert review)

Source: B. Cassano and V. Lotoreichik, “Self-adjointness for the MIT bag
model on an unbounded cone,” arXiv:2201.08192, published in *Mathematische
Nachrichten* 297 (2024), 1006–1041. The conjecture is Remark 2.4 on physical
PDF page 6; Appendix C gives the exact remaining scalar reduction.

The source proves essential self-adjointness for convex cones and conjectures
the same result for every aperture `0<omega<pi`. It reduces the re-entrant
range to excluding roots `lambda in [-1/2,1/2]` of

```text
(lambda+1) P_lambda^{-1}(cos omega) = P_{lambda-1}(cos omega).
```

This packet proves that the left side minus the right side is strictly
positive on the entire rectangle. A Ferrers recurrence and the
Mehler–Dirichlet formula produce an integral. For negative `lambda` its
integrand is pointwise positive; for `0<=lambda<=1/2` it is minimized at
`lambda=1/2`. The endpoint becomes
`(p+q)E(p)-qK(p)>0`, proved by pairing the elliptic-integral integrands at
`y` and `pi/2-y`. This closes the source reduction and proves essential
self-adjointness, with the conjectured `H^1` domain, for every aperture.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: self-contained proof source.
- `source_paper.pdf`: exact PDF compiled from the stored arXiv source.
- `figures/open_problem_crop.png`: rendered source-page evidence.
- `code/verifier.py`: high-precision independent checker.
- `VERIFIER_REPORT.md`: command, checks, and recorded verdict.

Novelty check: bounded searches on 2026-08-12 covered all four run indexes,
arXiv, the publisher page, exact title/conjecture text, the author pair, and
the core spectral terms. No later resolution was found. This does not
guarantee priority.

Human-review recommendation: check the source’s reduction from all modes to
the `k=0` Ferrers equation, and then equations (4.4)–(4.7) of the packet. The
verifier checks every special-function identity independently on 1,312 source
equation cases.
