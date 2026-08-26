# Analytic data, nonanalytic persisted orbit

This packet gives a candidate full counterexample to the natural question in
Remark 6.5 of arXiv:2103.05203. It constructs a three-dimensional analytic
state-dependent-delay equation, arbitrarily close to an analytic ODE with a
nondegenerate limit cycle, whose unique nearby periodic orbit is smooth but
not analytic.

The proof uses an expansive fixed point of the induced time map and an exact
rational Taylor certificate. Run:

```bash
conda run --no-capture-output -n sandbox python code/rigorous_certificate.py
```

The script performs all finite coefficient arithmetic with Python
`fractions.Fraction`; the PDF proves the infinite tail estimates.

Files:

- `solution_packet.pdf`: complete statement, construction, and proof.
- `main.tex`: packet source.
- `code/rigorous_certificate.py`: exact finite certificate and tail checks.
- `verification.md`: independent audit record.
- `attempts.md`: eight progressively deeper attempts.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: source question crop.
