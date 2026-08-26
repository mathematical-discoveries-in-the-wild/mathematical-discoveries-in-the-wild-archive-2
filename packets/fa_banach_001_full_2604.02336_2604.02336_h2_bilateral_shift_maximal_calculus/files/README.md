# Maximal H2 calculus of the bilateral shift

Source: Anand Ganesh, Babhrubahan Bose, and Anand Rajagopalan,
“The Shift Operator Calculus for Stationary Time Series Analysis,”
arXiv:2604.02336v2, conclusion, PDF page 7.

Status: candidate_full_likely_valid.

The source leaves as future work the unbounded operator f(B) for f in H2.
The packet gives a complete canonical realization. Under the Fourier unitary
ell_2(Z) -> L2(T), define f(B) to be maximal multiplication by the L2
boundary function F of f, with domain

    {x : F Ux belongs to L2(T)}.

This operator is densely defined, closed, and normal. Its adjoint, spectrum,
resolvent, boundedness threshold, and inverse criterion are explicit.
Finitely supported sequences are a graph core; Taylor power sums converge
there and their closure is precisely the maximal operator. Bounded spectral
truncations converge on every vector of the maximal domain. Each basis
vector is in the domain and recovers the expected moving-average series.

The result is a self-contained application and synthesis of classical
Hardy-space and multiplication-operator facts. Novelty confidence is
low-to-moderate because no exact answer tied to the source was found, but the
ingredients themselves are standard.

Review files:

- solution_packet.pdf
- main.tex
- verification.md
- figures/open_problem_crop.png
- source_paper.pdf
- ../../../../attempts/2604.02336_h2_bilateral_shift_unbounded_calculus.md

Ledger:
runs/fa_banach_001/ledger/results/2604.02336_h2_bilateral_shift_maximal_calculus.json.

