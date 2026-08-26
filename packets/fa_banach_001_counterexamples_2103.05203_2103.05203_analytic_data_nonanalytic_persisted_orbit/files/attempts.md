# Upgrade attempts

1. **Literature-boundary audit.** Located the exact question in Remark 6.5
   and checked Mallet-Paret--Nussbaum (time-dependent delay) and Hu (a special
   state-dependent system). Neither answers the source's general persistence
   question.

2. **Direct autonomization of a published nonanalytic periodic example.** A
   clock variable turns a time-dependent delay into a state-dependent one,
   but the published homogeneous example is resonant and does not visibly
   select the source theorem's unique local persisted branch. This route was
   retained as motivation but not used as the proof.

3. **Stable forced scalar equation.** Replaced resonance by
   `y'+y=sin(t)+epsilon*y(eta(t))`. The inverse of `D+1` has sup norm one,
   so this has a unique periodic solution for `|epsilon|<1` and directly
   matches a locally unique persisted orbit.

4. **Numerical obstruction probe.** FFT fixed-point iteration and 100 Taylor
   coefficients for `eta=t+sin(t)` showed normalized coefficients converging
   far from zero, including a homogeneous sensitivity calculation. This was
   exploratory only and is not used in the proof.

5. **Exact-rational finite certificate.** Expressed every Taylor coefficient
   through order 30 as an affine rational function of `y(0)`. The contraction
   bound on `y(0)` separates `w_30` from zero uniformly.

6. **Globally bounded analytic delay repair.** Replaced the affine delay by
   `r=2*pi-arctan(v)`, so the delay is positive, globally bounded, and real
   analytic. Recomputed the full rational certificate; the obstruction grew
   to a margin above 227.

7. **Symbolic infinite-tail bound.** Factored
   `eta(t)=2t(1+u(t))`, bounded `u` on `|t|=1/2`, used Cauchy estimates and
   log-convexity in the degree defect, and proved the total omitted displacement
   is below `0.001` (actual certified bound about `1.39e-5`).

8. **Arbitrarily-small-parameter upgrade and source matching.** Proved the
   obstruction is holomorphic on the punctured unit parameter disc and is not
   identically zero, so nonanalytic parameters occur arbitrarily close to
   zero. Audited the Floquet multipliers and local uniqueness to identify the
   constructed orbit with the source's persisted branch.
