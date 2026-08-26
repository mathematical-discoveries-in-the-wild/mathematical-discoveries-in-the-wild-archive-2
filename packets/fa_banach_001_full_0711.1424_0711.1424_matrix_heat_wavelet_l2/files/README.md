# Matrix heat-composite wavelets: a full `L2` inversion formula

Status: **candidate full solution to Problem A, likely valid; novelty
cautious**.

This packet gives a precise `L2` meaning to formulas (8.27)--(8.28) in
arXiv:0711.1424, supplies an explicit family of integrable signed cone
wavelets, and computes the normalization constants exactly.

The main conclusions are:

- for every nonnegative spectral cone-Laplace profile `W`, the balanced
  `L2` formula holds exactly when its weighted invariant Mellin integral is
  finite and nonzero;
- Cayley derivatives of matrix-gamma densities have
  `W(s)=det(s)^N det(I+s)^(-beta)` and are honest `L1` wavelet functions;
- the inversion constant is
  `B_m(N-alpha/2, beta-N+alpha/2)^(-1)`;
- for the reproducing formula one universal choice is `N=m`, `beta=2m`;
- Fourier multipliers and monotone cone truncations avoid the unresolved
  Fubini exchange in the source paper's Problem C.

Scope is deliberately exact: this fully answers Problem A in the natural
Hilbert-space setting.  It does not claim to solve the separate classification
in Problem B under the paper's particular Gårding--Gindikin Definition 8.7,
nor to characterize every wavelet for which that specific Fubini exchange is
valid.

Files:

- `solution_packet.pdf`: source question, theorem, proof, examples, constants,
  limitations, and novelty audit.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: Problem A on source PDF page 21.
- `figures/problem_c_crop.png`: the source's Fubini obstruction on page 23.
- `verification_report.md`: proof, provenance, build, and visual audit.
- `novelty_search.md`: bounded literature-search record.
- `code/symbolic_checks.py`: low-rank Rodrigues and scalar-beta checks.
- `tmp/`: build and rendering intermediates.

Human review should first inspect the matrix Rodrigues/Cayley derivative
lemma and the precise scope distinction between Problem A and Definition 8.7.

