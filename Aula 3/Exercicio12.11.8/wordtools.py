from string import punctuation

def cleanword(s):
    ans = ""
    for c in s:
        if c not in punctuation:
            ans = ans + c
    return ans

def has_dashdash(s):
    if s.find("--") == -1:
        return 0
    else:
        return 1

def extract_words(s):
    s = s.replace("--", " ")
    s = cleanword(s).lower()
    return s.split()

def wordcount(s, list):
    count = 0
    for word in list:
        if word == s:
            count = count + 1
    return count

def wordset(list):
    new_list = []
    for word in list:
       if word not in new_list:
          new_list.append(word)
    return sorted(new_list)

def longestword(list):
    if list == []:
        return 0
    current_max = len(list[0])
    for word in list:
       if len(word) > current_max:
          current_max = len(word)
    return current_max
