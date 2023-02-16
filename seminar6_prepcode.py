#seminar 7 - processing raw text
#characters -> UNICODE when transmitted or written into disk
# buffer when reading files/streams -> only a SLICE of the file at a time
# we use open() to read/write

# NLTK 3.3
import nltk
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
f = open(path, encoding='latin2')
for line in f:
    line = line.strip()
    print(line.encode('unicode_escape'))
    # b'Pruska Biblioteka Pa\\u0144stwowa. Jej dawne zbiory znane pod nazw\\u0105'
    # b'"Berlinka" to skarb kultury i sztuki niemieckiej. Przewiezione przez'
    # b'Niemc\\xf3w pod koniec II wojny \\u015bwiatowej na Dolny \\u015al\\u0105sk, zosta\\u0142y'
    # b'odnalezione po 1945 r. na terytorium Polski. Trafi\\u0142y do Biblioteki'
    # b'Jagiello\\u0144skiej w Krakowie, obejmuj\\u0105 ponad 500 tys. zabytkowych'
    # b'archiwali\\xf3w, m.in. manuskrypty Goethego, Mozarta, Beethovena, Bacha.'
    # unicode escape string: prefix of \u followed by glyph value

# py3 default: UTF-8
nacute = '\u0144'
nacute.encode('utf8')
import unicodedata
lines = open(path, encoding='latin2').readlines()
line = lines[2]
print(line.encode('unicode_escape'))
# b'Niemc\\xf3w pod koniec II wojny \\u015bwiatowej na Dolny \\u015al\\u0105sk, zosta\\u0142y\\n'
for c in line:
    if ord(c) > 127:
        print('{} U+{:04x} {}'.format(c.encode('utf8'), ord(c), unicodedata.name(c)))

from nltk import word_tokenize
line.find('zosta\u0142y')
# 54
line = line.lower()
print(line)
# 'niemców pod koniec ii wojny światowej na dolny śląsk, zostały\n'\
line.encode('unicode_escape')
# b'niemc\\xf3w pod koniec ii wojny \\u015bwiatowej na dolny \\u015bl\\u0105sk, zosta\\u0142y\\n'
import re
m = re.search('\u015b\w*', line)
m.group()
# '\u015bwiatowej'
print(word_tokenize(line))

# reading/writing files
f = open('workfile', 'w', encoding="utf-8")
with open('workfile', encoding='utf-8') as f:
    read_data = f.read()
    print(read_data)
# print(f.closed)

# f.seek(offset, whence) -> returns INT for file OBJ position in file presented as bytes/opaque number in text mode
# offset - reference point with offset arg;
# whence - the ref point of the function; 0 == beginning, 1 == current file position, 2 == end of file (DEF: 0)

# saving structured data with JSON
import json
x = [1, 'hard', 'dictionary']
json.dumps(x)

# dump() serialises OBJ to text file (e.g. f == text file obj)
# json.dump(x,f)
# decode with load()
# x = json.load(f)

# 7.1, .1, .2, .3
year = 2023
event = 'Championship'
print(f'Results of the {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
# specifies the accuracy in {} with str.format(*arg, **kwarg)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
# ' 42572654 YES votes  49.67%'

import math
print(f'The value of pi is approximately {math.pi:.5f}.')
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    # value after kwarg called -> min char length of field
    print(f'{name:10} ==> {phone:10d}')

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')
print(f'My hovercraft is full of {animals=}.')

for x in range(1, 11):
    # PT: for a range from 1 to 11, print 3 columns that is formatted to hold 2/3/4 chars minimally and the values
    # are to be in the following format== 1: x, 2: x^2, 3: x^3.
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# str.zfill() pads numeric strings (left-wise) with zeros; also can manage +/-
print('-3.14'.zfill(6))

# test your knowledge
import urllib.request
import requests
response = requests.get('https://gutenberg.org/files/76/76-0.txt')
finn_raw = response.content.decode('utf-8')
finn_lines = finn_raw.split('\n')

with open('finn.txt', 'w') as f:
    for line in finn_lines:
        f.write(line + '\n')

# response.content.decode('utf-8') is used to remove the encoding and convert the raw content into a string.
# Then, finn_raw.split('\n') is used to split the string into a list of lines.
# Finally, the lines are saved as a text file named "finn.txt" using a for loop and the write() method.