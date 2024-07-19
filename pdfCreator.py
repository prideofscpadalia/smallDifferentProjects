from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size = 12)

# Open the text file in read mode
with open("conversation.txt", "r") as file:
    for line in file:
        # Add a cell
        pdf.cell(200, 10, txt = line, ln = True)

# Save the pdf with name .pdf
pdf.output("conversation.pdf")

