# Nicole Thomas
# LabCollectionsP4.py
# February 5, 2024

# (a) Ask the user to enter a string. Convert all letters to uppercase.
# Count the frequency of each letter in the string. Store the frequency counts in a dictionary.
user_input = input("Enter a string: ")
user_input = user_input.upper()

frequency_dict = {}
for char in user_input:
    if char.isalpha():  # Count letters only, excluding digits and spaces
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

print("Frequency Dictionary:", frequency_dict)

# (b) Ask the user to enter a letter. Convert it to uppercase.
# Check whether the letter is in the dictionary. Display the frequency count and remove the letter.
letter_to_check = input("Enter a letter: ").upper()

if letter_to_check in frequency_dict:
    frequency_count = frequency_dict[letter_to_check]
    del frequency_dict[letter_to_check]
    print(f"Frequency count of {letter_to_check}: {frequency_count}")
    print("Dictionary after removing the letter:", frequency_dict)
else:
    print("Letter not in dictionary")

# (c) Create a list to store the letters that are in the dictionary. Sort and display the list.
letters_in_dict = list(frequency_dict.keys())
letters_in_dict.sort()
print("Sorted list of letters in the dictionary:", letters_in_dict)
