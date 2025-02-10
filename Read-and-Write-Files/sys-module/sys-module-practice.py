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
        try:
            parameter = sys.argv[2]
        except IndexError:
            print('The parameter cannot be empty.')
            sys.exit(1)
        with shelve.open('board') as db:
            try:
                db[parameter] = pyperclip.paste()
            except pyperclip.PyperclipException:
                print('Clipboard is empty')
                sys.exit(1)
    elif command.lower() == 'list':
        with shelve.open('board') as db:
            keys = list(db.keys())
            pyperclip.copy('\n'.join(keys))
    
    elif command.lower() == 'delete' and arguments>2:
        parameter = sys.argv[2]
        with shelve.open('board') as db:
            if parameter in db:
                del db[parameter]
                print(f'{parameter} deleted from clip.')
            else:
                print(f'{parameter} does not exist in the clipboard.')
        

    elif command.lower() == 'delete' and arguments==2:
        with shelve.open('board') as db:
            db.clear()
            print(f"Shelve cleared")

    else:
        print('Invalid Command')
        sys.exit(1)
    
else:
    print('Invalid number of arguments')
    sys.exit(1)
        



