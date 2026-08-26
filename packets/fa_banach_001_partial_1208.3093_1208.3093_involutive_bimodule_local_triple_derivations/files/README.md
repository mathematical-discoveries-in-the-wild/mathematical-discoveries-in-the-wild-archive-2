# Local triple derivations into involutive bimodules

Status: `candidate_partial_likely_valid_full_involutive_bimodule_subcase`

Source: M. Burgos, F. J. Fernández-Polo, J. J. Garcés, and A. M.
Peralta, *Local triple derivations on C*-algebras*, arXiv:1208.3093,
Problem 1 and the related C*-algebra/continuity questions.

## Literature boundary

The later paper arXiv:1303.4569 completely answers the self-valued and
automatic-continuity questions: local triple derivations on complex
JB*-triples and C*-algebras are triple derivations, and local triple
derivations on real or complex JB*-triples are continuous. It explicitly
retains as Problem 2.7 the statement for a continuous local triple derivation
`E -> X` into an arbitrary Banach triple module.

Niazi--Miri (Tamkang J. Math. 49 (2018), DOI
`10.5556/j.tkjm.49.2018.2228`) prove the iterated-dual cases `A -> A^(n)`.
The targeted search found no full answer for arbitrary modules.

## New partial theorem

Let `A` be a unital C*-algebra and `X` any unital involutive Banach
`A`-bimodule. Equip `X` with either standard ternary module structure:

```text
type II:
  [x,a,b]=(x a* b + b a* x)/2,
  [a,x,b]=(a x# b + b x# a)/2;

type I:
  [x,a,b]=(x a b* + b* a x)/2,
  [a,x,b]=(a* x# b* + b* x# a*)/2.
```

Then every bounded local triple derivation `T:A->X` is a triple derivation.
No duality, reflexivity, or normality hypothesis is imposed on `X`. The
theorem contains the known iterated-dual cases and applies to arbitrary
involutive operator, dual, and reflexive bimodules.

The proof uses:

1. a two-stage orthogonal-form identity on commutative C*-subalgebras;
2. an ordered Arens extension to the commutative bidual;
3. the support projection of `b` to prove
   `(1-p)T(b)#(1-p)=0`;
4. Li--Pan's zero-product characterization of generalized derivations;
5. normalization at the unit, a unitary symmetry argument, and Johnson's
   theorem that bounded Jordan derivations from C*-algebras to Banach
   bimodules are associative derivations.

## Remaining scope

The arbitrary Jordan Banach triple-module problem remains open. General
triple modules need not lift orthogonality and need not have an involution or
one-sided bimodule products. Those are exactly the two structural tools used
by the proof.

## Files

- `main.tex`, `solution_packet.pdf`: theorem, proof, literature boundary, and
  source evidence.
- `source_paper.pdf`, `later_answer_paper.pdf`: the original and later
  papers.
- `figures/`: exact source-problem and later-answer crops.
- `code/verify_standard_modules.py`, `code/verification_output.txt`:
  independent matrix checks for both ternary structures.
- `verification_report.md`: proof and artifact audit.

Attempt record:
`runs/fa_banach_001/attempts/1208.3093_local_triple_derivations_module_upgrade.md`.

Ledger:
`runs/fa_banach_001/ledger/results/1208.3093_involutive_bimodule_local_triple_derivations.json`.
