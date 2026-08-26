# Literature-implied answer: metrizability cannot be removed

The first loose end in Marcel Schmidt's *Energy forms* (arXiv:1703.04883v1, Chapter 5, Question 1, printed page 163 / arXiv PDF page 179) asks whether Theorem 1.38 remains true without metrizability of the form topology.

The answer is no. Susanne Dierolf's 1975 quotient theorem implies a direct counterexample. Apply it to the incomplete pre-Hilbert space `c_00` with its `ell_2` norm. It gives a complete Hausdorff topological vector space `Z` and a quotient map `pi: Z -> c_00`. The continuous quadratic form

`q(z) = ||pi(z)||_2^2`

is closed, its kernel is closed, and its canonical quotient embedding is a topological isomorphism. Nevertheless `(D(q)/ker q,q)` is `c_00`, hence is not Hilbert. Thus assertions (i) and (ii) of Theorem 1.38 do not imply assertion (iii) once metrizability is removed.

Files:

- `solution_packet.pdf`: compact status note and proof.
- `source_paper.pdf`: arXiv:1703.04883v1.
- `supporting_dierolf_1975.pdf`: S. Dierolf, *Uber Quotienten vollstandiger topologischer Vektorraume*, Manuscripta Math. 17 (1975), 73--78.
- `main.tex`: packet source.
- `verification.md`: hypothesis-by-hypothesis audit.

This is classified as a literature-implied answer because Dierolf's theorem predates the source question but does not state the quadratic-form consequence explicitly.
