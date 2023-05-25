"""
    Cluster and Cloud Computing 2023
    Assignment 2
    Team 46

    Kunal Patel : 1291822
    Mayank Yadav : 1403092
    Harsh Mangla : 1418017
    Sophie von Doussa : 1064884
    Maxson Stephen Mathew : 1428525

    City : Melbourne
"""


from string import punctuation
import spacy
from langdetect import detect
from nltk.stem import PorterStemmer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import html2text


class TootProcessor:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.h = html2text.HTML2Text()
        self.h.ignore_links = True



    #function to get hotwords
    def _get_hotwords(self, text):
        result = []
        pos_tag = ['PROPN', 'NOUN']  # removed 'ADJ' terms
        doc = self.nlp(text.lower()) 
        for token in doc:
            if(token.text in self.nlp.Defaults.stop_words or token.text in punctuation or token.text.startswith("http")):
                continue
            if(token.pos_ in pos_tag):
                result.append(token.text)
        return result



    def processToot(self, status, base_url):
        text=self.h.handle(status['content']).strip("\n ")

        try:
            language = detect(text)
        except:
            return None, None

        if status['language'] != 'en' or language != 'en':
            return None, None

        date=str(status['created_at'])
        toot_id=str(status['id'])

        # get the sentiment
        sentiment = SentimentIntensityAnalyzer()
        sentimentscore=sentiment.polarity_scores(text)
        # get the hottokens
        hottokens=self._get_hotwords(text)
        ps=PorterStemmer()
        hottokenstems=[]
        for word in hottokens:
            hottokenstems.append(ps.stem(word))
        hottokenstems=list(set(hottokenstems))

        data={
            'date':date,
            'server':base_url,
            'sentiment':sentimentscore,
            'hottokens':hottokenstems,
            'content':text
        }

        return toot_id, data