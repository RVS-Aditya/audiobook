#To read PDF file using Python pip install pypdf2 To Read text (Text to speech) pip install pyaudio pip install pyttsx3
import pyttsx3
import PyPDF2
book = open('crack python exam.pdf', 'rb' or any pdf u want)
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(1, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
