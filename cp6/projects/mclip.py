#! python3
# mclilp.py - A multi-clipboard program.

TEXT = {'description': """
        <p>
        </p>
        <p>
        <a href="">Planificación</a>
        </p>
        """,
        'imagestep': """
        <p>
        <img src="" width="480px" height="360px"/>
        </p>
        <p>
        Crea un nuevo proyecto. Tendrás un fondo blanco y un Sprite.
        </p>
        """,
        'videostep': """
        <iframe class="ql-video" allowfullscreen="true" src="" width="480px" height="360px" frameborder="0">
        </iframe>
        <p>
        </p>
        """,}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
