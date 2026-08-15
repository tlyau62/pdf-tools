# PDF Tools

A collection of PDF scripts.

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
