# Source problem and exact scope

Source: Konrad J. Swanepoel, *Sets of unit vectors with small subset sums*,
arXiv:1210.0366v2, published in Transactions of the AMS 368 (2016),
7153-7188.

The source defines `Cbar(k,d)` as the maximum, over all `d`-dimensional real
Banach spaces, of the size of a family of unit vectors for which every sum of
exactly `k` distinct members has norm at most one.

The exact relevant source statements are:

> Theorem 26. `Cbar(k,d)=max{k+1,2d}` in the following cases: ...
> `(3) d=6 and k in {3,4,5,...,10} union {17,18,19,...}`, and
> `(4) d=7 and k in {3,4,5,...,12} union {41,42,43,...}`.

> Conjecture 28. `Cbar(k,d)=k+1` whenever `k>=2d-1`.

This packet proves the two exact values immediately below the displayed
large-`k` ranges:

```text
Cbar(16,6)=17 and Cbar(40,7)=41.
```

It does not prove Conjecture 28 in general and does not address the source's
separate weak-balancing or strict-convexity questions.
