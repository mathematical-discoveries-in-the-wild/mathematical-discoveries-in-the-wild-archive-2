# The standard word metric of B3 is not CND

Status: `candidate_counterexample_likely_valid`

Source: Paweł Józiak, *Conditionally strictly negative definite kernels*,
arXiv:1307.1778. The introduction says that, unlike the Coxeter case, the
question whether standard word metrics of general Artin groups are
conditionally negative definite remained unsolved.

## Counterexample

Let

```text
B3 = <a,b | aba=bab>
```

with its standard symmetric word metric. Put `A=a^-1`, `B=b^-1`, and order
the eight elements as

```text
ab, BA, Ab, bA, ba, AB, Ba, aB.
```

Their exact distance matrix is recorded in `main.tex` and verified in
`code/verify_b3_witness.py`. For coefficients

```text
(1,1,1,1,-1,-1,-1,-1)
```

the coefficient sum is zero but the distance quadratic form is `8 > 0`.
This violates the defining CND inequality. Thus the standard word metric of
the Artin group `B3` is not conditionally negative definite, refuting the
universal form of the source question.

## Exactness

Distances are certified through the injective coordinate consisting of the
classical `SL(2,Z)` representation of `B3` together with exponent sum. Since
all selected elements have word length two, enumerating the Cayley ball of
radius four is enough. The verifier uses only integer arithmetic and asserts
the full matrix and the quadratic form.

## Scope and novelty check

This is a counterexample, not a classification of Artin groups with CND word
metric. Cheap repository indexes contained no duplicate. Bounded web searches
for Artin/braid word metrics and conditional negative definiteness through
2026-08-11 found the source question but no later statement of this `B3`
witness. The mathematical certificate is exact; novelty remains subject to
expert literature review.

## Files

- `source_paper.pdf`: arXiv:1307.1778.
- `main.tex` and `solution_packet.pdf`: review packet.
- `code/verify_b3_witness.py`: exact finite verifier.
- `code/OUTPUT.txt`: checked output.

Ledger: `runs/fa_banach_001/ledger/results/1307.1778_b3_word_metric_not_cnd.json`.

