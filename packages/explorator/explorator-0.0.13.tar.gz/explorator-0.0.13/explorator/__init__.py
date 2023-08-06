from . import general_info
from . import total_review
from . import functions
from explorator_library.setup import version

def libinfo():
    print('''
    Library explorator.
    Structure:
    Version: {version}
    1. General info
        get_total
    2. Functions
        - Convert series to str
        - Convert series to date
        - Convert series to numeric (specify int or float)
    '''.format(version=version))
