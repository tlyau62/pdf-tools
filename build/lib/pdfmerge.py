#!/usr/bin/env python3
import argparse
from pypdf import PdfWriter, PdfReader
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Args:
    files: list[str]
    out: str


def parse_args() -> Args:
    parser = argparse.ArgumentParser()

    parser.add_argument('--files', nargs='+')
    parser.add_argument('--out', default='merged.pdf')

    args = parser.parse_args()

    return Args(files=args.files, out=args.out)


def merge_pdfs(args: Args):
    writer = PdfWriter()
    page_count = 0
    pdf_files = [Path(file) for file in args.files]

    print(f'number of files to merge: {len(pdf_files)}')

    for pdf in pdf_files:
        reader = PdfReader(str(pdf))

        # add pages
        for page in reader.pages:
            writer.add_page(page)

        # add bookmark
        writer.add_outline_item(pdf.stem, page_count)

        page_count += len(reader.pages)

    with open(args.out, "wb") as f:
        writer.write(f)


def main():
    args = parse_args()

    merge_pdfs(args)


if __name__ == "__main__":
    main()
