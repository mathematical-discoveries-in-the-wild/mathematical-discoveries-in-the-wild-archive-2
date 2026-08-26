# Fourier-normal local maximality for Züst's coefficient kernel

Status: **candidate substantial partial result, likely valid pending expert
review**.

Source: Roger Züst, *The Riemannian hemisphere is almost calibrated in the
injective hull of its boundary*, arXiv:2104.04498v2 (2021; revised 2025),
Question 2 on PDF page 48.

The packet proves three exact facts about the question's functional:

- at the north pole, its quadratic form is diagonal in odd Fourier modes with
  eigenvalue `-(pi^2/2)(n-1)` on mode `n`;
- every embedded open-hemisphere profile is stationary in all smooth
  antiperiodic directions;
- after removing the first Fourier mode, the north pole is a strict nonlinear
  local maximizer, with a quantitative Fourier gap.

This does **not** prove the global inequality, nor the global equality
characterization.  Eight focused upgrade attempts are recorded in the packet
and in `attempts/2104.04498_kernel_fourier_upgrade_attempts.md`.

Files:

- `solution_packet.pdf`: expert-facing statement and proof;
- `source_paper.pdf`: original arXiv paper;
- `figures/open_problem_crop.png`: real crop of Question 2, PDF page 48;
- `code/verify_kernel.py`: numerical formula checks (not part of the proof);
- `verification.md`: proof audit and review priorities.

