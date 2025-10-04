import nltk
import enchant
import re 


class PreProcessing:
    def __init__(self):
        nltk.download('stopwords')
        self.stop_words = nltk.corpus.stopwords.words('portuguese')
        self.stemmer = nltk.stem.RSLPStemmer()
        self.words_dict = enchant.Dict("pt_BR")
        

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


    def tokenization(self, text):
        tokens = nltk.word_tokenize(text)
        for t in tokens:
            if '-' in t:
                tokens.remove(t)
                new_tokens = t.split('-')
                tokens.extend(new_tokens)


        return tokens
    
    def remove_special_characters(self, text):
        
        formatted_text = []
        for word in text:
            format_word = re.sub(r'[^\w\s]', '', word)
            if format_word:
                formatted_text.append(format_word)
        return formatted_text


    def stemming_words(self, text):
        
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
        
    
    def correct_words(self, text):
        from Levenshtein import distance

        formatted_text = []
        for word in text:

            if not self.words_dict.check(word):
                similar_words = self.words_dict.suggest(word)

                most_similar_word = {"word": word, "distance": 100}
                for s_word in similar_words:

                    dist = distance(word, s_word)
                    if dist < most_similar_word["distance"]:
                        most_similar_word["distance"] = dist
                        most_similar_word["word"] = s_word

                word = most_similar_word["word"]
                # word = self.words_dict.suggest(word)[0]
            formatted_text.append(word)

        return formatted_text
    

    def pipeline(self, text):
        # text = self.split_in_documents(text)
        text = self.lower_text(text)
        for sentence in text:
            tokens = self.tokenization(sentence)
            tokens = self.remove_special_characters(tokens)
            tokens = self.remove_stop_words(tokens)
            tokens = self.correct_words(tokens)
            tokens = self.stemming_words(tokens)
            text[text.index(sentence)] = tokens

        return text