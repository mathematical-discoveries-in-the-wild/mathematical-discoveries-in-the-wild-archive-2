#!/usr/bin/env python3
"""Mechanical packet checks; this does not verify the mathematical proof."""

from pathlib import Path
import json

import fitz


PACKET = Path(__file__).resolve().parents[1]
RUN = PACKET.parents[2]
LEDGER = RUN / "ledger" / "results" / f"{PACKET.name}.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    for relative in [
        "README.md",
        "main.tex",
        "solution_packet.pdf",
        "source_paper.pdf",
        "figures/open_problem_crop.png",
        "verification.md",
        "novelty.md",
    ]:
        path = PACKET / relative
        require(path.is_file() and path.stat().st_size > 0, f"missing/empty: {relative}")

    with fitz.open(PACKET / "source_paper.pdf") as source:
        require(source.page_count == 19, f"unexpected source pages: {source.page_count}")
    with fitz.open(PACKET / "solution_packet.pdf") as packet:
        require(packet.page_count >= 4, f"packet too short: {packet.page_count}")

    tex = (PACKET / "main.tex").read_text(encoding="utf-8")
    for marker in [
        "Idea of the proof",
        "phase-triangular",
        "Regularized general reduction",
        "Hard-edge obstruction",
        "Conjecture~1",
    ]:
        require(marker in tex, f"missing TeX marker: {marker}")

    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    require(data.get("model") == "GPT5.6", "ledger model must be GPT5.6")
    require(data.get("status") == "partial_result_likely_valid", "unexpected status")
    require(data.get("packet_path", "").endswith(f"/{PACKET.name}/"), "bad packet path")
    print("source/packet pages, assets, theorem markers, and ledger: OK")


if __name__ == "__main__":
    main()

