#!/usr/bin/env python3
"""Mechanical packet checks; this does not verify the analytic proof."""

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
    required = [
        "README.md",
        "main.tex",
        "solution_packet.pdf",
        "source_paper.pdf",
        "supporting_paper_1608.05489.pdf",
        "figures/open_problem_crop.png",
        "verification.md",
        "novelty.md",
    ]
    for relative in required:
        path = PACKET / relative
        require(path.is_file() and path.stat().st_size > 0, f"missing/empty: {relative}")

    with fitz.open(PACKET / "source_paper.pdf") as source_pdf:
        source_pages = source_pdf.page_count
    with fitz.open(PACKET / "solution_packet.pdf") as packet_pdf:
        packet_pages = packet_pdf.page_count
    require(source_pages == 28, f"unexpected source page count: {source_pages}")
    require(packet_pages >= 3, f"packet too short: {packet_pages} pages")

    tex = (PACKET / "main.tex").read_text(encoding="utf-8")
    for marker in [
        "Idea of the proof",
        "The weakly Lindel",
        "A mixed-band upgrade",
        "Scope, verification, and novelty",
        "Corollary~4.14",
    ]:
        require(marker in tex, f"missing TeX marker: {marker}")

    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    require(data.get("model") == "GPT5.6", "ledger model must be GPT5.6")
    require(data.get("status") == "partial_result_likely_valid", "unexpected status")
    require(data.get("packet_path", "").endswith(f"/{PACKET.name}/"), "bad packet path")

    print(f"source pages: {source_pages}")
    print(f"solution packet pages: {packet_pages}")
    print("required assets and theorem markers: OK")
    print("ledger model/status/path: OK")
    print("all mechanical checks passed")


if __name__ == "__main__":
    main()
