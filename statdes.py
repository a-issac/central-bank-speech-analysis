import datetime
import copy as c
import random
import collections
import time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
#!pip install spacy
import spacy
#!pip install langdetect
import langdetect
import nltk
from nltk.corpus import stopwords



def count_speeches(df, groupingby = 'Year', kind = 'line'):
    df_grouped = df.groupby(groupingby).count()
    dict1 = {'bar' : 'N', 'line' : 'Evolution du n'}
    dict2 = {'Year' : 'Année', 'Month' : 'Mois', 'Day' : 'Jour du mois', 'DayofWeek' : 'Jour de la semaine'}

    plot = df_grouped["date"].plot(title = dict1[kind] + 'ombre de discours du Comité Exécutif de la BCE par' + dict2[groupingby], xlabel = dict2[groupingby])
    return plot

def distinct_dates(df):
    n_dates=df["date"].nunique()
    print("Il y a",
          n_dates,
          "dates distinctes dans ce jeu de données, soit en moyenne environ",
          round(n_dates/len(df),3),
          "discours par jour.")
    #Pour aller plus loin dans l'analyse du nombre de discours par jour
    print("Il y a",
          (df["date"].value_counts()>=2).sum(),
          "jours pour lesquels plus qu'un seul discours, soit",
          round(((df["date"].value_counts()>=2).sum()/n_dates)*100,2),
          "% de l'échantillon étudié.")

    print("Il y a",
          (df["date"].value_counts()==2).sum(),
          "jours pour lesquels on a 2 discours.")
    print("Il y a",
          (df["date"].value_counts()==3).sum(),
          "jours pour lesquels on a 3 discours.")
    print("Il y a",
          (df["date"].value_counts()==4).sum(),
          "jours pour lesquels on a 4 discours.")
    print("Il y a",
          (df["date"].value_counts()==5).sum(),
          "jours pour lesquels on a 5 discours.")
    return None

def speech_months(df):
    plt.clf()
    plt.figure()
    df["Month_str"].value_counts().plot(kind="bar")
    plt.title("On which month are ECB speeches delivered?")
    return None

def top_speakers(df, n=15):
    plt.clf()
    plt.figure()
    df["speakers"].value_counts()[:n].plot(kind="bar")
    plt.title("Top " + str(n) + " ECB Speakers")
    return None
