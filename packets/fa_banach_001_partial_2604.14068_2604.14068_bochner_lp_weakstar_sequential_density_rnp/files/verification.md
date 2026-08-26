# Verification record

## Target match

- Source: Saurabh Dwivedi, arXiv:2604.14068, Question 3.13, page 13.
- Published DOI: `10.1007/s12044-026-00868-3`.
- Exact question: stability of weak-star sequential density under Bochner
  `L^p(mu,.)`, explicitly stated to remain open when `X*` and `X**` have RNP.
- Result: affirmative for that exact RNP subcase and all probability spaces;
  the non-atomic non-RNP case remains open.

The packet includes the 14-page original PDF and a readable full-width render
of page 13 containing the entire question.

## Proof audit: uniform sequential lifting

1. Define `|z|_s` as the infimum of `sup_n ||z_n||` over sequences
   `z_n in X` converging weak-star to `z in X**`.
2. Weak-star lower semicontinuity gives `||z|| <= |z|_s`; termwise sums give
   the triangle inequality.
3. For an `|.|_s`-Cauchy sequence, take a subsequence with successive
   `|.|_s` differences summable. Lift each difference by a sequence whose
   norm is bounded by the corresponding summable number.
4. At stage n, sum the nth terms of the first n lifting sequences. For every
   fixed `x*`, dominated convergence over the difference index proves
   weak-star convergence to the norm-limit in `X**`.
5. The same construction on tails proves convergence in `|.|_s`, so this is a
   Banach norm.
6. The identity from `(X**,|.|_s)` to the ordinary bidual is a continuous
   bijection. The open mapping theorem gives `|z|_s <= C_X||z||`, hence one
   uniform sequential-lifting constant.

## Proof audit: Bochner series

1. The two RNP assumptions give the canonical representations
   `Y*=Lq(mu,X*)` and `Y**=Lp(mu,X**)` for `Y=Lp(mu,X)`.
2. Approximate `f in Lp(mu,X**)` by simple `s_m` with error `4^-m`; the
   increments `d_m=s_m-s_(m-1)` have summable Lp norms.
3. Each finite value of each `d_m` has a weak-star lifting sequence bounded by
   `K_X` times its norm. Replacement produces simple `X`-valued functions
   `d_(m,n)` with pointwise weak-star convergence and pointwise norm
   domination.
4. Set `g_n=sum_(m<=n) d_(m,n)`. For fixed m and any `h in Lq(mu,X*)`, ordinary
   dominated convergence over `Omega` makes the pairing error tend to zero.
5. The error is bounded by `(K_X+1)||d_m||p||h||q`, summable in m. Dominated
   convergence over counting measure combines all head errors and the omitted
   tail, proving `g_n -> f` in `sigma(Y**,Y*)`.

## Atomic clause

On a purely atomic probability space, weighted rescaling identifies Bochner
Lp with a finite or countable ell_p sum. Its bidual is the corresponding
ell_p sum of `X**` without RNP assumptions. Coordinate lifts with the uniform
constant are dominated by a summable Holder product.

This clause is not claimed novel: it is an instance of the source's preceding
ell_p-sum proposition. It is included because the source's displayed
coordinate diagonal does not itself record the uniform norm domination that
weak-star convergence of the aggregate sequence requires.

## Upgrade audit

Eight routes were checked:

1. sequential approximation gauge — succeeded;
2. summable simple increments instead of a nonmetrizable one-term diagonal —
   succeeded under RNP;
3. atomic coordinate lifting — succeeded, same-paper subcase;
4. retain only RNP of `X*` — singular bidual elements remain;
5. retain only RNP of `X**` — nonrepresentable dual tests remain;
6. measurable selection — a general bidual element has no pointwise fibers;
7. finite partitions/martingales — singular components persist under
   refinement;
8. counterexamples through l1 or c0(Gamma) — obvious candidates fail the
   premise or are excluded by heredity of weak-star sequential density.

The remaining obstruction is precise and external to the proved part: lifting
singular Bochner-bidual elements that are not represented by `X**`-valued
functions.

## Novelty audit

- Four run indexes searched for the arXiv id, title, coreflexive, weak-star
  sequential density, Bochner Lp, RNP, and the exact Question 3.13 language.
- arXiv metadata query for coreflexive Banach returned only arXiv:2604.14068.
- Bounded Crossref/OpenAlex searches for weak-star sequential density plus
  Bochner Lp returned no direct result.
- OpenAlex reported zero citing works for the published source on 2026-08-11.
- R. D. McWilliams' 1970 paper on weak-star sequential density was checked at
  the metadata level; no Bochner stability theorem was located.

The search was bounded, not exhaustive. Novelty confidence is moderate.

## Artifact and human-review audit

- Source PDF has 14 pages (verified with pypdf).
- Problem image is a real render of page 13, not a transcription.
- Main LaTeX cites the source and the Bochner duality reference.
- PDF is compiled twice with all temporary artifacts confined to `tmp/`.
- Every rendered packet page is visually inspected.
- No computational verifier is used; the result is abstract and all checks
  are logical/source/artifact checks.

Recommendation: independent review of the approximation-norm completeness
argument and the double dominated-convergence diagonal. If accepted, promote
as a substantial partial answer closing the source's explicit RNP subcase.
