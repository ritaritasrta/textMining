from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as netx

def read_text(my_file):
    file = open(my_file, "r")
    data = file.readlines()
    text_blob = data[0].split(". ")
    sentences = []
    for sentences in text_blob:
        sentences.append(sentences.replace("[^a-za-Z]", " ").split(" "))
        sentences.pop()
        return sentences

def sentence_similarity_track(sen1, sen2, stopwords = None):
    if stopwords is None:
        stopwords = []
        
    #makes all words in sentences 1 and 2 lowercase and puts into array
    sen1 = [word.lower() for word in sen1]
    sen2 = [word.lower() for word in sen2]
    
    #combines all sentence 1 and 2
    full_text_words = list(set(sen1+sen2))
    
    
    #add proper commentary/documentation
    vector1 = [0] *len(full_text_words)
    vector2 = [0] *len(full_text_words)
    for words in sen1:
        if words in stopwords:
            continue
        vector1[full_text_words.index(w)] += 1
    for words in sen2:
        if words in stopwords:
            continue
        vector2[full_text_words.index(w)] += 1
        
    #checks the similarity between the 2 sentences
    return 1 - cosine_distance(vector1, vector2)

def similarity_matrix(sentences, stop_words):
    similarity_mat = np.zeroes(len(sentences), len(sentences))
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:
                continue
            similarity_mat[idx1][idx2] = sentence_similarity_track(sentences[idx1], sentences[idx2], stop_words)
    
    return similarity_mat

def show_summary(my_file, top_n = 5):
    stop_words = stopwords.words('english')
    summary = []
    sentences = read_text(my_file)
    sentence_sim_matrix = similarity_matrix(sentences, stop_words)
    sentence_sim_graph = netx.from_numpy_array(sentences)
    scoring = netx.pagerank(sentence_sim_graph)
    ranked_entences = sorted(((scoring[i],s) for i, s in enumerate(sentences)), reverse = true)
    for i in range(top_n):
        summary.append(" ".join(ranked_entences[i][1]))
    print("Summary: \n", ". ".join(show_summary))

show_summary("textMiningExample.txt", 2)