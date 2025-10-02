class VectorizationModel:
    def __init__(self, model_name: str):
        self.model_name = model_name

    def vectorize(self, text: str):
        # Dummy implementation for illustration purposes
        return [ord(char) for char in text]