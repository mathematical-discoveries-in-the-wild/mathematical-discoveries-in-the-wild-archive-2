# Literature-already-answered packet: composite HW Bohnenblust--Hille

Run: `fa_banach_001`  
Agent: `agent_lane_15`  
Result type: `literature_already_answered`

## Result

The conclusion of arXiv:2301.01438 asks what can be said for the
Heisenberg--Weyl basis when the local dimension `K` is composite.
arXiv:2406.08509 is a direct same-author split/follow-up and answers this by
proving a dimension-free BH inequality for every non-prime `K >= 4`:

```text
||Ahat||_{2(K-1)d / ((K-1)d+1)}
    <= C(d,K) ||A||_op,
C(d,K) <= K^(2d) BH_{Omega_K}^{<=(K-1)d}.
```

The factor `K^(2d)` can be replaced by `|Sigma_K|^d`. The result is uniform in
the tensor length `n`.

## Scope caveat

The later theorem loses degree from `d` to `(K-1)d`; it does not prove the
prime-case coefficient exponent in composite dimension. It also does not
settle the source's separate question whether exponential dependence of the
quantum BH constants on degree is necessary.

## Evidence

- `source_paper.pdf`: locally compiled arXiv:2301.01438v3; the exact question
  is on PDF page 32.
- `supporting_paper_2406.08509.pdf`: locally compiled arXiv:2406.08509; the
  decisive non-prime theorem is on PDF pages 5--6, with proof in Section 3.
- Source TeX lines inspected: 1461--1464 of the decompressed source.
- Supporting TeX lines inspected: 318--330 of the decompressed source.
- The official arXiv metadata for 2406.08509 was checked on 11 August 2026; its
  comments identify the old arXiv:2301.01438v2 version and the later split.

## Files

- `main.tex`: self-contained literature-status note.
- `solution_packet.pdf`: final rendered packet.
- `source_paper.pdf`: source-question paper.
- `supporting_paper_2406.08509.pdf`: decisive answer paper.
- `VERIFICATION.md`: theorem, render, and checksum audit.

## Human review recommendation

Verify source PDF page 32 and supporting Theorem 7 on pages 5--6. In
particular, use the theorem statement's `(K-1)d` degree and note two apparent
`(K+1)d` slips later in the proof text; the packet does not rely on those slips.
