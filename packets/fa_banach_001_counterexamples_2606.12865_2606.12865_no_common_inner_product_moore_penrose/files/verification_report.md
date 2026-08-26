# Verification report

Verified: 2026-08-17

## Mathematical checks

- Exact SymPy regression: `PASS`.
- Verified `phi^2=phi+1` and `delta*phi=-1`.
- Verified `beta_2(T)=diag(0,1)` and `T beta_2(T)=0`.
- Verified `S=2T*-T*^2T=[[a delta,2],[0,0]]`.
- Verified `ST=diag(1,0)`, `TS=[[-1,2a],[a delta,2]]`.
- Verified `TST=T` and `STS=S`.
- Verified that `(ST)^*G=G(ST)` forces the off-diagonal entry of a
  Hermitian `G` to vanish.
- Verified that the remaining equation is `delta*y=2*x`, inconsistent with
  `G=diag(x,y)>0` because `delta<0`.

## Build and artifact checks

- `latexmk -pdf -interaction=nonstopmode -halt-on-error`: PASS.
- LaTeX warnings, undefined references, overfull boxes, and underfull boxes:
  none in the final log.
- PDF pages: 3.
- Final PDF SHA-256:
  `5b6e0cc0e8f401a78a5101c891433768f7febd8930b5df3d761ff8094f09529f`.
- All three pages were rendered from the final PDF at 150 dpi and visually
  inspected.
- Source paper is present and the Question 6 crop was checked against PDF
  page 17.

## Literature/novelty check

The four run indexes, current arXiv record, exact title/question searches, and
variants involving 2-partial isometries, Moore--Penrose inverses, and changed
inner products were checked on 17 August 2026. The source remains arXiv v1 and
no later answer was found in this bounded search.
