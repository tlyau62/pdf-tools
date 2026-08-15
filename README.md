# PDF Tools

A collection of PDF scripts.

## Install

```sh
git clone https://github.com/tlyau62/pdf-tools
uv sync
uv tool install .
```

## Commands

Merge pdfs

```sh
# basic merge
pdfmerge --files file1 file2 ... --out merged.pdf
```

```sh
# find and merge in order
find . -name '*.pdf' | sort -V | xargs pdfmerge --out merged.pdf --files
```

Add page numbers

```sh
# basic page no
pdfpageno --file file --out output.pdf
```

## Development

Run test cases.

```sh
pytest
```
