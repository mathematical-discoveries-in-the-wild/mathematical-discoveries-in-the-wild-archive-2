# Counterexample: the elementary-symmetric formal series need not converge on the symmetrized polydisc

- **Source:** Amol Sasane, *Banach algebras of symmetric functions on the polydisc*, arXiv:2201.00183.
- **Target:** Section 7.1's question asking whether the formal series obtained in the elementary symmetric variables converges on a domain containing the symmetrized polydisc.
- **Status:** `candidate_full_counterexample_likely_valid`.
- **Model:** `GPT5.6`.

## Result

The answer is **no already for `d=2`**, and the source's own illustrative Wiener function supplies the counterexample:

```text
f(z,w) = sum_{n>=1} (z^2+w^2)^n / (n^2 2^n).
```

It belongs to the symmetric analytic Wiener algebra because the `n`th block has Wiener norm `1/n^2`. Writing `s1=z+w` and `s2=zw`, the associated formal series is

```text
g(s1,s2) = sum_{n>=1} sum_{k=0}^n
            binom(n,k)(-2)^k s1^(2n-2k)s2^k / (n^2 2^n).
```

At the symmetrized-bidisc point `(s1,s2)=(2r,r^2)`, obtained from `(z,w)=(r,r)`, the absolute mass of the `n`th block is exactly

```text
(3 r^2)^n / n^2.
```

For any `1/sqrt(3) < r < 1` this does not tend to zero, so the multivariable power series diverges absolutely at a point of the symmetrized bidisc. Consequently its convergence domain cannot contain that set.

## Important distinction

If the transformed polynomials are kept in weighted-homogeneous blocks, then

```text
sum_{n>=1} (s1^2-2s2)^n / (n^2 2^n)
```

does converge locally uniformly on the symmetrized bidisc and equals `f` after substitution. In fact the packet proves this block-factorization statement for every symmetric analytic Wiener function in every finite dimension. The negative answer concerns the source's formal **monomial** power series, whose standard analytic convergence is unconditional/absolute; cancellation inside each polynomial block cannot be used to redefine it.

## Files

- `main.tex` — full counterexample and corrected block-factorization theorem.
- `solution_packet.pdf` — compiled three-page proof packet.
- `source_paper.pdf` — official arXiv source.
- `figures/source_question_page17.png` — source question.
- `code/verify_counterexample.py` — exact-rational coefficient and divergence checks.
- `VERIFICATION.md` — independent mathematical and presentation checks.
