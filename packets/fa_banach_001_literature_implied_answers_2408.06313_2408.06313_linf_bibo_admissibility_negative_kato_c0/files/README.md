# Kato's c0 example gives a negative answer to Remark 5.9

Status: `literature_implied_answer (full negative answer)`

## Source question

Felix L. Schwenninger and Alexander A. Wierzba, *A dual notion to BIBO
stability*, arXiv:2408.06313, Proposition 5.8 and Remark 5.9 (arXiv PDF page
12).

For the identity-output system

`Sigma(A,B,I,(lambda I-A)^(-1)B)`,

Proposition 5.8 identifies `C^infinity`-BIBO stability with infinite-time
`C`-control-admissibility. Remark 5.9 asks whether the analogous equivalence
holds with `L^infinity` on both sides.

## Full negative answer

The Kato diagonal semigroup recorded in Example 2.3 of Jacob--Schwenninger--
Wintermayr, *A refinement of Baillon's theorem on maximal regularity*,
arXiv:2008.00459, gives a counterexample after a direct identification.

Take `X=U=c0`,

`A(x_n)=(-n x_n)`, `T(t)(x_n)=(exp(-nt)x_n)`, and `B=-A_{-1}`.

Then the zero-state identity output has coordinates

`x_n(t)=n int_0^t exp(-n(t-s)) u_n(s) ds`.

At almost every `t`, the Banach-valued Lebesgue differentiation theorem shows
that this sequence tends to zero, while its supremum is at most
`||u||_infinity`. Hence the system is `L^infinity`-BIBO stable with constant
one. This is also precisely the `L^infinity`-maximal-regularity property that
the supporting paper records for Kato's example.

However, Example 2.3 supplies an `L^infinity([0,tau],c0)` input whose endpoint
state has every sufficiently large coordinate equal to
`exp(-1/2)-exp(-1)>1/5`. The endpoint state is not in `c0`, so `B` is not
`L^infinity`-control-admissible.

Thus `L^infinity`-BIBO stability does not imply `L^infinity` control
admissibility, and the proposed analogue is false.

## Provenance and scope

The diagonal example, maximal-regularity fact, explicit bad input, and failure
of admissibility are all already in arXiv:2008.00459. The contribution of this
packet is the exact identification with Remark 5.9 and an explicit a.e.-output
argument in the system-node language. No new counterexample is claimed.

The broader Outlook question in arXiv:2408.06313—whether the three BIBO notions
are equivalent for arbitrary systems—is not settled by this example; here all
three BIBO notions hold. The packet also notes that the proposed equivalence
does hold when the state space is reflexive, because bounded endpoint limits
can then be recovered by weak compactness.

Files:

- `source_paper.pdf`: arXiv:2408.06313.
- `supporting_paper_2008.00459.pdf`: paper containing Kato's example.
- `main.tex`, `solution_packet.pdf`: detailed identification and proof.
