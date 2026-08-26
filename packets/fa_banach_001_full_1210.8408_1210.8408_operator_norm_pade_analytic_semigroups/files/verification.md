# Verification record

## Verdict

likely_valid_full_solution, pending expert review.

The proof answers the strongest conclusion in Egert–Rozendaal Remark 4.7 for the exact stated bounded-analytic setting: convergence occurs in operator norm, hence also strongly on the whole Banach space.

## Analytic checks

- The Saff–Varga–Ni type \((\mu,m)=(N-1,N)\) estimate gives exactly \(1/(2N)\).
- The Padé coefficients satisfy exactly \(p_j/q_j=(N-j)/N\), hence
  \(P_n(-z)=Q_n(z)-zQ_n'(z)/N\).
- Eneström–Kakeya applied to \(Q_n(-z)\) gives a polynomial root-radius bound; the deliberately coarse radius \(2N^2\) is sufficient.
- On the imaginary axis the coefficient identity converts the rational function into an average of \(\lambda_k/(\lambda_k-it)\), yielding \(|t r_n(-it)|\le4N^2\).
- The maximum-principle extension to the right half-plane is legitimate because \(z r_n(-z)\) is rational, pole-free there, and finite at infinity.
- The two-constants exponent in a quadrant is \(\delta_\theta=1-2\theta/\pi\).
- The contour split at \(R=N^{2+\delta}\) gives middle contribution \(O(N^{-\delta}\log N)\) and tail contribution \(O(N^{-\delta})\).
- Scaling \(s=tr\) makes the bound uniform for every \(t>0\); \(t=0\) is exact.

## Computational sanity check

Run:

    conda run --no-capture-output -n sandbox python \
      runs/fa_banach_001/solutions/full/1210.8408_operator_norm_pade_analytic_semigroups/code/verify_pade_endpoint.py

The script checks exact coefficient identities for \(1\le n\le20\), exact coefficient-ratio bounds for \(1\le n\le200\), and numerical samples of the scalar positive-ray, imaginary-tail, and strict-sector integral estimates. These computations are not used as proof.

## Bounded novelty check

Searches performed on 2026-08-09:

- exact Remark 4.7 wording;
- subdiagonal Padé + operator norm + bounded analytic semigroup;
- arXiv:1210.8408 and citation-focused searches;
- Neubrander–Özer–Windsperger (2020);
- Gomilko–Tomilov, arXiv:2403.14411 / JFA 2024;
- Batty–Gomilko–Tomilov, arXiv:2403.15894 / JLMS 2025;
- classical Saff–Varga–Ni approximation results.

No exact existing answer was found. The 2024 JFA paper still labels the whole-space endpoint open for general bounded semigroups; the 2025 JLMS paper concerns fixed-rational scaling formulas, not the variable unscaled \([n/(n+1)]\) sequence.

## Reviewer priorities

1. Confirm the historical Padé indexing in Saff–Varga–Ni Theorem 2.1.
2. Recheck the logarithmic-derivative formula in the tail lemma.
3. Confirm the functional-calculus identity when \(0\in\sigma(A)\); the difference function vanishes at zero, so no injectivity assumption should be needed.
