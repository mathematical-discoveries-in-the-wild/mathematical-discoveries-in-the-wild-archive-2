# Full solution: a positive-area critical family is common hypercyclic

status: `full_solution_likely_valid`

source: Fernando Costa Jr., *Common hypercyclic algebras for families of
products of backward shifts*, arXiv:2106.08949, Question 2.5 on PDF page 6.

## Result

There is an `L>0` such that the full square

    Lambda = [1,1+L]^2

has the requested property.  For `w_s(a)=1+a/sqrt(s)`, the family

    (B_{w(lambda)} x B_{w(mu)})_{(lambda,mu) in Lambda}

has a common hypercyclic vector on `c0 x c0`.  The same proof works on
`ell_p x ell_p` for every `1<=p<infinity`.

## Main idea

Partition the unit interval into consecutive 4-adic intervals and send them
through a standard Hilbert space-filling curve.  A 4-adic interval of length
`r^2` corresponds to a dyadic parameter square of side `r`.  Attach the
successive squares to arithmetic return times `n_h=n_0+hH`, choosing

    |I_h| comparable to beta/n_h.

The harmonic series guarantees that finitely many such cells cover the whole
parameter square.  Hilbert's `1/2`-Holder estimate gives

    |lambda_j-lambda_k|^2 <= kappa^2 (n_j-n_k)/n_j.

This is exactly the quadratic backward-jump control needed for weights whose
logarithmic products grow like `a sqrt(n)`.  The exact Bayart-Costa-Menet
characterization then yields a common hypercyclic vector.

## Verification and novelty bound

- The source question and Theorem 2.1 of arXiv:2103.13152 were checked from
  the source PDFs.
- The 4-adic alignment, finite harmonic termination, pairwise Hilbert bound,
  and exact weighted cross ratios are proved in `main.tex` and audited in
  `verification.md`.
- On 2026-08-17, the run indexes, local source corpus, exact-phrase searches,
  and close weighted-shift web searches found no later positive-area answer.
  The closest related paper found was arXiv:2306.16026 on critical
  self-similar fractals of zero area.  This is a bounded novelty check, not a
  priority guarantee.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2106.08949.
- `supporting_paper_2103.13152.pdf`: exact characterization used.
- `figures/open_problem_crop.png`: source question and endpoint context.
- `verification.md`: independent proof and rendering audit.
