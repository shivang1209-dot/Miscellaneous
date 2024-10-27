from PyPDF2 import PdfMerger
import os

merger = PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)

merger.write(input("Enter The Name Of The Output File: ") + ".pdf")
merger.close()