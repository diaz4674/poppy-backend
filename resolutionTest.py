from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io
import os
import sys
import string

AccountInfo = {
    "Type": "Business",
    "Ownership": "CCorp",
    "Benificiary": "",
    "BeneficiaryDetails": "",
    "totalSigners": 3,
    "BusinessName": "Ballerz Inc.",
    "Prefix": "DBA",
    "PrefixName": "Hulu",
    "AnotherName": "",
    "Street": "123 Main St",
    "City": "Santa Rosa, CA 94949",
    "EIN": "12-345676",
    "AccountType1": "Business Checking",
    "AccountNumber1": "01-1000088-8",
}

signer1 = {
    "Name": 'Bobby Brown',
    "Relationship": 'Owners',
    "Position": "COO",
    "Street": "123 Happy Dr",
    "City": "Petaluma, CA 94952",
    "MailingAddress": "PO Box 123, Petaluma CA 94954",
    "PrimaryIDType": "Drivers License",
    "Number": "D234354 CA",
    "IssueDate1": "10/07/2017",
    "ExpirationDate1": "10/18/2022",
    "OtherID": "Credit Card",
    "OtherDesc": "Visa",
    "Expires": "02/28/2023",
    "Employer": "Poppy Bank",
    "Title": "New Accounts/CSR-Poppy Bank",
    "email": "diaz1234@gmail.com",
    "WorkPhone": "",
    "HomePhone": "(707) 778-7756",
    "Cell": "(123) 456-7890",
    "DOB": "10/18/1991",
    "SSN": "123-34-2134"
}

signer2 = {
    "Name": 'James Brown',
    "Relationship": 'Owners',
    "Position": "COO",
    "Street": "123 Happy Dr",
    "City": "Petaluma, CA 94952",
    "MailingAddress": "PO Box 123, Petaluma CA 94954",
    "PrimaryIDType": "Drivers License",
    "Number": "D234354 CA",
    "IssueDate1": "10/07/2017",
    "ExpirationDate1": "10/18/2022",
    "OtherID": "Credit Card",
    "OtherDesc": "Visa",
    "Expires": "02/28/2023",
    "Employer": "Poppy Bank",
    "Title": "New Accounts/CSR-Poppy Bank",
    "email": "diaz1234@gmail.com",
    "WorkPhone": "(707) 778-7756",
    "HomePhone": "(707) 778-7756",
    "Cell": "(123) 456-7890",
    "DOB": "10/18/1991",
    "SSN": "123-34-2134"
}

signer3 = {
    "Name": 'Jimmy Neutron',
    "Relationship": 'Owners',
    "Position": "COO",
    "Street": "123 Happy Dr",
    "City": "Petaluma, CA 94952",
    "MailingAddress": "PO Box 123, Petaluma CA 94954",
    "PrimaryIDType": "Drivers License",
    "Number": "D234354 CA",
    "IssueDate1": "10/07/2017",
    "ExpirationDate1": "10/18/2022",
    "OtherID": "Credit Card",
    "OtherDesc": "Visa",
    "Expires": "02/28/2023",
    "Employer": "Poppy Bank",
    "Title": "New Accounts/CSR-Poppy Bank",
    "email": "diaz1234@gmail.com",
    "WorkPhone": "(707) 778-7756",
    "HomePhone": "(707) 778-7756",
    "Cell": "(123) 456-7890",
    "DOB": "10/18/1991",
    "SSN": "123-34-2134"
}
signer4 = {
    "Name": 'Timmy Turner',
    "Relationship": 'Owners',
    "Street": "123 Happy Dr",
    "Position": "COO",
    "City": "Petaluma, CA 94952",
    "MailingAddress": "PO Box 123, Petaluma CA 94954",
    "PrimaryIDType": "Drivers License",
    "Number": "D234354 CA",
    "IssueDate1": "10/07/2017",
    "ExpirationDate1": "10/18/2022",
    "OtherID": "Credit Card",
    "OtherDesc": "Visa",
    "Expires": "02/28/2023",
    "Employer": "Poppy Bank",
    "Title": "New Accounts/CSR-Poppy Bank",
    "email": "diaz1234@gmail.com",
    "WorkPhone": "(707) 778-7756",
    "HomePhone": "(707) 778-7756",
    "Cell": "(123) 456-7890",
    "DOB": "10/18/1991",
    "SSN": "123-34-2134"

}
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# reportlab.rl_config.TTFSearchPath.append(str(settings.BASE_DIR) + '/app/lib/reportlabs/fonts')
# pdfmetrics.registerFont(TTFont('Copperplate', 'Copperplate-Gothic-Bold.ttf'))

