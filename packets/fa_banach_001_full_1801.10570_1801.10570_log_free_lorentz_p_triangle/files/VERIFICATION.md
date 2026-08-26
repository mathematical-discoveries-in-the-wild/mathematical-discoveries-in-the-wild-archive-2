# Verification report

## Mathematical audit

- Matched the source normalization
  `||f||_{p,r}^r=(r/p) integral [t^(1/p) f*(t)]^r dt/t` throughout.
- Recomputed the common-cutoff weak endpoint from distribution functions;
  optimization at `beta=p alpha` gives exactly
  `D_p=p^(-1)(1-p)^(-1/p)`.
- Checked the flat-level case in the nonatomic rank construction by spreading
  each positive-measure level set across its full rearrangement interval.
- Verified directly that the factorization gives
  `||u||_p^p=(1-theta)||f||_{p,r}^r` and weak norm of `v` at most one.
- Audited the reciprocal rescaling of every factor pair, including all powers
  of `theta`, `1-theta`, `p`, and `r`.
- Checked the two-threshold product rearrangement and its integration after
  the change of variables `s=a t`.
- Optimized its splitting parameter at `a=1-theta` and independently reduced
  the resulting constant to the binary-entropy expression.
- Checked the endpoint limits: the refined constant tends to one as `r` tends
  down to `p`, and to the proved weak endpoint constant as `r` tends to
  infinity.
- Checked the extension from finite-support simple positive functions to
  arbitrary complex and countable families using lattice monotonicity and
  Fatou.
- Verified the absolute simplification using
  `H(theta)<=2` and `p^(-p theta)<=exp(1/e)`.

## Route and novelty audit

- The exact target was checked in arXiv:1801.10570, after equation (13) and in
  Appendix B.
- The run's cheap indexes contained no prior result, packet, attempt, or proof
  gap for this arXiv id or the sharp constant problem.
- Exact-phrase, title, author, and keyword searches through 2026-08-13 found
  the source and older strong/weak endpoint literature, but no later explicit
  removal of the logarithm.
- A formal complex-interpolation route was not used in the packet because
  quasi-Banach endpoint closure and norm-equivalence constants would obscure
  the quantitative claim.  The rank factorization gives the needed estimate
  directly.
- Novelty remains provisional pending expert literature review.

## Packet/render QA

- `main.tex` was compiled repeatedly with `pdflatex -halt-on-error`; the
  final log has no undefined references, overfull boxes, or mathematical
  compilation warnings.
- The final five-page PDF was extracted with Ghostscript text output and
  checked for the theorem statement, logarithm-removal conclusion, section
  headings, endpoint audit, and references.
- Every final page was rendered to PNG at 135 dpi and visually inspected.
  No clipping, overlap, missing glyphs, malformed spacing commands, or
  illegible formulas remain.
