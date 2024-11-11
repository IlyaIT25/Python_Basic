def popular_words(text, words):

    words_in_text = text.lower().split()

    word_count = {word: 0 for word in words}

    for word in words_in_text:
        if word in word_count:
            word_count[word] += 1

    return word_count

print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''',['i', 'was', 'three', 'near']))
