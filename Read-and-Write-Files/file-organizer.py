import os


print('You can organize any folder of your choosing and create folders for each file type.')
path = os.path.join(os.path.expanduser('~'), 'Desktop')
desktop_files = os.listdir(path)

file = 'things'
if os.path.exists(os.path.join(path, file)):
    os.chdir(os.path.join(path, file))
    print('The files you want to organize are:')
    files = os.listdir(os.path.join(path, file))
    x= 1
    for file in files:
        print(x,'.',file)
        x += 1
        file_name, file_extension = os.path.splitext(os.path.basename(file))
        if file_extension=='.pdf':
            dir_name = 'text'
            try:
                os.mkdir(dir_name)
                print('nice')
            except FileExistsError:
                print('File already exists')
            os.rename(os.path.join(path, file), dir_name)
        else:
            pass

    
            
        
    
        
    
       
else:
    print('folder does not exist!!!')
