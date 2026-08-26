# Discrete-kernel l1/l2 counterexample

Status: `candidate_counterexample_likely_valid` / full disproof of Conjecture
4.1 in arXiv:2409.11679 as stated.

Take the normalized delta kernel on the discrete Polish space of positive
integers. Its RKHS is `ell2`, while embeddings of finite signed measures have
exactly `ell1` coefficient sequences. A continuous target-dependent quadratic
cost makes `(1/n)` the unique regularized optimizer. This vector lies in
`ell2 \ ell1`, so it cannot be represented by one finite signed measure,
although its finite truncations give the approximating measures proved to
exist in the source paper.

Files:

- `solution_packet.pdf`: complete counterexample and verification bounds.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv:2409.11679 PDF.
- `figures/open_problem_crop.png`: full-width crop of PDF page 13 containing
  Conjecture 4.1.
- `code/check_counterexample.py`: optional finite-truncation sanity check;
  not used in the proof.
- `verification.md`: review checklist and artifact hashes.

Human review priority: confirm the source's standard finite-measure convention
and that its deliberately broad cost assumptions allow target-dependent
quadratic weights. The packet explicitly notes that narrower loss classes may
still admit a positive representer theorem.
