#!/usr/bin/python
# madLibs.py - Reads a file and substitutes ADJECTIVE, NOUN, ADVERB or VERB with
# they given arguments
import sys, re
from pathlib import Path

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Provide a name for the file.")
        sys.exit()
    if not Path.exists(Path.cwd() / sys.argv[1]):
        print("File doesn't exist.")
        sys.exit()

    text = ''
    with open(sys.argv[1]) as file:
        text = ''.join(file.readlines())
        print(text)

    with open('overwrite.txt', 'w') as file:
        keywords = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']

        pattern = r'(%s)' % '|'.join(keywords)
        matches = re.finditer(pattern, text)
        for m in matches:
            prompt = "Enter %s %s: "
            article = "a" if m.group(0) != 'ADJECTIVE' else 'an'
            newWord = input(prompt % (article, m.group(0).lower()))
            text = text.replace(m.group(0), newWord, 1)

        print("\n"+text)
        file.write(text)

    print("\nEnd operation")
