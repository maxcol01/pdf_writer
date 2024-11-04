from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

# Path preparation 
name_wtr = "wtr.pdf"
name_file = "merged-pdf.pdf"
output_file = "watermaked.pdf"
path_to_wtr = Path("./documents") / name_wtr
path_to_file = Path("./documents") / name_file
path_to_watermarked = Path("./documents") / output_file

with open(path_to_wtr, mode="rb") as wtr_file, open(path_to_file, "rb") as file:
    input_reader = PdfReader(wtr_file)
    file_reader = PdfReader(file)
    output_writer = PdfWriter()
    num_pages = len(PdfReader(file).pages)

    for page_num in range(0, num_pages):
        page = file_reader.pages[page_num]
        page.merge_page(input_reader.pages[0])
        output_writer.add_page(page)
    
    with open(path_to_watermarked, mode="wb") as output:
        output_writer.write(output)