import logging
import types
import inspect
from functools import wraps


class LoggingExt(type):
    """
    This decorates all functions in a Component with a logging function.
    """
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, types.FunctionType):
                attrs[attr_name] = cls.log_call(attr_value)

        return super(LoggingExt, cls).__new__(cls, name, bases, attrs)

    @classmethod
    def log_call(cls, func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            logger = self.logger
            if logger:
                cls.extract_metadata(self, func, self._session,
                                     *args, **kwargs)

            return func(self, *args, **kwargs)

        return wrapper

    @classmethod
    def extract_metadata(cls, self, func, session, *args, **kwargs):
        # Get the user calling the function
        subject = session.decoded_token.get('sub', 'UNKNOWN USER')

        if session.api_key:
            api_key = session.api_key[:6]

        # This is to find out what the 'arg' names are.
        argspec = inspect.getfullargspec(func)
        args_dict = dict(zip(argspec.args, [self, *args]))

        self.logger.info('Client Function Called', extra={
            'func': func,
            'subject': subject,
            'arguments': args_dict,
            'kwargs': dict(kwargs),
        })


class SirenComponent(metaclass=LoggingExt):

    def __init__(self, client=None):
        self.client = client
