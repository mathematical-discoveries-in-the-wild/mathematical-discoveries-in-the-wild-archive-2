# Literature-Already-Answered Packet: Uniform Negative-Alpha Spectral Gap

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status note: this packet records an explicit later-literature answer, not a
new result of this run.

## Source Question

- Emanuel Milman, *Harmonic Measures on the Sphere via
  Curvature-Dimension*, arXiv:1505.04335; published in *Annales de la Faculte
  des sciences de Toulouse* 26 (2017), 437--449.
- Exact location: Section 4.2, page 9 of `source_paper.pdf`.

For the probability measure on `S^n` with density proportional to
`|y-x|^{-(n+alpha)}`, Milman writes that interpolation between `alpha=-n`
and `alpha=0` suggests that the spectral gap remains of order `n`, uniformly
for `alpha in [-n,0]` and `|x|<1`.

## Supporting Literature

- Yutao Ma and Xinyu Wang, *A note on the spectral gap for general harmonic
  measures on spheres*, *Statistics & Probability Letters* 141 (2018),
  56--61, DOI: [10.1016/j.spl.2018.05.022](https://doi.org/10.1016/j.spl.2018.05.022).
- Decisive result: Theorem 1.1.

Ma--Wang use measures `mu_x^{m,beta}` on `S^{m-1}` with density proportional
to `|y-x|^{-(m+beta)}`. Set

```text
m = n+1,       beta = alpha-1.
```

Then their measure is exactly Milman's measure. Over Milman's target range,
Theorem 1.1 gives

```text
lambda_1 >= n-1                 if alpha <= 2-n,
lambda_1 >= (n-alpha)/2         if 2-n < alpha < 0,
lambda_1 >= n/2                 if alpha = 0.
```

Consequently `lambda_1 >= n/2` throughout `alpha in [-n,0]`, uniformly in
`|x|<1`. This proves precisely the order-`n` statement suggested in the
source.

## Explicit Provenance

This is an explicit answer, rather than an agent-only theorem
identification. The Ma--Wang abstract says that their estimates improve those
of Milman (2015) for general `beta in R`, and the publisher's article text
discusses Milman's generalized harmonic measures immediately before Theorem
1.1.

## Access Note

The source arXiv PDF is included as `source_paper.pdf`. The decisive 2018
article has no arXiv version located in the bounded title/DOI/author search,
and the publisher PDF endpoint returned HTTP 403. Its stable DOI, exact
theorem label, bibliographic metadata, parameter identification, and required
branches of the theorem are recorded here and in `main.tex`.

## Scope

- The suggested range `alpha in [-n,0]` is completely answered.
- Milman's separate question about `alpha<-n` is not addressed by this
  packet.
- This packet must not be counted as new mathematical progress.

## Search Evidence

The run indexes were searched for `1505.04335`, `harmonic measures`,
`spectral gap`, and `negative alpha`. The bounded external search used the
exact source title, the phrase `spectral-gap remains of the order of n`, the
supporting title, authors, DOI, and theorem formulas. The exact later article
was found through the publisher record and DOI metadata.

## Human Review Recommendation

Accept as `literature_already_answered`. Verify the two parameter substitutions
against Theorem 1.1 if institutional access to the supporting PDF is available.

