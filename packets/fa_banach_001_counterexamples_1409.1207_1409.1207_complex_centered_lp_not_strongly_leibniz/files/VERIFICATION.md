# Verification report

Verified at: 2026-08-17T21:51:59Z

Verdict: candidate_counterexample_likely_valid — a full negative answer to
the literal complex-valued strong-Leibniz question for every 1<=p<2.

## Mathematical audit

- The source defines sigma_p on complex-valued bounded random variables and
  asks whether all centered moments on general probability spaces are
  strongly Leibniz.
- Failure of the inverse inequality
  sigma_p(f^{-1}) <= ||f^{-1}||_infinity^2 sigma_p(f)
  is by itself enough to disprove strong Leibnizness.
- For z_k=(k^2-1-2ki)/(k^2+1), exact expansion gives |z_k|=1.
- For f_k=(1,z_k,2-z_k), its coordinate mean is one and
  |2-z_k|^2=(k^2+9)/(k^2+1)>1. Therefore f_k is invertible and
  ||f_k^{-1}||_infinity=1.
- The two nonzero centered coordinates of f_k both have modulus
  2/sqrt(k^2+1), giving
  sigma_p(f_k)^p=2^(p+1)/(3(k^2+1)^(p/2)).
- Direct subtraction of the coordinate mean of f_k^{-1} gives moduli
  8/(3sqrt(D_k)),
  2sqrt(9k^2+25)/(3sqrt(D_k)), and
  2sqrt(9k^2+1)/(3sqrt(D_k)), where
  D_k=(k^2+1)(k^2+9).
- Dividing the pth powers produces the exact ratio
  [4^p+(9k^2+25)^(p/2)+(9k^2+1)^(p/2)] /
  [2*3^p*(k^2+9)^(p/2)].
- If q=p/2<1, numerator minus denominator is 4^p plus two differences
  (9k^2+c)^q-(9k^2+81)^q. By the mean value theorem, each difference is
  O(k^(p-2)) and tends to zero. Hence the difference tends to 4^p>0 and
  the inverse inequality fails for every fixed 1<=p<2 once k is large.
- At p=1 and k=7, the exact rational-complex witness is
  f=(1,(24-7i)/25,(26+7i)/25), with inverse
  (1,(24+7i)/25,(26-7i)/29).
- Its exact values are
  sigma_1(f)=2sqrt(2)/15 and
  sigma_1(f^{-1})=
  [4sqrt(29)+sqrt(12818)+sqrt(13514)]/1305.
- The strict inequality follows from the rational certificates
  4sqrt(29)+sqrt(12818)+sqrt(13514)>249 and
  174sqrt(2)<174*(71/50)=6177/25<249.
- The construction is complex-valued, so it does not contradict the
  source's real three- and four-atom results. The p=2 boundary is also
  consistent with the known strong-Leibniz theorem.

## Upgrade record

Eight focused stages were completed: exact-scope audit, later-literature
boundary, finite direct search, complex weak-majorization obstruction,
optimized three-point witness, rationalization, exact family calculation,
and an asymptotic upgrade from one p=1 example to every 1<=p<2.

## Literature audit

The follow-up arXiv:1601.00440 proves the ordinary Leibniz product inequality
for real centered Lp moments and explicitly leaves the strong inverse
property open. Bounded primary-source searches through 2026-08-17 used the
source title, centered moments, strong Leibniz, complex-valued, inverse
inequality, and three-point terms. They found the source, the 2016 follow-up,
and Rieffel's p=2 theorem, but no source recording this complex obstruction.
This remains a bounded novelty screen rather than a definitive priority
determination.

## Computational and packet checks

- conda run --no-capture-output -n sandbox python code/verify_family.py
  passed. SymPy verifies the symbolic one-parameter deviations and the exact
  k=7 norms and radical comparison.
- LaTeX compiled with resolved references and no matched warnings, errors,
  overfull boxes, or underfull boxes in the final log.
- The final packet contains three A4 pages.
- Every final page was rendered at 180 DPI and visually inspected at original
  resolution. The source question crop, theorem, proof intuition, exact ratio,
  asymptotic argument, explicit radical certificate, limitations, and
  references are readable and unclipped.
- Text extraction contains all theorem and boundary sections and the
  references.

## SHA-256

    ef35df23f16254da0461880f71a4b77ad5ddc80a22bf934e6aa84dcb02faf222  solution_packet.pdf
    72f7c7e385dec0a34988bf7734484b3ce4ccbd80763d2abb3f9649f1b9a59402  source_paper.pdf
    0d974e8cd822830c17d1ec2e0d49890874497d4a87ef3f939264016263b4d760  supporting_paper_1601.00440.pdf
    7dd990cc1c5a7c12abc5dd13273b4537d33821202a02a9b7ad271f1bf6423a71  figures/open_problem_crop.png
    03b317ed4fda2a0c14820e5cf3dcd70efcdc20c142b08231d3132f3173514a36  code/verify_family.py

## Human-review recommendation

Recompute the three inverse-centered moduli and exact ratio independently,
then confirm that the source's complex-valued opening scope makes inverse
failure on complex l_infinity^3 a literal answer. The remaining real-valued
conjecture should be kept separate.

