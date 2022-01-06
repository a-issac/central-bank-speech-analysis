import copy as c
import random
import collections

import matplotlib.pyplot as plt
import re
import spacy
import nltk

from nltk.collocations import *
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer

# Etape d'initialisation des modules de nltk
nltk.download('genesis')
nltk.corpus.genesis.words('english-web.txt')
nltk.download('wordnet')
nltk.download('stopwords')

#Il faut définir un liste de stopwords (c'est-à-dire de mots non significatifs)
#En anglais
stop_words = set(stopwords.words('english'))
alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') #type(alphabet)=set "ensemble"
stop_words= stop_words | alphabet # On fait une union d'ensembles pour retirer des nuages de mots les lettres isolées
#L'étape précédeente peut êtr évitée en spécifiant min_word_length=2 dans la fonction WordCloud
wordlist=['The','It','And','this','This','The','the','these','These','those','Those','In','&','one','He','She','he','she','it','\\displaystyle','\\mathbb','\\neg','per','th','also','would','de','la']
stop_words.update(wordlist) #on ajoute des mots aux 'stopwords'
#Fonction qui permet d'obtenir une liste de mots en minuscules sans les stopwords

tokenizer = RegexpTokenizer(r'\w+')
#tokenizer.tokenize('Eighty-seven miles to go, yet.  Onward!')
#example_sent = "This is a sample sentence,showing off the stop words filtration."

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

lemmatizer = WordNetLemmatizer()


def randomsample(df, n=5):
    rawtext = ''
    L = random.sample(range(len(df)),n)
    for i in L:
        rawtext += df["title"][i] + df["contents"][i]
    # On commence par analyser 15 discours choisis au hasard
    return rawtext


def named_entity(rawtext):
    """Reconnaissance des entités nommées"""
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(rawtext)
    spacy.displacy.render(doc, style="ent", jupyter=True)
    return doc


def str_to_wordlist(text):
    text2 = c.copy(text)
    text2 = text2.lower() # minuscules
    text2 = re.sub(r'\d+','',text2) # enlever les nombres
    text2 = re.findall(r'\w+', text2) # enlever la ponctuation
    text2 = [word for word in text2 if not word in stop_words and len(word)>2] # enlever les stopwords
    return(text2)

#text = str_to_wordlist(text)

def freq_dict(text):
    res = {}
    for word in text:
        try:
            res[word] += 1
        except KeyError:
            res[word] = 1
    return(res)


#dictionary = freq_dict(rawtext)

def freq_mots(text):
    """Fonction pour récupérer les fréquences des mots d'un texte"""
    text = re.sub(r'==.*?==+', ' ', text)
    text = text.replace('\n', ' ')
    text = text.replace('\'',' ')
    text = re.sub(r'[^\w\s]',' ',text) #retire la ponctuation
    text = re.sub(r'\d+','',text) #retire les nombres
    text = text.replace('%',' ')
    text = text.replace('+',' ')
    text = text.replace('=',' ')
    text = text.replace('*',' ')
    text = text.replace('_',' ')
    text = text.replace('-',' ')
    T = [mot for mot in text.split() if mot not in list(stop_words)]
    return collections.Counter(T)

def liste_mots(text):
    """Fonction pour récupérer la liste des mots d'un texte brut"""
    text = re.sub(r'==.*?==+', ' ', text)
    text = text.replace('\n', ' ')
    text=text.replace('\'',' ')
    text=re.sub(r'[^\w\s]',' ',text) #retire la ponctuation
    text = re.sub(r'\d+',' ',text) #retire les nombres
    text=text.replace('%',' ')
    text=text.replace('+',' ')
    text=text.replace('=',' ')
    text=text.replace('*',' ')
    text=text.replace('_',' ')
    text=text.replace('-',' ')
    return [mot for mot in text.split() if mot not in list(stop_words)]

def plus_frequents(text, n):
    """Fonction pour récupérer les n mots les plus fréquents (hors stopwords) dans un texte brut"""
    L = []
    text = re.sub(r'==.*?==+', ' ', text)
    text = text.replace('\n', ' ')
    text = text.replace('\'',' ')
    text = re.sub(r'[^\w\s]',' ',text) #retire la ponctuation
    text = re.sub(r'\d+',' ',text) #retire les nombres
    text = text.replace('%',' ')
    text = text.replace('+',' ')
    text = text.replace('=',' ')
    text = text.replace('*',' ')
    text = text.replace('_',' ')
    text = text.replace('-',' ')
    T = [mot for mot in text.split() if mot not in list(stop_words)]
    for tuple in collections.Counter(T).most_common(n):
        L.append([tuple[0],tuple[1]])
    return L

def tokens_filter(text):
    word_tokens = tokenizer.tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words] #retire les stopwords
    return filtered_sentence

def word_counter(text, n):
    return collections.Counter(text).most_common(n)

def get_bigrams(text, freq = 3):
    """On détermine les Bigrammes"""
    finder = BigramCollocationFinder.from_words(text)
# only bigrams that appear 3+ times
    finder.apply_freq_filter(freq)
    return finder

def get_trigrams(text, freq = 3):
    """On détermine les Trigrammes"""
    finder = TrigramCollocationFinder.from_words(text)
# only trigrams that appear 3+ times
    finder.apply_freq_filter(freq)
    return finder



def print_trigram_likelihood(finder):
    """ return the 10 n-grams with the highest PMI"""
# print (finder.nbest(trigram_measures.likelihood_ratio, 10))
    for i in finder.score_ngrams(trigram_measures.likelihood_ratio):
        print (i)
    return None

def print_bigram_likelihood(finder):
    """return the 10 n-grams with the highest PMI"""
# print (finder.nbest(bigram_measures.likelihood_ratio, 10))
    for i in finder.score_ngrams(bigram_measures.likelihood_ratio):
        print (i)
    return None

def year_speeches(df, year):
    #df : pandas dataframe
    #year : int
    text=''
    df_year=df[df["Year"] == year].reset_index(drop=True)
    for i in range(len(df_year)):
        text+=df_year["title"][i]+df_year["contents"][i]
    return text

def freq_words_year(df,year,n = 10):
    #df : pandas dataframe
    #year : int
    #n : int
    text=year_speeches(df,year)
    return collections.Counter(tokens_filter(text)).most_common(n)

def plot_freq_word(df, year, n=10):
    """Affiche les mots les plus fréquents de l'année year """
    L = freq_words_year(df,year,n)
    x = []
    y = []
    z = []
    for i in range(len(L)):
        x.append(L[i][0])
        y.append(L[i][1])
        z.append(round(100*L[i][1]/L[0][1],1))

    plt.clf()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xticklabels(labels=x, rotation=45)
    ax.title.set_text("Termes les plus fréquents dans les discours de l'année " + str(year))
    return plt.bar(x,y)
