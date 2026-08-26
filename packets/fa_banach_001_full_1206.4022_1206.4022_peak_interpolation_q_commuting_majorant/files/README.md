# Peak interpolation with a q-commuting majorant

Status: **candidate full solution, likely valid**

Source: David P. Blecher and Charles John Read, *Operator algebras with
contractive approximate identities II*, arXiv:1206.4022v4, Corollary 5.4 and
Remark 2 on source PDF page 14.

The paper asks whether its one-sided peak interpolation theorem remains true
when the positive invertible majorant `d` is only required to commute with the
peak projection `q`, instead of the peak element `a`. The answer proved in this
packet is affirmative.

Let `E=oa(1,a)`, let `J={h in E:hq=0}`, and put `f=d^(-1/2)`. The proof works
in the cyclic weighted operator space

`X=closure(b E f)`, with `Y=closure(b J f)`.

The assumptions imply that every `q`-column from `X` has range orthogonal to
every `(1-q)`-column from `X`. Right multiplication by `1-q` is therefore an
M-projection on `X**`, and its range is exactly `Y**`. Thus `Y` is an M-ideal,
so it is proximinal and

`dist(bf,Y)=||bfq||<=1`.

An attaining `y in Y` gives `x=b-yf^(-1) in A`, with `xq=bq` and
`||xf||<=1`, hence `x^*x<=d`.

Packet contents:

- `main.tex` and `solution_packet.pdf`: full theorem and proof
- `source_paper.pdf`: local source PDF
- `figures/source_question_crop.png`: rendered source evidence
- `code/verify_core.py` and `code/verification_output.txt`: finite-matrix
  sanity checks of the mixed-product and max-norm mechanism
- `VERIFIER_REPORT.md`: proof audit and review priorities

Novelty check: bounded local-index and primary-source searches through
2026-08-13 used the exact question, commutation variants, arXiv:1211.5010, and
arXiv:1407.1356. No later answer was found, and the 2018 source version retains
the question. Novelty confidence is moderate, not certified.

Human review should focus on the cyclic weighted-space lemma: the realization
of `X**` in `B**`, persistence of fixed range orthogonality, and the identity
`X**(1-q)=Y**`. The remaining normalization is direct.
