# A representation-degree obstruction to p-group suborbit approximation

Candidate substantial partial result for Problem 2.6 of arXiv:1212.5351.

Let a finite group act orthogonally on \(V\), let \(L\subset V\) be
\(k\)-dimensional, and decompose the representation into real irreducible
blocks. If every block has dimension less than \(k\), then no orbit can come
within
\[
 \eta_k=\left[1-\frac{k}{k-1}
 \left(\frac{\Gamma(k/2)^2}
 {\Gamma((k-1)/2)\Gamma((k+1)/2)}\right)^2\right]^{1/2}
\]
of every point of \(S(L)\). More generally, an \(\varepsilon\)-covering orbit
forces almost all of the mean-square energy of \(L\) into irreducible
constituents of real dimension at least \(k\).

For \(k=3\), \(\eta_3=\sqrt{1-3\pi^2/32}\approx0.273358\). This improves the
source's \(1/4\) bound for abelian actions and extends it to every
representation with real irreducible degrees at most two, including dihedral
2-groups. The full p-group problem remains open in high-dimensional
irreducible blocks.

- `solution_packet.pdf`: review artifact
- `main.tex`: theorem and proof
- `source_paper.pdf`: official arXiv PDF
- `figures/problem_2_6_crop.png`: source question on PDF page 4
- `code/check_constants.py`: numerical constant audit
- `code/make_source_crop.py`: reproducible source crop
- `verification_report.md`: proof, scope, and novelty audit
- `attempt_log.md`: summary of six focused routes

Status: **candidate substantial partial theorem, likely valid, pending expert
review**.

