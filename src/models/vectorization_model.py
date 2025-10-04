from gensim.models import Word2Vec, FastText
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np


class VectorizationModel:


    def binary_aproach(self, text: str):

        vectorizer = CountVectorizer(binary=True)

        union_sentences = []
        for sentence in text:
            union_sentences.append(' '.join(sentence))
        sentence_matrix = vectorizer.fit_transform(union_sentences)

        words_names = vectorizer.get_feature_names_out()

        sentence_vectors = []
        sentence_vectors.append(words_names)
        sentence_vectors.extend(sentence_matrix.toarray())
        return sentence_vectors
        

    def bow_aproach(self, text: str):

        vectorizer = CountVectorizer()

        union_sentences = []
        for sentence in text:
            union_sentences.append(' '.join(sentence))
        sentence_matrix = vectorizer.fit_transform(union_sentences)

        words_names = vectorizer.get_feature_names_out()

        sentence_vectors = []
        sentence_vectors.append(words_names)
        sentence_vectors.extend(sentence_matrix.toarray())
        return sentence_vectors
    

    def tf_idf_aproach(self, text: str):

        vectorizer = TfidfVectorizer()
        union_sentences = []
        for sentence in text:
            union_sentences.append(' '.join(sentence))
        sentence_matrix = vectorizer.fit_transform(union_sentences)

        words_names = vectorizer.get_feature_names_out()

        sentence_vectors = []
        sentence_vectors.append(words_names)
        sentence_vectors.extend(sentence_matrix.toarray())
        
        return sentence_vectors
    
    def word2vec_aproach_words(self, text: str):
        model = Word2Vec(sentences=text, vector_size=100, window=5, min_count=1, workers=4, sg=1)
        word_vectors = []
        for setence in text:


            for word in setence:

                already_exists = False
                for w2 in word_vectors:
                    if word == w2:
                        already_exists = True
                
                if not already_exists:
                    word_vectors.append(
                        {
                            'word': word,
                            'vector': model.wv[word]
                        }
                    )
        return word_vectors
    

    def word2vec_aproach_sentences(self, text: str):
        model = Word2Vec(sentences=text, vector_size=100, window=5, min_count=1, workers=4, sg=1)
        sentence_vectors = []
        sentence_vectors.append(text)
        for setence in text:

            word_vectors = []
            for word in setence:

                word_vectors.append(model.wv[word])
            
            sentence_vectors.append(np.mean(word_vectors, axis=0))

        return sentence_vectors
    
    
    def fasttext_aproach_words(self, text: str):
        model = FastText(sentences=text, vector_size=100, window=5, min_count=1, workers=4, sg=1)
        word_vectors = []
        
        for setence in text:

            for word in setence:

                already_exists = False
                for w2 in word_vectors:
                    if word == w2:
                        already_exists = True
                
                if not already_exists:
                    word_vectors.append(
                        {
                            'word': word,
                            'vector': model.wv[word]
                        }
                    )
        return word_vectors
    

    def fasttext_aproach_sentences(self, text: str):
        model = FastText(sentences=text, vector_size=100, window=5, min_count=1, workers=4, sg=1)
        sentence_vectors = []
        sentence_vectors.append(text)
        for setence in text:

            word_vectors = []
            for word in setence:

                word_vectors.append(model.wv[word])
            
            sentence_vectors.append(np.mean(word_vectors, axis=0))

        return sentence_vectors