import os

if os.path.exists(os.path.join(os.path.expanduser('~'), 'Desktop', 'test_file.txt')):
    path = os.path.join(os.path.expanduser('~'), 'Desktop', 'test_file.txt')

file_object = open(path, 'w')
file_object.write('This is new text.')


