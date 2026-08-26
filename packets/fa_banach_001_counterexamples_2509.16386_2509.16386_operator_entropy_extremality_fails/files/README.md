# Counterexample packet: operator entropy extremality fails

Status: **candidate full counterexample to the closing operator-level
assertion; likely valid; human review required**

Source: Daniel Lazarev, *Stokes' theorem as an entropy-extremizing duality*,
arXiv:2509.16386, closing paragraph on PDF page 5.

## Result

Using the direct extension of the paper's entropy to an alternative operator,
namely `S*(D omega,M)`, the exterior derivative does not maximize entropy.

On `M=[0,1]`, a smooth family of local first-order linear operators

`D_e g = d(a_e g)`

is constructed with `a_e(0)=a_e(1)=1`.  Hence every `D_e` satisfies the
Stokes identity for every smooth input.  For `omega(x)=x`, however,

`D_e omega=(1+e sin(2 pi x)) dx`.

Its source entropy is strictly positive, whereas `d omega=dx` has entropy
zero.  Thus `d` is not a maximizer; for this input it is a minimizer.

Locality alone does not rescue the claim.  If competitors are additionally
required to be derivations (Leibniz rule), global Stokes compatibility forces
the operator to equal `d`, making uniqueness vacuous rather than entropic.

## Files

- `main.tex`: self-contained counterexample and rescue-condition dichotomy.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/operator_claim.jpg`: source page 5 crop.
- `code/verify_counterexample.py`: symbolic and high-precision audit.
- `verification.md`: source, proof, novelty, and rendering audit.

Ledger: `runs/fa_banach_001/ledger/results/2509.16386_operator_entropy_extremality_fails.json`.
