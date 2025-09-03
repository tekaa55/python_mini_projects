# open a file to read
with open("files/example.txt", "r") as file:
    content = file.read()

    words = content.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])

    # create and open a file to write - it fails if the file already exists
    with open("files/reversed_words.txt", "x") as new_file:
        new_file.write(" ".join(reversed_words))
