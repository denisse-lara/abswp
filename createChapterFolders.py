#!/usr/bin/python
# createChapterFolders.py - Creates a folder hierarchy structure to save 
# project and practice .py files from the book
from pathlib import Path

print('Creating folders')

# skip ch1
cp_total = 19
for _ in range(cp_total):
    cp_path = Path.cwd() / f'cp{_+2}' 
    Path.mkdir(cp_path)
    Path.mkdir(cp_path / 'projects')
    Path.mkdir(cp_path / 'practice')

print('Folders created.')

