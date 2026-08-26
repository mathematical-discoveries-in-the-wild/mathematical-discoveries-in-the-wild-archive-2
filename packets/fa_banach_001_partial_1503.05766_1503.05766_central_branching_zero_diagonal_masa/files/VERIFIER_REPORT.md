# Verification Report

## Claim checked

The central-obstruction theorem in `main.tex`: a Zorn-maximal zero-diagonal
abelian algebra is diffuse and, for separable predual, must be a MASA whenever
the expectation of `T` onto the center of its relative commutant vanishes.

## Verdict

Likely valid. Confidence: 86/100. Send to human review as a partial result.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Zorn upper bound | valid | `E_A(T)=0` is equivalent to `tau(Ta)=0` for every `a` in `A`; this survives the `L^2` closure of a chain. |
| Removal of atoms | valid | In an atomic corner `pMp`, normalized trace of `pTp` is zero; replacing `Cp` by the source's diffuse zero-diagonal algebra strictly enlarges `A` without changing the pairing. |
| Relative-commutant localization | valid | `S=E_N(T)` has the same pairing with every subalgebra of `N`; expectation composition is used in the correct direction. |
| Center-valued fiber reduction | valid | `E_Z(S)=0` gives scalar trace zero in almost every factor fiber. Matrix and `II_1` fiber conclusions are correct. |
| Measurable assembly | external but standard | With separable predual, the unit balls are standard Borel fields; projection, trace, and compression constraints are Borel and have nonempty closed fibers. Recursive measurable selection gives a decomposable abelian algebra. This is the main human-review point. |
| Strict extension | valid | The assembled algebra contains `Z`, hence `A`; if `N` is larger than `A`, it can be chosen larger on a positive central summand. |
| Conditional Lyapunov corollary | valid under stated hypothesis | The selected central projection has conditional mass `1/2` and zero conditional `g`-moment, so both atoms of `A vee {q}` have zero conditional `T`-moment. |

## Counterexample search

The included verifier exhausts all ranks of projections in
`M_2(C) direct_sum C` for the stated central element. It confirms that only
zero and identity have zero pairing. This does not contradict the theorem;
it shows why the hypothesis `E_Z(T)=0` cannot simply be dropped.

## Gaps and limits

- The result assumes separable predual for the measurable-field lemma.
- It does not prove that a suitable maximal algebra has vanishing central
  expectation, nor does it construct a counterexample when this fails.
- Relative atomlessness is used through the conditional Lyapunov theorem of
  Dynkin--Evstigneev, now cited explicitly in the packet; a reviewer should
  still confirm the standard two-coordinate conditional-vector-measure
  specialization.

## Recommended human action

Check the Borel selection of the dyadic projection trees and the conditional
Lyapunov formulation. If both are accepted, retain as a rigorous structural
reduction rather than a full solution.
