# Verification report

Verdict: `candidate_full_solution_likely_valid`

## Source audit

The packet's `source_paper.pdf` is arXiv:1205.4735, *A closed formula for
subexponential constants in the multilinear Bohnenblust--Hille inequality*, by
Diana Marcela Serrano-Rodríguez. The full-width crop is from PDF page 5 and
contains the complete explicit conjecture

```text
lim r_n = exp(1-gamma/2)/sqrt(2).
```

Equation (2.3) on PDF page 3 defines the corrected product for even `n>14`.
The packet also includes arXiv:1107.4814 as
`supporting_paper_1107.4814.pdf`; that earlier paper introduced the original
product and explicitly left its convergence unproved.

## Exact-cancellation audit

For `m=(n-2)/2`,

```text
sum_(k=1)^m (2k+1) = m(m+2) = (n^2-4)/4,
Gamma(3/2) = sqrt(pi)/2,
(6k+1)/(4k+2) = 3/2 - 1/(2k+1).
```

Substitution into the original formula cancels the full macroscopic `pi`
power and leaves

```text
log r_old = [(n-2)/(2n)] log 2
            - (1/n) sum_(k=1)^m (2k+1)
              [f(1/(2k+1))-f(0)],
f(x)=log Gamma(3/2-x).
```

This identity was checked both by hand and through direct high-precision
evaluation of the two sides.

## Taylor and rate audit

Taylor's theorem gives

```text
t[f(1/t)-f(0)] = f'(0) + f''(0)/(2t) + O(t^-2),
f'(0)=-psi(3/2), f''(0)=psi_1(3/2).
```

The odd harmonic sum is `(1/2)log n+O(1)`, while the squared-reciprocal
remainder is summable. After division by `n`, the trigamma contribution is
therefore exactly

```text
-[psi_1(3/2)/(4n)] log n.
```

Finally, `psi(3/2)=2-gamma-2 log 2`, so the constant logarithm is
`1-gamma/2-(log 2)/2`.

## Corrected-formula audit

Expanding the corrected exponents gives

```text
(n+14)(n-14)/(8n) = (n^2-196)/(8n),
((n+12)(n-14)-24)/(4n) = (n^2-2n-192)/(4n).
```

Relative to the original product, the `pi` exponent changes by `-24/n`, the
denominator exponent of `2` changes by `-48/n`, and the product omits exactly
`k=1,...,6`. Thus

```text
log r_corrected - log r_old = kappa/n,
kappa = 48 log 2 - 24 log pi
        + sum_(k=1)^6 (2k+1) log Gamma(3/2-1/(2k+1)).
```

This proves transfer of both the limit and the displayed logarithmic error.

## Recursive-upgrade audit

Writing `s_n=n log C_n` turns the source's two-step recurrence into

```text
s_n-s_(n-2) = (n/2+1)log 2
              -(n-1)[f(1/(n-1))-f(0)]
```

once the Khinchin parameter lies in Haagerup's gamma branch. All earlier terms
are absorbed into an `O(1)` constant separately on each parity. On either
parity,

```text
sum (j/2+1) = n^2/8+3n/4+O(1),
number of terms = n/2+O(1),
sum 1/(j-1) = (1/2)log n+O(1).
```

These identities give the asserted all-index asymptotic. Both parity errors
tend to zero, so subtracting adjacent logarithms justifies the one-step ratio
limit without assuming a pre-existing ratio limit.

## Computational audit

Command:

```text
conda run --no-capture-output -n sandbox python \
  code/check_gamma_product_limit.py
```

The script used 80-digit arithmetic. For `n=16,30,100,1000,10000`, the
residual in the exact finite-correction identity was below `8e-79`. It found

```text
conjectured limit = 1.44025268986944545315915399635
r_10000           = 1.43989424322734605
-psi_1(3/2)/4     = -0.233700550136169827354311374985
```

For the recurrence at `n=100000`, it found

```text
C_n/2^(n/8)       = 1.71270689821922649
target            = 1.71275874619455197766045871488
C_n/C_(n-1)       = 1.09050678191686343
target 2^(1/8)    = 1.09050773266525765920701065576
```

These computations are sanity checks and are not used in the proof.

## Novelty audit

Bounded searches on 2026-08-11 covered:

1. the four run indexes and exact arXiv identifiers;
2. exact web phrases combining `r_n`, `1.44025`, the conjectured constant, and
   the paper title;
3. Crossref records for DOI `10.1016/j.laa.2012.11.028`;
4. all eight works then returned by OpenAlex as citing that DOI; and
5. locally available arXiv full text for the relevant citing corpus, including
   arXiv:1205.2385, 1207.0124, 1302.3026, 1503.07306, 1506.00159, and
   1604.06323.

No proof of the exact product conjecture was found. ArXiv:1108.1550 proves a
related one-factor Khinchin limit with the same constant but does not state or
prove this product convergence. Novelty remains plausible rather than
certified.

## Scope and human verifier focus

The packet fully solves the explicit formula conjecture and strengthens the
asymptotic statement for the associated recursive estimates. It does not
determine the optimal Bohnenblust--Hille constants.

Human review should independently check:

1. the cancellation identity;
2. the factor `1/4` in the trigamma term;
3. all signs in `kappa`; and
4. the recurrence increment and the equal parity constants.

## Build and render audit

The packet compiled with `latexmk` to a five-page PDF with no unresolved
references, LaTeX warnings, overfull boxes, or underfull boxes. All five pages
were rendered at 130 dpi and visually inspected on 2026-08-11. The source crop
was inspected separately at original resolution. Equations, source evidence,
page breaks, and references are readable and clean, with no clipping, overlap,
missing glyphs, or malformed math.

SHA-256 checksums:

```text
16456264c46bae406444bc4cf86a5597529fce0d54fe927f9edcea8f2f120d8e  solution_packet.pdf
8751600b349e67145a7512d0fdc35043766a729c35c13f81fa2b3374a6066d1d  source_paper.pdf
a3c0f76e9a7e28f7f3148bbc6e6951a067660c1f7e53e5903307f0f85141cbdd  supporting_paper_1107.4814.pdf
af5bdfaca6369167599cb38e448bbe07e38c9863b25b36faffde23f288d01824  figures/open_problem_crop.png
```
