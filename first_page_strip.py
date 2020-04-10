from PyPDF2 import PdfFileReader, PdfFileWriter
from file_upload import upload_file

def strip(pdf, s3_bucket_name):
    #pdf = "pdf1.pdf"
    output = "firstpage+" + pdf

    reader = PdfFileReader(pdf)
    writer = PdfFileWriter()

    writer.addPage(reader.getPage(0))

    with open(output, "wb") as out:
        writer.write(out)

    upload_file( output, s3_bucket_name)
    return output