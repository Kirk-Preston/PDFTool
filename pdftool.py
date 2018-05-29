import sys
import argparse
import PyPDF2

parser = argparse.ArgumentParser(description="PDF Rotation Tool")
parser.add_argument("-90", action="store_true", dest="rotonce", help="Rotate PDF 90 Degrees CW", default=False)
parser.add_argument("-180", action="store_true", dest="rottwice", help="Rotate the PDF 180 Degrees CW", default=False)
parser.add_argument("-270", action="store_true", dest="rotthree", help="Rotate the PDF 270 Degrees CW", default=False)
parser.add_argument("-f", action="store", dest="filename", help="Specify filename")
results = parser.parse_args()

try:
    pdffile = sys.argv[1]
except:
    print("Didn't enter file name, exiting ...")
    parser.print_usage()
    sys.exit(1)

if results.rotonce == True:
    rotation = 90
elif results.rottwice == True:
    rotation = 180
elif results.rotthree == True:
    rotation = 270
else:
    pass

try:    
    pdf_in = open(results.filename, 'rb')
except:
    print("File not found !")
    sys.exit(1)
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()
 
for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    page.rotateClockwise(rotation)
    pdf_writer.addPage(page)

try:
    pdf_out = open(results.filename + ".rotated", 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
except:
    print("Couldn't save file !")
    sys.exit(1)
    
pdf_in.close()
