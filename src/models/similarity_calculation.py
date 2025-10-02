class SimilarityCalculation:
    def __init__(self, method: str):
        self.method = method

    def calculate(self, vec1, vec2):
        # Dummy implementation for illustration purposes
        return sum(a * b for a, b in zip(vec1, vec2))