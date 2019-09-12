import re
corpus3_sentences = []
with open('corpus3.txt','r') as f:
    corpus3_sentences.append(f.read())

def word_tokenizer(sentence):
    scanner = re.Scanner([
        (r"[a-z]+", lambda scanner,token: ("WORD",token))
    ])

    results,remainder = scanner.scan(sentence)
    print(results)

if __name__ == "__main__":
    for line in corpus3_sentences:
        word_tokenizer(line)