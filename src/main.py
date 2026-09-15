from calculator import add
from text_analyzer import count_words


def main():
    print("AI Engineering Day 6")

    result = add(10, 20)
    print("Addition:", result)

    text = "AI Engineering is interesting"
    print("Word count:", count_words(text))


if __name__ == "__main__":
    main()