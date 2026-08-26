# Verification record

## Exact source question

- Source: Shibananda Biswas, Gargi Ghosh, E. K. Narayanan, and Subrata
  Shyam Roy, arXiv:2409.11101.
- PDF page 20, Section 4.3: asks whether the trivial and sign weighted
  Bergman submodules are similar for general `n` and `lambda`, then proves
  only `n=2`, `lambda=1,2`.
- PDF page 21, Remark 4.22: states the general Vandermonde division question
  and again records only `n=2`, `lambda=1,2`.
- The packet contains readable full-width crops of both passages and retains
  the complete 23-page source PDF.

## Mathematical audit

- Symmetric polynomials are dense in the trivial module.
- After dividing the sign module by the Vandermonde, symmetric polynomials
  are also dense, because anti-symmetric polynomials are dense and every
  anti-symmetric polynomial is Vandermonde times a symmetric polynomial.
- Hence a bounded module isomorphism and its inverse are multiplication by
  symmetric holomorphic functions `psi` and `h` with `h psi=1`.
- The projected kernels are the permanent and determinant kernels,
  respectively. The divided determinant kernel extends across collisions.
- On the full diagonal, the exact kernel-norm ratio is
  `sqrt(c_n_lambda) (1-|a|^2)^(-n(n-1)/2)`.
- Adjoint multiplier estimates force `h(a,...,a)` to decay uniformly on
  every circle like a positive power of `1-|a|^2`; maximum modulus forces it
  to vanish, contradicting `h psi=1`.
- The same kernel divergence makes the canonical Vandermonde multiplier
  non-surjective by the open mapping theorem.

## Computational audit

- `code/verify_confluent_kernel.py` checks the mixed-derivative determinant
  identity exactly with SymPy for eleven `(n,lambda)` pairs, with
  `2 <= n <= 5` and `lambda` among `1, 2, 5/2`.
- Command:
  `conda run --no-capture-output -n sandbox python code/verify_confluent_kernel.py`.
- Result: all eleven exact checks passed.
- These finite symbolic checks audit the formula but do not replace the
  general proof.

## Novelty search

On 17 August 2026, bounded web and local-corpus searches used the source arXiv
id, exact title and authors, `trivial sign weighted Bergman similarity`,
`Vandermonde division polydisc`, and citation searches. They found no
all-parameter similarity or division answer. The strongest status evidence is
Jaydeb Sarkar's December 2025 survey arXiv:2512.20979, Section 1, which still
presents Vandermonde surjectivity/division on the polydisc as an open problem.

## Artifact QA

- `solution_packet.pdf` compiled to four A4 pages with no overfull or
  underfull boxes, unresolved references, or LaTeX warnings.
- All four final pages were rendered at 160 dpi and visually inspected. The
  source crops, formulas, theorem statements, and bibliography are legible;
  there is no clipping or overlap.
- Both source crops were inspected separately at original resolution.
- The result ledger parsed successfully with `python -m json.tool`.

## SHA-256

- `solution_packet.pdf`: `876c7780a72d25715131268cca73cee58d643c41b5460f2ce3ab0c6daf95668b`
- `source_paper.pdf`: `d61580c76179cd85429fced9aca8ebd1196f37b581fe1a6bc3520ff4c8f87fc6`
- `figures/open_problem_crop.png`: `5da18294fb3bcf94fcc9d1ef7f6e0e59807487710ad8c99758805a3366b8ef13`
- `figures/division_question_crop.png`: `e9e2224e957d193a914423b25b585460dcd6101b2fdf450022c1a0ea8dd52897`
- `code/verify_confluent_kernel.py`: `d703532e1fc3d23b2d2b6db5401ebf173d393fe2e9869e51cb0adb5c71d06d7f`
