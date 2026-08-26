# Variable-coefficient order-zero operators on compact fractafolds are Calderón–Zygmund

Status: `candidate full solution, likely valid; needs human review`

Source: Marius Ionescu, Luke G. Rogers, and Robert S. Strichartz,
*Pseudo-differential Operators on Fractals*, arXiv:1108.2246. Section 9
conjectures that every variable-coefficient operator `p(x,-Delta)` of order
zero is Calderón–Zygmund. The displayed conjecture and its immediately
preceding kernel expansion are on source PDF page 27.

The source expands the variable symbol in an eigenbasis of the `x`-Laplacian
and proves that the resulting constant-coefficient kernels have a uniform size
bound. The same pieces actually have uniform *standard-kernel difference*
bounds by the source’s constant-coefficient theorem and the
Ionescu–Rogers Calderón–Zygmund criterion. The source’s eigenfunction
summability then adds these difference bounds absolutely, exactly as it adds
the size bounds. No multiplication closure for `dom(Delta)` is needed because
the cited Calderón–Zygmund definition asks for regularity in the kernel’s
`y`-variable.

The proof uses `(I-Delta)^N` rather than `(-Delta)^N`, which also handles a
possible zero eigenvalue cleanly. It settles the conjecture in the compact,
boundaryless fractafold setting of Section 9. No extension to infinite
blow-ups is claimed.

Primary output: `solution_packet.pdf`.

Verification and novelty notes: `VERIFICATION.md`.

Ledger: `runs/fa_banach_001/ledger/results/1108.2246_variable_coefficient_fractal_calderon_zygmund.json`.

