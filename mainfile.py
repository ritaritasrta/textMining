

cleanFile = open("cleanText.txt", 'w')
with open('textMiningExample.txt') as myFile, open('stop_words_english.txt') as stopWordsFile:
    for line in myFile:
         #clean data by making all alpha lowercase
        line = line.lower() 

    #next split the file sentences into different lines
    #split by using period


        #remove all unicode characters
        line.encode('ascii', 'ignore').decode()
        a = myFile.read().split()
        b = stopWordsFile.read().split()

        #likely to marge some portion of unicode character removal into other file




 

