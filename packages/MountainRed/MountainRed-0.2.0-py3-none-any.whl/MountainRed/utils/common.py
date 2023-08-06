import warnings
import functools
import os
import sys
import importlib


def deprecated(message=''):
    def warpper(func):
        """This is a decorator which can be used to mark functions
        as deprecated. It will result in a warning being emitted
        when the function is used."""
        @functools.wraps(func)
        def new_func(*args, **kwargs):
            warnings.simplefilter(
                'always', DeprecationWarning)  # turn off filter
            warnings.warn("Call to deprecated function {}. {}".format(func.__name__, message),
                          category=DeprecationWarning,
                          stacklevel=2)
            warnings.simplefilter(
                'default', DeprecationWarning)  # reset filter
            return func(*args, **kwargs)
        return new_func
    return warpper


def dynamic_loading_settings(option: str):
    """
    动态加载整个Django项目配置文件中名为 option 的配置变量
    """

    settings = importlib.import_module(
        dict(os.environ)['DJANGO_SETTINGS_MODULE'])

    return getattr(settings, option, None)
