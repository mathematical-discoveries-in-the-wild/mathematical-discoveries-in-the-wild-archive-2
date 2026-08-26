# Verification report

## Source audit

- The downloaded arXiv:1610.02522 PDF has 17 letter-size pages and SHA-256
  `f2ed2f35f75cc792684cf8f2d6f4cf25a2b2685a13d0d448576c5d292b8d7b18`.
- PyMuPDF extraction locates Question 5.11 on PDF page 16. It asks exactly
  whether `(S_2)^omega` and `(S_omega)^omega` are `k_R`-spaces.
- The source defines `P_0` and states Lemma 3.6 on PDF page 5; its proof on
  page 6 constructs the strict closed fan showing that
  `S_omega x P_0` is not `k_R`.
- The source also explicitly uses that `S_omega` is the perfect image of
  `S_2` and that quotient maps preserve the `k_R`-property.

## Supporting-source audit

- Banakh--Gabriyelyan, arXiv:1412.2216, has 17 pages and SHA-256
  `7a654b9961854634a3530ccca0cc74c0fdee5f88d229a5d81757f1116e677606`.
  Proposition 5.11 starts on PDF page 11 and proves that a closed subspace
  of a stratifiable `k_R`-space is `k_R`. The published/source-paper
  numbering is Proposition 5.10.
- Ceder's 1961 paper has 25 PDF pages and SHA-256
  `e3d32313c49577f8b0fcb80d16f907803ca8a16a78454022f323640aeb5e1337`.
  Theorem 2.4 on PDF page 4 states that countable products of `M_i`-spaces,
  including `M_3` (stratifiable) spaces, remain `M_i`.
- Kim's 3-page note of 3 March 2026 has SHA-256
  `193baa34042366efe2b6379016005a15bd6d629d6dfcfd689aa5b99f1433242c`.
  Theorem 2.2 on PDF page 2 proves that the Arens space `S_2` is a
  1-paracomplex; the introduction recalls that paracomplexes are `M_1` and
  hence stratifiable.

## Later-literature audit

- Exact-title, exact-question, `Question 5.11`, `(S_2)^omega`,
  `(S_omega)^omega`, `k_R`, sequential-fan, Arens-space, and citation
  searches were run through 2026-08-11.
- No later paper located states a resolution of Question 5.11. The 2025/26
  paper *Weak approximation by points in function spaces and in the power
  of Arens' space* studies the WAP property of `(S_2)^omega`, not its
  `k_R`-property. Kim's 2026 note supplies only the stratifiability input.
- The source publisher page reports no citing papers. Because citation
  indexing can be incomplete, novelty confidence is moderate rather than
  high.

## Proof audit

1. In discrete Baire space, the set of sequences with support of size at
   most one is closed: its complement is witnessed by two nonzero
   coordinates.
2. Its distinguished zero point has the tail neighborhoods required in the
   definition of `P_0`, while every other point is isolated.
3. A closed countable discrete `D` in a factor gives a closed `D^omega` in
   the power, so the `P_0` copy remains closed in the ambient tail.
4. The displayed sets `D_omega={a(n,1)}` and `D_2={x_n(1)}` are both closed
   and discrete; explicit fan/Arens neighborhoods avoid them.
5. Splitting off one coordinate therefore gives closed copies of
   `S_omega x P_0` and `S_2 x P_0` in the respective powers.
6. `S_omega` is Lašnev and hence stratifiable. `S_2` is a 1-paracomplex and
   hence stratifiable. Ceder's theorem makes both countable powers
   stratifiable.
7. If `(S_omega)^omega` were `k_R`, closed heredity inside a stratifiable
   ambient space would make `S_omega x P_0` `k_R`, contradicting source
   Lemma 3.6.
8. If `(S_2)^omega` were `k_R`, the same theorem would make the closed
   `S_2 x P_0` subspace `k_R`.
9. Collapsing `C_0={infinity} union {x_n}` in `S_2` gives `S_omega`. The map
   is closed because the saturation of a closed set is either itself or
   its union with the closed `C_0`; all fibers are compact, so it is
   perfect.
10. The product of this perfect map with `id_(P_0)` is perfect and therefore
    quotient.
11. Quotient images of `k_R`-spaces are `k_R`: a compact-continuous real
    function pulls back to a compact-continuous function, becomes
    continuous, and descends by the quotient property.
12. Hence `S_omega x P_0` would again be `k_R`, the final contradiction.

No logical gap was found in this audit. The only non-elementary inputs are
the three precisely cited inheritance/stratifiability facts and the source's
own strict-fan lemma.

## PDF and render audit

- Final PDF SHA-256:
  `508aaa04335f9f2d470c2ed4e276b331429e89f4cd7e8d2dc11fd5f224aff429`.
- Final packet: 4 letter-size pages.
- Latexmk completed after two passes with no warnings, undefined
  references, overfull boxes, or underfull boxes.
- PyMuPDF reopened the final PDF and extracted nonempty text from all four
  pages.
- All four pages were rendered at 144 dpi after the final edit and inspected
  individually. The theorem, equations, section headings, citations, URLs,
  and page boundaries are legible; no clipping, overlap, broken glyphs, or
  malformed spacing was found.
