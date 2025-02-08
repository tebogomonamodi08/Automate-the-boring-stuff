import shelve, os


print('The current directory is:', os.getcwd())

os.chdir(os.path.join(os.path.expanduser('~'), 'Desktop'))

if os.path.exists(os.path.join(os.path.expanduser('~'), 'Desktop')):
    with shelve.open('data') as db:
        db['name'] = 'tebogo'
        db['scores'] = [12,56,67]

    with shelve.open('data') as db:
        print(db['name'])
    
else:
    print('The file does not exist.')