"""Deterministic sanity checks for the depth-barrier packet.

This verifies exact algebraic identities and bookkeeping used in the proof.
It does not attempt to computationally verify the VC-dimension or
semialgebraic-dimension theorems.
"""

from fractions import Fraction
from math import floor


def lrelu(x: Fraction, alpha: Fraction) -> Fraction:
    return x if x >= 0 else alpha * x


def verify_relu_simulation() -> None:
    alphas = [Fraction(1, 7), Fraction(2, 5), Fraction(4, 5)]
    samples = [Fraction(n, 11) for n in range(-30, 31)]
    for alpha in alphas:
        for x in samples:
            reconstructed = (
                lrelu(x, alpha) + alpha * lrelu(-x, alpha)
            ) / (1 - alpha * alpha)
            assert reconstructed == max(x, 0)


def verify_parameter_bound() -> None:
    # Maximize over all scalar input/output width profiles in small cases and
    # compare with the uniform n*w*(w+3) bound. Each hidden unit is charged two
    # activation parameters, covering stepped LReLU families.
    for width in range(1, 8):
        for depth in range(1, 9):
            dims = [1] + [width] * (depth - 1) + [1]
            affine = sum(
                dims[i] * (dims[i - 1] + 1) for i in range(1, depth + 1)
            )
            activation = 2 * sum(dims[1:-1])
            assert affine + activation <= depth * width * (width + 3)


def verify_floor_capacity_obstruction() -> None:
    # h_A(x)=floor(Ax)-2 floor(floor(Ax)/2) extracts an arbitrary bit string
    # on geometrically spaced points x_i=2^(i-N). This is realizable by a
    # width-two network with FLOOR and identity, showing why finite-piece VC
    # bounds cannot simply be extended to FLOOR.
    patterns = [
        [0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 0],
    ]
    for bits in patterns:
        count = len(bits)
        a = sum(Fraction(bit, 2**i) for i, bit in enumerate(bits, start=1))
        weight = (2**count) * a
        outputs = []
        for i in range(1, count + 1):
            x = Fraction(2**i, 2**count)
            first = floor(weight * x)
            outputs.append(first - 2 * floor(Fraction(first, 2)))
        assert outputs == bits


def main() -> None:
    verify_relu_simulation()
    verify_parameter_bound()
    verify_floor_capacity_obstruction()
    print("ReLU-to-LReLU identity: exact on 183 rational cases")
    print("parameter bound: checked for widths 1..7 and depths 1..8")
    print("FLOOR bit extraction: checked on four six-bit labelings")


if __name__ == "__main__":
    main()
