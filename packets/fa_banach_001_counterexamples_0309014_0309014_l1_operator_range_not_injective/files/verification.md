# Verification audit

Date: 2026-08-11

## Definition and source

- Remark 4.4 is on PDF page 13 of arXiv:math/0309014.  The crop contains the
  full question.
- Definition 4.1 requires the domain to be a closed subspace of `X^n` for a
  finite `n`.  The counterexample rules out injective presentations for every
  such finite order.
- This is stricter than the common arbitrary-Banach-domain definition.  Under
  that broader definition quotienting a domain by the kernel trivially gives
  an injective parametrization; the packet does not confuse the two notions.

## Quotient `Q:ell_1 ->> ell_2`

- The map `Q(a)=sum a_k u_k` is bounded with norm at most 1 because each
  `u_k` has norm 1.
- Choosing a sequence whose every tail is dense permits strictly increasing
  approximation indices.
- The residual norms decay by a factor below `1/2`, and the sum of the chosen
  coefficients is at most `2||x||_2`; hence the constructed coefficient vector
  lies in `ell_1` and its image is exactly `x`.

## Diagonal injection and range

- `J(x)_k=2^(-k)x_k` is injective.
- Cauchy--Schwarz gives
  `||Jx||_1 <= (sum 4^(-k))^(1/2)||x||_2`, so `J` is bounded.
- `T=JQ` is a bounded endomorphism of `ell_1` and
  `Range(T)=J(ell_2)`, making the range order one under the source definition.

## Exclusion of every injective finite-order presentation

- Assume `S:N->ell_1` is bounded and injective, `N` is closed in
  `(ell_1)^m`, and `S(N)=J(ell_2)`.
- `U=J^(-1)S` is a well-defined linear bijection `N->ell_2`.
- If `u_k->u` in `N` and `Uu_k->z` in `ell_2`, continuity gives
  `Su_k->Su` and `J(Uu_k)->Jz`; equality `Su_k=J(Uu_k)` yields `Su=Jz`,
  and injectivity of `J` yields `Uu=z`.  Thus the graph is closed.
- Both spaces are Banach, so closed graph makes `U` bounded and open mapping
  makes `U^(-1)` bounded.  Hence `N` is isomorphic to `ell_2`.
- Finite products of `ell_1` have the Schur property; closed subspaces and
  isomorphic copies inherit it.  The standard unit basis of `ell_2` is weakly
  null but not norm null.  Contradiction.

## Stress tests

- No complementability of `N` in `(ell_1)^m` is assumed or used.
- No continuity of `J^(-1)` in the ambient `ell_1` norm is assumed; it is
  derived for the competing parametrization by closed graph.
- The proof works over the real and complex fields.
- The result answers Remark 4.4 fully but does not answer the paper's separate
  simultaneous-smallness question for general transitive algebras.

## Reproducibility

- `main.tex` was compiled with `latexmk -pdf`.
- The PDF was rendered page by page and visually inspected for clipping,
  missing glyphs, broken references, and crop legibility.
- No computation is used as mathematical evidence.
