from fractions import Fraction


def diagonal_mass_of_uniform_cyclic_group(order: int) -> Fraction:
    # There are `order` diagonal pairs, each of product mass 1/order^2.
    return Fraction(1, order)


orders = [2, 3, 5, 10, 100, 1000]
masses = [diagonal_mass_of_uniform_cyclic_group(n) for n in orders]
assert all(masses[i + 1] < masses[i] for i in range(len(masses) - 1))
assert diagonal_mass_of_uniform_cyclic_group(10**6) == Fraction(1, 10**6)

print("normalized finite-group diagonal masses:")
for n, mass in zip(orders, masses):
    print(f"  C_{n}: {mass}")
print("nonatomic compact-group limit: 0; conjectural d=1 right side: 1")

