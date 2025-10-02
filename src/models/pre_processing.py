import nltk
import enchant
import re 


class PreProcessing:
    def __init__(self):
        nltk.download('stopwords')
        self.stop_words = nltk.corpus.stopwords.words('portuguese')
        self.stemmer = nltk.stem.RSLPStemmer()
        # self.words_dict = enchant.Dict("pt_BR")
        

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

    # def stemming_words(self, text):
    #     stemmed_words = [self.stemmer.stem(word) for word in text]
    #     formatted_text = ' '.join(stemmed_words)
    #     return formatted_text

    def tokenization(self, text):
        tokens = nltk.word_tokenize(text)
        
        

        return tokens
    
    def remove_special_characters(self, text):
        
        formatted_text = []
        for word in text:
            format_word = re.sub(r'[^\w\s]', '', word)
            if format_word:
                formatted_text.append(format_word)
        return formatted_text


    def stemizer(self, text):
        
        formatted_text = []
        for word in text:
            formatted_text.append(self.stemmer.stem(word))

        return formatted_text
    
    def lower_text(self, text):
        if isinstance(text, list):
            new_text = [sentence.lower() for sentence in text] 
        else:
            new_text = text.lower()

        return new_text
        
    
    # def correct_words(self, text):

    #     formatted_text = []
    #     for word in text:

    #         if not self.words_dict.check(word):
    #             formatted_text.append(self.words_dict.suggest(word))

    #     return formatted_text