from sklearn.metrics import jaccard_score
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial import distance

class SimilarityCalculation:

    def cosine_similarity_method(self, word_verctor):
        matrix = []  
        for index in range(1, len(word_verctor)):

            array = []
            for index2 in range(1, len(word_verctor)):

                cosine_distance = distance.cosine(word_verctor[index], word_verctor[index2])
                similarity = 1 - cosine_distance
                array.append(similarity)

            matrix.append(array)
        
        return matrix
        

    def jaccard_distance_method(self, word_verctor):

        matrix = []  
        for index in range(1, len(word_verctor)):

            array = []
            for index2 in range(1, len(word_verctor)):
                similarity = jaccard_score(word_verctor[index], word_verctor[index2])
                # distance = 1 - similarity
                array.append(similarity)

            matrix.append(array)
        
        return matrix
        

