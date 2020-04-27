import os,re
import nltk
from nltk.tokenize import sent_tokenize
from konlpy.tag import Okt
okt = Okt()

txt = r"E:\Programming\python\창회선배스터디\창회선배 자료\텍스트자료\Test-earthquake.txt"
with open(txt, "r", encoding='utf-8') as filetoread:
    fileread = filetoread.read()

token = re.findall(r'\b\w[\w-]*\b', fileread)
sent_token = sent_tokenize(fileread)
twit_token = okt.morphs(fileread)

print(token[:30])
print(sent_token[:30])
print(twit_token[:30])

