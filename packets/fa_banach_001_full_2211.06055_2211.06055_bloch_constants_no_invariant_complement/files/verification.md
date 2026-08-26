# Verification report

Verdict: `candidate_full_negative_answer_likely_valid`

## Source-statement audit

Page 3 and footnote 1 of arXiv:2211.06055 ask whether one can find a
`\widetilde U_0`-invariant algebraic complement of the constants in the
classical Bloch space.  The packet proves nonexistence, without assuming that
the complement is closed or that its associated projection is continuous.

## Automorphism audit

For `C(z)=(1+z)/(1-z)` and `phi=C^{-1} o (2C)`, direct simplification gives

```text
phi(z)=(3z+1)/(z+3),        C(phi(z))=2C(z).
```

The Cayley map is a biholomorphism from the disk onto the right half-plane;
multiplication by 2 is an automorphism there.  Hence `phi` is a disk
automorphism.  It lies in the source action (or, equivalently, has a lift to
the universal covering group).

## Logarithm and Abel-equation audit

The right half-plane avoids the principal logarithm's branch cut.  Since 2 is
positive real,

```text
Log(2C(z))=log 2+Log(C(z))
```

with no `2 pi i` ambiguity.  Thus `h=Log(C)/log 2` is holomorphic and satisfies
`h o phi-h=1` identically.

## Bloch estimate audit

Differentiation gives

```text
h'(z)=2/((1-z^2)log 2).
```

The exact identity

```text
|1-z^2|^2-(1-|z|^2)^2=4(Im z)^2
```

implies `|1-z^2| >= 1-|z|^2`.  Therefore the Bloch seminorm of `h` is at most
`2/log 2`, so the crucial Abel function really belongs to the source space.

## Splitting audit

If `B=C1 direct-sum Y` and `Y` is invariant under the full group, the algebraic
projection `P` onto `C1` along `Y` commutes with every composition operator:
constants are fixed and the group maps `Y` onto itself.  Applying `P` to
`h o phi-h=1` gives `0=1`.  No boundedness, continuity, or closedness is used.

## Novelty audit

Bounded local-index and web searches on 2026-08-11 found no later answer to the
source footnote and no matching use of the hyperbolic Bloch Abel function for
this invariant-complement question.  The function and Abel-equation technique
are classical, so novelty confidence is moderate.

## Packet render audit

Final packet compiled without unresolved references or layout warnings.  All
four pages were rendered at 150 dpi and inspected individually on 2026-08-11;
the text, formulas, source-question crops, page breaks, and margins are clear
and unclipped.  SHA-256 of that build of `solution_packet.pdf`:
`8203392c70539726d983113846f233f819813396a51b8047667918e5be8a3f5d`.

## Human verifier focus

1. Confirm the source means invariance for the full `U_0` composition action.
2. Check that an invariant algebraic direct-sum complement forces the algebraic
   projection to commute with composition.
3. Recheck the principal-log identity on the right half-plane.

## Interrupted-lane recovery audit (2026-08-21)

The source's `lambda=0` action was checked to be composition (up to inverse),
so full automorphism invariance covers the displayed hyperbolic map and its
inverse. The Abel equation, principal-log branch, Bloch estimate, and
algebraic-projection contradiction were rederived independently. `main.tex`
was force-rebuilt to four pages. The log has no LaTeX errors, undefined
references, or overfull boxes. All pages were rendered at 120 dpi and visually
inspected with no clipping, overlap, malformed formulas, or unreadable
evidence. Legacy top-level render pages were moved under `tmp/`.

## Protocol structure QA (2026-08-21)

An explicit `Proof intuition` section now appears after the source evidence
and before the negative-answer theorem. The packet was force-rebuilt to four
pages; its final log has no LaTeX errors, undefined references, or overfull
boxes. All pages were rendered with Poppler at 130 dpi and visually inspected.
The source question, footnote, Abel-function intuition, proof, and margins are
readable and unclipped. SHA-256 of the final `solution_packet.pdf`:
`e016f9437c055606ba782d52a356c62c9a6631bf6a0c7933ad3bf978d5990d40`.
