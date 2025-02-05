import re

pretext = 'He came and looked for the gun and he eventually found it. The coldness of the gun scared him but he had to muster courage for the sake of his children.'


gender = 'f'
if gender.lower()=='f':
    pretext = re.sub(r'\bHe\b|\bhe\b', 'She', pretext)
    pretext = re.sub(r'\bHim\b|\bhim\b', 'Her', pretext)

print(pretext)

