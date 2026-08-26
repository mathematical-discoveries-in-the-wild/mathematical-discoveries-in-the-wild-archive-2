#!/usr/bin/env python3
"""Run the reproducible audit maintained with the lane attempt."""

from pathlib import Path
import runpy


REPO_ROOT = Path(__file__).resolve().parents[6]
SCRIPT = REPO_ROOT / "runs/fa_banach_001/attempts/code/check_1712_08874_mcp_extremality.py"
runpy.run_path(str(SCRIPT), run_name="__main__")

