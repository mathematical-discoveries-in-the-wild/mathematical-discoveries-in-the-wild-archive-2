# Candidate full counterexample for arXiv:1910.06891

Aleksandrov and Peller ask whether, for 0<p<1, Pisier's sufficient class

    Y_{p_flat},  p_flat=2p/(2-p),

is contained in the p-projective tensor product
ell^infinity tensor_p ell^infinity.

This packet gives a negative answer for every 0<p<1. The counterexample is
block diagonal. Its blocks are scaled Fourier unitaries

    c_j n_j^{-1/p_sharp} U_{n_j},

where c_j=(j+1)^(-1/p) and the dimensions grow sufficiently rapidly. Flat
entries put the matrix in the smaller one-sided class
ell^{p_flat}(ell^infinity). Equal singular values and separated dimensions
force disjoint windows of coefficient p-mass in any alleged tensor
representation; those masses dominate the harmonic series.

Files:

- solution_packet.pdf: complete candidate proof and source-question crop;
- main.tex: packet source;
- source_paper.pdf: arXiv source PDF;
- figures/open_problem_crop.png: genuine page-20 crop;
- verification.md: proof audit and scope;
- code/verify_exponents.py: exact exponent and finite Fourier checks.

The result does not settle the paper's automatic complete-boundedness problem,
its integral-kernel extension problem, its diagonal Lorentz conjecture, or the
general equality between p-tensor and bounded pointwise closure.
