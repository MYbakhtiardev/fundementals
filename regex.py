import re

text = "The quick brown fox jumps over the lazy dog"

search = re.search(r"fox", text)
if search:
    print(search.group())
search2 = re.search(r"\w+", text)
if search2:
    print(search2.group())

search3 = re.search(r"[a-z]+", text)
if search3:
    print(search3.group())