from pathlib import Path
from RenameFile import renamePdfFile, skipFile, getCurrentFiles
from Settings import PDF_FILE_PATH



def main() -> None:

    files = getCurrentFiles(PDF_FILE_PATH)

    for index, file in enumerate(files):
        fileToRename = Path(file)
        
        if skipFile(fileToRename):
            continue

        renamePdfFile(filepath= PDF_FILE_PATH, oldFileName= fileToRename, counter= index)
           

if __name__ == "__main__":
    main()