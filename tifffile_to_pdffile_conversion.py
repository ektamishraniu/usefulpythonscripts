import img2pdf 
from PIL import Image 
import os 
  
img_file = "sample.tif"
img_name = img_file.rsplit('.',1)[0]
img_fmt  = img_file.rsplit('.',1)[1].upper()
pdf_file = img_file.rsplit('.',1)[0] + ".pdf"

def convertToPdf(img_file):
    pdf_file = img_file.rsplit('.',1)[0] + ".pdf"
    myimage = Image.open(img_file)
    pdf_bytes = img2pdf.convert(myimage.filename) 
    myfile = open(pdf_file, "wb") 
    myfile.write(pdf_bytes) 
    myimage.close() 
    myfile.close() 
    print("Successfully made pdf file: ", pdf_file) 


convertToPdf(img_file)    