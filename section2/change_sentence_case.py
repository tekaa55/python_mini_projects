with open("files/snowwhite.txt", "r") as file:
    content = file.read()
    sentences = content.split(".")

    corrected_sentences = []

    for sentence in sentences:
        corrected_sentence = sentence
        if sentence[0] == " ":
            corrected_sentence = sentence[1:]
        if sentence[-1] != ".":
            corrected_sentence = corrected_sentence + "."

        corrected_sentence = corrected_sentence.capitalize()
        corrected_sentences.append(corrected_sentence)

    with open("files/snowwhite_corrected.txt", "w") as corrected_file:
        corrected_file.write(" ".join(corrected_sentences))
