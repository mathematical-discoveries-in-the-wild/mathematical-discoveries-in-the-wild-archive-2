# Sampling/density moment bridge for unbounded multigraphons

Status: `candidate partial; likely valid`.

For the open-ended question in Section 4.4 of Kunszenti-Kovács--Lovász--
Szegedy (arXiv:1406.7846), this packet proves three linked statements for
genuine probability-valued multigraphons:

- conditional on convergence of all finite sample laws, full node-and-edge
  density convergence is equivalent to convergence of the one-edge bond
  moments;
- node-and-edge density convergence implies finite-sample convergence when
  the limiting bond moment sequence is Stieltjes-determinate;
- under one uniform exponential moment, the two convergence notions are
  equivalent.

Two examples show why the mechanisms are genuine: rare spikes give sampling
convergence without density convergence, while alternating distinct
integer-valued laws with identical moments gives density convergence without
sampling convergence.

The source question is broad, and the packet does not classify every
moment-indeterminate family or solve the measurable-representative problem for
quotient-valued moment graphons. It is therefore promoted conservatively as a
substantial partial result.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: locally rebuilt original arXiv paper.
- `figures/open_problem_crop.png`: source page 32, question and obstacles.
- `figures/open_problem_scope_crop.png`: source page 33, expected-settings
  sentence.
- `code/make_open_problem_crops.py`: reproducible crop generator.
- `verification.md`: proof, source, build, hash, and visual-QA report.
- Ledger: `ledger/results/1406.7846_sampling_density_moment_bridge.json`.
