# Verification report

## Claim checked

For every Tychonoff space `X`, `(C_k(X),w)` is
Eberlein--Grothendieck if and only if `X` is hemicompact.

## Adversarial mathematical audit

- Checked that the source's Proposition 2.1 gives exactly the needed
  equivalence between EG of `(C_k(X),w)` and weak-star sigma-compactness of
  `C_k(X)^*`.
- Checked the source's compactly supported Radon representation and, in
  particular, the support-localization clause used to choose `g_n` with
  `mu_n(g_n)=1` and support inside a prescribed open band.
- Reconstructed the band induction: the lower endpoint of band `n+1` is above
  the maximum of `|u|` on every earlier selected compact support.  Therefore
  `g_j` vanishes on `supp(mu_i)` whenever `j>i`.
- Checked local finiteness independently: the band lower endpoints tend to
  infinity, while `|u|` is locally bounded at every point.  Thus the weighted
  sum of the `g_n` is a genuine continuous function even when its coefficients
  are unbounded.
- Checked the scalar recursion: because `mu_n(g_n)=1`, the coefficient `c_n`
  can make the finite partial evaluation equal to `n`; every later summand is
  zero on `supp(mu_n)`.  Compactness of the measure family then contradicts
  unbounded evaluation at the resulting single function.
- Audited the topology step: the closed Dirac copy of `X` inside a
  sigma-compact dual makes `X` sigma-compact.  A Tychonoff sigma-compact space
  is Lindelöf and paracompact; every functionally bounded subset of a
  paracompact Hausdorff space has compact closure.  The packet includes a
  direct proof using pseudocompactness, normality, and Tietze extension.
- Checked that finite unions turn an arbitrary compact cover of the dual into
  an increasing compact cover, and hence make the support envelopes
  increasing.
- Checked the cofinality diagonal: if compact `K` is not contained in any
  `H_n`, the positive series `mu=sum 2^{-n}delta_{x_n}` is a Radon probability
  supported in `K` and satisfies `|mu(f)|<=sup_K|f|`; hence it is continuous
  on `C_k(X)`.
- Because every selected point is a positive atom, every `x_n` belongs to
  `supp(mu)`.  If `mu in A_N`, then `supp(mu) subset H_N`; but for `n>=N`,
  `H_N subset H_n` and `x_n notin H_n`.  This is the required contradiction.
- Checked that no first-countability, sequence convergence, separability,
  local compactness, or full-support measure on an arbitrary compact space is
  smuggled into the proof.

## Counterexample audit

The tempting stronger lemma that every weak-star compact family has compact
total support fails on general pseudocompact spaces.  The proof does not use
that false statement: it first obtains functional boundedness and only then
uses sigma-compactness forced by EG to invoke the `mu`-space property.

Compact spaces without strictly positive measures also cause no issue.  The
diagonal uses a countable atomic probability whose selected atoms, not all of
`K`, are required to lie in its support.

## Novelty audit

- Searched all four cheap run indexes for arXiv:2206.10684, the title,
  hemicompactness, and weak-star support terminology; no matching result or
  attempt existed.
- Exact-problem, exact-title, notation, author, and support-lemma searches
  through 2026-08-13 found no later explicit solution.
- Search results included the source paper and slides that still state only
  the first-countable theorem, plus unrelated later citations.
- Novelty confidence is substantial but provisional; a specialist topology
  literature review is still recommended.

## Packet/render QA

- The source PDF is the official 20-page arXiv PDF.
- The evidence crop uses full page width and contains the whole statement of
  Problem 2.6 plus the sentence delimiting the source's first-countable result.
- The final packet was compiled twice with fatal-error checking, text
  extracted, and every rendered page visually inspected.

## Verdict

Candidate full solution, likely valid.  Recommended verifier focus: the
support-localization lemma's triangular construction and the paracompact
`mu`-space implication.
