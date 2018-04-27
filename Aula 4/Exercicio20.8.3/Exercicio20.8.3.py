import collections
import re

def remove_special_characters(string):
    """ Removes special characters of each word """
    # Removing double --
    string = re.sub('-{2,}', ' ', string)
    # Removing special characters from english words
    string = re.sub('\'ll', 'contractedWill', string)
    string = re.sub('I\'m', 'Im', string)
    string = re.sub('\'[Rr][Ee](?!.)', 'contractedAre', string)
    string = re.sub('\'s(?![a-zA-Z])', 'contractedIs', string)
    string = re.sub('\'S(?![a-zA-Z])', 'contractedIs', string)
    string = re.sub('n\'t', 'contractedNot', string)
    # Removing special characters from the book, except dash
    string = re.sub(r'[^-a-zA-Z ]', ' ', string)
    # Adding special characters to the english words again
    string = re.sub('contractedWill', '\'ll', string)
    string = re.sub('Im', 'I\'m', string)
    string = re.sub('contractedAre', '\'re', string)
    string = re.sub('contractedIs', '\'s', string)
    string = re.sub('contractedNot', 'n\'t', string)

    return string.split()

#_____________________________________________________________________________#

book = open("Alice’s Adventures in Wonderland.txt", "r")
content = book.read()
# Initializes dictionary
dict = {}

word_count = open("alice_words.txt", "w")
word_count.write("Word                 Count\n==========================\n")

# Removes special characters ( ) " " ' ' - _
words = remove_special_characters(content)

# Lowercase all words of the list
n = 0
size = len(words)
while n < size:
    words[n] = words[n].lower()
    n = n + 1

# Insert new words in the dictionary or update number of instances
for word in words:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] = dict[word] + 1

# Print sorted dictionary on output file
ord_dict = collections.OrderedDict(sorted(dict.items()))
for word, value in ord_dict.items():
    if len(word) > 15:
        word_count.write("{0}\t{1}\n".format(word, value))
    elif len(word) > 7:
        word_count.write("{0}\t\t{1}\n".format(word, value))
    else:
        word_count.write("{0}\t\t\t{1}\n".format(word, value))

print("Words printed on the output file\n")

alice = dict["alice"]
alices = dict["alice's"]
print("The word alice appears {0} times and the word alice's appears {1} times"
      " adding up to {2}".format(alice, alices, alice + alices))

# Closing files
book.close()
word_count.close()
