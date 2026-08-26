# Superconservative Hilbert bases are unconditional for constant coefficients

Status: `candidate_substantial_partial_likely_valid_human_review_needed`

Source question: Miguel Berasategui, Pablo M. Berná, and Silvia Lassalle,
*Strong partially greedy bases and Lebesgue-type inequalities*,
arXiv:2001.01226v2, Remark 2.5 (PDF page 7).

## Result

Let `(x_n)` be a semi-normalized Schauder basis of a Hilbert space, let
`Delta` be its superconservative constant, and let `K` be its basis constant.
If

```text
a = inf_n ||x_n|| > 0,    b = sup_n ||x_n|| < infinity,
```

then the basis is superdemocratic, quantitatively:

```text
||1_(epsilon A)||
 <= sqrt(3) Delta^2 (1+K) (b/a) ||1_(delta B)||
```

for all finite sets `|A| <= |B|` and all signs. In particular it is
unconditional for constant coefficients. The Schauder assumption can be
weakened to bounded tail suppression on constant-coefficient vectors.

The packet also proves that in a Banach space of type `p` and cotype `q`, a
semi-normalized superconservative Schauder basis satisfies

```text
gamma_m <= C m^(1/p-1/q).
```

The Hilbert theorem is the matched-exponent case `p=q=2`.

## Proof mechanism

Random signs on a later set produce a signed sum of norm at most `b sqrt(m)`;
superconservativeness transfers this upper estimate to any earlier signed
set. For the denominator, split its support into ordered first and last
halves. Random signs make some first-half sum at least `a sqrt(m/3)`, and
superconservativeness transfers that lower estimate to the prescribed signs
on the last half. The Schauder tail projection then compares the last half
with the original denominator.

## Limitation

The unrestricted Markushevich-basis question remains open. Without a bounded
tail projection, a large prescribed last-half sum can in principle cancel
against the first half in the complete signed sum. Eight focused upgrade
attempts did not remove this obstruction or produce a counterexample. The
source's second question—whether every partially greedy Markushevich basis is
quasi-greedy—also remains open.

## Files

- `solution_packet.pdf`: theorem, proof, type/cotype extension, audit, and limitations.
- `source_paper.pdf`: arXiv:2001.01226v2.
- `figures/open_problem_crop.png`: source Remark 2.5.
- Attempt log: `runs/fa_banach_001/attempts/2001.01226_superconservative_ucc_hilbert.md`.

Human review should focus on the ordered-halves denominator estimate and the
quantifiers in the superconservative definition. No computational dependency
is used.
