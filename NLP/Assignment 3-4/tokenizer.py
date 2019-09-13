import re

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
        (b"[\x80-\xff]+", lambda scanner,token: ("EMOJI",token)),
        (r"[a-zA-Z0-9]+@([a-zA-Z0-9]+\.*){2,3}",lambda scanner,token: ("EMAIL",token)),
        (r"http[s]*://[A-Z0-9a-z./]*",lambda scanner,token: ("LINK",token)),
        (r"#[A-Za-z0-9]+",lambda scanner,token: ("HASHTAG",token)),
        (r"@[A-Za-z0-9]+",lambda scanner,token: ("MENTION",token)),
        (r"[A-Za-z_]+", lambda scanner,token: ("WORD",token)),
        (r"$[0-9]+(.[0-9]+)*",lambda scanner,token: ("CURRENCY",token)),
        (r"\s",lambda scanner,token: None),
        (r"[0-9]+", lambda scanner,token: ("NUMBERS",token)),
        (r"[,.?!`'’\-@&;\(\):\/#]+", lambda scanner,token: ("PUNC",token)),
    ])
    results,remainder = scanner.scan(sentence)
    print(results)
    # remainder.encode('utf-8')
    # for word in remainder.split(r"\\"):
    # print(scanner.scan(remainder))
    # deEmojify(remainder)
    # results,remainder = scanner.scan(sentence)
    # print(results)
    print(remainder)

if __name__ == "__main__":
    # for line in corpus3_sentences[:3]:
    #     print(line)
    #     word_tokenizer(line)
    
    for line in corpus4_sentences:
        print(line)
        word_tokenizer(line.encode('utf-8'))