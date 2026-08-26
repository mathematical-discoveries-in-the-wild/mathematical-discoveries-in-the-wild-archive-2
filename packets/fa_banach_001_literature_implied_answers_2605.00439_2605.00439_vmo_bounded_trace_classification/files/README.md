# VMO bounded-trace classification

Same-paper consequence clarifying the literal VMO existence bullet in
arXiv:2605.00439v3. This is supporting triage, not claimed as a new result.

The source's bounded weak-solution definition and Proposition 3.4(b) imply a uniform
`L^infinity((0,T) x R^n)` bound and distributional convergence to the initial
datum. Any such trace is necessarily in `L^infinity`. Conversely, the
source's Corollary 1.5 provides a bounded weak solution for every bounded
datum satisfying its range condition. Therefore the exact VMO trace class is
`VMO intersection L^infinity`.

The explicit function

`f(x) = log(log(e^e + |x|))`

is locally bounded, globally unbounded, and lies even in `CMO`, the BMO
closure of compactly supported smooth functions. Taking `a=I` and `O=R`
therefore gives a concrete heat-equation counterexample to any literal
extension to all VMO data.

Supporting deliverable: `solution_packet.pdf`.
