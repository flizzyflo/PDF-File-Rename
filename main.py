import os

from pathlib import Path
from RenameFile import renamePdfFile
from Settings import SKIPABBLE_FILE_SUFFIX, ORIGINAL_PATH


def main() -> None:

    files = os.listdir(ORIGINAL_PATH)

    for file in files:
        fileToRename = Path(file)

        if fileToRename.suffix in SKIPABBLE_FILE_SUFFIX:
            continue

        if fileToRename.suffix == ".pdf":
            renamePdfFile(ORIGINAL_PATH, fileToRename)


if __name__ == "__main__":
    main()