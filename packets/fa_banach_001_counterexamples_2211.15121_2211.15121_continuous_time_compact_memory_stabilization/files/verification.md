# Verifier report

Date: 2026-08-17

Verdict: `likely valid`, suitable for human review as a candidate counterexample to the continuous-time suspicion following Example 5.3 of arXiv:2211.15121v3.

## Hypothesis audit

- On the complex Hilbert space $H=H_0\oplus\mathbb C$, $A(y,a)=(y,0)$ is bounded and generates $(e^{tA})(y,a)=(e^t y,a)$.
- $A-I$ has infinite-dimensional kernel, $A$ itself is Fredholm, and $A-\lambda I$ is invertible off $\{0,1\}$; hence $\sigma_e(A)=\{1\}$.
- $K(y,a)=(0,\sqrt{\|y\|})$ is continuous. Its image on any bounded set is bounded in a one-dimensional subspace, hence precompact.
- The term $G(y,a)=(-2|a|^2y/(\|y\|+|a|^2),0)$ is continuous and satisfies $\|G(y,a)\|\le2|a|^2\le2\|(y,a)\|^2$.

## Well-posedness audit

- The first component is $y'=q(t)y$ with $|q(t)|\le1$. If $y(0)=0$, Gronwall forces $y\equiv0$ and then $a$ is constant.
- If $y(0)\ne0$, the scalar-coefficient equation keeps $y$ nonzero and on its initial ray. The reduced variables $s=\|y\|$, $u=\operatorname{Re}a$, and $v=\operatorname{Im}a$ solve a locally Lipschitz finite-dimensional system on $s>0$.
- The bounds $s(0)e^{-t}\le s(t)\le s(0)e^t$ and $u'=\sqrt{s}$ exclude finite-time blow-up. Thus all solutions are unique and global despite the failure of local Lipschitz continuity of the full vector field at zero.

## Stability audit

With $w=\sqrt{s}$, one has $w'=(q/2)w$, $u'=w$, $v'=0$, and therefore $dw/du=q/2$ while $w>0$.

- During $u<0$, $dw/du\le1/2$ bounds $w$ until $u$ reaches zero, if it ever does.
- For $u\ge0$, $D=u^2+v^2-w^2$ satisfies $D'=2uw+D w^2/(w^2+u^2+v^2)\ge0$ whenever $D\ge0$, so that region is invariant.
- Before entry, $dw/du\le1/2$ forces entry within an increase of $2w_*$ in $u$, with $w_1\le2w_*$.
- After entry, $w$ is non-increasing. Once $u\ge\sqrt3 w_1$, $q\le-1/2$ and $dw/du\le-1/4$, so $u$ can increase by at most another $4w_1$.
- These estimates yield $w\le2B$, $|u|\le12B$, and $|v|\le B$ for $B=w(0)+|u(0)|+|v|$. For initial Hilbert norm $\eta\le1$, $B<(5/2)\sqrt\eta$, which implies the advertised bound $\sup_t\|x(t)\|<50\sqrt\eta$.

## Computational check

`code/simulate_reduced.py` integrates the exact reduced $(w,u,v)$ system for deterministic phases and logarithmically spaced initial norms. It checks the theoretical stability envelope and prints the largest sampled ratio. This is only a regression/sanity check; the phase-plane inequalities above are the proof.

The final run tested 960 trajectories with initial norms $10^{-1},\ldots,10^{-10}$, six allocations between the unstable and memory components, and sixteen complex phases. The largest sampled value of $\max_t\|x(t)\|/\sqrt{\|x(0)\|}$ was `5.19160781`; every sample satisfied the proved constant `50`.

## Scope audit

The memory map is only $1/2$-Holder at zero and is neither locally Lipschitz nor Frechet differentiable there. The packet does not settle variants requiring that extra regularity. It does settle the natural continuous-time analogue at the continuity and compactness level explicitly used in the source's discrete counterexample.

## Novelty and render audit

The bounded novelty search is recorded in the packet. No later explicit resolution was found. The final five-page PDF was rendered at 150 dpi and inspected page by page. The source image contains the complete quoted suspicion, the continuous equation, and the source's stability definition. No clipping, overlap, broken formula, undefined reference, undefined citation, or overfull box remains.
