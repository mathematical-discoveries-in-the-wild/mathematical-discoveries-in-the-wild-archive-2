# C1-alpha Wasserstein/Hilbert lift counterexample

Candidate full negative answer to Remark 3.12(i) of arXiv:2004.01660.

For every exponent 0 < alpha < 1, the functional

    U_alpha(mu) = (1/(1+alpha)) (integral q^2 dmu)^{(1+alpha)/2}

has a globally C1-alpha Hilbert lift, but its Wasserstein gradient at the
standard Gaussian is q -> q, which is not globally alpha-Hölder on its
support R. The functional nevertheless satisfies the source's
optimal-coupling Taylor-remainder condition.

Files:

- solution_packet.pdf: review artifact;
- main.tex: complete proof;
- code/verify_radial_holder.py: sampled finite-dimensional stress test;
- verification.md: audit record;
- figures/source_page25-25.png: source page containing Definition 3.8;
- figures/source_page27-27.png: source page containing the open problem;
- figures/source_2004.01660.pdf: official arXiv PDF.
