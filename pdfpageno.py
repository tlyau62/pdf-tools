#!/usr/bin/env python3
import argparse
from pypdf import PdfWriter, PdfReader
from dataclasses import dataclass
from pathlib import Path
import io
from reportlab.pdfgen import canvas


@dataclass
class Args:
    file: str
    out: str


def parse_args() -> Args:
    parser = argparse.ArgumentParser()

    parser.add_argument('--file', nargs='?')
    parser.add_argument('--out', default='pageno.pdf')

    args = parser.parse_args()

    if not args.file:
        parser.error("No PDF files provided.")

    return Args(file=args.file, out=args.out)


def overlay_page_no(width, height, number):
    """Create a single-page PDF (in memory) with the page number centered at the bottom."""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(width, height))
    c.setFont("Helvetica", 10)
    # Draw the number centered, ~20 points up from the bottom edge
    c.drawCentredString(width / 2, 20, str(number))
    c.save()
    buf.seek(0)

    return PdfReader(buf).pages[0]


def add_page_no(args: Args):
    reader = PdfReader(args.file)
    writer = PdfWriter()

    for pageno, page in enumerate(reader.pages):
        w = float(page.mediabox.width)
        h = float(page.mediabox.height)

        overlay = overlay_page_no(w, h, pageno + 1)
        page.merge_page(overlay)

        writer.add_page(page)

    with open(args.out, "wb") as f:
        writer.write(f)


def main():
    args = parse_args()

    add_page_no(args)


if __name__ == "__main__":
    main()
