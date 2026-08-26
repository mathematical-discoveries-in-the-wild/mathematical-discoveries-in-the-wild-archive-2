# Literature-Already-Answered Packet: two positive-increase endpoint questions

Run: `fa_banach_001`

Result type: `literature_already_answered (two scoped questions)`

Status: a separate later paper explicitly extends the source paper's decay
theorems to every resolvent control function of positive increase.  This
settles the logarithmic-loss endpoint after Theorem 1.3(b) and the analogous
"slightly faster than a power" question at zero.  A third, unrelated converse
in Remark 4.8 remains unresolved after a separate eight-route attempt.

## Original problem source

- Charles J. K. Batty, Ralph Chill, and Yuri Tomilov, *Fine scales of decay of
  operator semigroups*, arXiv:1305.5365; J. Eur. Math. Soc. 18 (2016),
  853--929.
- First signal: PDF page 5, immediately after Theorem 1.3(b).
- Second signal: PDF page 6, immediately before Theorem 1.5.
- Local PDF: `source_paper.pdf`.

For `alpha>0` and `beta>=0`, Theorem 1.3(b) assumes

    ||(is+A)^{-1}|| = O(|s|^alpha (log |s|)^beta)

and obtains

    ||T(t)A^{-1}|| = O(t^{-1/alpha}
                           (log t)^{epsilon+beta/alpha})

for every `epsilon>0`.  The authors ask whether `epsilon=0` is valid.

At zero, the paper proves the scale with a negative logarithmic exponent and
says that characterizing decay when the resolvent grows slightly faster than
a power of `|s|^{-1}` remains open.

## Supporting answer source

- Jan Rozendaal, David Seifert, and Reinhard Stahn, *Optimal rates of decay
  for operator semigroups on Hilbert spaces*, arXiv:1709.08895; Adv. Math.
  346 (2019), 359--388.
- Explicit provenance statement: PDF page 3.
- Positive-increase definition and regularly varying inclusion: PDF page 6.
- Singularity at infinity: Theorem 3.2, PDF page 8.
- Singularity at zero: Theorem 3.6, PDF page 13.
- Local PDF: `supporting_paper_1709.08895.pdf`.

The supporting authors cite the source paper as reference [6], say that it
does not obtain the improved estimate for all regularly varying functions,
and state that their purpose is to extend its main results to all functions
of positive increase.  Thus they explicitly know the source/result chain;
this is not an agent-invented reformulation.

## Identification

Every regularly varying function of positive index has positive increase.  In
particular,

    M(s)=s^alpha (log s)^beta

has positive increase when `alpha>0`.  Theorem 3.2 of the supporting paper
therefore gives

    ||T(t)A^{-1}|| = O(1/M^{-1}(t))
                    = O(t^{-1/alpha}(log t)^{beta/alpha}),

which is exactly the source's requested `epsilon=0` conclusion.  Since
`M^{-1}(t)` is asymptotic, up to a constant, to
`t^(1/alpha)(log t)^(-beta/alpha)`, there is no hidden logarithmic loss.

Theorem 3.6 is the zero-frequency analogue.  Under the source's natural
spectral and high-frequency boundedness hypotheses, taking the same
`M(s)=s^alpha(log s)^beta` for the bound on `R(i/s,A)` yields

    ||T(t)A R(1,A)|| = O(t^{-1/alpha}(log t)^{beta/alpha}).

This supplies the missing faster-than-a-power direction.  With the minimal
resolvent envelope (or matching two-sided resolvent growth), the lower bounds
already discussed in the source give the corresponding sharp
characterization.

## Scope limitations

This packet clears only the two positive-increase/regular-variation questions
above.  It does **not** claim to settle source Remark 4.8, which asks whether
`||T(t)B||=O(t^{-1})` for an arbitrary bounded commuting `B` implies a uniform
first-resolvent bound.  That strict endpoint is documented in
`runs/fa_banach_001/attempts/1305.5365_semigroup_resolvent_converse_attempts.md`
and remains open here.

The supporting theorems are Hilbert-space results, matching the source
questions.  The zero-frequency statement retains its explicit assumptions:
the only imaginary-axis spectral point is zero and the resolvent is bounded
at high frequency.

## Verification and search evidence

- Same-paper check: the two source passages expressly state that the relevant
  endpoints are unknown/open in arXiv:1305.5365.
- Separate-source check: arXiv:1709.08895 is a distinct later paper, cites the
  source, describes the exact limitation, and explicitly announces the
  extension.
- Formula check: direct inversion of
  `M(s)=s^alpha(log s)^beta` gives the requested logarithmic exponent.
- Bounded searches included the exact question phrases, source theorem and
  remark numbers, the source citation in later papers, and the later
  Hilbert-space semigroup literature.  No evidence was found that Remark 4.8
  has been settled.

## Files

- `README.md`: this status and scope record.
- `main.tex`: compact review note.
- `solution_packet.pdf`: rendered review note.
- `source_paper.pdf`: original open-problem source.
- `supporting_paper_1709.08895.pdf`: decisive later answer source.

## Human review recommendation

Verify the two exact source locations (PDF pages 5 and 6), the explicit
provenance statement on supporting PDF page 3, and Theorems 3.2 and 3.6 on
supporting PDF pages 8 and 13.  In particular, keep the scoped literature
answer separate from the unresolved arbitrary-`B` converse.
