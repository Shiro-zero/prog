import feedparser
import csv
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import requests
from bs4 import BeautifulSoup
import time


# URLs des flux RSS et des pages web à analyser
rss_urls = ["https://www.01net.com/actualites/feed","https://www.zdnet.fr/services/rss/","https://www.computerworld.com/news/index.rss"]
web_urls = []

# Création d'un fichier CSV pour enregistrer les articles filtrés
with open('articles.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    # Écriture des en-têtes de colonnes
    writer.writerow(['Titre', 'Date', 'Lien', 'Auteur',
                    'Sujet', 'Mots-clés', 'Résumé'])

    # Téléchargement des données de l'outil de tokenization de NLTK si elles ne sont pas déjà présentes
    nltk.download('stopwords')
    nltk.download('punkt')

    # Création d'un objet PorterStemmer pour le stemming des mots
    stemmer = PorterStemmer()

    # Parcours des flux RSS
    for rss_url in rss_urls:
        # Récupération des articles du flux RSS
        feed = feedparser.parse(rss_url)

        # Parcours des articles du flux RSS
        for entry in feed.entries:
            # Filtrage des articles publiés après le 1er janvier 2021
            timestamp_article = time.mktime(entry.published_parsed)
            depuis =  time.mktime((2021, 1, 1, 0, 0, 0, 0, 0, 0))
            if entry.published_parsed > depuis:
                # Récupération de l'auteur, du sujet et des mots-clés de l'article
                author = entry.author if 'author' in entry else ''
                subject = entry.tags[0]['term'] if 'tags' in entry else ''
                keywords = ', '.join(
                    [tag['term'] for tag in entry.tags[1:]]) if 'tags' in entry else ''

                # Téléchargement des données de stopwords de NLTK si elles ne sont pas déjà présentes
                nltk.download('stopwords')

                # Récupération du contenu de l'article et préparation du texte pour l'analyse
                content = entry.content[0]['value']
                # Suppression des balises HTML
                content = re.sub(r'<[^>]*>', '', content)
                content = content.lower()  # Mise en minuscules
                # Suppression des caractères spéciaux
                content = re.sub(r'[^a-zA-Z0-9 ]', '', content)
                words = word_tokenize(content)  # Tokenization des mots
                words = [word for word in words if word not in stopwords.words(
                    'english')]  # Filtrage des stopwords
                words = [stemmer.stem(word)
                         for word in words]  # Stemming des mots
                # Reconstitution du texte à partir des mots traités
                content = ' '.join(words)

                # Génération d'un résumé automatisé de l'article en utilisant les mots les plus fréquents
                word_frequencies = {}
                for word in words:
                    if word in word_frequencies:
                        word_frequencies[word] += 1
                    else:
                        word_frequencies[word] = 1
                summary = ''
                for word, frequency in word_frequencies.items():
                    if frequency > 1:
                        summary += f'{word} '
                # Troncature du résumé à 300 caractères
                summary = summary[:300] + '...'

                # Écriture des informations de l'article dans le fichier CSV
                writer.writerow([entry.title, entry.published,
                                entry.link, author, subject, keywords, summary])


    # Parcours des pages web
    for web_url in web_urls:
        # Récupération du contenu de la page web
        page = requests.get(web_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Sélection des éléments contenant les informations des articles
        articles = soup.select('.article')

        # Parcours des articles
        for article in articles:
            # Récupération de l'auteur, du sujet et des mots-clés de l'article
            author = article.select('.author')[0].text if article.select('.author') else ''
            subject = article.select('.subject')[0].text if article.select('.subject') else ''
            keywords = article.select('.keywords')[0].text if article.select('.keywords') else ''
            title = article.select('.title')[0].text
            link = article.select('.title')[0]['href']
            # Téléchargement des données de stopwords de NLTK si elles ne sont pas déjà présentes
            nltk.download('stopwords')

            # Récupération du contenu de l'article et préparation du texte pour l'analyse
            content = article.select('.content')[0].text
            content = content.lower()  # Mise en minuscules
            # Suppression des caractères spéciaux
            content = re.sub(r'[^a-zA-Z0-9 ]', '', content)
            words = word_tokenize(content)  # Tokenization des mots
            words = [word for word in words if word not in stopwords.words(
                'english')]  # Filtrage des stopwords
            words = [stemmer.stem(word) for word in words]  # Stemming des mots
            # Reconstitution du texte à partir des mots traités
            content = ' '.join(words)

            # Reconstitution du texte à partir des mots traités
            content = ' '.join(words)

            # Génération d'un résumé automatisé de l'article en utilisant les mots les plus fréquents
            word_frequencies = {}
            for word in words:
                if word in word_frequencies:
                    word_frequencies[word] += 1
                else:
                    word_frequencies[word] = 1
            summary = ''
            for word, frequency in word_frequencies.items():
                if frequency > 1:
                    summary += f'{word} '
            # Troncature du résumé à 300 caractères
            summary = summary[:300] + '...'

            # Écriture des informations de l'article dans le fichier CSV
            writer.writerow([article.select('.title')[0].text,
                            '', '', author, subject, keywords, summary])
