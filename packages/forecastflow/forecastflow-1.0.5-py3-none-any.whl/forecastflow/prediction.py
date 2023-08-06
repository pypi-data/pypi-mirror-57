from io import BytesIO
from typing import TYPE_CHECKING

import pandas as pd

from forecastflow.exceptions import InvalidID
from forecastflow.firebase_api import cloud_firestore, storage
from forecastflow.firebase_api.exceptions import NotFound
from forecastflow.util import wait_until_prediction_done

if TYPE_CHECKING:
    from forecastflow import Model, Project, User


class Prediction:
    """
    ForecastFlow prediction object
    """

    def __init__(self, model: 'Model', prediction_id: str):
        """
        Instantiate object with given prediction ID.

        Args:
            model:
                Model which makes this predict.

            prediction_id:
                ID of prediction you want to open.
        """
        self.model = model
        self.prediction_id = prediction_id
        self.is_ready = False

        try:
            document = self._document
        except NotFound:
            raise InvalidID('Given Prediction ID is not found')

        if document['mid'] != model.model_id:
            raise InvalidID('Given Prediction ID is not for this model')

        self.name = document['name']

    @property
    def _document(self):
        doc = cloud_firestore.get(f'users/{self.user.user_id}/projects/{self.project.project_id}'
                                  f'/predicts/{self.prediction_id}',
                                  self.user.id_token)
        return doc['fields']

    def get_result(self) -> pd.DataFrame:
        """
        Download the result from ForecastFlow.

        Returns:
            result with primary key and predicted values.
        """
        self.wait_until_done()
        if not self.is_ready:
            raise Exception('Prediction has failed.')
        f = BytesIO()
        storage.download(f"{self.user.user_id}/predict/{self.prediction_id}/predict_proba.csv",
                         f, self.user.id_token)
        f.seek(0)
        result = pd.read_csv(f)
        return result

    @property
    def project(self) -> 'Project':
        return self.model.project

    @property
    def rid(self) -> str:
        return self.prediction_id

    @property
    def user(self) -> 'User':
        return self.model.project.user

    def wait_until_done(self):
        """
        Wait until ForecastFlow finish predict.
        """
        if not self.is_ready:
            wait_until_prediction_done(self.user.id_token, self.user.user_id,
                                       self.project.project_id, self.prediction_id)
            if self._document.get('status') != 'Completed':
                self.is_ready = False
            else:
                self.is_ready = True
