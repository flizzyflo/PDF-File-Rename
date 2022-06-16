import os

from PyPDF2 import PdfFileReader
from Settings import FORBIDDEN_CHARS, PDF_FILE_PATH, SKIPABBLE_FILE_SUFFIX
from pathlib import Path

def getPdfFileMetaData(filepath: str, oldFilename: str) -> tuple[str, str]:
        """Helper Function to extract meta data of PDF files.
        Returns the PDF Title and the PDF author in a tuple of (title, author)"""
           
        try:
            with open(f"{os.path.join(filepath, oldFilename)}", "rb") as file:
                pdf_file_information = PdfFileReader(file).getDocumentInfo()
                pdf_title = pdf_file_information["/Title"]
                pdf_author = pdf_file_information["/Author"]

            return (pdf_author, pdf_title)
        
        except:
            return ("No title found in metadata", "No author found in metadata")


def skipFile(oldFilename: Path) -> bool:
    """Helper function to check whether a file should be skipped or if it should be renamed."""

    
    if oldFilename.suffix != ".pdf" or oldFilename.suffix in SKIPABBLE_FILE_SUFFIX:
            
        print(f"Your file '{oldFilename}' is not a pdf. This file cant be renamed with this method. However, all pdf files in this folder will be renamed.")
        return True

    return False


def replaceForbiddenCharacters(author: str, title: str) -> tuple[str, str]:
    """Helper Function to check whether forbidden characters are included in the pdf file name or pdf authors name"""
    
    for forbiddenChar in FORBIDDEN_CHARS:
        title = title.replace(forbiddenChar, " - ")
        author = author.replace(forbiddenChar, " - ")

    return author, title


def renamePdfFile(filepath: str, oldFilename: Path) -> None:
    """Function to rename PDF files according to their stored Meta data, namely Title and Author.
    Filepath is the path, where the files to be renamed are stored."""
    

    if skipFile(oldFilename= oldFilename):
        return

    pdfAuthor, pdfTitle = getPdfFileMetaData(filepath= filepath, oldFilename= oldFilename)
    pdfAuthor, pdfTitle = replaceForbiddenCharacters(author= pdfAuthor, title = pdfTitle)

    try:
        os.rename(os.path.join(PDF_FILE_PATH, oldFilename), os.path.join(PDF_FILE_PATH, f"{pdfAuthor} - {pdfTitle}.pdf" ))
    
    except: 
        os.rename(os.path.join(PDF_FILE_PATH, oldFilename), os.path.join(PDF_FILE_PATH, f"{pdfAuthor} - {pdfTitle} - copy.pdf" ))