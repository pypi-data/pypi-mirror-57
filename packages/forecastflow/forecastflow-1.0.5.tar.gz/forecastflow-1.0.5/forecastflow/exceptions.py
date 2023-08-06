class ForecastFlowException(Exception):
    """
    Base Exception of ForecastFlow
    """


class InvalidID(ForecastFlowException):
    """
    ID is not found or invalid.
    """