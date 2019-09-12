import re
corpus3_sentences = []
f = open('corpus3.txt','r')
corpus3_sentences=f.readlines()
f.close()

corpus4_sentences = []
f = open('corpus4.txt','r')
corpus4_sentences=f.readlines()
f.close()

def word_tokenizer(sentence):
    scanner = re.Scanner([
        (r"[a-zA-Z0-9]+@([a-zA-Z0-9]+\.*){2,3}",lambda scanner,token: ("EMAIL",token)),
        (r"http[s]*://[A-Z0-9a-z./]*",lambda scanner,token: ("LINK",token)),
        (r"#[A-Za-z0-9]+",lambda scanner,token: ("HASHTAG",token)),
        (r"@[A-Za-z0-9]+",lambda scanner,token: ("MENTION",token)),
        (r"[A-Za-z]+", lambda scanner,token: ("WORD",token)),
        (r"\s",lambda scanner,token: ("SPACE",token)),
        (r"[0-9]+", lambda scanner,token: ("NUMBERS",token)),
        (r"[,.?`’\-]+", lambda scanner,token: ("PUNC",token)),

    ])

    results,remainder = scanner.scan(sentence)
    print(results)

if __name__ == "__main__":
    # for line in corpus3_sentences[:3]:
    #     print(line)
    #     word_tokenizer(line)
    
    for line in corpus4_sentences[:6]:
        print(line)
        word_tokenizer(line)