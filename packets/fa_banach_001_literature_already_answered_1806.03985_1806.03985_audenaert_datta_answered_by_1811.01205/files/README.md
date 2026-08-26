# Literature Answer: Audenaert–Datta / Carlen–Frank–Lieb conjectures

- **Source:** Carlen–Frank–Lieb, arXiv:1806.03985.
- **Answering paper:** Haonan Zhang, arXiv:1811.01205.
- **Status:** `literature_already_answered` (affirmative; stronger conjecture proved).
- **Model:** `GPT5.6`.

Source PDF page 7, Conjecture 1 asks for joint convexity of `Psi_{p,q,1/(p+q)}` in the Audenaert–Datta range. Page 10, Conjecture 4 asks for the stronger range `s >= 1/(p+q)`.

Zhang explicitly reproduces these as Conjectures 1 and 2 on PDF page 2 and states that the paper confirms the stronger Carlen–Frank–Lieb conjecture. Theorem 1.1(3), PDF page 3, proves joint convexity for

```text
-1 <= q <= 0,  1 <= p <= 2,  (p,q) != (1,-1),  s >= 1/(p+q).
```

The paper also explains why singular `K` follows by approximation. Hence source Conjecture 4 is fully affirmative, and Conjecture 1 follows by taking equality in `s`.

Files:

- `solution_packet.pdf` — compact status/identification note.
- `source_paper.pdf` — arXiv:1806.03985.
- `supporting_paper_1811.01205.pdf` — explicit answering paper.
