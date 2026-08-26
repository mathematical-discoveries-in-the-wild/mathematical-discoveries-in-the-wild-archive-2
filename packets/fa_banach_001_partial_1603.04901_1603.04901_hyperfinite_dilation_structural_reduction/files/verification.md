# Verification

Status: passed as a candidate partial result.

## Mathematical checks

- If every positive-time map factors through a hyperfinite von Neumann
  algebra, semidiscreteness of that algebra supplies matrix factorizations of
  each `T_t`; weak* convergence `T_t -> id_M` as `t -> 0+` then makes `M`
  semidiscrete.  With separable predual this makes `M` hyperfinite.
- A finite set of nonnegative rational times has a common denominator `d`.
  A hyperfinite discrete dilation of `T_{1/d}` realizes every requested
  `T_{m/d}` by the corresponding power of one automorphism.
- For factorial meshes `h_n=1/n!`, the compatibility relation
  `iota_n S_n = S_{n+1}^{n+1} iota_n` makes the rational-time action on the
  inductive limit independent of the chosen mesh.
- The Markov dilation identity supplies strong-star continuity on the embedded
  copy of `M`; state preservation propagates this continuity to the
  orbit-generated algebra, so the rational action extends to a real action.
- Restricting a sufficiently fine discrete dilation produces every prescribed
  finite compatible tower.  The unresolved step is an infinite compatible
  branch; an ultraproduct does not preserve hyperfiniteness in general.
- Eight focused upgrade attempts were made.  They covered the base-algebra
  obstruction, finite rational compatibility, compatible-root completion,
  finite tower construction, compactness/ultraproduct routes, and a possible
  counterexample route.  None justifies the unrestricted conjecture.

## Source verification

- The locally compiled source paper has 30 pages.
- Rendered source page 18 was visually inspected and contains Remark 3.10,
  including the exact hyperfinite-dilation question and the known Schur
  multiplier special case.

## Build and visual QA

- `pdflatex` completed repeated final passes with no warnings, overfull boxes,
  underfull boxes, undefined references, or errors in the final log.
- Final packet: 4 US-letter pages, 287718 bytes.
- All four packet pages were rendered and visually inspected.  The theorem
  statements, proofs, equations, scope boundary, references, and margins are
  clean; nothing is clipped or overlapped.
- PDF text extraction finds the title, hyperfinite-base reduction,
  compatible-root completion, and references on the expected pages.

## Artifact hashes

```text
source_paper.pdf         46d00ddf2623913e622b93d789398479a595ad80537679b56ce0471967623dfe
source_question_page.png a61eb2f81c8520828e0034ebdaaac4afb0013262d817264f5c34a681e826c026
solution_packet.pdf      a8cb94b9d1b1e95c527eddf573246bbe39c48bcd8314b3ee446ce4940ee0574b
```
