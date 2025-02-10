#py sys-module-practice.pyw sys will get input from commandline
#py sys-module-practice.pyw pyperclip paste and copy from clipboard
#py sys-module-practice.pyw shelve will save keyword associate to clipboard

import sys, pyperclip, shelve
arguments = len(sys.argv)
try:
    command = sys.argv[1]
except IndexError:
    sys.exit(0)

if arguments>1:
    if command.lower() == 'save':
        parameter = sys.argv[2]
        with shelve.open('board') as db:
            try:
                db[parameter] = pyperclip.paste()
            except:
                print('Clipboard is empty')
                sys.exit(1)
    elif command.lower() == 'list':
        with shelve.open('board') as db:
            keys = list(db.keys())
            pyperclip.copy = keys
    else:
        print('Invalid command.')
        sys.exit(1)
    
else:
    print('Invalid number of arguments')
    sys.exit(1)
        



