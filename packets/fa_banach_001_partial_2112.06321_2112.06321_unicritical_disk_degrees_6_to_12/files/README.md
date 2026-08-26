# Candidate partial result: unicritical degrees 6 through 12

Status: `candidate_partial_likely_valid`

Source question: Bickel--Gorkin, arXiv:2112.06321, Question 1 on PDF page 28. If a finite Blaschke product `Theta` is unicritical of degree `n`, must `W(S_Theta)` contain a pseudohyperbolic disk of radius `2^(-1/(n-1))`?

Result in this packet: yes for every unicritical `Theta` of every degree `2 <= n <= 12`. The cases `n <= 4` are in the source paper and degree 5 is Theorem 2.1 of arXiv:2312.04537. The new proof here covers all degrees `6 <= n <= 12`, uniformly over the repeated zero in the unit disk.

The proof uses the published KMS test curve in the numerical range. For each degree, an exact rational Bernstein certificate proves that the curve winds around a sufficiently large Euclidean disk. A second exact certificate converts that disk to a pseudohyperbolic disk of the required radius. The checker uses algebraic root isolation and rational arithmetic; it is part of the proof, not a floating-point experiment.

Run the verifier from this directory with:

```bash
conda run --no-capture-output -n sandbox python code/verify_degrees_6_to_12.py
```

Expected result: seven `PASS` lines, one for each degree 6 through 12. A recorded run is in `verification_report.txt`.

Scope limitation: the source question for arbitrary degree remains open here. The degree-specific positivity certificates show a stable pattern, but this packet does not infer or claim a uniform inequality for `n >= 13`.

Human review recommendation: prioritize the winding-number-to-convex-hull step and the sign conversion in the pseudohyperbolic-radius lemma, then rerun the exact verifier.

