"""Upload the built deck to Google Drive as Google Slides through the gws-personal CLI.

    uv run python3 presentations/2026-swe-growth/benchmark-setup-coding-agent/deck/publish.py

Idempotent. The first run creates the file in the Drive folder "Talks" and records its id in
deck/drive.json. Later runs update that file's content in place.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

DECK_DIR = Path(__file__).resolve().parent
OUTPUT = DECK_DIR.parent / "output" / "benchmark-setup-coding-agent.pptx"
STATE = DECK_DIR / "drive.json"
NAME = "Benchmarking My Coding Agent Setup (SWE Growth 2026)"
FOLDER = "Talks"
SLIDES_MIME = "application/vnd.google-apps.presentation"
FOLDER_MIME = "application/vnd.google-apps.folder"
PPTX_MIME = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
FIELDS = "id,name,webViewLink"


def gws(*args: str, cwd: Path | None = None) -> dict:
    proc = subprocess.run(["gws-personal", *args], cwd=cwd, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.exit(f"gws-personal {' '.join(args[:3])} failed: {proc.stderr.strip() or proc.stdout.strip()}")
    start = proc.stdout.find("{")
    if start < 0:
        sys.exit(f"gws-personal returned no JSON: {proc.stdout.strip()}")
    return json.JSONDecoder().raw_decode(proc.stdout[start:])[0]


def find_folder() -> str:
    q = f"name='{FOLDER}' and mimeType='{FOLDER_MIME}' and trashed=false"
    found = gws("drive", "files", "list", "--params", json.dumps({"q": q, "fields": "files(id,name)"}))
    files = found.get("files", [])
    if files:
        return files[0]["id"]
    created = gws(
        "drive", "files", "create",
        "--params", json.dumps({"fields": "id"}),
        "--json", json.dumps({"name": FOLDER, "mimeType": FOLDER_MIME}),
    )
    return created["id"]


def create(folder_id: str) -> dict:
    return gws(
        "drive", "files", "create",
        "--params", json.dumps({"fields": FIELDS}),
        "--json", json.dumps({"name": NAME, "mimeType": SLIDES_MIME, "parents": [folder_id]}),
        "--upload", OUTPUT.name,
        "--upload-content-type", PPTX_MIME,
        cwd=OUTPUT.parent,
    )


def update(file_id: str) -> dict:
    return gws(
        "drive", "files", "update",
        "--params", json.dumps({"fileId": file_id, "fields": FIELDS}),
        "--upload", OUTPUT.name,
        "--upload-content-type", PPTX_MIME,
        cwd=OUTPUT.parent,
    )


def main() -> int:
    if not OUTPUT.exists():
        sys.exit(f"{OUTPUT} is missing, run deck/build.py first")
    if STATE.exists():
        file_id = json.loads(STATE.read_text())["fileId"]
        result = update(file_id)
    else:
        result = create(find_folder())
        STATE.write_text(json.dumps({"fileId": result["id"], "name": NAME}, indent=2) + "\n")
    print(result.get("webViewLink", f"https://docs.google.com/presentation/d/{result['id']}/edit"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
