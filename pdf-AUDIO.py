import PyPDF2
from gtts import gTTS

pdfFileObj=open("1.pdf","rb")
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)

mytext=""

for pageNum in range(pdfReader.numPages):
    pageObj= pdfReader.getPage(pageNum)

    mytext +=pageObj.extractText()
print(mytext)
f=open("output/final.txt","w")
f.write(mytext)
pdfFileObj.close()

tts=gTTS(text=mytext,lang='en')
tts.save("output/final.mp3")