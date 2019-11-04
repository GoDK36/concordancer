import os,re
import nltk
from nltk.tokenize import sent_tokenize
from konlpy.tag import Okt
okt = Okt()

txt = "D:\GOD's folder\programming\school pj\창회선배 자료\Test-earthquake.txt"
with open(txt, "r") as filetoread:
    fileread = filetoread.read()

token = re.findall(r'\b\w[\w-]*\b', fileread)
sent_token = sent_tokenize(fileread)
twit_token = okt.morphs(fileread)

print(token[:30])
print(sent_token[:30])
print(twit_token[:30])

