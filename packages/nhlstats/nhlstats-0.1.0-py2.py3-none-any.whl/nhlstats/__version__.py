__author__ = 'tcaruso'

VERSION = (0, 1, 0)

POST = None

__version__ = '.'.join(map(str, VERSION)) + ('.{}'.format(POST) if POST else '')
