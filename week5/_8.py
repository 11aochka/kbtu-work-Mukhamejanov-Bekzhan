import re

f = open("C:/Users/bboya/OneDrive/Desktop/pp2/week5/row.txt", "r", encoding="utf-8")

pat = r'([A-Z])'
text = f.read().split()

for word in text:
    print(re.sub(pat, r' \1', word))