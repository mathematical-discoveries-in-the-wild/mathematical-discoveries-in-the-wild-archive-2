# SRD detailed balance does not imply GNS detailed balance

Status: `candidate full counterexample likely valid`

Source: Cao--Lu--Lu, arXiv:1810.00906, Remark IV.5(2), source PDF page 23.

The packet gives a three-parameter family of primitive qubit GKSL generators
that are self-adjoint for every sandwiched-Renyi weight but not for the GNS
weight.  The smallest displayed instance uses rates `(a,b,c)=(1,3,1)` and has
stationary state `diag(2/3,1/3)`.

Core mechanism: all SRD weights agree on the oppositely oriented coherences
`E01,E10`, whereas GNS weights them by different stationary probabilities.  A
Pauli-X dissipator mixes those coherences and separates the two notions.

Files:

- `main.tex`, `solution_packet.pdf`: human-readable proof packet.
- `source_paper.pdf`: original arXiv source.
- `figures/open_problem_crop.png`: source question crop.
- `code/verify_counterexample.py`: independent matrix calculation.
- `code/verification_output.txt`: saved verifier output.

Human review should check the weighted-adjoint convention and the two
off-diagonal GNS weights.  The exact block calculation makes both checks local.

