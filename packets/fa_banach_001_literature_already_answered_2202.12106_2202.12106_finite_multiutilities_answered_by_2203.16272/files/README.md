# Finite Multi-Utility Question Answered by arXiv:2203.16272

Status: `literature_already_answered`.

Original/open-problem source: Pedro Hack, Daniel A. Braun, and Sebastian Gottwald, "The classification of preordered spaces in terms of monotones: complexity and optimization," arXiv:2202.12106; *Theory and Decision* 94 (2023), 103--125. After Proposition 10 (`finite relations`) and again in the final "Open questions" paragraph, the authors ask whether every preorder with a finite multi-utility has a finite injective-monotone multi-utility, or whether a counterexample exists.

Supporting answer: Pedro Hack, Daniel A. Braun, and Sebastian Gottwald, "The infinite information gap between mathematical and physical representations," arXiv:2203.16272v4 (earlier versions were titled "On a geometrical notion of dimension for partially ordered sets"). In its terminology, multi-utilities are mathematical representations, strict-monotone multi-utilities are physical representations, and injective-monotone multi-utilities are injective physical representations. Theorem 2 constructs a partial order with a minimal two-function multi-utility but a countably infinite minimal strict-monotone multi-utility. Since every injective monotone is strict, this already answers the source question negatively. Lemma 1 and Theorem 7 give the direct dimension formulation: finite geometrical dimension can coexist with countably infinite Debreu dimension, while Debreu dimension equals the minimum size of an injective-monotone multi-utility.

The supporting paper is separate, later, written by the same authors, cites the classification work, and explicitly advertises its results as improving that classification. The answer is full for the finite-multi-utility versus finite-injective-monotone-multi-utility question. A separate question about finite strict versus finite injective physical representations remains open in arXiv:2203.16272v4.

The direct-attack note `runs/fa_banach_001/attempts/2202.12106_finite_multiutility_injective_counterexample_lane08.md` contains an independent short square-product counterexample, but it is not claimed as a new solution because the exact question was already settled.

Files:

- `source_paper.pdf`: arXiv:2202.12106
- `supporting_paper_2203.16272.pdf`: arXiv:2203.16272
- `main.tex`: compact status note
- `solution_packet.pdf`: rendered status note

Ledger: `runs/fa_banach_001/ledger/results/2202.12106_finite_multiutilities_answered_by_2203.16272.json`.
