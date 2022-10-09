import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


def generate_phonetic():
    user_word = input("Enter a word:").upper()
    try:
        code_list = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(code_list)


generate_phonetic()


