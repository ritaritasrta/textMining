import readline
import nltk
#from nltk.corpus import stopwords
from nltk import tokenize
from nltk.tokenize import sent_tokenize

p = "Hey this is Rita and welcome to my text mining project. This txt file will be used as an input feeder. I'm just going to type a bunch of stuff here and feed it into the main program that is called text_summarizer. I watched a bunch of YouTube videos and tried to copy different methods and pieced together different variations on how to efficiently write a summarizer program. Feel free to scour the code and download it to run your text file through. It can really help you with summarizing textbooks, books, phamphlets, etc. Enjoy!"
pnew = tokenize.sent_tokenize(p)
print(p)