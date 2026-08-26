# Verification report

Status: candidate partial; proof complete for stated obstruction; ready for
human mathematical review.

## Mathematical audit

- The question and Nd representer bound were checked in the official arXiv
  v3 PDF, page 33.
- On finite discrete Omega, a vector measure is uniquely a tuple of output
  vectors, and its total variation is their sum of Euclidean norms.
- The first N feature rows form a rank-N matrix A; they can therefore be
  completed by rows to an invertible (2N-1)-by-(2N-1) matrix F. This makes
  the coefficient-to-function map injective on the whole domain.
- The identities G^T a_j=s_j give the exact first-order optimality equation
  at the proposed nonzero coefficient tuple.
- The 2N-1 matrices a_j s_j^T are independent: rows 3,...,N isolate two
  matrices each, and the remaining three are independent in the top 2-by-2
  block.
- Strict convexity fixes every minimizer's training prediction. Equality in
  the dual norm bound then forces each coefficient to be a nonnegative
  multiple of s_j; matrix independence forces all multiples to be one.
- Because F is invertible, coefficient uniqueness also excludes any
  alternative kernel expansion with fewer distinct sites.

## Independent finite checks

Command:

~~~text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2509.26371_group_l2_2nminus1_term_obstruction/code/verify_construction.py
~~~

Observed result:

~~~text
all checks passed for 2 <= N <= 12
~~~

For each tested N, the script checks the ranks of A, F, and the flattened
prediction atoms; the exposing identities; the exact KKT residual; the dual
certificate value; uniqueness of the equality-case ray scales; and random
global and prediction-preserving perturbations. These checks are sanity
checks, not dependencies of the general proof.

## Build and visual audit

- latexmk completed with no final warnings, undefined references, overfull
  boxes, or underfull boxes.
- The final packet has 3 letter-size pages.
- Every final page was rendered at 150 dpi to an RGB PNG (1275 by 1650) and
  visually inspected. No clipping, overlap, unreadable glyph, broken formula,
  or malformed page transition was found.
- The source crop is a real render from source page 33 and includes equation
  (7.4), the discussion of groupwise sparsity, and the full open question.
- Extracted final PDF text contains no unresolved question-mark marker.
- The ledger JSON parses and records model GPT5.6.

## SHA-256

~~~text
98102f3964799ac909bdae0ac32c3cac51dd405de2aebc2da6e1d4baaff37bab  solution_packet.pdf
14e99b26e004e41178c165a30bac48cc987cd4e03001daa3bf1ad63acc67aad2  source_paper.pdf
12350c888ceffead6ed1e1f57056f366f85e241dbb6b6b2432b0c0e9649d4c5f  figures/open_problem_crop.png
c767bc8baaa8fb7627f83f80e43ae8c415a4e3bf97afc91b568a5e99151110e7  main.tex
7d362d0439e903562853e9f05467625fbd8c0922d6c0973a70ecef4bb65efc14  code/verify_construction.py
~~~

## Human-review focus

Check that the finite discrete construction satisfies the paper's integral
vv-RKBS definition with its quotient norm reduced to the unique group-l2
coefficient norm; verify the linear independence argument for the 2N-1
prediction atoms; and confirm that equality in every Cauchy inequality forces
nonnegative ray coefficients. The packet deliberately does not claim that
stronger structured group penalties cannot yield an N-term theorem.
