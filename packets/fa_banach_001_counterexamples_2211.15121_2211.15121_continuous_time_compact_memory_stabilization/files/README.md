# Continuous-time compact-memory stabilization

**Status:** candidate counterexample (likely valid; human scope review requested)

After its stable discrete Example 5.3, arXiv:2211.15121 says that the authors lack a similar continuous-time construction and suspect that one may not exist. This packet gives an autonomous continuous-time example on $H_0\oplus\mathbb C$.

The bounded linear generator is $A(y,a)=(y,0)$, so its essential spectral bound is $1$. The compact memory map is $K(y,a)=(0,\sqrt{\|y\|})$, and the higher-order term is

$$
G(y,a)=\left(-\frac{2|a|^2}{\|y\|+|a|^2}y,0\right),
$$

which satisfies $\|G(x)\|\le 2\|x\|^2$. Nevertheless, the zero solution is Lyapunov stable; the proof gives $\sup_{t\ge0}\|x(t)\|\le50\sqrt{\|x(0)\|}$ for initial norm at most one.

The compact map is continuous but not locally Lipschitz at zero. The result therefore answers the source's continuity-level suspicion and leaves stronger regularity variants open.

- Main packet: `solution_packet.pdf`
- Source paper: `source_paper.pdf` (arXiv:2211.15121v3)
- Source evidence: `figures/open_problem_crop.png`
- Numerical sanity check: `code/simulate_reduced.py`
- Proof audit: `verification.md`
- Ledger: `runs/fa_banach_001/ledger/results/2211.15121_continuous_time_compact_memory_stabilization.json`
