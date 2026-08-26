# Projection-support formula for Hilbert--Schmidt closure

This packet gives a candidate partial answer to Question 4.14 of
arXiv:2511.23121.  Its main result is the exact formula

```text
e^hsc = 1 - join { s_A(omega_xi) : xi is trace class and e xi = 0 },
```

where `A = M tensor M^op` acts on the Hilbert--Schmidt space and
`s_A(omega_xi)` is the support projection of the vector functional on
`A`.  It also classifies every finite-corank projection when `M=B(H)`.

Files:

- `main.tex`: mathematical write-up.
- `solution_packet.pdf`: rendered solution packet.
- `verification.md`: proof, source, scope, and render audit.
- `source_paper.pdf`: arXiv:2511.23121v1, retained for verification.

Status: candidate partial result, likely valid; independent expert review is
requested before treating the claimed formulation as new.
