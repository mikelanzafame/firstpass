import argparse
from first_page_strip import strip
from extract import full_process
from nat_lang import nlp_process
########################################################
# S3-Bucket:
s3_bucket_hardcoded = 'firstpass-s3'
# PDF Name: (Used if Command line args do not specify a PDF.)
pdf_hardcoded = 'pdf1.pdf'
########################################################

# Argument Parsing:
parser = argparse.ArgumentParser()
parser.add_argument('--pdf', help='OPTIONAL: PDF for Input Procesing')
parser.add_argument('--bucket', help='OPTIONAL: S3 Bucket to store PDFs for Textract')
args = parser.parse_args()

pdf = args.pdf
s3_bucket = args.bucket

# Catch if args arent specified & use hardcoded values.
if pdf == None:
    print('No PDF Specified, using hardcoded value of {pdf}'.format(pdf = pdf_hardcoded))
    pdf = pdf_hardcoded 

if s3_bucket == None:
    print('No S3 Bucket Specified, using hardcoded value of {bucket}'.format(bucket = s3_bucket_hardcoded))
    s3_bucket = s3_bucket_hardcoded 

# Split First Page & Return Output File Name:
output_file = strip(pdf, s3_bucket)

# Submit PDF to Textract to Process
processed_text = full_process(output_file, s3_bucket)

# NLP:
nlp_process(processed_text)