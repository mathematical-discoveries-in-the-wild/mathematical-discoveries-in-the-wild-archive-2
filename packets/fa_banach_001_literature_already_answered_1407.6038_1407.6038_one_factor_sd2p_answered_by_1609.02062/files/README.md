# Literature resolution: one-factor SD2P stability is false

- **Source:** Becerra Guerrero–López-Pérez–Rueda Zoca, *Octahedral norms in spaces of operators*, arXiv:1407.6038.
- **Question:** after Corollary 3.6 (source PDF page 7), whether `X tensor_pi Y` must have the strong diameter two property (SD2P) if only one factor has SD2P.
- **Answering paper:** Langemets–Lima–Rueda Zoca, *Octahedral norms in tensor products of Banach spaces*, arXiv:1609.02062, Corollary 3.9 and Remark 3.11 (supporting PDF pages 10--11).
- **Status:** `literature_already_answered_full_negative`.
- **Model:** `GPT5.6`.

## Resolution

For every `2<p<infinity` and `n>=3`, Corollary 3.9 of arXiv:1609.02062 proves that

```text
ell_infinity tensor_pi ell_p^n
and
L_infinity tensor_pi ell_p^n
```

fail SD2P. Yet `L_infinity` has the Daugavet property, hence SD2P. This is an explicit negative answer to the source's one-factor question. Remark 3.11 states the relation directly: projective products preserve SD2P from both factors, but not in general from one.

The earlier introductory question detected by the scanner—stability when both factors have SD2P—is answered affirmatively by Corollary 3.6 of the source paper itself and is therefore a same-paper ask-and-answer signal.

## Files

- `main.tex` / `solution_packet.pdf` — compact provenance note.
- `source_paper.pdf` — arXiv:1407.6038.
- `supporting_paper_1609.02062.pdf` — later negative answer.
