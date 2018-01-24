#!C:\Users\IP520\PycharmProjects\PersonalBlogGenerator\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'create','console_scripts','create'
__requires__ = 'create'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('create', 'console_scripts', 'create')()
    )
