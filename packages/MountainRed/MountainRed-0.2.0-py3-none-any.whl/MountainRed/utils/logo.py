
LOGO = r"""
 __  __                       _           _         ____             _
|  \/  |  ___   _   _  _ __  | |_   __ _ (_) _ __  |  _ \   ___   __| |
| |\/| | / _ \ | | | || '_ \ | __| / _` || || '_ \ | |_) | / _ \ / _` |
| |  | || (_) || |_| || | | || |_ | (_| || || | | ||  _ < |  __/| (_| |
|_|  |_| \___/  \__,_||_| |_| \__| \__,_||_||_| |_||_| \_\ \___| \__,_|

"""


def show_version():
    """
    show current version of MountainRed
    """
    import importlib
    version = importlib.import_module('MountainRed').__version__
    print(LOGO)
    print('Current version: v%s' % version)
