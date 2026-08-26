# Bounded Stepanov almost-automorphic exponent invariance

Status: candidate full solution to the unnumbered problem on printed page 9
of arXiv:1903.05869, pending expert review.

For every variable exponent p in D_+([0,1]), the packet proves

    L∞ ∩ AAS^{p(x)} = L∞ ∩ AAS^1
    L∞ ∩ AAAS^{p(x)} = L∞ ∩ AAAS^1.

The main tool is that uniformly bounded local L1 convergence upgrades to
Luxemburg L^{p(x)} convergence when p^+ is finite. In the asymptotic class, a
translation-to-infinity argument first proves that both decomposition pieces
are bounded. See solution_packet.pdf for the full proof and review notes.

Verification:

    conda run --no-capture-output -n sandbox python code/verify_modular_upgrade.py