pdfmetrics.registerFont(TTFont('Courier New Regular', 'cour.ttf'))

#  Font mapping
packet = io.BytesIO()
packet2 = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=(612, 792), bottomup=0)
can.setFont('Courier New Regular', 7.98)

# Business Account Titling Box
if AccountInfo["Type"] == "Business":
    if AccountInfo["Prefix"] == "FBO":
        can.drawString(312.5, 61.5, AccountInfo["PrefixName"])
        can.drawString(312, 72, AccountInfo["Street"])
        can.drawString(312, 82, AccountInfo["City"])
    else:
        can.drawString(312.5, 61.5, AccountInfo["BusinessName"])
        can.drawString(312, 72, AccountInfo["Street"])
        can.drawString(312, 82, AccountInfo["City"])

#  Manger field
can.drawString(38, 173, signer1["Name"])


#  EIN Field
can.drawString(172, 196.5, AccountInfo["EIN"])

# Name FIeld in Paragraph
if AccountInfo["Prefix"] == "FBO":
    can.drawString(27.5, 208, AccountInfo["PrefixName"])
else:
    can.drawString(312.5, 61.5, AccountInfo["BusinessName"])

# Adding Signers & Titles
can.drawString(41, 350, f'{signer1["Name"]}-{signer1["Position"]}')
if signer2 != {}:
    can.drawString(41, 392, f'{signer2["Name"]}-{signer2["Position"]}')

if signer3 != {}:
    can.drawString(41, 433, f'{signer3["Name"]}-{signer3["Position"]}')

# Checking Ownership Type
if AccountInfo["Ownership"] == "Joint":
    can.drawString(17, 382.5, "X")
if AccountInfo["Ownership"] == "LLC":
    can.drawString(17, 448, "X")
if AccountInfo["Ownership"] == "CCorp":
    can.drawString(17, 459, "X")
if AccountInfo["Ownership"] == "SCorp":
    can.drawString(91.5, 459, "X")

#  Beneficiary Info
if AccountInfo["Benificiary"] == "POD":
    can.drawString(138.5, 518.5, "X")
    can.drawString(26, 576, AccountInfo["BeneficiaryDetails"])

can.save()

page2 = canvas.Canvas(packet2, pagesize=(612, 792), bottomup=0)
page2.setFont('Courier New Regular', 7.98)

#  Signer 2 Information Box
minSigners = str(chr(ord('@')+1))
maxSigners = str(chr(ord('@')+AccountInfo["totalSigners"]))

totalSigners = f'{minSigners}-{maxSigners}'

page2.drawString(32, 114, totalSigners)


page2.save()
# move to the beginning of the StringIO buffer
packet.seek(0)
packet2.seek(0)

new_pdf = PdfFileReader(packet)
new_pdf2 = PdfFileReader(packet2)
# read your existing PDF
existing_pdf = PdfFileReader('OGResolution.pdf', "rb+")
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
page2 = existing_pdf.getPage(1)
page2.mergePage(new_pdf2.getPage(0))

output.addPage(page)
output.addPage(page2)
output.addPage(existing_pdf.getPage(3))
# output.addPage(existing_pdf.getPage(4))

# finally, write "output" to a real file
outputStream = open("NewResolution.pdf", "wb")
output.write(outputStream)
outputStream.close()
# response = make_response("newSigCard.pdf")
# response.headers['Content-Type'] = 'application/pdf'
# response.headers['Content-Disposition'] = \
#     'inline; filename=%s.pdf' % 'yourfilename'
