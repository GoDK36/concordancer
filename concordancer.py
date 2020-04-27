import os,re
# import nltk
# from nltk.tokenize import sent_tokenize

txt = r"E:\Programming\python\창회선배스터디\창회선배 자료\텍스트자료\토지2.txt"
with open(txt, "r", encoding="UTF-8") as filetoread:
    fileread = filetoread.read()

token = re.findall(r'\b\w[\w-]*\b', fileread)
# sent_token = sent_tokenize(fileread)

# print(token[:10])

keyword = input("검색할 키워드 입력 : ").lower()
length = input("양 옆으로 몇 어절을 검색할까요? ")

def conc(keyword, text_path, length, encoding="UTF-8"):
    with open(text_path, "r", encoding=encoding) as filetoread:
        fileread = filetoread.read()

    token = re.findall(r'\b\w[\w-]*\b', fileread)

    res = []
    print(token[:10])
    end = len(token)
    for key in range(end):
        if keyword in token[key]:
            if (key - length) < 0:
                beginCon = 0
            else:
                beginCon = key - length

            if (key + length) > end:
                endCon = end
            else:
                endCon = key + length + 1

            theContext = (token[beginCon:endCon])
            concordance = ' '.join(theContext)
            res.append(concordance)

    return res
print(conc(keyword, txt, int(length)))
