# Delayed smoothing defeats global one-sided resolvent propagation

This packet gives a candidate negative answer to the open question following
Proposition 4.7 of Arora--Glück, arXiv:2104.12205.

On three copies of `L2(T)`, a positive cyclic operator `Q` transfers two
components unchanged and applies Poisson smoothing on the third transition.
Thus `Q^3` and `(Q')^3` map into `L-infinity`, but the lower powers retain an
identity channel.  For `A=I-Q^{-1}`, all domination and spectral hypotheses of
the source hold with `m1=m2=3`, and `R(1,A)=Q>=0`.  Nevertheless, for every
`delta>0`, `R(1+delta,A)` is not bounded below by any multiple of the source's
rank-one operator.  Sign reversal gives the corresponding failure for upper
bounds.  Hence neither side condition in Theorem 4.5 can be dropped in the
stated generality.

Files:

- `solution_packet.pdf`: self-contained proof and novelty/limitation record.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: source question on PDF page 15.
- `code/verify_counterexample.py`: cyclic-grid algebra and divergence audit.
- `verification.md`: concise verification record.
