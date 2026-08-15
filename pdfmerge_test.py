import pytest
import sys
from pdfmerge import main


def test_empty_arguments(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["pdfmerge"])

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1

    captured = capsys.readouterr()
    assert "Error: No PDF files provided." in captured.err
