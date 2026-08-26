# A two-valent Miniowitz map onto the punctured plane

Status: `candidate_counterexample_likely_valid`

The live question in arXiv:2309.12947 asks for quasiregular maps satisfying
the paper's Möbius-invariant multiplicity condition (M) and Miniowitz
estimate (Min), but not its radial omitted-set hypothesis—ideally omitting
only the origin.

The packet gives the explicit family

`F_m(z)=((1+z)/(1-z))^m`, `m>=3`.

Every member is 1-quasiregular and maps the disk onto the punctured plane.
It has valence at most `ceil(m/2)`, so (M) holds with `a=0`. A direct
pseudohyperbolic calculation proves (Min) after every disk recentering with
`C=1`, `alpha=m`. For `m=3` this is an at-most-two-valent example. The packet
also proves `F_m in H^p` exactly when `mp<1`.

Files:

- `solution_packet.pdf` — expert-facing proof packet
- `source_paper.pdf` — arXiv:2309.12947
- `main.tex` — packet source
- `verification.md` — mathematical and artifact audit
- `tmp/` — build and render QA artifacts

Attempt:
`runs/fa_banach_001/attempts/2309.12947_cayley_cube_min_counterexample.md`

Ledger:
`runs/fa_banach_001/ledger/results/2309.12947_cayley_power_min_example.json`
