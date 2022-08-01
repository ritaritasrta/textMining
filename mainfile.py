

cleanFile = open("cleanText.txt", 'w')
with open('textMiningExample.txt') as myFile, open('stop_words_english.txt') as stopWordsFile:
    for line in myFile:
         #clean data by making all alpha lowercase
        line = line.lower() 

        #remove all unicode characters
        line.encode('ascii', 'ignore').decode()
        a = myFile.read().split()
        b = stopWordsFile.read().split()





 

