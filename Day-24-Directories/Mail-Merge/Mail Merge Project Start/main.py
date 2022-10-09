
with open("Input/Names/invited_names.txt") as names_file:
    names = []
    for name in names_file.readlines():
        names.append(name.strip("\n"))

print(names)


for name in names:
    with open("Input/Letters/starting_letter.txt") as starting_letter:
        new_letter = starting_letter.read()
        new_letter= new_letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}", mode="w") as letter_out:
            letter_out.write(new_letter)
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp