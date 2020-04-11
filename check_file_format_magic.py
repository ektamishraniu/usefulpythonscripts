import magic #pip install python-magic-bin==0.4.14
import os

path = 'c:\\projects\\hc2\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

for f in files:
    if magic.from_file(f, mime=True).rsplit('/')[1] == 'plain':
        print(f, "   --    ", magic.from_file(f, mime=True))

print( magic.from_file('txtFile.txt', mime=True).rsplit('/')[1])

'''
#AWS Lambda function
def getFileFormat(myfile):
    s3c.download_file(sourceBucket, myfile, '/tmp/' + myfile)
    return magic.from_file("/tmp/" + myfile, mime=True).rsplit('/')[1].upper()   

def isPlainFileFormat(myfile):
    s3c.download_file(sourceBucket, myfile, '/tmp/' + myfile)
    if magic.from_file("/tmp/" + myfile, mime=True).rsplit('/')[1]=="plain":
        return True
'''