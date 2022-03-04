#!/usr/bin/python
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - Deletes the keyword.
#        py.exe mcb.pyw delete - Deletes all keywords.
#        py.exe mcb.pyw show <keyword> - Displays keyword to terminal.
#        py.exe mcb.pyw keywords - Displays keyword lsit.

import shelve, pyperclip, sys

availableCommands = """Available commands:
save <keyword>      - Saves clipboard to keyword.
<keyword>           - Loads keyword to clipboard.
show <keyword>      - Displays keyword to the terminal.
list                - Loads all keywords to clipboard.
show list           - Displays all the saved keywords.
delete <keyword>    - Deletes the keyword.
delete              - Deletes all keywords."""

def unpack(argv):
    command = argv[1].lower() if len(argv) >= 2 else ''
    keyword = argv[2] if len(argv) == 3 else ''
    return command, keyword

def exit(display=''):
    print(display)
    sys.exit()

def getKeywords(shelf):
    return [k for k in shelf.keys()]

def save(mcbShelf, keyword):
    data = pyperclip.paste()
    mcbShelf[keyword] = data
    exit("Saving %s to keyword %s." % (data, keyword))

def show(mcbShelf, keyword):
    exit(mcbShelf[keyword])

def keyword(mcbShelf, keyword):
    pyperclip.copy(mcbShelf[keyword])
    exit("Copied keyword to clipboard.")

def delete(mcbShelf, keyword):
    flag = keyword in mcbShelf
    if flag:
        del mcbShelf[keyword]
        exit("Deleted %s keyword." % keyword)
    else:
        exit("Error: Keyword doesn't exist.")

def list(mcbShelf):
    pyperclip.copy("%s" % getKeywords(mcbShelf))

def deleteAll(mcbShelf):
    mcbShelf.clear()
    exit("Deleted all keywords.")

def keywords(mcbShelf):
    keywords = getKeywords(mcbShelf)
    exit(keywords)

keywordCommands = {'save': save, 'show': show, 'delete': delete}
shelfCommands = {'list': list, 'delete': deleteAll, 'keywords': keywords}

def main():
    command, keyword = unpack(sys.argv)

    if len(command) == 0 or \
       command not in keywordCommands.keys() or \
       command not in shelfCommands.keys():
        exit(availableCommands)

    mcbShelf = shelve.open('mcb')

    if command in keywordCommands:
        if len(keyword) == 0:
            exit("Error: Keyword is empty")
        keywordCommands[command](mcbShelf, keyword)
    elif command in shelfCommands:
        shelfCommands[command](mcbShelf)

    mcbShelf.close()

if __name__ == '__main__':
    main()
