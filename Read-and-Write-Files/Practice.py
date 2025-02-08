import os


cwd = os.getcwd()
print(cwd)
path = os.path.join(os.path.expanduser('~'), 'Desktop')

if os.path.exists(path):
    os.chdir(path)
    with open('test_file.txt','w') as file_object:
        file_object.write('This is the file you created')
    print(f'File created successfully in: {os.getcwd()}')
else:
    print('The directory does not exist.')

try:
    os.mkdir(os.path.join(os.path.expanduser('~'), 'Desktop', 'new', 'Inside_out'))
except FileExistsError:
    print('The file already exists.')


path = os.path.join(os.path.expanduser('~'), 'Desktop')
print(os.path.relpath(path, 'Read-and-Write-Files'))

#print(os.path.basename(os.getcwd()))

path = 'C:\\users\\windows\\Desktop\\AUTOMATE-THE-BORING-STUFF\\Read-And-Write-Files\\Practice.py'
path_tuple = os.path.split(path) #This method returns a tuple of the directory and the filename
print(path_tuple[0]) #I just extracted the directory name from the tuple output.

print(path.split(os.path.sep))

path = os.path.join(os.path.expanduser('~'), 'Desktop')
desktop_folders = os.listdir(path)

for folder in desktop_folders:
    ''''This loop returns all the directories and files that start with a "B"'''
    if folder[0].upper()=='B': 
        print(folder)
    
print(os.path.getsize(path))
print(os.listdir(path))

print(os.path.exists('D:\\'))
