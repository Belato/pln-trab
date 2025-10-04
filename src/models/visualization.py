import numpy as np
import pandas as pd

class Visualization:


    def plot(self, similarity_data, original_docs, vec_model = 'binary', sim_method = 'jaccard_distance'):
    
        formatted_data = np.tril(similarity_data, k=-1)
        similarity_matrix = pd.DataFrame(formatted_data, 
            index=original_docs,
            columns=original_docs) 
        
        
        similarity_matrix.to_csv(f"data/{vec_model}-{sim_method}.csv")
        similarity_matrix.to_excel(f"data/{vec_model}-{sim_method}.xlsx")

        return similarity_matrix
