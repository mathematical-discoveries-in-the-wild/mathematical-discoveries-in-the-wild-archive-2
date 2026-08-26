# Verification report

## Mathematical checks

- The 8-cycle has normalized-Laplacian eigenvalues
  `1-cos(2*pi*k/8)`.  The cutoff `omega=1-1/sqrt(2)` is positive, belongs
  to the spectrum, and gives a three-dimensional low eigenspace.
- A 10-regular Ramanujan graph has every nonconstant normalized-Laplacian
  eigenvalue at least `1-6/10=2/5>omega`; its contribution below the cutoff
  is exactly its constant line.
- The Hilbert direct-sum spectral projection therefore has precisely the
  componentwise description used in the proof.
- Sampling all of `C_8` and one vertex from each expander is injective.
- Normalized component constants have ambient norm one and sampling norm
  `N_n^{-1/2}`, disproving a uniform lower frame bound.
- The coefficient sequence `1/n`, after choosing `N_n>=n^4`, is the limit
  of a sampling-norm Cauchy sequence but is not ambient square summable.
- For the complement-supported test function `phi_n`, exact calculation gives
  `||phi_n||^2=N_n-1` and `||L phi_n||^2=11/10`, so no lambda constant exists.

Run the exact verifier with:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2511.17343_uniqueness_not_sampling/code/verify_counterexample.py
```

## Source and scope checks

- Source PDF page 8 states that completeness of the uniqueness norm is unknown.
- Source PDF page 10 states that existence of uniqueness sets which are not
  complements of lambda-sets is unknown.
- The source's enumerated graph hypotheses do not include connectedness.
- The construction satisfies all enumerated hypotheses and uses a positive
  cutoff which is an actual normalized-Laplacian eigenvalue.
- No conclusion is claimed under an additional connectedness hypothesis.

## Novelty check

On 2026-08-17 the run's cheap indexes were searched for arXiv:2511.17343 and
the core uniqueness/lambda-set terms; no duplicate answer was found.  Bounded
web and arXiv searches for graph Paley--Wiener uniqueness sets not sampling or
not complementing lambda-sets returned no matching result.  The Ramanujan-family
input is classical (Marcus--Spielman--Srivastava, arXiv:1304.4132); the candidate
novelty is the direct-sum construction and its simultaneous resolution of the
two explicit questions, not any claim that the component ingredients are new.

## Packet QA

- The final LaTeX log has no box, reference, citation, or layout warnings.
- Every rendered packet page and both source-evidence images were visually
  inspected.
- Final PDF: 3 A4 pages.
- SHA-256 `solution_packet.pdf`:
  `e6b96b31b3dff2ded932192981337727c315985e868c10e9f95d40f150ea6c38`.
- SHA-256 `source_paper.pdf`:
  `2dcd3bd95e136bb76241f4dc76d884b6ae0f4910575d27dd529d236c81e5caf5`.
- SHA-256 `figures/source_page_8.png`:
  `fc167644c25b87b7fd58d2340d5844d1a4272200fc4c87d63ad4afc4ecaf209e`.
- SHA-256 `figures/source_page_10.png`:
  `2c29873245955761a1f8b5515df185f23912690fe32567159701cbea6b1d4252`.
- SHA-256 `code/verify_counterexample.py`:
  `dee393404c3c74e540b4850c20bb8add0c867f92860d63c293cbc509cf11c5f3`.
