def correct_sentence(text: str):
    sentences = text.split('. ')
    corrected_sentences = []

    for sentence in sentences:
        corrected_sentence = sentence.capitalize()

        if not corrected_sentence.endswith('.'):
            corrected_sentence += '.'
        corrected_sentences.append(corrected_sentence)

    return ' '.join(corrected_sentences)

print(correct_sentence("greetings, friends."))
