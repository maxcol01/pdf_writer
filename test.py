from PyPDF2 import PdfReader, PdfWriter  
from pathlib import Path 
import sys

# test
folder = Path(".") / "documents"

list_of_file = sys.argv[1:]
list_of_path = list()

for item in list_of_file:
    list_of_path.append(folder/  f"{item}")

merger = PdfWriter()
for pdf in list_of_path:
    merger.append(pdf)

merger.write(folder / "merged-pdf.pdf")
merger.close() 
    