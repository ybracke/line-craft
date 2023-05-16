import json
import os
import re

import pytest

from line_craft import filter_lines, modify_lines, sample_lines


def test_filter_lines_jsonl_condition_uneven_number():
    infile = "tests/testdata/example01.jsonl"
    outfile = "tests/testdata/example01.tmp.out.jsonl"

    # condition
    def is_uneven_number(line):
        line_obj = json.loads(line)
        return not (line_obj["numeric_property"] % 2 == 0)

    condition = is_uneven_number
    # Write filtered file
    filter_lines(infile, outfile, condition)
    # Check result
    target_out = (
        """{"numeric_property": 3, "textual_property": "angels", "boolean_property": true}\n"""
        """{"numeric_property": 5, "textual_property": "alpha", "boolean_property": true}\n"""
    )
    with open(outfile, "r", encoding="utf-8") as f:
        actual_out = f.read()
    assert target_out == actual_out
    # Remove files that were created during test
    os.remove(outfile)


def test_modify_lines():
    infile = "tests/testdata/example01.jsonl"
    outfile = "tests/testdata/example01.tmp.out.jsonl"

    # modification
    def upper_text(line):
        line_obj = json.loads(line)
        line_obj["textual_property"] = line_obj["textual_property"].upper()
        return json.dumps(line_obj).rstrip() + "\n"

    modify = upper_text
    # Write filtered file
    modify_lines(infile, outfile, modify)
    # Check result
    target_out = (
        """{"numeric_property": 10, "textual_property": "APPLES", "boolean_property": false}\n"""
        """{"numeric_property": 2, "textual_property": "ORANGES", "boolean_property": true}\n"""
        """{"numeric_property": 3, "textual_property": "ANGELS", "boolean_property": true}\n"""
        """{"numeric_property": 5, "textual_property": "ALPHA", "boolean_property": true}\n"""
        """{"numeric_property": 18, "textual_property": "BETA", "boolean_property": false}\n"""
    )
    with open(outfile, "r", encoding="utf-8") as f:
        actual_out = f.read()
    assert target_out == actual_out
    # Remove files that were created during test
    os.remove(outfile)


def test_subsample_lines_normal():
    infile = "tests/testdata/example01.jsonl"
    outfile = "tests/testdata/example01.tmp.out.jsonl"
    n_lines_in_output = 3
    sample_lines(infile, outfile, n_lines_in_output)
    # Check result
    with open(outfile, "r", encoding="utf-8") as f:
        out_lines = f.readlines()
    assert len(out_lines) == n_lines_in_output
    # Remove files that were created during test
    os.remove(outfile)


def test_subsample_lines_n_too_high():
    infile = "tests/testdata/example01.jsonl"
    outfile = "tests/testdata/example01.tmp.out.jsonl"
    n_lines_in_output = 6
    # Function call should raise a ValueError
    with pytest.raises(
        ValueError, match=re.escape("n exceeds number of lines in file (n=6, lines=5)")
    ):
        _ = sample_lines(infile, outfile, n_lines_in_output)
