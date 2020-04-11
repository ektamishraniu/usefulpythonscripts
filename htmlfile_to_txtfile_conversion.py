from bs4 import BeautifulSoup
import json

def getHtml(filename):
    txt_file = filename.rsplit('.', 1)[0] + ".txt"
    myfile = open(txt_file, "w")

    filename=open(filename, 'rb').read()
    soup= BeautifulSoup(filename, features='lxml')
    fulltext= soup.get_text()
    fulltext="\n".join([ll.rstrip() for ll in fulltext.splitlines() if ll.strip()])
    myfile.write(fulltext)
    
    #form= soup.find('form')
    if soup.find('form') is not None:
        fields = soup.find('form').findAll('input')
        formdata = dict( (field.get('name'), field.get('value')) for field in fields)
        myfile.write(json.dumps(formdata))
        
    myfile.close()

    
print(getHtml("htmfile.htm"))

'''
#AWS Lambda function

import json
import boto3
from bs4 import BeautifulSoup
import os

s3c = boto3.client('s3')
s3r = boto3.resource('s3')

textractBucket = "target-bucket"
sourceBucket = "source-bucket"


def convHtmlToText(Html_file):
    s3c.download_file(sourceBucket, Html_file, '/tmp/' + Html_file)
    html = open('/tmp/' + Html_file, 'rb')
    soup = BeautifulSoup(html.read(), features='lxml')
    text = soup.get_text()
    text = "\n".join([ll.rstrip() for ll in text.splitlines() if ll.strip()])
    txt_file = Html_file.rsplit('.', 1)[0] + ".txt"
    myfile = open('/tmp/' + txt_file, "w")
    myfile.write(text)
    if soup.find('form') is not None:
        fields = soup.find('form').findAll('input')
        formdata = dict( (field.get('name'), field.get('value')) for field in fields)
        myfile.write(json.dumps(formdata))    

    myfile.close()
    os.remove('/tmp/' + Html_file)
    s3r.Object(textractBucket, txt_file).put(
        Body=open('/tmp/' + txt_file, 'rb'))

def lambda_handler(event, context):
    # theobjects = s3c.list_objects_v2(Bucket=sourceBucket)
    # for object in theobjects['Contents']:
    #     Html_file = object['Key']
    #     basename = os.path.basename(Html_file)
    #     dn, dext = os.path.splitext(basename)
    #     Html_extn = dext[1:].upper()

    #     if Html_extn in ["HTML", "HTM"]:
    Html_file = event['Filename']
    convHtmlToText(Html_file)

    return
'''