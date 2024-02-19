import PyPDF2
import sys
# inputs = sys.argv[1:]
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfMerger()
#     for pdf in pdf_list:
#         merger.append(pdf)
#     merger.write("pdfs/super.pdf")
# pdf_combiner(inputs)
# dummy.pdf         dummy_rotated.pdf twopage.pdf       wtr.pdf

# with open("pdfs/dummy.pdf", "rb") as pdf_file:
#     reader = PyPDF2.PdfReader(pdf_file)
#     page = reader.pages[0]
#     page.rotate(90)
#     writer = PyPDF2.PdfWriter()
#     writer.add_page(page)
#     with open("pdfs/dummy_rotated.pdf", "wb") as new_file:
#         writer.write(new_file)
template = PyPDF2.PdfReader(open('pdfs/super.pdf',"rb"))
watermark = PyPDF2.PdfReader(open('pdfs/wtr.pdf',"rb"))
output = PyPDF2.PdfWriter()
for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)
with open("pdfs/super_watermarked.pdf", "wb") as new_file:
    output.write(new_file)