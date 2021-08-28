import zipfile
from pathlib import Path
p = Path('.')
for f in p.glob('*.zip'):
    with zipfile.ZipFile(f, 'r') as archive:
        archive.extractall(path=f'./{f.stem}')
        print(f'Done {f.stem}')
