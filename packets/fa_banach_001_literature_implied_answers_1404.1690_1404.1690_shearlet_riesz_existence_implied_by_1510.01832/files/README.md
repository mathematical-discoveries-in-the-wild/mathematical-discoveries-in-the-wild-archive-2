# Broad Shearlet Riesz-Basis Existence Is Literature-Implied

Status: `literature_implied_answer (broad existence positive; compact cone-adapted subclass open)`

Source paper: Jackie Ma and Philipp Petersen, *Linear independence of compactly supported separable shearlet systems*, arXiv:1404.1690.

Supporting paper: Hartmut Führ and Yannic Maus, *Wavelet Riesz Bases Associated to Nonisotropic Dilations*, arXiv:1510.01832.

## Source question

In Section 5, `Beyond linear independence`, PDF page 18, Ma--Petersen ask about the existence of omega-independent shearlet frames, equivalently shearlet Riesz bases. Their Lemma 5.2 immediately before the question identifies the Riesz-basis and omega-independence properties for a frame.

## Identification

Führ--Maus Corollary 4.3 (PDF page 9) proves that, for every pair of rational parameters `a>1` and `b>0`, there exist `psi in L^2(R^2)` and a translation set `Lambda` for which

`(D_{A_{a^k}} D_{S_{mb}} T_lambda psi)_{k,m in Z, lambda in Lambda}`

is a Riesz basis of `L^2(R^2)`. Their abstract describes this as the first known shearlet Riesz basis. Since a Riesz basis is a frame and omega-independent, this answers the literal broad existence question positively.

The supporting authors do not cite Ma--Petersen and do not state that they are resolving that paper's question. The theorem-to-question relation is therefore an agent-identified implication, so the durable classification is `literature_implied_answers`, not `literature_already_answered`.

## Scope limitation

This is not a positive answer for the exact compactly supported separable cone-adapted class studied by Ma--Petersen. Führ--Maus use a wavelet-set generator whose Fourier transform is the characteristic function of a bounded set, and their translation set is a quasicrystal rather than the source paper's regular lattice sampling. Remark 4.5 says that cone-adapted shearlet Riesz bases are expected, but does not construct one. Thus the compactly supported cone-adapted/lattice-sampled subproblem remains open on the evidence checked here.

## Evidence and search bounds

- `source_paper.pdf`: arXiv:1404.1690; exact question on PDF page 18.
- `supporting_paper_1510.01832.pdf`: arXiv:1510.01832; Corollary 4.3 and Remarks 4.4--4.5 on PDF page 9.
- Cheap run indexes were searched for the arXiv ids and the phrases `shearlet Riesz`, `omega-independent shearlet`, `cone-adapted`, and `compactly supported shearlet`.
- Local primary-source and bounded web/arXiv searches found the Führ--Maus construction but no later construction or impossibility theorem for the compactly supported separable cone-adapted subclass.

## Human review recommendation

Accept as a scoped provenance/status packet. Count it as a literature-implied positive answer only to broad shearlet Riesz-basis existence. Do not count it as a new result or as a resolution of the compactly supported cone-adapted subclass.

The ledger record is `runs/fa_banach_001/ledger/results/1404.1690_shearlet_riesz_existence_implied_by_1510.01832.json`.
