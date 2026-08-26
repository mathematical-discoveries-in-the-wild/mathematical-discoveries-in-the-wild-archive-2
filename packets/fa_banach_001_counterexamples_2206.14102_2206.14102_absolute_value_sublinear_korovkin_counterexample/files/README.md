# Absolute-value counterexample to the direct sublinear Wulbert analogue

- **Source:** S. G. Gal and C. P. Niculescu, *Korovkin type theorems for
  weakly nonlinear and monotone operators*, arXiv:2206.14102, PDF page 12.
- **Exact question:** whether Wulbert's non-monotone `L1[0,1]` Korovkin
  theorem has an analogue for continuous sublinear operators.
- **Status:** candidate full counterexample to the direct analogue; likely
  valid, wording-scope review requested.
- **Model:** `GPT5.6`.

Let `T_n(f)=|f|` for every `n`.  This is a norm-one, 1-Lipschitz continuous
sublinear map under the source's pointwise-order definition.  It fixes every
nonnegative function, hence Wulbert's test functions `1,x,x^2`, exactly.  All
test convergence therefore holds even in norm and `||T_n||=1`.  Nevertheless
`T_n(-1)=1`, so the distance to `-1` is constantly 2.

More generally, no family contained in the positive cone can be a Korovkin
test family for all continuous sublinear contractions: the modulus map fixes
the entire positive cone and is not the identity.

Scope: the source uses the informal phrase "an analogue."  This packet fully
refutes the direct analogue obtained by replacing Wulbert's linear maps with
continuous sublinear maps while retaining his hypotheses.  It does not rule
out a repaired theorem that also tests negative functions or assumes
asymptotic oddness.

Files:

- `solution_packet.pdf` -- source-backed proof and scope audit.
- `source_paper.pdf` -- arXiv:2206.14102.
- `supporting_paper_2403.03476.pdf` -- later primary restatement of Wulbert's
  exact three hypotheses.
- `figures/open_question_crop.png` -- source question on PDF page 12.
- Attempt: `attempts/2206.14102_sublinear_wulbert_counterexample_upgrade.md`.
- Ledger:
  `ledger/results/2206.14102_absolute_value_sublinear_korovkin_counterexample.json`.
