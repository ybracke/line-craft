import os

from line_craft import cli


def test_parse_arguments():
    print(
        cli.parse_arguments(
            ["--out", "outfile.txt", "sample", "-n", "5", "testdata/example01.txt"]
        )
    )


def test_main():
    outfile = "tests/testdata/example01.rand3.jsonl"
    print(
        cli.main(
            ["--out", outfile, "sample", "-n", "3", "tests/testdata/example01.jsonl"]
        )
    )
    os.remove(outfile)
