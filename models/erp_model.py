 # The fit method trains the model on the input data X and labels y, the predict method returns binary predictions for the input X, and the predict_proba method returns the predicted probabilities of the positive class. You will need to modify this code to implement your own machine learning models.



import pandas as pd
from sklearn.linear_model import LogisticRegression

class ERPPredictor:
    def __init__(self):
        self.model = LogisticRegression()
    
    def fit(self, X, y):
        self.model.fit(X, y)
    
    def predict(self, X):
        y_pred = self.model.predict(X)
        return y_pred
    
    def predict_proba(self, X):
        y_prob = self.model.predict_proba(X)
        return y_prob
