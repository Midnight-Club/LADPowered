import re


#Parses the sentences in the text and returns a list of dictionaries containing the sentence text, normalized text, and position in the text.
def parse_sentences(text):
    text = re.sub(r"\.{3,}", "<ELLIPSIS>", text)

    sentences = re.split(r'(?<=[.!?])(?=\s|$)', text)
#    print(sentences)
    clean_sentences = []

    for sentence in sentences:
        if sentence.strip():
            sentence = sentence.replace("<ELLIPSIS>", "...")

            clean_text = sentence.strip().rstrip(".!?")
            

            clean_sentence = {
                "text": clean_text,
                "normalized": clean_text.lower(),
                "position": len(clean_sentences)
            }

            clean_sentences.append(clean_sentence)

    return clean_sentences

#Parses the words in a sentence and returns a list of cleaned words, removing punctuation but preserving apostrophes.
def parse_words(sentence):
    words = sentence.split()
    clean_words = []

    for word in words:
        clean_word = word.strip('.,!?;:"')
        clean_words.append(clean_word)

    return clean_words


with open("chapter_01.txt", "r") as file:
    text = file.read()

sentences = parse_sentences(text)

for sentence in sentences:
    words = parse_words(sentence["text"])

    for word in words:
        print(word)

print(sentences)