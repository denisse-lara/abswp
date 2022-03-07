import re

def regxStrip(text, char=' '):
    if char == ' ':
        whiteSpace = re.compile(r'^(\s*)(\w*)(\s*)$')
        whiteSpace = whiteSpace.match(text)
        return whiteSpace.groups()[1]

    splitBy = re.compile(r'%s' % char)
    return ''.join(splitBy.split(text))

if __name__ == '__main__':
    text = '    yes    '
    print('Start: %s' % text)
    print('End: %s' % regxStrip(text))

    text = '    AB1yesAB    '
    print('Start: %s' % text)
    print('End: %s' % regxStrip(text, 'AB'))
