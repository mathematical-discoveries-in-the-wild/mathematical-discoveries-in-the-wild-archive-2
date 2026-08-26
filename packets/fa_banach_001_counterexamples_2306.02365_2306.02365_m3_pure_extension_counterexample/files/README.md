# arXiv:2306.02365 — a pure-extension counterexample in M3

Status: candidate full negative resolution; high validity confidence and
moderate novelty confidence.

The source proves that every unital subspace of M2 has the pure extension
property, recalls a failure in M4, and explicitly leaves the M3 case open.
This packet gives an elementary counterexample that generates the full ambient
algebra.

Let

    H = E11 + E22,
    X = E13 + E31,
    Y = E23 + E32,
    A = H + iX,
    B = H + iY.

Then M = span{I,A,B} is a three-dimensional unital subspace of M3 and
C*(M)=M3. The e1 and e2 vector states agree on M. Their common restriction is
the unique maximizer of

    psi -> Re((psi(A)+psi(B))/2),

so it is exposed and pure, while the two vector states are distinct pure
extensions to M3. Thus M fails the pure extension property.

The packet also proves the stronger self-adjoint statement: the
four-dimensional operator system

    S = M + M* = span{I,H,X,Y}

generates M3 and has the same exposed pure state with two distinct pure
extensions.

- Proof packet: solution_packet.pdf
- Source paper: source_paper.pdf
- Open-question crop: figures/open_problem_crop.png
- Optional exact-matrix checker: code/verify_m3_counterexample.py
- Attempt audit: runs/fa_banach_001/attempts/2306.02365_m3_pure_extension_counterexample.md
- Ledger: runs/fa_banach_001/ledger/results/2306.02365_m3_pure_extension_counterexample.json

The bounded novelty sweep checked the arXiv record, the 2025 published paper,
exact M3/pure-extension queries, and later operator-system work surfaced by
those queries. No later exact answer was found. A specialist citation search
is still recommended before any public priority claim.

