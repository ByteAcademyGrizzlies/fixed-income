import abc


class base_view(abc.ABC):
    """The base class for all options strategies"""

    STRATEGY_NAME = "Base"

    def __init__(self):
        pass

    @abc.abstractmethod
    def printshit(self, mortgage_metric_holder):
        """The abstract method that MUST be implemented by any option strategy
            sub-class"""
        raise NotImplementedError
