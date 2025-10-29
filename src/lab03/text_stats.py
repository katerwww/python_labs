import sys
import re
from lib.text import normalize, tokenize, count_freq, top_n

a = str(input())
n =normalize(a) 
allwords = tokenize(n) 
uw = count_freq(allwords) 
top = top_n(uw,5) 
print(f'Всего слов: {len(allwords)}') 
print(f"Уникальных слов: {len(uw)}")
print("Топ-5:")
for y in top:
    print(y[0] + ': ' + str(y[1]))

