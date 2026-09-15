import re
from collections import Counter


def word_count(text):
    words = text.split()
    return len(words)


def character_count(text):
    return len(text)


def sentence_count(text):
    sentences = re.split(r'[.!?]+', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return len(sentences)


def unique_word_count(text):
    words = text.lower().split()
    return len(set(words))


def most_common_word(text):
    words = text.lower().split()
    word_counts = Counter(words)

    if not word_counts:
        return None

    return word_counts.most_common(1)[0][0]