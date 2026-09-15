from calculator import add, subtract, multiply, divide
from text_analyzer import (
    word_count,
    character_count,
    sentence_count,
    unique_word_count,
    most_common_word
)


def main():
    # Calculator
    a = 20
    b = 10

    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))
    print("Division:", divide(a, b))

    # Text Analyzer
    text = "Python is powerful. Python is simple! Python is useful."

    print("\nText:", text)
    print("Word count:", word_count(text))
    print("Character count:", character_count(text))
    print("Sentence count:", sentence_count(text))
    print("Unique word count:", unique_word_count(text))
    print("Most common word:", most_common_word(text))


if __name__ == "__main__":
    main()