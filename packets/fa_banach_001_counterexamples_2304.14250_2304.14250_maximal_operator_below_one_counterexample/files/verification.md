# Verification record

Date: 2026-08-11

Status: candidate full counterexample to the direct interpretation, likely
valid, subject to human review.

## Mathematical audit

- The source defines discrete `A_p` only for `p>1`; therefore its `p<1`
  signal is formally underspecified.
- Any direct extension including the constant weight necessarily implies the
  unweighted `ell^p` inequality.
- The source explicitly recalls that the discrete Hardy--Littlewood maximal
  operator is bounded on `ell^{p0}(w)` for every `p0>1` and every discrete
  `A_{p0}` weight, with characteristic-dependent norm.
- A monotone envelope of that dependence meets the source's increasing
  control-function convention.
- For `e_1`, the initial interval `{1,...,n}` gives `M e_1(n)>=1/n`.
- The p-series diverges for every `0<p<=1`, while `||e_1||_p^p=1`.
- The same example is a counterexample in the source's family-of-pairs
  formulation, independent of operator linearity.

## Upgrade attempts

1. Located the exact signal in the abstract and Introduction.
2. Audited the target notation and found that `A_p` is not defined below one.
3. Extracted the minimal necessary unweighted consequence of any direct
   extension.
4. Tested the discrete maximal operator, which satisfies the strongest
   relevant `p0` premise and has an explicit harmonic tail on a point mass.
5. Lifted the obstruction to the family-of-pairs formalism used by the paper.
6. Checked stronger `A_infinity`-input and restricted-sequence variants and
   recorded why the counterexample does not reach those different theorems.

## Literature audit

- The cheap indexes contained no hit for arXiv:2304.14250 or the exact signal.
- The locally parsed source itself states the discrete weighted maximal
  theorem used in the proof and cites its primary 2021 source.
- Exact local and bounded primary-source web searches found arXiv:2603.06109,
  which concerns quasi-nonincreasing sequences and a different weight class;
  its main extrapolation is upward and does not answer the source signal.
- The novelty statement is bounded; the elementary obstruction should be
  viewed chiefly as a precise clarification of an underspecified question.

## Artifact audit

- The archived arXiv source is compiled locally after commenting out its
  unavailable proprietary `tcilatex.tex` compatibility input; no body command
  depends on that file.
- The source page containing the open signal is rendered and embedded.
- The packet is compiled twice and checked for LaTeX errors, undefined
  references, and overfull boxes.
- Every final PDF page and the embedded source page are rendered at high
  resolution and visually inspected.

## Human-review focus

Check that the intended discrete maximal operator includes initial intervals
and that the phrase “the case `0<p<1`” was meant to retain an unweighted
strong-type conclusion. The counterexample is decisive for that direct
interpretation; it intentionally does not claim to settle every possible
reformulation.
