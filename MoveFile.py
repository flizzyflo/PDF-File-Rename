from pathlib import Path
import shutil
import os
from PyPDF2 import PdfFileReader


"""Path input; serves as source folder for the initial read in and as destination folder
where the (renamed) files should be transferred to."""

destination_path = r"C:\Users\flori\Desktop\Downloads sortiert"
original_path = r"C:\Users\flori\Downloads"

skippable_file_suffix = [".ini"]


def get_pdf_file_metainformation(filepath: str, filename: str) -> tuple[str, str]:
        """Helper Function to extract meta data of PDF files"""

        try:
            with open(f"{os.path.join(filepath, filename)}", "rb") as file:
                pdf_file_information = PdfFileReader(file).getDocumentInfo()
                pdf_title = pdf_file_information["/Title"]
                pdf_author = pdf_file_information["/Author"]

            return (pdf_title, pdf_author)
        
        except:
            return ("No title found in metadata", "No author found in metadata")


def rename_pdf_file(filepath: str, filename: Path) -> None:
    """Function to rename PDF files according to their stored Meta data, namely Title and Author"""
    
    pdf_title, pdf_author = get_pdf_file_metainformation(filepath, filename)

    try:
        os.rename(os.path.join(original_path, filename), os.path.join(original_path, f"{pdf_author} - {pdf_title}.pdf" ))
    
    except: 
        os.rename(os.path.join(original_path, filename), os.path.join(original_path, f"{pdf_author} - {pdf_title} - copy.pdf" ))


def move_pdf_file(file: Path, source_path: str, destination_path: str) -> None:
    """Function to move .pdf file from source path to destination path"""

    try:
        shutil.move(src= os.path.join(source_path, file.name), dst= destination_path)

    except:
        print(f"'{file}' already exists in '{destination_path}'")


def move_exe_files(file: Path, source_path: str, destination_path: str) -> None:
    """Function to move .exe file from source path to destination path"""

    try:
        if file.suffix.lower() == ".exe":
            shutil.move(src= os.path.join(source_path, file.name), dst= destination_path)
    except:
        print(f"'{file}' already exists in '{destination_path}'")


def move_zip_files(file: Path, source_path: str, destination_path: str) -> None:
    """Function to move .zip file from source path to destination path"""

    try:
        if file.suffix.lower() == ".zip":
            shutil.move(src= os.path.join(source_path, file.name), dst= destination_path)
    except:
        print(f"'{file}' already exists in '{destination_path}'")


####################################################################################

target_folders = os.listdir(destination_path)
print

for file in os.listdir(original_path):
    f = Path(file)
    
    filename, filesuffix = f.name, f.suffix

    if filesuffix in skippable_file_suffix:
        continue

    if filesuffix == ".pdf":

        rename_pdf_file(original_path, f)
        move_pdf_file(f, original_path, fr"{destination_path}\{target_folders[1]}")

    move_exe_files(f, original_path, fr"{destination_path}\{target_folders[0]}")
    # move_zip_files(f, original_path, fr"{destination_path}\{target_folders[2]}")
