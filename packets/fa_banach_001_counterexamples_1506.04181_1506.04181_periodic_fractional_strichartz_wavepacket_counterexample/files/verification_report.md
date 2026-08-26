# Verification report

## Mathematical checks

- [x] For `M~N^(1-alpha/2)`, one has `M=o(N)` for every `0<alpha<1`.
- [x] Taylor's theorem gives a uniform phase-remainder bound
  `O(N^(alpha-2)M^2)=O(1)`.
- [x] The moving tube has spacetime measure comparable to `1/M` on the full
  interval `[0,1]`.
- [x] All summand phases lie in a fixed arc, yielding pointwise size `cM`.
- [x] The resulting `L4` lower bound is `c M^(3/4)`.
- [x] Frequency comparability gives `||u_N||_H^gamma~N^gamma M^(1/2)`.
- [x] Combining the bounds forces `gamma>=1/4-alpha/8`.
- [x] At the proposed `gamma_0`, the estimate ratio diverges like
  `N^(alpha/8)`.
- [x] The result addresses the linear estimate, not the nonlinear threshold
  independently of that estimate.

## Source and novelty checks

- [x] Equation (33), both exponents, and the open question were checked in the
  rendered primary PDF and raw TeX.
- [x] The exact wording remains in the 2017 published version.
- [x] Bounded local and web searches found no prior explicit resolution.

## Artifact checks

- [x] LaTeX compiled without errors or warnings.
- [x] No overfull/underfull boxes or undefined references remain.
- [x] Extracted PDF text contains the theorem, packet, moving-tube estimate,
  sharp exponent, and scope limitation.
- [x] Every rendered packet page was visually inspected (three pages).
- [x] The open-question source crop was visually inspected.
- [x] File types, page counts, and SHA-256 values were recorded.

The final packet is a three-page US-letter PDF 1.7. The target is a 29-page
A4 PDF 1.4. SHA-256:

- `solution_packet.pdf`: `1f617dee2ba1ab41c2e762e1011949350a974411019afc00a553ef5746ce2212`
- `source_paper.pdf`: `7c7ac3e97506ac5815a0fbf764a4dbedbc87ddd88d6fd3fb0c22fa1e7318d22c`

## Human review

- [ ] Human expert review completed.
