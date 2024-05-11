import json


def load_word_dictionary() -> dict:
    with open('words_dictionary.json') as word_file:
        data = json.load(word_file)
        return data


def print_word_dictionary() -> None:
    data = load_word_dictionary()
    print(data)


if __name__ == '__main__':
    print_word_dictionary()