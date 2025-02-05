#imports
import pyperclip
import re

sample_text = 'Hi my name is Tebogo Monamodi and number is 0652427162, my other number is 0828875523 and my email is tebogomonamodi@gmail.com and my other email is tebogo24@gmail.com'

pyperclip.copy(sample_text) #copy sample text to the clipboard

number_match_object = re.findall(r'\d{10,12}', pyperclip.paste()) #find the regular expression for numbers
email_match_object = re.findall(r'[\w\d\.]+@[\w\.]+', pyperclip.paste()) #find the regualr expression for the email

print('The numbers found are: ')
for i in range(0,len(number_match_object)):
    print(number_match_object[i])
print('The emails found are: ')
for i in range(0, len(email_match_object)):
    print(email_match_object[i])
    

