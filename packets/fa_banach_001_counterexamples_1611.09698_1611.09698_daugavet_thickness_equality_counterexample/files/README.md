# Hilbert-space counterexample to the weakly compact thickness equality

Status: **candidate full counterexample, likely valid; specialist review
recommended**.

Question 2 on PDF page 16 of Abraham Rueda Zoca, *Daugavet property
and separability in Banach spaces*, arXiv:1611.09698, asks whether

norm(T+I) = max{mathcal T(X), mathcal T_{w*}(X*)}

for every Banach space X and weakly compact operator T:X->X.

Take any infinite-dimensional Hilbert space H and T=I_H. Arbitrarily
thin spherical caps in the Hilbert unit ball show
mathcal T(H)=0. Since H is reflexive, weak-star and weak topology on
H* coincide, so mathcal T_{w*}(H*)=0. Yet T is norm-one and weakly
compact and norm(T+I)=2.

Thus the answer to Question 2 is no, even for a separable reflexive Hilbert
space and even if the norm-one hypothesis from the preceding proposition
was intended. Question 1 in the same source is not addressed.

Files:

- main.tex and solution_packet.pdf: counterexample and proof.
- source_paper.pdf: local source PDF.
- figures/open_question_crop.png: both source questions, including
  Question 2.
- VERIFICATION.md: proof, source, layout, and novelty checks.
