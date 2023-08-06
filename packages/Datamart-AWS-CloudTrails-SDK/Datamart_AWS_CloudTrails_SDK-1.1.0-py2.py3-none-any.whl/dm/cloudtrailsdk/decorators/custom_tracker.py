import json
import logging
from dm.cloudtrailsdk.model.event import Event
from dm.cloudtrailsdk.utils.functions import configure_tracker

logger = logging.getLogger(__name__)


class CustomLogger:
    """

    """

    def __init__(self, app_name="", app_version="", tracker_environment=None):
        """

        :param app_name:
        :param app_version:
        :param tracker_environment:
        """
        self.tracker = configure_tracker(app_name=app_name, app_version=app_version,
                                         tracker_environment=tracker_environment)

    def __call__(self, func):
        """

        :param func:
        :return:
        """
        return lambda *args, **kwargs: self.callFunc(func, *args, **kwargs)

    def callFunc(self, func, *args, **kwargs):
        """

        :param func:
        :param args:
        :param kwargs:
        :return:
        """
        func_name = func.__name__
        r = func(*args, **kwargs)
        try:
            custom_event = Event()
            custom_event.Properties.update({
                'Method': func_name,
                'RequestPayload': json.dumps(args),
                'ResponsePayload': json.dumps(r),
                'ResponseHttpStatus': 200
            })
            custom_event.Properties.update(kwargs)
            self.tracker.track_event(custom_event)
        except Exception as e:
            logger.error(str(e))
        return r
