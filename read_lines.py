def read_lines(path: str) -> list[str]:
    """
    Read all lines from a text file and return them stripped.
    """
    with open(path, "r") as f:
        return [ln.rstrip("\n") for ln in f]