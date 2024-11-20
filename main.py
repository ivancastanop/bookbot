def main():
    content = get_text()
    word_count(content)
    characters_dict = character_count(content)
    print_report(characters_dict)


def word_count(file_text):
    words = file_text.split()
    print(len(words))


def character_count(file_text):
    character_dict = {}
    for char in file_text:
        char = char.lower()
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1
    return character_dict


def get_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents


def print_report(character_dict):
    character_dict = dict(
        sorted(character_dict.items(), key=lambda item: item[1], reverse=True)
    )
    for key, value in character_dict.items():
        print(f"The {key} character was found {value} times")


main()
