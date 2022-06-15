from pathlib import Path
import shutil
import os
from PyPDF2 import PdfFileReader

destination_path = r"C:\Users\flori\Desktop\Downloads sortiert"
original_path = r"C:\Users\flori\Downloads"

skippable_file_suffix = [".ini"]


def read_information(filename: str, filepath: str) -> tuple[str, str]:
        """Helper Function to extract meta data of PDF files"""
        
        try:
            with open(f"{filepath}\{filename}", "rb") as file:
                pdf_file_information = PdfFileReader(file).getDocumentInfo()
                pdf_title = pdf_file_information["/Title"]
                pdf_author = pdf_file_information["/Author"]

            return tuple(pdf_title, pdf_author)
        
        except:
            return tuple("No title found in metadata", "No Author found in Metadata")


def rename_pdf_file(filename: Path, filepath: str) -> None:
    """Function to rename PDF files according to their stored Meta data, namely Title and Author"""
    
    pdf_title, pdf_author = read_information(filename, filepath)

    os.rename(f"{original_path}\{filename}", f"{original_path}\{pdf_author} - {pdf_title}.pdf")


def move_pdf_file(file: Path, source_path: str, destination_path: str) -> None:
    """Function to move .pdf file from source path to destination path"""

    try:
        shutil.move(src= source_path, dst= destination_path)

    except:
        print(f"'{file}' already exists in '{destination_path}'")


def move_exe_files(file: Path, source_path: str, destination_path: str) -> None:
    """Function to move .exe file from source path to destination path"""

    try:
        if file.suffix.lower() == ".exe":
            shutil.move(src= source_path, dst= destination_path)
    except:
        print(f"'{file}' already exists in '{destination_path}'")


def move_zip_files(file: Path, source_path: str, destination_path: str) -> None:
    """Function to move .zip file from source path to destination path"""

    try:
        if file.suffix.lower() == ".zip":
            shutil.move(src= source_path, dst= destination_path)
    except:
        print(f"'{file}' already exists in '{destination_path}'")


####################################################################################

target_folders = os.listdir(destination_path)

for file in os.listdir(original_path):
    f = Path(file)
    print(os.listdir(original_path))
    
    filename, filesuffix = f.name, f.suffix

    if filesuffix in skippable_file_suffix:
        continue

    if filesuffix == ".pdf":

        rename_pdf_file(f, original_path)
        move_pdf_file(f, f"{original_path}\{filename}", fr"{destination_path}\{target_folders[1]}")

    # move_exe_files(f, f"{original_path}\{filename}", fr"{destination_path}\{target_folders[0]}")
    # move_zip_files(f, f"{original_path}\{filename}", fr"{destination_path}\{target_folders[2]}")
