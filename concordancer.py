import os,re
# import nltk
# from nltk.tokenize import sent_tokenize

txt = "D:\GOD's folder\programming\school pj\창회선배 자료\Test-earthquake.txt"
with open(txt, "r") as filetoread:
    fileread = filetoread.read()

token = re.findall(r'\b\w[\w-]*\b', fileread)
# sent_token = sent_tokenize(fileread)

#print(token)

keyword = input("검색할 키워드 입력 : ").lower()
length = input("양 옆으로 몇 어절을 검색할까요? ")

def conc(word, list, context, conclist):
    end = len(list)
    for key in range(end):
        if list[key] in word:
            if (key - context) < 0:
                beginCon = 0
            else:
                beginCon = key - context

            if (key + context) > end:
                endCon = end
            else:
                endCon = key + context + 1

            theContext = (list[beginCon:endCon])
            concordance = ' '.join(theContext)
            conclist.append(concordance)
res = []
conc(keyword, token, int(length), res)
print(res)