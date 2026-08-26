# Verification report

Status: **candidate full solution, likely valid, needs expert review**

## Formal checks performed

1. The function \(Y(\theta)=|\theta''|^2-\ell/n\) is the restriction of
   the harmonic polynomial
   \(|x''|^2-(\ell/n)|x|^2\), hence is an even, degree-two,
   \(K_\ell\)-invariant spherical harmonic.
2. The Funk-Hecke multiplier ratio for \(M^{1-i}\) is
   \(m_2/m_0=-i/(n-i)=-i/k\), while
   \(m_0=\sigma_{n-1}\Gamma(i/2)/\Gamma(k/2)>0\).
3. The interval
   \(kn/[i(n-\ell)]<\varepsilon<n/\ell\) is nonempty exactly because
   \(i>\ell\). Its upper bound keeps \(\rho_B^k\) positive; its lower
   bound makes the unique representing density negative at the block axis.
4. In a coordinate two-plane the polar curvature numerator at the
   complementary axis equals
   \(a^{2/k-1}(a-2\varepsilon/k)\), where
   \(a=1-\varepsilon\ell/n\). For \(i=\ell+1\), the density-negativity
   lower bound is strictly stronger than the negative-curvature bound; for
   \(i=\ell+2\), the two bounds coincide.
5. Rubin's inversion and Radon-cosine intertwining lemmas give both the
   pairing identity used in the strict volume reversal and the section
   comparison for every \(\xi\in G_{n,i}\).
6. The perturbation is arbitrarily small in \(C^\infty\), so positivity of
   the radial function and strict negative planar curvature persist.

## Computational sanity check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/0701317_nonconvex_axial_ldbp_counterexamples/code/verifier.py
```

The script checks every admissible triple with \(3\leq n\leq100\), using the
midpoint of the allowed epsilon interval. It checks the radial-power
positivity, negative representing-density value, negative curvature sign, and
201 sampled angles for each triple. This is a sanity check only; it does not
replace the Funk-Hecke calculation or Rubin's transform lemmas.

Output:

```text
checked 4851 admissible (n, ell, i) triples with 3 <= n <= 100
first cases: [(3, 1, 2), (4, 1, 2), (4, 1, 3), (5, 1, 2), (5, 1, 3), (5, 2, 3)]
all positivity, density-sign, and curvature-sign checks passed
```

## Literature and duplicate bounds

Searched on 11 August 2026:

- `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and
  `proof_gaps/index.tsv` for `0701317`, the exact title, generalized axial
  symmetry, canonical angles, the nonconvex conjecture, and the endpoint
  indices;
- exact web phrases from the conjecture, the source title, arXiv id, and DOI;
- Rubin-related lower-dimensional Busemann-Petty results and the later
  symmetry paper Dann-Zymonopoulou, arXiv:1307.3206;
- the existing run packet for arXiv:0704.0061, which answers a different
  \((q,\ell)\)-ball lambda-intersection-body problem and only cites 0701317
  as related literature.

No explicit later solution or the present degree-two construction was found.
The search was bounded and novelty remains provisional.

## Reviewer checklist

- Audit the precise normalization and degree-two multiplier of \(M^{1-i}\).
- Confirm injectivity of \(M^{1-k}\) on even distributions at these integer
  parameters, hence uniqueness of the smooth representing density.
- Check the index substitution \(k=n-i\) in Rubin's Lemmas 4.1 and 4.2.
- Check the polar-curvature calculation and its persistence under the
  perturbation.
- Independently repeat the later-literature search before any originality
  claim.
