# Verification report

Status: `candidate_partial_likely_valid`

## Exact target

- Source: arXiv:1212.1094v2, Section 8, PDF page 14.
- Open direction: weaken finite-face decomposition and formulate a stability
  result for the unit spheres in Examples 3.4--3.5.
- Result here: the finite-face assumption can be replaced by a positive
  distance between cross-site directions and unit-sphere flat directions.
  Closedness of the flat-direction set turns this into the source's qualitative
  general-position condition and covers the cylinder norm.

## Dependency audit

1. A source search for every occurrence of `finite face decomposition` shows
   that, inside the proof layer, it occurs only in Lemmas 9.10 and 9.12.
2. Those lemmas are used to prove one output: the positive lower bound in
   Lemma 9.13 between cross-site directions and flat directions.
3. The proof of Theorem 5.1 starts by invoking Lemma 9.13 for a number `2r`.
   Every subsequent line uses only `r`, site separation, compactness,
   Hausdorff direction estimates, Lemma 9.15, and Proposition 9.2.
4. Supplying `2r` as a hypothesis therefore removes the only use of finite
   faces without changing the rest of the proof.

## Proof audit

1. For compact sites separated by `eta>0`, every cross-site direction set is
   compact: it is the continuous image of a compact product under
   `(p,a) -> (a-p)/||a-p||`, together with its negative.
2. Let the original gap be `rho=2r>0`.  For site perturbations of Hausdorff
   size `Delta`, the source's direction estimate gives
   `D(hat(P_k,A_k),hat(P'_k,A'_k)) <= 4 Delta/eta`.
3. Choosing `Delta<r eta/8` leaves the perturbed gap greater than `r`.
   Separation also remains greater than twice the proof scale.
4. Lemma 9.15 supplies one margin `lambda` for all original and perturbed
   pairs with these two bounds.  Taking additionally
   `Delta<lambda/[8(1+diam(X)/epsilon)]` verifies Proposition 9.2, which gives
   Hausdorff stability of every cell.
5. The source's Theorem 7.1 and Corollary 5.2 then give bisector stability;
   the positive gap implies their no-parallel-segment hypothesis for both
   original and perturbed sites.
6. If `hat(S)` is closed and the qualitative condition holds, disjointness of
   a compact site-direction set and closed `hat(S)` on the compact unit sphere
   gives the required positive distance.
7. For `B_2 x [-1,1]`, a boundary segment lies in an exposed face.  A product
   support functional has a non-singleton face only when its planar or scalar
   component vanishes, yielding respectively a vertical generator or a
   horizontal top/bottom disk.  Hence the asserted cylinder direction set is
   exact and closed.

## Novelty audit

The run indexes and parsed arXiv corpus were searched for arXiv:1212.1094,
finite-face decomposition, flat-direction transversality, and arbitrary-norm
Voronoi stability.  No prior packet or later exact theorem with this
replacement hypothesis was found.  Novelty confidence is moderate because
the result is a sharp dependency extraction from the source proof and may be
known informally.

## Reviewer focus

Check that no hidden finite-face use remains in the source's Lemma 9.15 or
Proposition 9.2, the constants in preservation of the angular gap, and the
classification of non-singleton exposed faces of the cylinder ball.

