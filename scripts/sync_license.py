#!/usr/bin/env python3
"""Generate the plain-text license from the authoritative ODT document."""

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import BadZipFile, ZipFile


ROOT = Path(__file__).resolve().parent.parent
ODT_PATH = ROOT / "MAPLE.odt"
TEXT_PATH = ROOT / "docs" / "MAPLE-DRAFT.txt"
OFFICE = "{urn:oasis:names:tc:opendocument:xmlns:office:1.0}"
TEXT = "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}"


def paragraph_text(element):
    """Extract displayed text and explicit ODF whitespace from a paragraph."""
    parts = [element.text or ""]
    for child in element:
        if child.tag == TEXT + "s":
            count = int(child.get(TEXT + "c", "1"))
            if count < 1:
                raise ValueError("An ODT space count must be positive")
            parts.append(" " * count)
        elif child.tag == TEXT + "tab":
            parts.append("\t")
        elif child.tag == TEXT + "line-break":
            parts.append("\n")
        elif child.tag == TEXT + "soft-page-break":
            pass
        elif child.tag in {TEXT + "span", TEXT + "a"}:
            parts.append(paragraph_text(child))
        else:
            raise ValueError(f"Unsupported ODT inline element: {child.tag}")
        parts.append(child.tail or "")
    return "".join(parts)


def extract_license(path):
    """Return the ODT body as UTF-8 text, retaining paragraph breaks."""
    with ZipFile(path) as document:
        root = ET.fromstring(document.read("content.xml"))
    body = root.find(f"./{OFFICE}body/{OFFICE}text")
    if body is None:
        raise ValueError("The ODT does not contain a text document body")

    paragraphs = []
    for element in body:
        if element.tag == TEXT + "sequence-decls":
            continue
        if element.tag not in {TEXT + "p", TEXT + "h"}:
            raise ValueError(f"Unsupported ODT body element: {element.tag}")
        paragraphs.append(paragraph_text(element))
    if not paragraphs:
        raise ValueError("The ODT contains no paragraphs")
    return "\n".join(paragraphs) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check without changing files")
    args = parser.parse_args()

    try:
        expected = extract_license(ODT_PATH).encode("utf-8")
        current = TEXT_PATH.read_bytes() if TEXT_PATH.exists() else None
        if current == expected:
            print("The plain-text license matches MAPLE.odt.")
            return 0
        if args.check:
            print("The plain-text license is out of sync. Run: python3 scripts/sync_license.py", file=sys.stderr)
            return 1
        TEXT_PATH.write_bytes(expected)
        print("Updated docs/MAPLE-DRAFT.txt from MAPLE.odt.")
        return 0
    except (OSError, BadZipFile, KeyError, ET.ParseError, ValueError) as exc:
        print(f"Could not synchronize the license: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
