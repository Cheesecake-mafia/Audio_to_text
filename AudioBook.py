# -*- coding: utf-8 -*-
import PyPDF2
from gtts import gTTS
import os
import pyttsx3 

def tts(filePath,speak=False):
    book = open(filePath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    textToBeRead = ' '
    
    filename = os.path.split(filePath)[-1]
    
    pageObj = pdfReader.getPage(0)
    
    if speak == True:
        speaker = pyttsx3.init()
        for num in range(pages):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()
    
    for page in range(pages):
        pageObj = pdfReader.getPage(page)
        textToBeRead = textToBeRead + pageObj.extractText()
    
    
    
    book.close()
    language = 'en'
    savename = filename.split(".")[0]
    myobj = gTTS(text=textToBeRead, lang=language, slow=False)
    myobj.save(savename + ".mp3")

