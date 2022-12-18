#from PyPDF2 import PdfFileReader, PdfFileWriter
import PyPDF2
import os
import pandas as pd

pd.set_option('display.max_rows', 500)

pd.set_option('display.max_rows', 500)

# Set the directory where the PDF files are located
directory = './pdf'


text = []
# Use a for loop to iterate over the files in the directory
for filename in os.listdir(directory):
    # Check if the current file is a PDF file
    if filename.endswith('.pdf'):
        # Open the PDF file using the PyPDF2 library
        with open(os.path.join(directory, filename), 'rb') as f:
            reader = PyPDF2.PdfFileReader(f)

            # Use the reader.numPages property to get the number of pages in the PDF
            num_pages = reader.numPages

            # Use a for loop to iterate over the pages in the PDF
            for page_num in range(num_pages):
                # Use the reader.getPage() method to get the current page
                page = reader.getPage(page_num)

                # Use the page.extractText() method to extract the text from the page
                page_text = page.extractText()

                # Print the text from the current page
                #print(page_text)
                text.append(page_text)


#extra steps needed for test

df = pd.read_excel('.\excell\date.xlsx', header=0)

#print(df['Name'])
df['full_name'] = df['Förnamn'] + ' ' + df['Efternamn']

num_rows = df.shape[0]
newdf = df.drop(num_rows - 1)





checklist = []
for name in newdf['full_name']:
    for t in text:
        if name in t:
            checklist.append(name)
        else:
            pass

for name in newdf['full_name']:
    if name not in checklist:
        print(name)








