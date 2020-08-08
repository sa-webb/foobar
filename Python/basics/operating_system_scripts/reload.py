'''
reload() is a rudimentary way to watch for disk changes and reload modules for updates
'''

import sys

from importlib import reload

reload(sys)