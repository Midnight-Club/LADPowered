from main import parse_sentences, parse_words


def test_sentence_splitting():
    text = "Ore walked home. The door was open! Where is everyone?"

    sentences = parse_sentences(text)

    assert len(sentences) == 3


def test_exclamation_and_question_marks():
    text = "Stop! Where are you?"

    sentences = parse_sentences(text)

    assert len(sentences) == 2

def test_sentence_whitespace():
    text = "   Ore walked home.   The door was open.   "

    sentences = parse_sentences(text)

    assert sentences[0]["text"] == "Ore walked home"
    assert sentences[1]["text"] == "The door was open"

def test_sentence_normalization():
    text = "Ore Walked Home."

    sentences = parse_sentences(text)

    assert sentences[0]["text"] == "Ore Walked Home"
    assert sentences[0]["normalized"] == "ore walked home"

def test_word_punctuation():
    text = '"Hello," Ore said. "Where is everyone?"'

    sentences = parse_sentences(text)

    words = sentences[0]["text"].split()

    clean_words = []

    for word in words:
        clean_word = word.strip('.,!?;:"')
        clean_words.append(clean_word)

    assert clean_words == ["Hello", "Ore", "said"]

def test_apostrophes_are_preserved():
    text = "Ore wasn't sure. It's fine."

    sentences = parse_sentences(text)

    words = sentences[0]["text"].split()

    clean_words = []

    for word in words:
        clean_word = word.strip('.,!?;:"')
        clean_words.append(clean_word)

    assert clean_words == ["Ore", "wasn't", "sure"]

def test_ellipses_are_preserved():
    text = "Ore stared at the door... Nobody moved."

    sentences = parse_sentences(text)

    assert len(sentences) == 1
    assert sentences[0]["text"] == "Ore stared at the door... Nobody moved"


def test_long_ellipses_are_handled():
    text = "Ore stared at the door...... Nobody moved."

    sentences = parse_sentences(text)

    assert len(sentences) == 1
    assert sentences[0]["text"] == "Ore stared at the door... Nobody moved"

def test_dialogue_punctuation():
    text = '"Hello," Ore said. "Where are you?"'

    sentences = parse_sentences(text)

    words = sentences[0]["text"].split()

    clean_words = []

    for word in words:
        clean_word = word.strip('.,!?;:"')
        clean_words.append(clean_word)

    assert clean_words == ["Hello", "Ore", "said"]

def test_sentence_structure():
    text = "Ore Walked Home. The Door Was Open."

    sentences = parse_sentences(text)

    assert sentences[0] == {
        "text": "Ore Walked Home",
        "normalized": "ore walked home",
        "position": 0
    }

    assert sentences[1] == {
        "text": "The Door Was Open",
        "normalized": "the door was open",
        "position": 1
    }

def test_word_cleaning():
    sentence = '"Hello," Ore said.'

    words = parse_words(sentence)

    assert words == ["Hello", "Ore", "said"]

def test_parser_with_realistic_prose():
    text = (
        'Ore walked toward the old house. '
        '"Where is everyone?" he asked. '
        'Nobody answered... He wasn\'t sure what to do, but he opened the door.'
    )
    sentences = parse_sentences(text)
    assert len(sentences) == 3
    assert sentences[0]["text"] == "Ore walked toward the old house"
    assert sentences[1]["text"] == '"Where is everyone?" he asked'
    assert sentences[2]["text"] == 'Nobody answered... He wasn\'t sure what to do, but he opened the door'