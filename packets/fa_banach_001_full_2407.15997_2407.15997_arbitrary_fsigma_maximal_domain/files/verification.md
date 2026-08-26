# Verification record

## Mathematical audit

- The local model is injective: if
  `c+(z-gamma)g=0` with the Taylor coefficients of `g` in `c_0`, then
  `g=c/(gamma-z)`; its coefficients have constant modulus, forcing `c=0`
  and then `g=0`.
- Convergence in the `c_0` coefficient norm implies locally uniform
  convergence on the disk.
- A Cauchy sequence for the final norm that tends to zero in `H^2` tends to
  zero in every local component.  Supremum convergence on each closed layer
  and Fatou's lemma for the weighted `l_1` sum then rule out ghost vectors.
- Multiplication by `z` sends a local pair `(c,g)` to
  `(gamma*c, c+z*g)` and has norm at most two, uniformly in `gamma` and the
  closed layer.
- For the boundary peak `q_N(z)=((1+conj(w)z)/2)^N`, polynomial division
  gives binomial-tail coefficients.  They are bounded by one everywhere.
  On a closed set separated from `w`, Abel summation bounds their supremum by
  `C/(dist(w,K)*sqrt(N+1))`; the boundary values decay exponentially there.
- The identity
  `||q_N||_{H^2}^2=4^{-N}*binom(2N,N)` gives convergence to zero.
- For `|w|>1`, `(z/w)^N` has all local and `H^2` norms bounded by a constant
  times `|w|^{-N}`.
- Hence all and only points of `D union Gamma` support continuous polynomial
  evaluation.

## Computational sanity check

`code/check_peak_coefficients.py` directly compares polynomial-division
coefficients with the binomial-tail formula on a finite grid and checks the
uniform bound.  It is supplementary and is not used as proof.

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2407.15997_arbitrary_fsigma_maximal_domain/code/check_peak_coefficients.py
```

## Bounded novelty search

Checked through 2026-08-11:

- the run registry, solution, attempt, and proof-gap indexes;
- arXiv:2407.15997v2 and the published DOI `10.1090/proc/17344`;
- exact-title, exact-problem, arXiv-id, DOI, author, citation, and phrase
  searches involving `maximal domain`, `F_sigma`, `Hilbert/Banach`, and the
  authors' explicit rational-boundary example;
- search results for papers citing or discussing the source.

The retrieved source and publication records still state only the
`F_sigma`-and-`G_delta` Hilbert result.  No later paper or independent theorem
explicitly answering Problem 4.7 was found.  Novelty confidence is moderate:
the construction appears new in the bounded search, but the search is not a
proof of priority.

## Human review focus

Check the Abel-summation estimate uniformly in the truncation index and the
no-ghost completeness argument.  These are the two structural points on
which the full result rests.

Verdict: `candidate_full_solution`, likely valid.

