# Verification record

The construction is checked in two independent layers.

1. Human-readable proof: main.tex lists all eight Gaussian-integer monomial
   Kraus matrices. The input-column and output-row moduli are permutations
   of 1 through 8, giving both normalizations with scalar 204. A specified
   leading 64-by-64 minor certifies the required bi-linear independence.

2. Exact executable certificate: run

       conda run --no-capture-output -n sandbox python verify_exact.py

   in this directory. The verifier uses only Python integer arithmetic. It
   represents Gaussian integers as integer pairs, reconstructs every Kraus
   product, checks both normalization matrices exactly, and reduces the
   specified determinant from Z[i] to F_101 via i -> 10. The result is 19,
   hence nonzero.

Expected output:

    sum_j W_j^* W_j = 204 I_6
    sum_j W_j W_j^* = 204 I_6
    leading 64-by-64 extremality minor modulo 101 = 19
    certificate verified

The source paper was compiled locally from the archived arXiv TeX. Its PDF
page 17 was rendered to the included PNG and visually checked.
