#!C:\Users\IP520\PycharmProjects\PersonalBlogGenerator\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'generate','console_scripts','generate'
__requires__ = 'generate'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('generate', 'console_scripts', 'generate')()
    )
