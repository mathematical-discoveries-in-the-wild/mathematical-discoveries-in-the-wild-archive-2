# Verification record

## Mathematical checks

1. Direct quaternion multiplication gives
   `j^*(1+i)j=1-i` and `j^*ij=-i`.
2. For `A_n^0=diag(1+i,1+i,0,...,0)`, an arbitrary quaternionic unit vector
   gives real part `a` and imaginary-vector norm at most `a`. If the value is
   in the upper complex plane, it is therefore `a+bi` with
   `0<=b<=a<=1`.
3. Conversely, every such `a+bi` is produced by squared coordinate weights
   `(a+b)/2`, `(a-b)/2`, and `1-a`, with quaternionic directions `1`, `j`,
   and `1`. This proves the exact triangle, not merely one point outside the
   complex range.
4. The positive-definite family has complex range `[i,1+i]` and quaternionic
   real values `1/2` and `1`. The convex hull of that horizontal segment and
   any one real point meets the real axis in only that one real point.
5. The indefinite family's proposed hull is `conv{i,1/2,1+i}`, whose real
   intersection is `{1/2}`; the quaternionic value 1 lies outside it.
6. Appending repeated diagonal entries of `0`, `i`, or `-i` does not change
   the relevant complex segments or witnesses, so every argument holds for
   all `n>=3`.

The verifier uses exact SymPy arithmetic for the identities and symbolic
constructions. It also samples 10,000 random quaternionic vectors and checks
the norm bound underlying the singular-PSD description.

Command:

```sh
conda run --no-capture-output -n sandbox python code/verify_counterexamples.py
```

The randomized check is only a sanity check. The displayed inequalities and
explicit parametrization in the packet are the proof.

## Source and novelty checks

- The original paper is Luís Carvalho, Cristina Diogo, and Sérgio Mendes,
  *Quaternionic Numerical Range of Complex Matrices*, arXiv:2008.02850
  (published in Linear Algebra and its Applications 620 (2021), 168--181).
- Source PDF page 9 contains Corollary 3.11, the natural question, and Example
  3.12. The example explicitly handles the indefinite and positive-definite
  cases at size three, but not the singular positive-semidefinite case.
- A bounded search through 2026-08-13 used the arXiv id and title; the exact
  matrix `diag(1+i,1+i,0)`; `upper bild`; `quaternionic numerical range`;
  `positive semi-definite`/`positive semidefinite`; the run registry; local
  title/abstract/full-source indexes; and general web search. Related local
  papers arXiv:2210.05520 and arXiv:2210.05535 cite the source and develop
  quaternionic numerical-range theory, but the searched text contains no
  matching construction or explicit settlement of this missing branch.
- No separate prior occurrence of the exact singular-PSD triangle or the
  all-dimension three-family statement was found. This is a bounded search,
  not an exhaustive priority determination.

## Artifact and PDF checks

- The original PDF was downloaded from arXiv and archived as
  `source_paper.pdf`.
- Source PDF page 9 was rendered at 180 dpi; the full-width question crop was
  visually checked for complete, readable text.
- The solution packet was compiled into `tmp/build`; all final pages were
  rendered to PNG and visually inspected.
- The LaTeX log was checked for undefined references, missing citations,
  overfull boxes, and fatal warnings.

## Human review recommendation

Likely valid as a full negative answer to the intended three-formula
generalization question. First verify the exact singular-PSD upper-bild lemma,
especially the converse parametrization. Novelty confidence is moderate:
mathematical correctness is elementary and high-confidence, but two branches
are already in the source paper and the incremental new content is the third
branch plus the uniform closure.
