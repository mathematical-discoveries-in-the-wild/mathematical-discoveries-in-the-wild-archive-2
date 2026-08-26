# Sharp cov(N) minima for Questions 1--3

Status: candidate substantial partial result; likely valid.

For every directed set A with |A| < cov(N), the three pathological families
NM_A, NF_A, and ND_A defined in arXiv:2306.03862 are empty. The key proof
converts any persistent positive-measure tail of a convergent net into a
cover of a positive-measure set by |A| null sets.

Combining this lower bound with the source paper's constructions gives:

- the exact smallest cardinality in Q1 is cov(N) for every
  1 <= mu <= 2^c;
- the exact smallest cardinality in Q2 is cov(N) for the same full range;
- the exact smallest cardinality in Q3 is cov(N) for
  1 <= mu <= c, using one common product directed set.

The packet does not classify all directed sets, settle Q3 for
c < mu <= 2^c, or settle the regular-cardinal Questions 4--6.

Files:

- main.tex and solution_packet.pdf: theorem, proof, corollaries, and scope.
- source_paper.pdf: official arXiv PDF.
- figures/open_problem_crop.png: Q1--Q3 on printed page 26.
- verification.md: proof-audit report.

Ledger:
runs/fa_banach_001/ledger/results/2306.03862_covN_sharp_minimal_directed_cardinality.json.

