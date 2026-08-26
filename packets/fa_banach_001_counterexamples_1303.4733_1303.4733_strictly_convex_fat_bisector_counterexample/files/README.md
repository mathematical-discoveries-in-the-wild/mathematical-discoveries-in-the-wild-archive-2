# Strictly convex fat-bisector counterexample

Status: `candidate_counterexample` (`likely valid`; human review requested)

Source: Daniel Reem, *Topological properties of sets represented by an inequality involving distances*, arXiv:1303.4733v2, Section 5, PDF page 11.

The source conjectures that strict convexity alone admits counterexamples to Theorem 3.3. This packet gives one on a strictly convex equivalent norm of real `ell_1`:

```text
||x||_* = ||x||_1 + (sum_n 2^{-n} x_n^2)^{1/2},
A = {e_n},
P = {(e_n+e_m)/2 : n != m}.
```

The sites are closed and satisfy `d_*(P,A)=1`. Also `d_*(0,P)=d_*(0,A)=1`, while the whole ball `B_*(0,1/2)` is contained in `dom(P,A)`. Thus the origin is an interior equality point and is not on the boundary, contradicting the boundary and interior conclusions of Theorem 3.3 under strict convexity.

Files:

- `main.tex`: self-contained proof and bounded novelty report.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: real source-page crop containing the conjecture.
- `code/verifier.py`: deterministic finite numerical sanity check.
- `VERIFICATION.md`: verifier report and proof-audit checklist.

Run the checker with:

```bash
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/counterexamples/1303.4733_strictly_convex_fat_bisector_counterexample/code/verifier.py
```

Human-review focus: check the tail limit for `(e_n+e_m)/2` and the radicand gap `2^{-n}(3/4-x_n)>0` for `||x||_*<1/2`.
