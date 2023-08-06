import datetime
import logging
import time

from forecastflow.firebase_api import cloud_firestore

logger = logging.getLogger(__name__)


# TODO: This file will be too messy, should be refactored.

class ExpirationTimer:
    """
    Manage expiration
    """
    def __init__(self, seconds: int):
        self.seconds = seconds
        self.start = datetime.datetime.now()

    @property
    def is_expired(self) -> bool:
        """
        Returns:
            True if expired
        """
        delta = datetime.datetime.now() - self.start
        if delta.seconds > self.seconds:
            return True
        else:
            return False


def parse_type(type_str: str) -> type:
    """
    Parse type string to python type.
    Use this function to parse type in schema.

    Args:
        type_str:
            Type string like 'float', 'int', ...
    Returns:
        Python native type
    """
    if type_str == 'float':
        return float
    elif type_str == 'int':
        return int
    elif type_str == 'str':
        return str
    elif type_str == 'bool':
        return bool
    else:
        raise ValueError(f"Unsupported type '{type_str}'.")


def wait_until_profile_done(id_token: str, uid: str, pid: str, did: str):
    """
    Wait while Forecast Flow profiler is running.

    Args:
        id_token:
            User's ID token.

        uid:
            User ID

        pid:
            Project ID

        did:
            Data ID
    """
    path = f"users/{uid}/projects/{pid}/dataSources/{did}"
    while True:
        res = cloud_firestore.get(path, id_token)['fields']
        status = res['profile']  # TODO: WTF !?
        if status == '':
            logger.info('Profile Waiting')
        elif status == 'In Progress':
            logger.info('Profile In Progress')
        elif status == 'Error':
            logger.info('Profile Error')
            return None
        else:
            return res
        time.sleep(5)


def wait_until_prediction_done(id_token: str, uid: str, pid: str, rid: str):
    """
    Wait while Forecast Flow predictor is running.

    Args:
        id_token:
            User's ID token

        uid:
            User ID

        pid:
            Project ID

        rid:
            Prediction ID
    """
    path = f"users/{uid}/projects/{pid}/predicts/{rid}"
    while True:
        res = cloud_firestore.get(path, id_token)['fields']
        status = res['status']
        if status == 'Waiting':
            logger.info('Prediction Waiting')
        elif status == 'In Progress':
            logger.info('Prediction In Progress')
        elif status == 'Completed':
            logger.info('Prediction has been completed')
            return res
        else:
            raise Exception(f'Unknown status {status}')
        time.sleep(5)
