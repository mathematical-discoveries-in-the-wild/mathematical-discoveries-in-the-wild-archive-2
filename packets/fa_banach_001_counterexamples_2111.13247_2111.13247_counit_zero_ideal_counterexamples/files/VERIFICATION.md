# Verification report

Status: `PASS` as a proof-level structural audit; human review remains
required by the solution-packet protocol.

## Audit checklist

1. **Example exists.** For a nonamenable discrete group `Gamma`, the compact
   dual quantum group `G=hat Gamma` is noncoamenable. Taking
   `Gamma=F_2` is concrete.
2. **Counit is admissible.** The universal counit is a unital character,
   hence a norm-one positive functional and convolution idempotent (indeed,
   the convolution unit). Thus it is a contractive idempotent in `M^u(G)`.
3. **Multiplier range.** The counit identity gives
   `M^l_{epsilon^u}=id`, so its range is all of `L^infinity(G)`.
4. **Compact quasi-subgroup.** Under the source's correspondence between
   idempotent states and compact quasi-subgroups, the counit corresponds to
   the whole von Neumann algebra `N=L^infinity(G)`.
5. **Zero ideal has a brai.** Both `J^1(N)=N_perp` and the annihilator of the
   multiplier range are `{0}`. The constant net `e_i=0` is bounded and
   satisfies `f*e_i -> f` for the only `f` in the ideal, namely `f=0`.
6. **Counit is not reduced.** If `epsilon^u` belonged to `M^r(G)`, it would
   factor through the reducing morphism. This is the existence of a reduced
   counit and implies coamenability, contradicting the choice of `G`.
7. **Question 5.3.** Its hypothesis holds but its conclusion fails.
8. **Question 5.4.** Its ideal has a brai while `G` is not coamenable, so the
   proposed equivalence fails.

## Computational verification

None is applicable. The example follows directly from the unit/counit
identities and the definitions.

## Reviewer focus

Check conventions: (i) a compact quasi-subgroup is allowed to be the whole
algebra, and (ii) approximate identities are allowed for the zero ideal.
Both are standard and neither is excluded in the source questions. A repaired
proper/nonzero version remains open here.
