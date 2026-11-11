def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])


def main():
    sentence = input()
    print(reverse_words(sentence))


if __name__ == "__main__":
    main()