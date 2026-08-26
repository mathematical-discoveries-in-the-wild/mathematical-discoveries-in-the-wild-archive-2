"""Rigorous interval certificate for the d=5 orbit-5a deformation.

This reconstructs the exact Scott--Grassl radical fiducial, applies the finite
Clifford/displacement normalization in the packet, builds the Zauner-block
constraint map, and encloses a nonzero 3-by-3 Jacobian minor.  mpmath.iv uses
outward-rounded interval arithmetic.
"""
from mpmath import iv

iv.dps = 60
R = iv.mpf


class C:
    """Minimal complex interval class (avoids an mpmath.iv conjugation bug)."""

    def __init__(self, real=0, imag=0):
        self.r, self.i = R(real), R(imag)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, C) else C(value)

    def __add__(self, other):
        other = C.coerce(other)
        return C(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-C.coerce(other))

    def __rsub__(self, other):
        return C.coerce(other) - self

    def __mul__(self, other):
        other = C.coerce(other)
        return C(
            self.r * other.r - self.i * other.i,
            self.r * other.i + self.i * other.r,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = C.coerce(other)
        denominator = other.r * other.r + other.i * other.i
        return C(
            (self.r * other.r + self.i * other.i) / denominator,
            (self.i * other.r - self.r * other.i) / denominator,
        )

    def __rtruediv__(self, other):
        return C.coerce(other) / self

    def __pow__(self, power):
        if power < 0:
            return (C(1) / self) ** (-power)
        result, factor = C(1), self
        while power:
            if power & 1:
                result = result * factor
            factor = factor * factor
            power //= 2
        return result

    def conj(self):
        return C(self.r, -self.i)

    @property
    def real(self):
        return self.r

    def __repr__(self):
        return f"({self.r}) + i*({self.i})"


I = C(0, 1)
w3, w5 = iv.sqrt(3), iv.sqrt(5)
w15 = w3 * w5
r1 = iv.sqrt(w5 / 2 + R(5) / 2)
r2 = iv.sqrt(
    ((-w3 + w5 + 3) * r1) / 8
    + w15 / 8
    + 5 * w3 / 8
    + w5 / 16
    - R(5) / 16
)

# The exact unnormalized fiducial in sicsymbolic_5a.txt (arXiv:0910.5784).
p0 = C(16 * r1)
p1 = C(
    ((-6*w15-6*w3+8*w5+24)*r1+(-12*w15-20*w3+12*w5+40))*r2
    +(4*w5-8)*r1-4*w15-4*w5,
    ((8*w3-10*w5-2)*r1+20*w3-16*w5)*r2
    +((2*w5+2)*r1+(2*w5+10)),
)
p2 = C(
    ((2*w15-2*w3+4*w5-12)*r1-2*w5-10)*r2
    +(w5+3)*r1+3*w15-5*w3-2*w5+10,
    ((16*w3-14*w5+6)*r1+(-2*w15+30*w3-24*w5))*r2
    +((w15-5*w3+4)*r1-3*w5+5),
)
p3 = C(
    ((2*w15+2*w3-2*w5-18)*r1+20*w3-12*w5)*r2
    +(3*w5-1)*r1-2*w15,
    ((-6*w15-6*w3+6*w5+14)*r1+(-8*w15-20*w3+16*w5+20))*r2
    +((w15+5*w3-2*w5+6)*r1+4*w15-2*w5),
)
p4 = C(
    ((-4*w3-4)*r1+2*w15-10*w3+2*w5-10)*r2
    +(-w15+5*w3+2*w5)*r1+3*w15+5*w3+w5+5,
    ((-8*w15+12*w3-12*w5+32)*r1+(-10*w15+10*w3-6*w5+30))*r2
    +((-2*w15+w5+3)*r1+w15+5*w3+3*w5+5),
)
phi = [p0, p1, p2, p3, p4]
norm2 = sum((x.conj() * x for x in phi), C(0))
tau = C(-(1 + w5) / 4, -iv.sqrt(10 - 2*w5) / 4)


def overlap_dagger(a, b):
    return sum(
        (phi[(j+a) % 5].conj() * tau**(b*(a+2*j)) * phi[j]
         for j in range(5)), C(0)
    ) / norm2


def old_m(a, b):
    if a % 5 == 0 and b % 5 == 0:
        return C(1)
    return 6 * overlap_dagger(a % 5, b % 5).conj() ** 2


def new_m(a, b):
    """Equation (normalization) in the packet."""
    aa, bb = (3*a+b) % 5, (2*a+b) % 5
    return tau ** (-4 * ((4*b-a) % 5)) * old_m(aa, bb)


base = [new_m(0, 1), new_m(0, 2), new_m(1, 2), new_m(1, 3)]

# Finite check of the claimed four-phase pattern.  Exact equality follows by
# simplifying the displayed radical expressions; interval containment is a
# reproducible independent guard against transcription or normalization errors.
pattern_labels = (
    (0, 1, 2, -2, -1),
    (1, -1, 3, 4, 3),
    (2, -3, -2, 4, 4),
    (-2, -4, -4, 2, 3),
    (-1, -3, -4, -3, 1),
)
for row in range(5):
    for column in range(5):
        label = pattern_labels[row][column]
        expected = C(1) if label == 0 else (
            base[label-1] if label > 0 else 1 / base[-label-1]
        )
        difference = new_m(row, column) - expected
        assert 0 in difference.r and 0 in difference.i


def zero():
    return [[C(0) for _ in range(5)] for _ in range(5)]


def eye():
    result = zero()
    for j in range(5):
        result[j][j] = C(1)
    return result


def add(a, b):
    return [[a[r][c] + b[r][c] for c in range(5)] for r in range(5)]


def scale(x, a):
    x = C.coerce(x)
    return [[x * a[r][c] for c in range(5)] for r in range(5)]


def mul(a, b):
    return [[sum((a[r][j] * b[j][c] for j in range(5)), C(0))
             for c in range(5)] for r in range(5)]


def adjoint(a):
    return [[a[c][r].conj() for c in range(5)] for r in range(5)]


def trace(a):
    return sum((a[j][j] for j in range(5)), C(0))


def displacement(a, b):
    result = zero()
    for j in range(5):
        result[(j+a) % 5][j] = tau ** (b*(a+2*j))
    return result


labels = pattern_labels

# A = I/5 + sum_j (x_j C_j + conjugate(x_j) C_j^*).
coefficients = []
for label in range(1, 5):
    coefficient = zero()
    for a in range(5):
        for b in range(5):
            if labels[a][(3*b) % 5] == label:
                coefficient = add(coefficient, scale(R(1)/5, displacement(a, b)))
    coefficients.append(coefficient)

a_matrix = scale(R(1)/5, eye())
derivatives = []
for phase, coefficient in zip(base, coefficients):
    star = adjoint(coefficient)
    a_matrix = add(a_matrix, add(scale(phase, coefficient), scale(1/phase, star)))
    derivatives.append(scale(I, add(scale(phase, coefficient), scale(-1/phase, star))))

u_matrix = [[tau ** ((2*r*r+4*r*s) % 5) / w5 for s in range(5)]
            for r in range(5)]
omega = C(-R(1)/2, w3/2)
u_squared = mul(u_matrix, u_matrix)
p_zero = scale(R(1)/3, add(add(eye(), u_matrix), u_squared))
p_one = scale(R(1)/3, add(add(eye(), scale(omega**2, u_matrix)),
                                scale(omega, u_squared)))

jacobian = [
    [trace(mul(p_zero, b)).real for b in derivatives],
    [trace(mul(p_one, b)).real for b in derivatives],
    [trace(mul(p_one, add(mul(a_matrix, b), mul(b, a_matrix)))).real
     for b in derivatives],
]

# Determinant of columns 0,2,3; the second phase is the local parameter.
a, b, c = jacobian[0][0], jacobian[0][2], jacobian[0][3]
d, e, f = jacobian[1][0], jacobian[1][2], jacobian[1][3]
g, h, k = jacobian[2][0], jacobian[2][2], jacobian[2][3]
determinant = a*(e*k-f*h) - b*(d*k-f*g) + c*(d*h-e*g)

print("base phase enclosures:")
for phase in base:
    print(phase)
print("all 25 normalized entries match the four-phase pattern")
print("Jacobian rows:")
for row in jacobian:
    print(*row)
print("det(columns 0,2,3) =", determinant)
