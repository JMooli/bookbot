
path_to_file = "books/frankenstein.txt"

def main():
    with open(path_to_file) as f:
        file_contents = f.read()

        make_report(path_to_file, count_words(file_contents), count_characters(file_contents) )


def count_words(input_str):
    words = input_str.split()
    return len(words)

def count_characters(input_str):
    characters = {}
    lowered_string = input_str.lower()
    for c in lowered_string:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def convert_dict_to_list_of_dicts(dict):
    list_of_dicts = []
    for d in dict:
        
        list_of_dicts.append({"name": d, "num": dict[d]})
    return list_of_dicts

def sort_on(sortdict):
    return sortdict["num"]

def make_report(path, word_count, characters):
    print(f"--- Begin report of {path}---")
    print(f"{word_count} words found in the document" + "\n")

    list_of_character_dicts = convert_dict_to_list_of_dicts(characters)
    list_of_character_dicts.sort(reverse=True, key=sort_on)

    for d in list_of_character_dicts:
        if d["name"].isalpha():
            char = d["name"]
            count = d["num"]
            print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

    
main()