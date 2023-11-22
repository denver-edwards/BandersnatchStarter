from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
import joblib
from datetime import datetime


class Machine:

    def __init__(self, df: DataFrame = None, model=None):
        """
        Initializes with a RandomForestClassifier
        model trained on the provided DataFrame.

          Args: df (DataFrame): A DataFrame
        """
        self.name = "Random Forest Classifier"
        self.timestamp = "2023-11-22 11:51:38 AM"

        if df is not None:
            target = df["Rarity"]
            features = df.drop(columns=["Rarity"])
            self.model = RandomForestClassifier()
            self.model.fit(features, target)
        elif model is not None:
            self.model = model

    def __call__(self, pred_basis: DataFrame):
        """
        Makes a prediction based on the input DataFrame.

        Args: pred_basis (DataFrame): The input DataFrame to make
        predictions on.

        Returns:
            The prediction made by the model and its confidence.
        """
        prediction, *_ = self.model.predict(pred_basis)
        confidence = max(self.model.predict_proba(pred_basis)[0])
        return prediction, confidence

    def save(self, filepath):
        """
        Saves the model to the specified filepath.

        Args:
            filepath (str): The path where the model should be saved.
        """
        joblib.dump(self.model, filepath)

    @staticmethod
    def open(filepath):
        """
         Loads a model from the specified filepath.

         Args: filepath (str): The path from where the model should be
         loaded.

         Returns:
             Model
         """
        return joblib.load(filepath)

    def info(self):
        """
        Provides information about the model.
        """
        model_info = (f"<p>Base Model: {self.name}<br/>"
                      f"Timestamp: {self.timestamp}</p>")

        return model_info
