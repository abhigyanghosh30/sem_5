import re
# import unicodedata
# from unidecode import unidecode

corpus3_sentences = []
f = open('corpus3.txt','r')
corpus3_sentences=f.readlines()
f.close()

corpus4_sentences = []
f = open('corpus4.txt','r',encoding='utf-8')
corpus4_sentences=f.readlines()
f.close()


# def deEmojify(inputString):
#     returnString = ""

#     for character in inputString:
#         try:
#             character.encode("ascii")
#             returnString += character
#         except UnicodeEncodeError:
#             replaced = unidecode(str(character))
#             if replaced != '':
#                 returnString += replaced
#             else:
#                 try:
#                      returnString += "[" + unicodedata.name(character) + "]"
#                 except ValueError:
#                      returnString += "[x]"

#     return returnString

def word_tokenizer(sentence):
    scanner = re.Scanner([
        (r"[a-zA-Z0-9]+@([a-zA-Z0-9]+\.*){2,3}",lambda scanner,token: ("EMAIL",token)),
        (r"http[s]*://[A-Z0-9a-z./]*",lambda scanner,token: ("LINK",token)),
        (r"#[A-Za-z0-9]+",lambda scanner,token: ("HASHTAG",token)),
        (r"@[A-Za-z0-9]+",lambda scanner,token: ("MENTION",token)),
        (r"[A-Za-z_]+", lambda scanner,token: ("WORD",token)),
        (r"$[0-9]+(.[0-9]+)*",lambda scanner,token: ("CURRENCY",token)),
        (r"\s",lambda scanner,token: ("SPACE",token)),
        (r"[0-9]+", lambda scanner,token: ("NUMBERS",token)),
        (r"[,.?!`'’\-@&;\(\):\/#]+", lambda scanner,token: ("PUNC",token)),
        (u"(\ud83d[\ude00-\ude4f])=", lambda scanner,token: ("EMOJI",token)),
        (u"(\ud83c[\udf00-\uffff])+", lambda scanner,token: ("EMOJI",token)),
        (u"(\ud83d[\u0000-\uddff])+", lambda scanner,token: ("EMOJI",token)),
        (u"(\ud83d[\ude80-\udeff])+", lambda scanner,token: ("EMOJI",token)),
        (u"(\ud83c[\udde0-\uddff])+", lambda scanner,token: ("EMOJI",token)),
    ])
    results,remainder = scanner.scan(sentence)
    print(results)
    for word in remainder.split(r"\\"):
        print(word)
    # deEmojify(remainder)
    # results,remainder = scanner.scan(sentence)
    # print(results)
    print()

if __name__ == "__main__":
    # for line in corpus3_sentences[:3]:
    #     print(line)
    #     word_tokenizer(line)
    
    for line in corpus4_sentences:
        print(line)
        word_tokenizer(line)