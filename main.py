with open("chapter_01.txt", "r") as file:
    text = file.read()

print(text)
sentences = text.replace("?", ".").replace("!", ".").split(".")

for sentence in sentences:
   # print(sentence)
    words = sentence.split()
    

    for word in words:
        clean_word = word.strip('"')
        print(clean_word)


    