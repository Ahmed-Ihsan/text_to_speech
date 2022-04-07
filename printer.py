from win32com import client
import time


def printWordDocument(filename):
    word = client.Dispatch("Word.Application")
    word.Documents.Open(filename)
    word.ActiveDocument.PrintOut()
    time.sleep(2)
    word.ActiveDocument.Close()

    word.Quit()

def printPDFDocument(filename):
    ie = client.Dispatch("InternetExplorer.Application")
    ie.Navigate(filename)

    if ie.Busy:
        time.sleep(1)
    ie.Document.printAll()
    time.sleep(2)
    ie.Quit()
