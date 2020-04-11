import docx #installed via python-docx
        
def getText(filename):
    doc = docx.Document(filename)
    print(getdocumenttext(doc))           
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return ""
    return '\n'.join(fullText)
    
print(getText("docxfile.docx"))
