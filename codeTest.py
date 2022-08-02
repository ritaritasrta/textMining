from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize


with open('textMiningExample.txt', 'r') as file:
    lines = file.readline()

    #first clean data by making all lower-case
    for lines in file:
        lines = lines.lower()

    #next split the file sentences into different sentences
    #use nltk tokenize lib function
    token_text = sent_tokenize(file)
    print(token_text)

    #remove any/all unicode characters
    for i in lines:
        file_all_ascii = file.encode("ascii", "ignore")






    file.close()


