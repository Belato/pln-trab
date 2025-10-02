import nltk
from nltk.tokenize import PunktTokenizer
import re 

class PreProcessing:
    def __init__(self):
        nltk.download('stopwords')
        self.stop_words = nltk.corpus.stopwords.words('portuguese')
        # self.stemmer = nltk.stem.RSLPStemmer()
        

    def split_in_documents(self, text):
        sentences = text.split(';')
        return [sentence.strip() for sentence in sentences if sentence.strip()]

    def remove_stop_words(self, text):
        if isinstance(text, str):
            sentence = text.split()
            words = [word for word in sentence if word not in self.stop_words]
            formatted_text = ' '.join(words)
        else:
            formatted_text = [word for word in text if word not in self.stop_words]

        
        return formatted_text

    def stemming_words(self, text):
        stemmed_words = [self.stemmer.stem(word) for word in words]
        formatted_text = ' '.join(stemmed_words)
        return formatted_text

    def tokenization(self, text):
        tokens = nltk.word_tokenize(text)
        return tokens
    
    def remove_special_characters(self, text):
        formatted_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return formatted_text