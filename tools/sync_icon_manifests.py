#!/usr/bin/env python3
"""Synchronize icon manifest JSON files with PNG files on disk."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
ICONS_ROOT = REPOSITORY_ROOT / "Icons"
RAW_BASE_URL = "https://raw.githubusercontent.com/sunfing/iNg/main/Icons"
DESCRIPTION = "\u8ba2\u9605\u9891\u9053\uff1ahttps://t.me/i_chl"
MANIFESTS = (
    ("AirportIcons", "AirportIcon.json", "Airport Icon"),
    ("EmbyIcons", "EmbyIcon.json", "Emby Icon"),
    ("FlagIcons", "FlagIcon.json", "Flag Icon"),
    ("GeneralIcons", "GeneralIcon.json", "General Icon"),
)


def render_manifest(directory_name: str, display_name: str) -> str:
    icon_directory = ICONS_ROOT / directory_name
    image_paths = sorted(
        (
            path
            for path in icon_directory.iterdir()
            if path.is_file() and path.suffix.lower() == ".png"
        ),
        key=lambda path: path.name,
    )

    lines = [
        "{",
        f'  "name": {json.dumps(display_name, ensure_ascii=False)},',
        f'  "description": {json.dumps(DESCRIPTION, ensure_ascii=False)},',
    ]
    if image_paths:
        lines.append('  "icons": [')
        for index, image_path in enumerate(image_paths):
            icon = {
                "name": image_path.stem,
                "url": f"{RAW_BASE_URL}/{directory_name}/{image_path.name}",
            }
            comma = "," if index < len(image_paths) - 1 else ""
            lines.append(f"    {json.dumps(icon, ensure_ascii=False)}{comma}")
        lines.append("  ]")
    else:
        lines.append('  "icons": []')
    lines.append("}")
    return "\n".join(lines) + "\n"


def synchronize(check_only: bool) -> int:
    stale_manifests: list[Path] = []

    for directory_name, manifest_name, display_name in MANIFESTS:
        manifest_path = ICONS_ROOT / manifest_name
        expected = render_manifest(directory_name, display_name)
        current = (
            manifest_path.read_text(encoding="utf-8")
            if manifest_path.exists()
            else None
        )
        if current == expected:
            continue

        stale_manifests.append(manifest_path)
        if not check_only:
            with manifest_path.open("w", encoding="utf-8", newline="\n") as output:
                output.write(expected)
            print(f"updated: {manifest_path.relative_to(REPOSITORY_ROOT)}")

    if check_only and stale_manifests:
        for manifest_path in stale_manifests:
            print(f"stale: {manifest_path.relative_to(REPOSITORY_ROOT)}")
        print("Run: python tools/sync_icon_manifests.py")
        return 1

    if not stale_manifests:
        print("Icon manifests are up to date.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="report stale manifests without changing files",
    )
    args = parser.parse_args()
    return synchronize(check_only=args.check)


if __name__ == "__main__":
    raise SystemExit(main())
