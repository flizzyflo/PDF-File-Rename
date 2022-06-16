

# ORIGINAL_PATH serves as source folder for the initial read in and as destination folder
# where the (renamed) files should be transferred to.
# FORBIDDEN_CHARS are chars which are not allowed to be used in a file name according to the OS.
# SKIPABBLE_FILE_SUFFIX contains suffix which should be skipped while renaming files in a given directory.

ORIGINAL_PATH = r"C:\Users\flori\Downloads"

FORBIDDEN_CHARS = ["?", ":", "/", "\\", "*", "|", "<", ">", '"']
SKIPABBLE_FILE_SUFFIX = [".ini"]