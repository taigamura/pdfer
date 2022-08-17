from PyPDF2 import PdfFileMerger
from os import listdir
from os.path import isfile, join

def get_filenames(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

def create_filepaths(filenames) -> list:
    return_list = []
    for filename in filenames:
        return_list.append(f"./pdf_files_to_merge/{filename}")
    return return_list

if __name__ == "__main__":
    merger = PdfFileMerger()

    pdf_files = create_filepaths(get_filenames("./pdf_files_to_merge"))

    for pdf_file in pdf_files:
        merger.append(pdf_file)

    merger.write("merged.pdf")
    merger.close()