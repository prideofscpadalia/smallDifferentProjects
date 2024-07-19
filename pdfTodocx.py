from pdf2docx import Converter


def pdf_to_word(pdf_file, word_file):
    # Create a Converter object
    cv = Converter(pdf_file)
    
    # Convert PDF to DOCX format
    cv.convert(word_file, start=0, end=None)
    
    # Close the converter
    cv.close()
    print(f"Conversion complete. {word_file} has been created.")

# Specify the path to the PDF file and the desired output path for the Word file
pdf_file_path = '/home/rengoku/Downloads/JanPdf.pdf'
word_file_path = '/home/rengoku/Document/output.docx'

# Call the function to convert PDF to Word
pdf_to_word(pdf_file_path, word_file_path)

