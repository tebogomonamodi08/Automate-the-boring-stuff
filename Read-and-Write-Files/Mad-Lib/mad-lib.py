#re used for mad-lib.py to find and replace words
import re, os

file_path = os.path.join(os.getcwd(), 'Read-and-Write-Files', 'Mad-Lib','short.txt')

try:
    with open(file_path) as file_object:
        content = file_object.read()
        print(content)
except FileNotFoundError:
    print('File not found')


user_input = input('Enter ADJECTIVE ')
content = re.sub('ADJECTIVE',user_input, content)
user_input = input('Enter NOUN ')
content = re.sub('NOUN',user_input, content)
user_input = input('Enter VERB')
content = re.sub('VERB',user_input, content)

try:
    with open(file_path, 'w') as file_object:
        file_object.write(content)
except FileNotFoundError:
    print('File not found')




