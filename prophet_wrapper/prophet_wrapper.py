from sklearn.base import BaseEstimator, RegressorMixin


class ProphetWrapper(BaseEstimator, RegressorMixin):
    def __init__(self, model):
        self.model = model

    def predict(self, X):
        return self.model.predict(X)
