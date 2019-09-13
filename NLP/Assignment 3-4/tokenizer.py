import re

corpus3_sentences = []
f = open('corpus3.txt','r')
corpus3_sentences=f.readlines()
f.close()

corpus4_sentences = []
f = open('corpus4.txt','r',encoding='utf-8')
corpus4_sentences=f.readlines()
f.close()


def word_tokenizer(sentence):
    scanner = re.Scanner([
        (b"[\x80-\xff]+", lambda scanner,token: ("EMOJI",token)),
        (r"[a-zA-Z0-9]+@([a-zA-Z0-9]+\.*){2,3}",lambda scanner,token: ("EMAIL",token)),
        (r"http[s]*://[A-Z0-9a-z./]*",lambda scanner,token: ("LINK",token)),
        (r"#\S+",lambda scanner,token: ("HASHTAG",token)),
        (r"@\S+",lambda scanner,token: ("MENTION",token)),
        (r'[A-Z][a-z]*\.', lambda scanner, token: ("NNP",token)),
        (r"[0-9]+% | [0-9]+\ %", lambda scanner,token: ("PERCENT",token)),
        (r"[0-9.]+", lambda scanner,token: ("DECIMAL",token)),
        (r"\w+", lambda scanner,token: ("WORD",token)),
        (r"$[0-9]+(.[0-9]+)*",lambda scanner,token: ("CURRENCY",token)),
        (r"\s+",lambda scanner,token: None),
        (r"\n",lambda scanner,token: None),
        (r"\\n",lambda scanner,token: None),
        (r"[0-9]+", lambda scanner,token: ("NUMBERS",token)),
        (r"[\",.?!`'’\-@&;\(\):\/#$\*\|=]+", lambda scanner,token: ("PUNC",token)),
    ])
    results,remainder = scanner.scan(sentence)

    if(len(remainder)>0):
        print(sentence)
        print(results)
        print(remainder)

if __name__ == "__main__":
    for line in corpus3_sentences:
        # print(line)
        word_tokenizer(line.encode('utf-8'))
    
    # for line in corpus4_sentences:
    #     word_tokenizer(line.encode('utf-8'))
    # word_tokenizer(b'Rev. St. Francis of Assisi')