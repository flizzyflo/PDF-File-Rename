import os

from PyPDF2 import PdfFileReader
from Settings import FORBIDDEN_CHARS
from pathlib import Path

global counter 
counter = 0

def getPdfFileMetaData(filepath: str, oldFilename: str) -> tuple[str, str]:
        """Helper Function to extract meta data of PDF files.
        Returns the PDF Title and the PDF author in a tuple of (title, author)"""
        
        global counter

        try:
            with open(f"{os.path.join(filepath, oldFilename)}", "rb") as file:
                pdf_file_information = PdfFileReader(file).getDocumentInfo()
                pdf_title = pdf_file_information["/Title"]
                pdf_author = pdf_file_information["/Author"]

            return (pdf_author, pdf_title)

        except:
            counter += 1
            return ("No author found in metadata", f"No title found in metadata {counter}")


def skipFile(oldFilename: Path) -> bool:
    """Helper function to check whether a file should be skipped or if it should be renamed."""

    
    if oldFilename.suffix != ".pdf":
            
        print(f"Your file '{oldFilename}' is not a pdf. This file cant be renamed with this method. However, all pdf files in this folder will be renamed.")
        return True

    return False


def replaceForbiddenCharacters(author: str, title: str) -> tuple[str, str]:
    """Helper Function to check whether forbidden characters mentioned in constant file
     are included in the pdf file name or pdf authors name"""
    

    for forbiddenChar in FORBIDDEN_CHARS:
        title = title.replace(forbiddenChar, " - ")
        author = author.replace(forbiddenChar, " - ")

    return author, title


def renamePdfFile(filepath: str, oldFileName: Path, counter: int) -> bool:
    """Function to rename PDF files according to their stored Meta data, namely Title and Author.
    Filepath is the path, where the files to be renamed are stored. Returns True if file is renamed unique, false if a file
    is a copy of another file"""
    
    
    pdfAuthor, pdfTitle = getPdfFileMetaData(filepath= filepath, oldFilename= oldFileName)
    pdfAuthor, pdfTitle = replaceForbiddenCharacters(author= pdfAuthor, title = pdfTitle)
    
    try:
        os.rename(os.path.join(filepath, oldFileName), os.path.join(filepath, f"{pdfAuthor} - {pdfTitle}.pdf" ))
        
    except:          
        counter += 1
        os.rename(os.path.join(filepath, oldFileName), os.path.join(filepath, f"{pdfAuthor} - {pdfTitle} {counter}.pdf" ))


def getCurrentFiles(filepath: str) -> list[str]:
    """Returns a list containing the files stored in the filepath, where the files to be renamed are stored."""

    return os.listdir(filepath)
