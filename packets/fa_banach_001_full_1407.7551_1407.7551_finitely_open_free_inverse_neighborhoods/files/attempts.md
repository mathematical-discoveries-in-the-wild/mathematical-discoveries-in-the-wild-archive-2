# Upgrade attempts

1. **Exact extraction and duplicate check.** Located the question immediately
   after Proposition 5.5 and searched the run indexes for the arXiv id and the
   phrases “finitely open”, “G-free sets”, and “inverse function theorem”.  No
   existing run result answered it.

2. **Uniform inverse theorem.** Compared the question with the source's own
   uniformly-open theorem and with Abduvalieva--Kaliuzhnyi-Verbovetskyi.  Those
   results require a uniform nc ball/completely bounded control, absent here,
   so they do not settle the finitely-open problem.

3. **Fine-topology global theorem.** Used Pascoe's fine inverse theorem to
   reduce the issue to finding a finitely open nc neighborhood of zero on which
   the derivative is nonsingular everywhere.  The theorem itself assumes that
   nonsingularity on the whole domain and therefore does not supply the missing
   neighborhood.

4. **Analytic-germ gluing.** Investigated formal and analytic inverse germs,
   including the 2019 local theory of nc germs.  Levelwise convergence alone
   does not visibly make the convergence domain open at forced direct sums;
   polynomial-identity terms can be invisible on the block diagonal.  This
   route therefore left the original compatibility gap.

5. **Counterexample search with polynomial identities.** Tried to exploit
   Amitsur--Levitzki identities and rapidly growing, level-selective terms to
   make inverse radii collapse.  The obstruction is that the derivative at a
   finite direct sum decomposes into diagonal and pairwise off-diagonal block
   channels; repetitions do not introduce new channels.  This defeated the
   proposed counterexamples and suggested a pairwise criterion.

6. **Pairwise derivative criterion.** Proved that if every summand derivative
   and every two-summand derivative is invertible, then the derivative at the
   whole finite direct sum is invertible.  Block sign matrices split the tangent
   space into diagonal channels and one channel for every unordered pair of
   summands.

7. **Compact size induction.** Constructed precompact orthogonal/unitary
   invariant neighborhoods level by level.  At level n, the compact forced set
   consists of all conjugates of direct sums of the previously chosen closed
   neighborhoods.  Pairwise compatibility holds on this compact set, hence on
   a sufficiently small invariant open neighborhood.  This gives a finitely
   open compact-group-free domain with nonsingular derivative everywhere.

8. **GL upgrade and stress test.** Took the full GL-similarity envelope of the
   compact-group domain.  It remains finitely open, free, inside the original
   domain, and preserves derivative nonsingularity.  The standard block
   collision identity then proves injectivity, while the classical inverse
   theorem makes the image open and the inverse C^r.  Exact-phrase, citation,
   fine-topology, and nc-germ searches through 12 August 2026 found no later
   source explicitly resolving the question.
