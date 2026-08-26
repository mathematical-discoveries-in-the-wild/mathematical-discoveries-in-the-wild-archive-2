# Verification audit

Verdict: `literature_already_answered` (exact full negative answer).

## Exact match

- Original source: Matthew Daws, arXiv:math/0604372, Section 4, PDF page 13.
- Source question: if `X subset ell^infty(Z)` is shift invariant and its dual
  is naturally `ell^1(Z)`, must `X` equal `c_0(Z)`?
- Supporting source: Daws--Haydon--Schlumprecht--White,
  arXiv:1101.5696.
- Explicit provenance: supporting PDF page 2 says that the first named author
  asked in reference [12] whether the canonical weak-star topology is unique,
  and then says the paper answers the question negatively. Reference [12] is
  the original Daws paper.
- Mathematical answer: supporting Proposition 2.3 proves that the dual-Banach-
  algebra compatibility condition is equivalent to shift invariance;
  Theorem 3.4 constructs `F^(lambda)`; Corollary 3.5 (PDF page 10) proves that
  these give continuum many distinct compatible weak-star topologies, none
  canonical.

## Scope checks

- The constructed `F^(lambda)` are concrete subspaces of `ell^infty(Z)` and
  are preduals of `ell^1(Z)`, exactly matching the source formulation.
- The first family is isomorphic to `c_0` merely as an abstract Banach space,
  but it is not equal to the canonical concrete predual and induces a distinct
  weak-star topology. This alone refutes the source statement as written.
- The supporting paper also constructs preduals not isomorphic to `c_0`, so
  even an isomorphic-uniqueness strengthening fails.
- Requiring weak-star continuity of both product and coproduct is a stronger
  hypothesis under which canonical uniqueness does hold; it is not the source
  question.

## Search bounds

Checked on 2026-08-11:

- run registry, solution, attempt, and proof-gap indexes for arXiv:0604372 and
  core unique-predual/dual-Banach-algebra terms;
- arXiv source text for the exact question;
- arXiv:1101.5696 abstract, introduction, Proposition 2.3, Theorem 3.4,
  Corollary 3.5, and bibliography;
- exact-title and exact-phrase web searches;
- journal metadata at the Institute of Mathematics of the Polish Academy of
  Sciences and university repository metadata for the Israel Journal paper.

No prior packet for this exact source-answer pair was found in the run.

## Reviewer focus

Verify the equivalence in supporting Proposition 2.3 and the statement of
Corollary 3.5. No new proof is claimed by this packet.
