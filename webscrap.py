import time

import urllib
import lxml.html
import requests
import bs4 #Beautiful Soup
import pandas as pd

def get_all_links(url):
    '''renvoie la liste de tous les liens présents sur la page correspondant à l'url'''
    list_links=[] #on initialise avec une liste vide
    STATUS_CODE=requests.get(url).status_code
    #Si le code retour est 200, il y a bien du contenu accessible sur la page.
    if STATUS_CODE!=200:
        print("ERREUR CODE", STATUS_CODE)
    else: #il y a bien du contenu accessible sur la page
        page = urllib.request.urlopen(url) # on se connecte à la page pour obtenir le code source
        dom =  lxml.html.fromstring(page.read()) #permet de "lire" le code source
        for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
            list_links.append(link)
        return list_links

def find_first_link_with_string(list_links, string):
    '''renvoie le premier lien de la liste contenant une certaine chaine de caractères'''
    for link in list_links:
        if string in link:
            return link

def get_dataset_url(url):
    '''renvoie la partie de l'url du dataset des discours de la BCE'''
    '''on utilise toutes les fonctions précédentes'''
    string="/press/key/shared/data/all_ECB_speeches.csv" #chaine de caractères identifiant le lien du dataset
    list_links=get_all_links(url) #on obtient la liste de tous les liens de la page
    url=find_first_link_with_string(list_links,string) #on cherche le lien du dataset grâce à la chaine de caractères
    return url

def last_update_dataset(url):
    '''renvoie la date de la dernière mise à jour du dataset'''
    STATUS_CODE=requests.get(url).status_code
    #Si le code retour est 200, il y a bien du contenu accessible sur la page.
    if STATUS_CODE!=200:
        print("ERREUR CODE", STATUS_CODE)
    else: #il y a bien du contenu accessible sur la page
        request_text = urllib.request.urlopen(url).read() #On se connecte à la page pour obtenir le code source
        page = bs4.BeautifulSoup(request_text, "lxml")
        update_date=page.select_one("span[class*=lastUpdate]").text #on sélectionne le contenu de la classe lastUpdate
        return update_date
