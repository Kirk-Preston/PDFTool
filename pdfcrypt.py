import sys
import argparse
import PyPDF2

parser = argparse.ArgumentParser(description="PDF Encryption / Decryption Tool")
parser.add_argument("-f", "--file", action="store", dest="filename", help="Specify filename")
parser.add_argument("-e", "--encrypt", action="store_true", dest="ecrypt", help="Encrypt file", default=False)
parser.add_argument("-d", "--decrypt", action="store_true", dest="dcrypt", help="Decrypt file", default=False)
parser.add_argument("-p", "--password", action="store", dest="password", help="Password")
results = parser.parse_args()

try:
    pdffile = sys.argv[1]
except:
    print("Didn't enter file name, exiting ...")
    parser.print_usage()
    sys.exit(1)
try:    
    pdf_in = open(results.filename, 'rb')
except:
    print("File not found !")
    sys.exit(1)
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()

if results.ecrypt == True:
    try:
        for pagenum in range(pdf_reader.numPages):
            page = pdf_reader.getPage(pagenum)
            pdf_writer.addpage(page)
            pdf_writer.encrypt(results.password)
    except:
        print("Couldn't open file!")
    try:
        pdf_out = open(results.filename + ".encrypted", "wb")
        pdf_out.close()
    except:
        print("Couldn't save file!")
        sys.exit(1)

if results.dcrypt == True:
    try:
        for pagenum in range(pdf_reader.numPages):
            page = pdf_reader.getPage(pagenum)
            pdf_writer.addpage(page)
            pdf_writer.decrypt(results.password)
    except:
        print("Couldn't open file!")
    try:
        pdf_out = open(results.filename + ".decrypted", "wb")
        pdf_out.close()
    except:
        print("Couldn't save file!")
        sys.exit(1)
    
pdf_in.close()
