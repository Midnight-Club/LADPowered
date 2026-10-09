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


#Finds the entities in a sentence based on a given vocabulary and returns a list of found entities.
def find_entities(sentence, vocabulary):

    found = []
    words = parse_words(sentence)

    for word in words:
        for entity in vocabulary:
            if word.lower() == entity.lower():
                if entity not in found:
                    found.append(entity)

    return found


#Finds the sentences that contain the entities in the vocabulary and returns a dictionary with the entity as the key and a list of sentences as the value.
def find_entity_sentences(list_of_sentences, vocabulary):

    dictionary_for_each_entity_list = {}

    for entity in vocabulary:
        dictionary_for_each_entity_list[entity] = []

    for sentence in list_of_sentences:
        found = find_entities(sentence["text"], vocabulary)

        for entity in found:
            dictionary_for_each_entity_list[entity].append(sentence["text"])

    return dictionary_for_each_entity_list



#----------------------------------------------------------------------------------------------------------------



# Known entity vocabularies

characters = ["Ore", "Maribelle"]
objects = ["fountain", "phone", "wallet", "theo-tool"]
locations = ["gate", "garden", "pier", "Lair of the Arachnid"]


# Read and parse the chapter

with open("chapter_01.txt", "r", encoding="utf-8") as file:
    text = file.read()

list_of_sentences = parse_sentences(text)


# Index sentences by entity category

character_sentences = find_entity_sentences(list_of_sentences, characters)
object_sentences = find_entity_sentences(list_of_sentences, objects)
location_sentences = find_entity_sentences(list_of_sentences, locations)


# Display results

print("Characters:", character_sentences)
print("Objects:", object_sentences)
print("Locations:", location_sentences)

