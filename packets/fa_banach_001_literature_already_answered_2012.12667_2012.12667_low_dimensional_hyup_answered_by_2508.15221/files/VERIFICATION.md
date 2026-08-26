# Verification

## Mathematical scope

- Source conjecture: arXiv:2012.12667, Remark 2.4, PDF page 5.
- Negative answer: arXiv:2508.15221, Theorem 1.1, PDF page 5.
- Explicit test: arXiv:2508.15221, proof on PDF pages 9--10.
- Remaining dimension: arXiv:2510.00453, Theorem 1.2, PDF page 3.
- All papers use the same quotient with `Delta u`, `grad u`, and
  `|grad u|^2/|x|` on `R^N`.
- Chen--Tang's test is the degree-one spherical harmonic
  `u(r sigma)=r exp(-r) phi_1(sigma)`, equivalent up to normalization to
  `x_1 exp(-|x|)`.

## Exact arithmetic

`verify_quotients.py` uses only integer and rational arithmetic.  It checks:

```text
N=2: Q=3/4 < target=9/4
N=3: Q=84/25 < target=4
N=4: Q=225/32 >= target=25/4
```

The first two lines refute the conjecture; the third explains why the same
test does not settle dimension four.

## Source evidence

- All full-page renders and crops in `evidence/` are RGB PNGs made directly
  from the official arXiv PDFs.
- `source_conjecture_crop.png` contains Theorem 2.3 and Remark 2.4.
- `support2508_theorem_crop.png` contains Chen--Tang Theorem 1.1.
- `support2508_test_crop.png` and `support2508_quotient_crop.png` contain the
  explicit test and exact Gamma-function quotient.
- `support2510_n4_crop.png` contains Huang--Ye Theorem 1.2.

## Packet QA

- `latexmk -pdf` completed successfully.
- Every final packet page was rendered to PNG in RGB mode and visually
  inspected.
- Page count and SHA-256 hashes are recorded after final sealing below.

## Sealed artifacts

- Final packet page count: 4.
- Final render mode: RGB for all four pages; all pages visually inspected.
- Sealed at: `2026-08-11T22:08:49Z`.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `solution_packet.pdf` | 753280 | `2748d7d6451a43acaeb07cfd7f86a012ac818f0dd87b012295dab9f9991a0f11` |
| `source_paper.pdf` | 277213 | `cb11b8ce3cf62e936ab736e2c528a64ed9a240e914487294e771ace45670e723` |
| `supporting_paper_2508.15221.pdf` | 432568 | `e954f13152c6243ef11851f4f510eb7b20a7251839459c35a79dde7942523f06` |
| `supporting_paper_2510.00453.pdf` | 406624 | `706fc17f03f5727b2e3cbf708e5b1c3622d0e5a3e5c75428f41821f5c58974bc` |
| `evidence/source_conjecture_crop.png` | 111930 | `ea83f0f2b16aeb149bfdc9e33ac32e8f702223e6eb123dae12cc1feec5f250e8` |
| `evidence/support2508_theorem_crop.png` | 123146 | `5e37f2c02ea57a7481c09573762fedd94ac18ea113d8f6e0098a5f4bc73275b4` |
| `evidence/support2508_test_crop.png` | 194539 | `083b733762d254b3fc439745fb421869b303552fdd086f8f3746f33cae838d94` |
| `evidence/support2510_n4_crop.png` | 174653 | `d2c837ef7c1c054cf9f53f9d000aa3d56dcda8da9c864e2a7f46cd22213e5fc7` |
| `verify_quotients.py` | 887 | `0d0fc7e4ac8bf1144b34707aa75e86a7db7162591ea32103f2b074f16f78f418` |
