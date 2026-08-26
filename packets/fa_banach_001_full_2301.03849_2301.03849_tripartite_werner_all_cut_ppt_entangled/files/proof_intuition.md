# Proof intuition

Tripartite Werner states form a five-dimensional convex body.  Eggeling and
Werner coordinatize it by two scalar weights `r_plus,r_minus` and a Bloch
vector `(r_1,r_2,r_3)` of radius at most
`r_0=1-r_plus-r_minus`.  In these coordinates both PPT and separability across
one bipartition are given by explicit quadratic inequalities.

The source paper's known examples are symmetric under a transposition of two
systems.  That symmetry forces PPT to coincide with separability for the
corresponding cut and blocks an all-cuts example.  The construction here uses
instead only cyclic symmetry.  Setting `r_1=r_2=0` makes the state invariant
under the three-cycle, so every bipartition has the same PPT and separability
status.  Keeping `r_3` nonzero breaks every transposition symmetry and evades
the obstruction quoted in the source.

At the rational point `(3/4,1/32,0,0,3/16)`, the state and PPT inequalities
hold with room to spare, but the relevant biseparability quadratic is violated
strictly.  One exact calculation therefore proves PPT entanglement for one
cut, and cyclic symmetry proves it simultaneously for all three.
