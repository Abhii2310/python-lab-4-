#3)a.create a dictionary for words and their meanings

dictionary = {}

def add_entry(word, meaning):
    dictionary[word] = meaning
    print(f"Added: {word} -> {meaning}")

def search_word(word):
    return f"The meaning of '{word}' is: {dictionary[word]}" if word in dictionary else f"'{word}' not found."

def find_words_with_meaning(meaning):
    words = [word for word, m in dictionary.items() if m == meaning]
    return ', '.join(words) if words else f"No words found with meaning '{meaning}'."

def remove_entry(word):
    print(f"Removed: {word}" if dictionary.pop(word, None) else f"'{word}' not found.")

def display_all_words():
    print("All words:", ', '.join(sorted(dictionary.keys())))

def menu():
    actions = {
        '1': lambda: add_entry(input("Word: "), input("Meaning: ")),
        '2': lambda: print(search_word(input("Word to search: "))),
        '3': lambda: print(find_words_with_meaning(input("Meaning to search: "))),
        '4': lambda: remove_entry(input("Word to remove: ")),
        '5': display_all_words,
        '6': exit
    }
    while True:
        print("\n1. Add 2. Search 3. Find by meaning 4. Remove 5. Display all 6. Exit")
        actions.get(input("Choice: "), lambda: print("Invalid choice"))()

menu()