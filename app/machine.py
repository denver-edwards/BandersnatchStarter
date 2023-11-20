from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
import joblib
import os


class Machine:

    def __init__(self, df: DataFrame):
        """
        Initializes with a RandomForestClassifier
        model trained on the provided DataFrame.

          Args: df (DataFrame): A DataFrame
        """
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

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
        os.makedirs(os.path.dirname(filepath))
        joblib.dump(self.model, filepath)

    @staticmethod
    def open(filepath):
        """
         Loads a model from the specified filepath.

         Args: filepath (str): The path from where the model should be
         loaded.

         Returns:
             Machine instance containing model
         """
        model = joblib.load(filepath)
        machine = Machine.__new__(Machine)
        machine.model = model
        machine.name = "Random Forest Classifier"
        return machine

    def info(self):
        """
        Provides information about the model.
        """
        model_info = f"<p>Base Model: {self.name}</p>"

        return model_info
