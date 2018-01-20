#!/usr/bin/python
import os
from PyPDF2 import PdfFileWriter, PdfFileReader

# This script will get all pdf file in the working folder, then convert them in to one single pdf

if os.path.isfile("result.pdf"):
        os.remove("result.pdf")

pdfs = [i for i in os.listdir(os.getcwd()) if i.endswith(".pdf")]

if len(pdfs) > 0:
    merger = PdfFileWriter()
    for pdf in pdfs:
        pdffile = PdfFileReader(open(pdf, 'rb'))
        #Loop through all the pages
        for pageNum in range(0, pdffile.numPages):
            pageObj = pdffile.getPage(pageNum)
            merger.addPage(pageObj)
    with open('result.pdf', 'wb') as fout:
        merger.write(fout)
