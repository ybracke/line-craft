import random
from typing import Callable


def filter_lines(
    fname_in: str, fname_out: str, condition: Callable[[str], bool]
) -> None:
    """Read in a text file and write lines fulfilling `condition` of it to an output file"""
    with open(fname_in, "r", encoding="utf-8") as fin:
        with open(fname_out, "w", encoding="utf-8") as fout:
            for line in fin:
                if condition(line):
                    fout.write(line)
    return None


def modify_lines(
    fname_in: str, fname_out: str, modification: Callable[[str], str]
) -> None:
    """Read in a text file, apply `modification` per line and write lines to an output file"""
    with open(fname_in, "r", encoding="utf-8") as fin:
        with open(fname_out, "w", encoding="utf-8") as fout:
            for line in fin:
                fout.write(modification(line))
    return None


def sample_lines(fname_in: str, fname_out: str, n: int, seed: int = 42) -> None:
    """Read in a text file and write a subsample of lines to an output file"""
    # Seed
    random.seed(seed)
    with open(fname_in, "r", encoding="utf-8") as fin:
        # Get number of lines in input file
        for i, line in enumerate(fin):
            pass
        len_fin = i + 1
        if n > len_fin:
            raise ValueError(
                f"n exceeds number of lines in file (n={n}, lines={len_fin})"
            )
        # Get n random indices
        indices = set(random.sample(range(len_fin), n))
        # Write n selected lines to output file
        with open(fname_out, "w", encoding="utf-8") as fout:
            # Jump back to the start of input file
            fin.seek(0)
            for i, line in enumerate(fin):
                if i in indices:
                    fout.write(line)
    return None
