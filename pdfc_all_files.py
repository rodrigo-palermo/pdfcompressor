#! python
import sys
import os
from pathlib import Path

p = Path('C:\\Users\\avila\\Desktop\\Nova pasta')
print('this dir: ' + str(p))
# somente arquivos dentro das pastas filho (1 nivel)
subfolders = [x for x in p.iterdir() if p.is_dir()]


files = list(p.glob("**/*.pdf"))
print(files)

[ os.system('py pdfc -c 3 "%s"' % x) for x in files]


