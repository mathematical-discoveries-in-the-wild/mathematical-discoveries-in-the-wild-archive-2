# Verification report

Verdict: **candidate full affirmative answer to Problem 2.7; likely valid**.

## Independent checks

1. With the unitary Fourier convention, the scale-`j` translate coefficients
   are exactly the Fourier-series coefficients of the `2^j`-periodization.
   Parseval therefore gives the packet's identity with no missing scale factor.
2. Since the Fourier support lies in `(-2^j,2^j)`, a fundamental interval
   contains only the positive frequency `x` and the negative frequency
   `x-2^j`.  Splitting at `b2^j` and `(1-b)2^j` gives the three displayed
   integrals exactly.
3. For `t=2^m r`, `1<r<2`, and `1/8<b<=1/6`, only powers
   `2^(m+1)`, `2^(m+2)`, and possibly `2^(m+3)` are active.  The third occurs
   iff `r>8b`; the first is an edge below `2(1-b)` and a pin above it.
4. If `r<8b<=4/3`, the two neighboring mantissas are `4-2r` and
   `2-r/2`, both at least `8b`.  Thus the unpinned degree-two class is
   independent outside null boundary fibers.
5. Orienting an edge from the larger magnitude `t` to the smaller one forces
   its dyadic sum `P` into `(t/(1-b),2t)`.  This interval has ratio strictly
   below two, hence contains at most one power of two.  Out-degree is at most
   one, and the edge reflection is Lebesgue-measure preserving.
6. The two boundary estimates are algebraically independent:
   `B>=h` follows from the degree identity and internal-edge bound;
   `2l<=3h+B` follows from independence of the low-degree class.  Splitting at
   `l=2h` gives `B>=(l+h)/3` in both cases.
7. Layer cake turns the measured boundary inequality into the absolute
   difference of squared moduli.  Cauchy--Schwarz, the diamagnetic inequality,
   and total incidence at most three give the stated lower bound `1/54`.
8. The reverse estimate uses only `|z-w|^2<=2(|z|^2+|w|^2)` and gives upper
   bound `6`.  Hence the form is both bounded and bounded below on a dense
   class and extends to all of `L^2`.

## Endpoint audit

At `b=1/6`, the mantissa `r=4/3` is a null boundary fiber.  It indeed carries
an unpinned degree-two chain, as the exact-rational exploratory script shows,
but the frame inequality is an almost-everywhere statement and the measured
Cheeger proof discards only a countable union of such points.  Any non-null
one-sided neighborhood falls into the degree classification used in the
proof.

## Computational role

`attempts/code/1905_08230_alias_graph_probe.py` was used only to discover and
stress-test the graph structure.  No numerical eigenvalue or floating-point
claim appears in the proof.
