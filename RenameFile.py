import os

from PyPDF2 import PdfFileReader
from Settings import FORBIDDEN_CHARS, ORIGINAL_PATH
from pathlib import Path

def getPdfFileMetaData(filepath: str, filename: str) -> tuple[str, str]:
        """Helper Function to extract meta data of PDF files.
        Returns the PDF Title and the PDF author in a tuple of (title, author)"""

        if filename.suffix != ".pdf":
            raise IOError("Your file is no pdf. This file cant be renamed with this method.")

        else: 
            try:
                with open(f"{os.path.join(filepath, filename)}", "rb") as file:
                    pdf_file_information = PdfFileReader(file).getDocumentInfo()
                    pdf_title = pdf_file_information["/Title"]
                    pdf_author = pdf_file_information["/Author"]

                return (pdf_author, pdf_title)
            
            except:
                return ("No title found in metadata", "No author found in metadata")


def renamePdfFile(filepath: str, oldFilename: Path) -> None:
    """Function to rename PDF files according to their stored Meta data, namely Title and Author.
    Filepath is the path, where the files to be renamed are stored."""
    
    pdfAuthor, pdfTitle = getPdfFileMetaData(filepath, oldFilename)

    for forbiddenChar in FORBIDDEN_CHARS:
        pdfTitle = pdfTitle.replace(forbiddenChar, " - ")
        pdfAuthor = pdfAuthor.replace(forbiddenChar, " - ")

    try:
        os.rename(os.path.join(ORIGINAL_PATH, oldFilename), os.path.join(ORIGINAL_PATH, f"{pdfAuthor} - {pdfTitle}.pdf" ))
    
    except: 
        os.rename(os.path.join(ORIGINAL_PATH, oldFilename), os.path.join(ORIGINAL_PATH, f"{pdfAuthor} - {pdfTitle} - copy.pdf" ))