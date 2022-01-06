# Description du dossier "tests"

Ce dossier a permis de faire des essais pour l'import, le traitement et la visualisation des données puis tester différents modèles.
Ce travail a été divisé en plusieurs notebooks pour accélérer l'exécution du code et permettre une plus grande lisibilité des différentes parties.

## Détail du contenu de "tests"

- *Tests-WebscrapingLink.ipynb* : ce notebook contient le code pour "webscraper" le lien du dataset des discours sur le site de la Banque Centrale Européenne et la date de la dernière mise à jour de ce dataset.

- *Tests-CentralBankSpeeches.ipynb* : ce notebook a servi à tester l'import des données, au nettoyage du dataset. Il contient les premières étapes de statistiques descriptives et de NLP.

- *Tests-LanguageDetection.ipynb* : comme tous les discours ne sont pas en anglais, il faut enlever les discours gênants. Pour cela, on compare plusieurs méthodes de détection de langage dans ce notebook.

- *Tests-EconomicData.ipynb* : ce notebook sert à tester différentes sources et méthodes pour importer des données économiques et financières.

- *Tests-SentimentAnalysis.ipynb* : pour chaque discours du dataset, on cherche à évaluer par différentes méthodes un score reflétant les "sentiments" (positivité et négativité). On utilise pour cela des bases de données de mots "polarisés" déjà existantes.

- *Tests-LDA.ipynb* : pour classifier les différents sujets abordés dans les discours, on utilise la Latent Dirichlet Allocation (LDA) permettant de faire du topic modelling

- *Tests-regression-random-forest.ipynb* : ce notebook contient quelques tests sur de régressions linéaires et avec Random Forest sur les données et variables obtenues précédemment.

- *regression.ipynb* : ce notebook contient d'autres tests sur de régressions linéaires et avec Random Forest sur les données et variables obtenues précédemment.

- *finbert + tf idf.ipynb* : ce notebook contient des éléments de nettoyage de données, une tentative d'utilisation de finbert pour l'analyse de sentiment et le calcul du score de tf-idf pour les documents (infructueux par manque de mémoire)0

