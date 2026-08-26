# The am-infinity cancellation envelope of every principal ideal is finite rank

Status: `full_solution_likely_valid`

## Source question

Victor Kaftal and Gary Weiss, “A survey on the interplay between arithmetic
mean ideals, traces, lattices of operator ideals, and an infinite Schur-Horn
majorization theorem,” arXiv:0707.3271 (2007), Question 7 on PDF page 24.

For

`widehat(I)^infinity = intersection { J : J_{a_infinity} contains I_{a_infinity} }`,

the authors ask whether `widehat(I)^infinity` is principal for principal
`I=(xi)`, and whether it has an explicit generator.

## Result

For every nonzero principal ideal `I` of `B(H)`,

`widehat(I)^infinity = F`,

where `F` is the finite-rank ideal. Thus Question 7 has a full affirmative
answer, with a generator independent of `xi`: any nonzero finite-rank operator
generates `F` as a two-sided ideal.

## Proof intuition

The arithmetic mean at infinity only controls tails. A prescribed tail mass
can be spread over an arbitrarily long constant block, making the block height
as small as desired. Given any infinite-rank test sequence `rho`, choose those
blocks diagonally so that their heights defeat every possible ampliation
`D_m` in the criterion for `rho` to belong to a principal ideal.

For a summable generator `xi`, replacing each block by its average increases
all tail sums, so the resulting principal ideal still qualifies in the
intersection. For a nonsummable generator, long low plateaux with mass at
least one per block remain nonsummable, so their arithmetic-mean-at-infinity
ideal is the same universal ideal `se(omega)`. In either case the qualifying
principal ideal omits the prescribed `rho`. Hence no infinite-rank operator
survives the intersection, while every nonzero ideal contains `F`.

## Verification

- The proof separately treats finite-rank, summable infinite-rank, and
  nonsummable generators.
- In the summable case, ordered block averages form a decreasing summable
  sequence and dominate every tail sum of `xi`.
- If membership `rho <= C D_m eta` is proposed, the construction chooses a
  later block `k >= m`, `k > C`; evaluation at `m q_k` contradicts it.
- In the nonsummable case, each plateau has mass at least one, while its height
  tends to zero, so the constructed generator is compact but not trace class.
- The only substantive external input is Kaftal-Weiss Lemma 4.7
  (arXiv:0707.3169), identifying `(xi)_{a_infinity}` for summable and
  nonsummable principal generators.
- Verdict: `likely valid`, confidence 93/100. No computation is used.

## Bounded novelty search

On 9 August 2026, the run’s registry, solution, attempt, and proof-gap indexes
were searched for arXiv:0707.3271, the exact Question 7 language, and the core
am-infinity cancellation-envelope terms. The local parsed-source corpus was
also searched for notation and phrase variants. Web searches used the exact
question, `widehat I^infinity`, “arithmetic mean at infinity cancellation,”
and the authors’ names. They found the source’s 2007 multipaper series and the
2012 paper on majorization and arithmetic mean ideals, but no separate paper
answering Question 7. This is a bounded search, not a guarantee of novelty.

## Files

- `main.tex`: full theorem, proof, verification notes, and references.
- `solution_packet.pdf`: compiled human-review packet.
- `source_paper.pdf`: arXiv:0707.3271.
- `supporting_paper_0707.3169.pdf`: source of the decisive principal-ideal
  arithmetic-mean-at-infinity identity.
- `figures/open_problem_crop.png`: Question 7 on source PDF page 24.
- Attempt and adversarial verification:
  `runs/fa_banach_001/attempts/0707.3271_am_infinity_cancellation_envelope_full_attempt.md`.

## Human review recommendation

Prioritize the tail-domination inequality for block averages, the use of
Lemma 4.7 in both infinite-rank cases, and the diagonal argument against every
fixed ampliation `D_m`. Also confirm the source’s finite-rank convention for
`F_{a_infinity}=F`.

