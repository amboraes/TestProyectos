from sys import maxsize
from csv import DictReader, field_size_limit
from os import listdir
from re import findall
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
maxInt = maxsize
decrement = True

set(stopwords.words('english'))

def countT(texto, palabra):
    nlist = findall(r"[\w']+", texto)
    return nlist.count(palabra)

def test():
    try:
        a = input('Ingrese la palabra que desea buscar: ')
    except ValueError:
        print ("Not a string")

    arr = []
    count = 0
    finalstr = ""
    listDir = listdir('./all-the-news')
    for dirs in listDir:
        with open ('./all-the-news/'+dirs) as csvf:
            readCSV = DictReader(csvf)
            for row in readCSV:
                tempCont = row['content'].lower()
                tempTitle = row['title'].lower()
                finalstr +=tempCont
                finalstr +=tempTitle

                #count = countT(tempCont, a.lower()) + countT(tempTitle, a.lower())
            print("done processing")
        csvf.close()
    wortdtokens = word_tokenize(finalstr)
    print("done tokenizer")

    arr = sorted(arr, key=lambda x: x[0])
    arr.reverse()

while decrement:

    decrement = False
    try:
        field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

    test()
