import string

input_hashtag = input("Enter future hashtag: ")

words = input_hashtag.split()
words_new = []

for word in words:
    for letter in word:
        if letter in string.punctuation:
            word = word.replace(letter, '')

    words_new.append(word.capitalize())

hashtag = "#" + "".join(words_new)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)

