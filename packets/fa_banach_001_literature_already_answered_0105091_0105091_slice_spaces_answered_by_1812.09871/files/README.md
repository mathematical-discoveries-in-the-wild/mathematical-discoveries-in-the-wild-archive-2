# Slice-Space Boundedness Classification Answered by Akian--Gaubert--Hochart

Status: `literature_already_answered`.

Original/open-problem source: Stephane Gaubert and Jeremy Gunawardena, "The Perron-Frobenius Theorem for Homogeneous, Monotone Functions," arXiv:math/0105091; *Transactions of the American Mathematical Society* 356 (2004), 4931--4950. In the subsection "Slice spaces and recession functions," journal page 4937, the authors ask whether boundedness of all slice spaces can be determined by combinatorial or graph-theoretic constructions.

Supporting answer: Marianne Akian, Stephane Gaubert, and Antoine Hochart, "A game theory approach to the existence and uniqueness of nonlinear Perron-Frobenius eigenvectors," arXiv:1812.09871. The introduction transcribes the source question as Problem 1 and explicitly says the paper solves it. Theorem 1.2 characterizes boundedness of every slice space by absence of disjoint dominions in the game `Gamma_infinity(f)`, and Section 4 gives directed-hypergraph reachability tests for the dominion condition.

This is an exact, author-aware answer, not an inferred consequence. The classification applies to every finite-dimensional monotone homogeneous self-map of the open positive orthant, which is precisely the scope of the original question. It does not address the separate infinite-dimensional Banach-cone question at the end of the source paper.

Files:

- `source_paper.pdf`: arXiv:math/0105091
- `supporting_paper_1812.09871.pdf`: arXiv:1812.09871
- `main.tex`: compact status note
- `solution_packet.pdf`: rendered status note

Ledger: `runs/fa_banach_001/ledger/results/0105091_slice_spaces_answered_by_1812.09871.json`.
