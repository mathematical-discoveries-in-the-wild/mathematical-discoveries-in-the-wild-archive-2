# Candidate full solution: two moving observations of the periodic beam

Source: Philippe Jaming and Vilmos Komornik, *Moving and oblique
observations of beams and plates*, arXiv:1903.07804, later published in
*Evolution Equations and Control Theory* 9 (2020), 447--468.

Status: `candidate_full_likely_valid`.

Open Question (iv) asks whether the inverse observability inequality (4.8)
holds for every pair of distinct non-integer rational velocities. The packet
gives an affirmative answer, strengthened to every pair of distinct
non-integer real velocities.

The source reduces failure to a coordinate-sharing cycle among lattice points
on two circles. If a cycle is written alternately as
`(x_i,y_i)` on the first circle and `(x_{i+1},y_i)` on the second, subtracting
and summing the circle equations gives `sum x_i=sum y_i`. Summing the first
circle equations then forces the sum of all coordinate squares to vanish,
contradicting the exclusion of the origin.

Main review files:

- `solution_packet.pdf`
- `main.tex`
- `verification.md`
- `figures/open_problem_crop.png`
- `code/cycle_search.py`
- `source_paper.pdf`

Ledger record:
`runs/fa_banach_001/ledger/results/1903.07804_no_coordinate_cycles_beam_observability.json`.
