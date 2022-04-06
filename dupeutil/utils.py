import hashlib
import pathlib


def get_hexdigest(file: pathlib.Path, size: int = -1) -> str:
    with open(file, "rb") as f:
        buffer = f.read(size)
        m = hashlib.md5()
        m.update(buffer)
        return m.hexdigest()


def cmp_bytes(file1: pathlib.Path, file2: pathlib.Path) -> bool:
    with open(file1, "rb") as f1:
        with open(file2, "rb") as f2:
            while True:
                b1 = f1.read(8192)
                b2 = f2.read(8192)

                # Returns False if the buffers aren't equal
                if b1 != b2:
                    return False

                # Returns True if their eofs are reached at the same time
                if not b1 and not b2:
                    return True


def quantify(count: int, singular: str, plural: str = ""):
    return singular if count == 1 else (plural if plural else singular + "s")
