import importlib
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
utils = importlib.import_module('MountainRed.utils')
utils.entry_point()
