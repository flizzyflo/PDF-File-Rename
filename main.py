import os

from pathlib import Path
from RenameFile import renamePdfFile
from Settings import SKIPABBLE_FILE_SUFFIX, PDF_FILE_PATH


def main() -> None:

    files = os.listdir(PDF_FILE_PATH)

    for file in files:
        fileToRename = Path(file)

        renamePdfFile(PDF_FILE_PATH, fileToRename)


if __name__ == "__main__":
    main()