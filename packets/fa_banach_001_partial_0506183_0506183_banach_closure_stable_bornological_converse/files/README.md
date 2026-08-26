# A closure-stable Banach-target converse to Remark 5.6

**Status:** candidate substantial partial result, likely valid, pending human
review.

Source: Ngai-Ching Wong, *The triangle of operators, topologies,
bornologies*, arXiv:math/0506183, Remark 5.6 (PDF p. 18).

Let \(\mathcal M=\mathcal B(\mathcal A)\).  The source asks whether the
operator identity

\[
\mathcal L^b(X,Y)\cap\mathcal O(\mathcal M)(X,Y)
=\mathcal O^b(\mathcal M)(X,Y)\qquad(\text{all LCS }X)
\]

forces \(Y\) to be \(\mathcal A\)-bornological.  The packet proves an
affirmative answer when \(Y\) is Banach and the ideal bornology
\(\mathcal M(Y)\) is stable under norm closure.  The proof uses the strongest
locally convex topology on the underlying vector space to extract an
absorbing \(\mathcal M\)-bounded disk, then closes it and invokes Baire
category.  The result applies in particular to finite-dimensional,
precompact/compact, and relatively weakly compact ideal bornologies.

The unrestricted LCS case and Banach ideal bornologies not stable under norm
closure remain open.

Files:

- `solution_packet.pdf`: review packet.
- `main.tex`: proof source.
- `source_paper.pdf`: original target paper.
- `figures/open_question_crop.png`: Remark 5.6 and its context.
- attempt history:
  `runs/fa_banach_001/attempts/0506183_bornological_converse_upgrade_attempts.md`.

Human review should check the bounded-set description of the strongest
locally convex topology and the exact closure stability of any operator ideal
to which the theorem is applied.
