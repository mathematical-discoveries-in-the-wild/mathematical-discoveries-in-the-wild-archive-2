# Verification report

Verdict: `likely valid candidate partial result`.

## Exact scope

- Source conjecture: the canonical operator space on `S_0(G)` is maximal iff `G` has an open abelian subgroup.
- Proved scope: all locally compact `G` possessing a compact open subgroup; hence all totally disconnected locally compact groups.
- Additional necessary condition: maximality of `S_0(G)` forces every compact subgroup of `G` to be virtually abelian.
- Unproved scope: groups with noncompact identity component, including connected abelian sufficiency and connected nonabelian necessity in general.

## Dependency audit

1. Source Theorem 3.3: restriction `S_0(G) -> S_0(K)` is completely surjective; the source defines this as complete isomorphism after quotienting by the kernel.
2. Quotients of maximal operator spaces are maximal up to complete isomorphism.
3. Source Corollary 2.5(ii): for compact `K`, `S_0(K) ~= A(K)` completely isomorphically.
4. Maximal operator structures convert the operator projective tensor product into the Banach projective tensor product.
5. Source Theorem 3.1: `S_0(K) operator_tensor S_0(K) ~= S_0(K x K)` naturally.
6. Source Corollary 2.5(ii) again: `S_0(K x K) ~= A(K x K)`.
7. Losert (1984): the natural map `A(K) tensor_gamma A(K) -> A(K x K)` is an isomorphism only if `K` is virtually abelian.
8. Source paragraph following the conjecture: a compact abelian open subgroup suffices for maximality.

The natural tensor map remains the elementary map `u tensor v -> ((s,t) -> u(s)v(t))` throughout, so Losert applies to the composed identification rather than merely to an abstract Banach-space isomorphism.

## Group-topology audit

- If `B` is open in compact open `K`, and `K` is open in `G`, then `B` is open in `G`.
- If `A` and `K` are open subgroups of `G`, then `A intersect K` is open in `G`; it is compact as a closed subgroup of compact `K`, and abelian as a subgroup of `A`.
- Van Dantzig supplies a compact open subgroup for every t.d.l.c. group.

## Upgrade audit

Eight distinct routes are recorded in the attempt and packet. The surviving barrier is the absence, outside compact-open geometry, of a completely complemented local Fourier ideal that transfers maximality from `S_0(G)` to `A(G)` or to a compact non-virtually-abelian subgroup/quotient.

## Artifact verification

- `latexmk` completed successfully; the final log has no warnings, undefined references, overfull boxes, or underfull boxes.
- `solution_packet.pdf` is a three-page A4 document and parses successfully with Ghostscript.
- All three pages were rendered at 170 dpi and inspected at original detail; text, equations, the source crop, and page boundaries are clean and legible.
- SHA-256 of `solution_packet.pdf`: `90951440ddb2dadd887337420656ebd9a721ecd1f69b405df8564a3ad66d75e6`.
- SHA-256 of `source_paper.pdf`: `dc532775b3f202d8858f6050a6646492e20fbc2037f871f3155db975a4b58270`.
- Ledger JSON validation and `git diff --check` passed before archival.
