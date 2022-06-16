from pathlib import Path
from RenameFile import renamePdfFile, skipFile, getCurrentFiles
from Settings import PDF_FILE_PATH



def main() -> None:

    files = getCurrentFiles(PDF_FILE_PATH)

    for file in files:
        fileToRename = Path(file)
        
        if skipFile(fileToRename, files):
            continue
        
        renamePdfFile(filepath= PDF_FILE_PATH, oldFileName= fileToRename)
           

if __name__ == "__main__":
    main()