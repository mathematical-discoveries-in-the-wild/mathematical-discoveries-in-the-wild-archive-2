# S-matrix conjecture through all dimensions n >= 158

Status: `candidate_partial_likely_valid`.

The source target is Roman Drnovsek, *On the S-matrix conjecture*,
arXiv:1306.6786v2. It proves the conjecture for odd dimensions and gives a
strictly weaker estimate for even dimensions. Frankel and Urschel later proved
the conjecture for every `n >= 1000` in arXiv:2409.04354 / Linear Algebra and
its Applications 708 (2025), 193--203.

This packet makes a new quantitative upgrade to the later argument. Their
structural Lemma 3.2 is stated with a free integer parameter `t`, but their
final projection contradiction fixes `t=50`. Keeping `t` free and retaining a
lower bound for the variance of the projected coordinates gives a stronger
general projection lemma. Rigorous 80-digit interval arithmetic verifies its
hypotheses for every even `158 <= n <= 998`. Combining this finite range with
Frankel--Urschel for `n >= 1000` proves the conjectured lower bound for every
`n >= 158`. Together with Drnovsek/Cheng, the conjecture is therefore known for
all odd dimensions, `n=2`, and all dimensions `n >= 158`.

The remaining scope is exactly the even dimensions
`n = 4, 6, ..., 156`. This is a partial result, not a full solution.

Verification:

```bash
conda run --no-capture-output -n sandbox python code/verify_cutoff.py
```

The script certifies 421 even dimensions. Its weakest positive lower endpoint
is approximately `2.579293062736265e-4` at `(n,t)=(160,23)`.

Files:

- `solution_packet.pdf`: review packet.
- `source_paper.pdf`: original arXiv:1306.6786 source paper.
- `supporting_paper_2409.04354.pdf`: decisive later structural theorem.
- `figures/open_problem_crop.png`: exact conjecture statement from source PDF
  page 2.
- `code/verify_cutoff.py`: interval certificate for the finite parameter range.
- `code/make_crop.py`: reproducible crop script.

Ledger:
`runs/fa_banach_001/ledger/results/1306.6786_s_matrix_even_n_ge_158.json`.

