import os

from pathlib import Path
from PyPDF2 import PdfFileReader
from settings import FORBIDDEN_CHARS

global counter
counter: int = 0


class RenameFile:
    fileDict: dict[str, int] = {}

    @staticmethod
    def __get_pdf_file_meta_data(filepath: str, old_filename: Path) -> tuple[str, str]:

        """
        Helper Function to extract meta-data of PDF files.
            Returns the PDF Title and the PDF author in a tuple of (title, author)
        """

        global counter

        try:
            with open(f"{os.path.join(filepath, old_filename)}", "rb") as file:
                pdf_file_information = PdfFileReader(file).getDocumentInfo()
                pdf_title: str = pdf_file_information["/Title"]
                pdf_author: str = pdf_file_information["/Author"]

            return pdf_author, pdf_title

        except:
            return "No author found in metadata", f"No title found in metadata"

    @staticmethod
    def __skip_file(old_filename: Path) -> bool:
        """Helper function to check whether a file should be skipped or if it should be renamed."""

        if old_filename.suffix != ".pdf":
            print(
                f"Your file '{old_filename}' is not a pdf. "
                f"This file cant be renamed with this method. "
                f"However, all pdf files in this folder will be renamed.")
            return True

        return False

    @staticmethod
    def __replace_forbidden_characters(author: str, title: str) -> tuple[str, str]:
        """Helper Function to check whether forbidden characters mentioned in constant file
        are included in the pdf file name or pdf authors name"""

        for forbiddenChar in FORBIDDEN_CHARS:
            title = title.replace(forbiddenChar, " - ")
            author = author.replace(forbiddenChar, " - ")

        return author, title

    @staticmethod
    def __rename_pdf_file(filepath: str, old_file_name: Path) -> None:
        """Function to rename PDF files according to their stored Meta-data, namely Title and Author.
        Filepath is the path, where the files to be renamed are stored.
        Returns True if file is renamed unique, false if a file
        is a copy of another file"""

        pdf_author, pdf_title = RenameFile.__get_pdf_file_meta_data(filepath=filepath, old_filename=old_file_name)
        pdf_author, pdf_title = RenameFile.__replace_forbidden_characters(author=pdf_author, title=pdf_title)

        RenameFile.__create_file_dict(pdf_author=pdf_author,
                                      pdf_title=pdf_title)

        if RenameFile.__get_file_name_count(pdf_author, pdf_title) == 1:
            try:
                source_data = os.path.join(filepath, old_file_name)
                renamed_data = os.path.join(filepath, f"{pdf_author} - {pdf_title}.pdf")
                os.rename(source_data, renamed_data)

            except:
                print(f"Filename {pdf_author} - {pdf_title}.pdf already exists")

        else:
            try:
                file_name_count = RenameFile.__get_file_name_count(pdf_author, pdf_title)
                source_data = os.path.join(filepath, old_file_name)
                renamed_data = os.path.join(filepath, f"{pdf_author} - {pdf_title} ({file_name_count}).pdf")

                os.rename(source_data, renamed_data)

            except:
                print(f"Filename {pdf_author} - {pdf_title} ({file_name_count}).pdf already exists")

    @staticmethod
    def __get_file_name_count(pdf_author: str, pdf_title: str) -> int:

        return RenameFile.fileDict[f"{pdf_author} - {pdf_title}"]

    @staticmethod
    def __get_current_files(filepath: str) -> list[str]:
        """Returns a list containing the files stored in the filepath, where the files to be renamed are stored."""

        return os.listdir(filepath)

    @staticmethod
    def __create_file_dict(pdf_author: str, pdf_title: str) -> None:
        """Creates a global dictionary which counts the amount of files.
        Is used to keep track of duplicate values to name them accordingly."""

        if f"{pdf_author} - {pdf_title}" in RenameFile.fileDict.keys():
            RenameFile.fileDict[f"{pdf_author} - {pdf_title}"] += 1

        else:
            RenameFile.fileDict[f"{pdf_author} - {pdf_title}"] = 1

    @staticmethod
    def rename_files(filepath: str) -> None:
        """Function wrapps all the subroutines from this class and makes it accessible for the outside."""

        files = RenameFile.__get_current_files(filepath)

        for file in files:
            file_to_rename = Path(file)

            if RenameFile.__skip_file(file_to_rename):
                continue

            RenameFile.__rename_pdf_file(filepath=filepath,
                                         old_file_name=file_to_rename)

        RenameFile.__reset_file_counter()

    @staticmethod
    def __reset_file_counter() -> None:
        for key in RenameFile.fileDict.keys():
            RenameFile.fileDict[key] = 0
